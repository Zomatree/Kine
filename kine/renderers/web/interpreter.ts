// original code is from https://github.com/DioxusLabs/dioxus/blob/master/packages/liveview/src/interpreter.js and is licensed under the MIT license

declare module msgpack {
    export function encode(any): Uint8Array;
    export function decode(Uint8Array): any;
}

type TypedEvent<Name, Evt> = { type: Name } & Evt;
type TypedEditEvent<Name, Evt> = TypedEvent<Name, Evt> & { root: number };

type EditEvent =
    | TypedEditEvent<"AppendChildren", { children: number[] }>
    | TypedEditEvent<"ReplaceWith", { nodes: number[] }>
    | TypedEditEvent<"InsertAfter", { nodes: number[] }>
    | TypedEditEvent<"InsertBefore", { nodes: number[] }>
    | TypedEditEvent<"Remove", { nodes: number[] }>
    | TypedEditEvent<"CreateTextNode", { text: string }>
    | TypedEditEvent<"CreateElement", { tag: string }>
    | TypedEditEvent<"CreatePlaceholder", {}>
    | TypedEditEvent<"RemoveEventListener", { event_name: string }>
    | TypedEditEvent<"NewEventListener", { event_name: string }>
    | TypedEditEvent<"SetText", { text: string }>
    | TypedEditEvent<"SetAttribute", { field: string; value: string }>
    | TypedEditEvent<"RemoveAttribute", { name: string }>
    | TypedEditEvent<"EvalMessage", { code: string }>
    | TypedEditEvent<"RemoveAllChildren", {}>;

type DomEvent =
    | TypedEvent<"copy" | "cut" | "paste", ClipboardEvent>
    | TypedEvent<
            "compositionend" | "compositionstart" | "compositionupdate",
            CompositionEvent
        >
    | TypedEvent<"keydown" | "keypress" | "keyup", KeyboardEvent>
    | TypedEvent<"focus" | "blur", FocusEvent>
    | TypedEvent<"change", Event>
    | TypedEvent<"input" | "invalid" | "reset" | "submit", Event>
    | TypedEvent<
            | "click"
            | "contextmenu"
            | "doubleclick"
            | "dblclick"
            | "drag"
            | "dragend"
            | "dragenter"
            | "dragexit"
            | "dragleave"
            | "dragover"
            | "dragstart"
            | "drop"
            | "mousedown"
            | "mouseenter"
            | "mouseleave"
            | "mousemove"
            | "mouseout"
            | "mouseover"
            | "mouseup",
            MouseEvent
        >
    | TypedEvent<
            | "pointerdown"
            | "pointermove"
            | "pointerup"
            | "pointercancel"
            | "gotpointercapture"
            | "lostpointercapture"
            | "pointerenter"
            | "pointerleave"
            | "pointerover"
            | "pointerout",
            PointerEvent
        >
    | TypedEvent<"select", Event>
    | TypedEvent<
            "touchcancel" | "touchend" | "touchmove" | "touchstart",
            TouchEvent
        >
    | TypedEvent<"scroll", Event>
    | TypedEvent<"wheel", WheelEvent>
    | TypedEvent<
            "animationstart" | "animationend" | "animationiteration",
            AnimationEvent
        >
    | TypedEvent<"transitionend", TransitionEvent>
    | TypedEvent<
            | "abort"
            | "canplay"
            | "canplaythrough"
            | "durationchange"
            | "emptied"
            | "encrypted"
            | "ended"
            | "error"
            | "loadeddata"
            | "loadedmetadata"
            | "loadstart"
            | "pause"
            | "play"
            | "playing"
            | "progress"
            | "ratechange"
            | "seeked"
            | "seeking"
            | "stalled"
            | "suspend"
            | "timeupdate"
            | "volumechange"
            | "waiting",
            Event
        >
    | TypedEvent<"toggle", Event>;

let ipc: IPC;

function main(ws_addr: string) {
    let root = window.document.getElementById("main");

    if (root != null) {
        ipc = new IPC(root, ws_addr);
    }
}

class IPC {
    interpreter: Interpreter;
    ws: WebSocket;

    constructor(root: HTMLElement, ws_addr: string) {
        this.interpreter = new Interpreter(root, this);
        this.ws = new WebSocket(ws_addr);

        this.ws.onopen = () => {
            console.log("Connected to the websocket");
            this.send(serializeIpcMessage("initialize"));
        };

        this.ws.onerror = (err) => {
            console.error("Error: ", err);
        };

        this.ws.onmessage = async (event: MessageEvent<Blob>) => {
            let data = await event.data.arrayBuffer();
            let view = new Uint8Array(data);
            let edits = msgpack.decode(view);
            this.interpreter.handleEdits(edits);
        };
    }

    send(msg) {
        this.ws.send(msg);
    }
}

class ListenerMap {
    global: Map<string, { active: number; callback: { (...args) } }>;
    local: Map<string, Map<string, { (...args) }>>;
    root: HTMLElement;

    constructor(root) {
        // bubbling events can listen at the root element
        this.global = new Map();
        // non bubbling events listen at the element the listener was created at
        this.local = new Map();
        this.root = root;
    }

    create(
        event_name: string,
        element: HTMLElement,
        handler: { (...args) },
        bubbles: boolean
    ) {
        if (bubbles) {
            let global = this.global.get(event_name);

            if (!global) {
                this.global.set(event_name, {
                    active: 1,
                    callback: handler,
                });

                this.root.addEventListener(event_name, handler);
            } else {
                global.active++;
            }
        } else {
            const id = element.getAttribute("data-kine-id")!;
            let local = this.local.get(id);

            if (!local) {
                local = new Map();
                this.local.set(id, local);
            }
            local.set(event_name, handler);
            element.addEventListener(event_name, handler);
        }
    }

    remove(element: HTMLElement, event_name: string, bubbles: boolean) {
        if (bubbles) {
            this.global[event_name].active--;
            if (this.global[event_name].active === 0) {
                this.root.removeEventListener(
                    event_name,
                    this.global[event_name].callback
                );
                delete this.global[event_name];
            }
        } else {
            const id = element.getAttribute("data-kine-id")!;
            let element_listeners = this.local.get(id)!;

            let handler = element_listeners.get(event_name)!;
            element_listeners.delete(event_name);

            if (element_listeners.size === 0) {
                this.local.delete(id);
            }
            element.removeEventListener(event_name, handler);
        }
    }
}

class Interpreter {
    root: HTMLElement;
    lastNode: HTMLElement | Text;
    listeners: ListenerMap;
    nodes: (HTMLElement | Text)[];
    parents: (HTMLElement | Text)[];
    ipc: IPC;

    constructor(root: HTMLElement, ipc: IPC) {
        this.root = root;
        this.ipc = ipc;
        this.lastNode = root;
        this.listeners = new ListenerMap(root);
        this.nodes = [root];
        this.parents = [];
    }

    checkAppendParent() {
        if (this.parents.length > 0) {
            const lastParent = this.parents[this.parents.length - 1];

            lastParent[1]--;

            if (lastParent[1] === 0) {
                this.parents.pop();
            }

            lastParent[0].appendChild(this.lastNode);
        }
    }

    AppendChildren(root: number | null, children: number[]) {
        let node = root != null ? this.nodes[root] : this.lastNode;

        for (let child of children) {
            node.appendChild(this.nodes[child]);
        }
    }

    ReplaceWith(root: number | null, nodes: number[]) {
        let node = root != null ? this.nodes[root] : this.lastNode;
        let els: (HTMLElement | Text)[] = [];

        for (let new_node of nodes) {
            els.push(this.nodes[new_node]);
        }

        console.log(node, els);

        node.replaceWith(...els);
    }

    InsertAfter(root: number | null, nodes: number[]) {
        let node = root != null ? this.nodes[root] : this.lastNode;
        let els: (HTMLElement | Text)[] = [];

        for (let new_node of nodes) {
            els.push(this.nodes[new_node]);
        }

        node.after(...els);
    }

    InsertBefore(root: number | null, nodes: number[]) {
        let node = root != null ? this.nodes[root] : this.lastNode;
        let els: (HTMLElement | Text)[] = [];

        for (let new_node of nodes) {
            els.push(this.nodes[new_node]);
        }

        node.before(...els);
    }

    Remove(root: number | null) {
        let node = root != null ? this.nodes[root] : this.lastNode;

        if (node !== undefined) {
            node.remove();
        }
    }

    CreateTextNode(text: string, root: number | null) {
        let node = document.createTextNode(text);
        this.checkAppendParent();

        if (root != null) {
            this.nodes[root] = node;
        }
    }

    CreateElement(tag: string, root: number | null) {
        this.lastNode = document.createElement(tag);
        this.checkAppendParent();

        if (root != null) {
            this.nodes[root] = this.lastNode;
        }
    }

    CreatePlaceholder(root: number | null) {
        this.lastNode = document.createElement("div");
        this.lastNode.hidden = true;
        this.checkAppendParent();

        if (root != null) {
            this.nodes[root] = this.lastNode;
        }
    }

    NewEventListener(
        event_name: string,
        root: number,
        handler: { (...args) },
        bubbles: boolean
    ) {
        let node = (root != null ? this.nodes[root] : this.lastNode) as HTMLElement;

        node.setAttribute("data-kine-id", `${root}`);
        this.listeners.create(event_name, node, handler, bubbles);
    }

    RemoveEventListener(root: number, event_name: string, bubbles: boolean) {
        let node = (root != null ? this.nodes[root] : this.lastNode) as HTMLElement;

        node.removeAttribute(`data-kine-id`);
        this.listeners.remove(node, event_name, bubbles);
    }

    SetText(root: number | null, text: string) {
        let node = (root != null ? this.nodes[root] : this.lastNode) as Text;

        node.data = text;
    }

    SetAttribute(root: number | null, field: string, value: string) {
        const name = field;
        let node = (root != null ? this.nodes[root] : this.lastNode) as HTMLElement;

        switch (name) {
            case "value":
                if (value !== (node as HTMLInputElement).value) {
                    (node as HTMLInputElement).value = value;
                }
                break;
            case "checked":
                (node as HTMLInputElement).checked = value === "true";
                break;
            case "selected":
                (node as HTMLOptionElement).selected = value === "true";
                break;
            case "dangerous_inner_html":
                node.innerHTML = value;
                break;
            default:
                // https://github.com/facebook/react/blob/8b88ac2592c5f555f315f9440cbb665dd1e7457a/packages/react-dom/src/shared/DOMProperty.js#L352-L364
                if (value === "false" && bool_attrs.hasOwnProperty(name)) {
                    node.removeAttribute(name);
                } else {
                    node.setAttribute(name, value);
                }
        }
    }

    RemoveAttribute(root: number | null, field: string) {
        const name = field;
        let node = (root != null ? this.nodes[root] : this.lastNode) as HTMLElement;

        if (name === "value") {
            (node as HTMLInputElement).value = "";
        } else if (name === "checked") {
            (node as HTMLInputElement).checked = false;
        } else if (name === "selected") {
            (node as HTMLOptionElement).selected = false;
        } else if (name === "dangerous_inner_html") {
            node.innerHTML = "";
        } else {
            node.removeAttribute(name);
        }
    }

    removeAllChildren(root: number) {
        let node = this.nodes[root] as HTMLElement;
        node.replaceChildren();
    }

    handleEdits(edits: any[]) {
        for (let edit of edits) {
            this.handleEdit(edit);
        }
    }

    handleEdit(edit: EditEvent) {
        switch (edit.type) {
            case "AppendChildren":
                this.AppendChildren(edit.root, edit.children);
                break;
            case "ReplaceWith":
                this.ReplaceWith(edit.root, edit.nodes);
                break;
            case "InsertAfter":
                this.InsertAfter(edit.root, edit.nodes);
                break;
            case "InsertBefore":
                this.InsertBefore(edit.root, edit.nodes);
                break;
            case "Remove":
                this.Remove(edit.root);
                break;
            case "CreateTextNode":
                this.CreateTextNode(edit.text, edit.root);
                break;
            case "CreateElement":
                this.CreateElement(edit.tag, edit.root);
                break;
            case "CreatePlaceholder":
                this.CreatePlaceholder(edit.root);
                break;
            case "RemoveEventListener":
                this.RemoveEventListener(
                    edit.root,
                    edit.event_name,
                    event_bubbles(edit.event_name)
                );
                break;
            case "NewEventListener":
                // this handler is only provided on desktop implementations since this
                // method is not used by the web implementation
                let handler = (event) => {
                    let target = event.target;

                    if (target == null) return;

                    let realId = target.getAttribute(`data-kine-id`);
                    let shouldPreventDefault =
                        target.getAttribute(`kine-prevent-default`);

                    if (event.type === "click") {
                        // todo call prevent default if it's the right type of event
                        if (shouldPreventDefault !== `onclick`) {
                            if (target.tagName === "A") {
                                event.preventDefault();
                                const href = target.getAttribute("href");
                                if (href !== "" && href !== null && href !== undefined) {
                                    this.ipc.send(
                                        serializeIpcMessage("browser_open", { href })
                                    );
                                }
                            }
                        }

                        // also prevent buttons from submitting
                        if (target.tagName === "BUTTON" && event.type == "submit") {
                            event.preventDefault();
                        }
                    }
                    // walk the tree to find the real element
                    while (realId == null) {
                        // we've reached the root we don't want to send an event
                        if (target.parentElement === null) {
                            return;
                        }

                        target = target.parentElement;
                        realId = target.getAttribute(`data-kine-id`);
                    }

                    shouldPreventDefault = target.getAttribute(`kine-prevent-default`);

                    let contents = serialize_event(event);

                    if (shouldPreventDefault === `on${event.type}`) {
                        event.preventDefault();
                    }

                    if (event.type === "submit") {
                        event.preventDefault();
                    }

                    if (
                        target.tagName === "FORM" &&
                        (event.type === "submit" || event.type === "input")
                    ) {
                        for (let x = 0; x < target.elements.length; x++) {
                            let element = target.elements[x];
                            let name = element.getAttribute("name");
                            if (name != null) {
                                if (element.getAttribute("type") === "checkbox") {
                                    // @ts-ignore
                                    contents.values[name] = element.checked ? "true" : "false";
                                } else if (element.getAttribute("type") === "radio") {
                                    if (element.checked) {
                                        contents.values![name] = element.value;
                                    }
                                } else {
                                    // @ts-ignore
                                    contents.values[name] =
                                        element.value ?? element.textContent;
                                }
                            }
                        }
                    }

                    if (realId === null) {
                        return;
                    }
                    realId = parseInt(realId);
                    this.ipc.send(
                        serializeIpcMessage("user_event", {
                            event: edit.event_name,
                            mounted_dom_id: realId,
                            contents: contents,
                        })
                    );
                };
                this.NewEventListener(
                    edit.event_name,
                    edit.root,
                    handler,
                    event_bubbles(edit.event_name)
                );

                break;
            case "SetText":
                this.SetText(edit.root, edit.text);
                break;
            case "SetAttribute":
                this.SetAttribute(edit.root, edit.field, edit.value);
                break;
            case "RemoveAttribute":
                this.RemoveAttribute(edit.root, edit.name);
                break;
            case "EvalMessage":
                eval(edit.code);
                break;
            case "RemoveAllChildren":
                this.removeAllChildren(edit.root);
                break;
        }
    }
}

function serialize_event(event: DomEvent) {
    switch (event.type) {
        case "copy":
        case "cut":
        case "paste": {
            return {};
        }
        case "compositionend":
        case "compositionstart":
        case "compositionupdate": {
            let { data } = event;
            return {
                data,
            };
        }
        case "keydown":
        case "keypress":
        case "keyup": {
            let {
                charCode,
                key,
                altKey,
                ctrlKey,
                metaKey,
                keyCode,
                shiftKey,
                location,
                repeat,
                which,
                code,
            } = event;
            return {
                char_code: charCode,
                key: key,
                alt_key: altKey,
                ctrl_key: ctrlKey,
                meta_key: metaKey,
                key_code: keyCode,
                shift_key: shiftKey,
                location,
                repeat,
                which,
                code,
            };
        }
        case "focus":
        case "blur": {
            return {};
        }
        case "change": {
            let target = event.target as HTMLInputElement;
            let value;
            if (target.type === "checkbox" || target.type === "radio") {
                value = target.checked ? "true" : "false";
            } else {
                value = target.value ?? target.textContent;
            }
            return {
                value: value,
                values: {},
            };
        }
        case "input":
        case "invalid":
        case "reset":
        case "submit": {
            let target = event.target as HTMLInputElement;
            let value = target.value ?? target.textContent;

            if (target.type === "checkbox") {
                value = target.checked ? "true" : "false";
            }

            return {
                value: value,
                values: {},
            };
        }
        case "click":
        case "contextmenu":
        case "doubleclick":
        case "dblclick":
        case "drag":
        case "dragend":
        case "dragenter":
        case "dragexit":
        case "dragleave":
        case "dragover":
        case "dragstart":
        case "drop":
        case "mousedown":
        case "mouseenter":
        case "mouseleave":
        case "mousemove":
        case "mouseout":
        case "mouseover":
        case "mouseup": {
            const {
                altKey,
                button,
                buttons,
                clientX,
                clientY,
                ctrlKey,
                metaKey,
                offsetX,
                offsetY,
                pageX,
                pageY,
                screenX,
                screenY,
                shiftKey,
            } = event;
            return {
                alt_key: altKey,
                button: button,
                buttons: buttons,
                client_x: clientX,
                client_y: clientY,
                ctrl_key: ctrlKey,
                meta_key: metaKey,
                offset_x: offsetX,
                offset_y: offsetY,
                page_x: pageX,
                page_y: pageY,
                screen_x: screenX,
                screen_y: screenY,
                shift_key: shiftKey,
            };
        }
        case "pointerdown":
        case "pointermove":
        case "pointerup":
        case "pointercancel":
        case "gotpointercapture":
        case "lostpointercapture":
        case "pointerenter":
        case "pointerleave":
        case "pointerover":
        case "pointerout": {
            const {
                altKey,
                button,
                buttons,
                clientX,
                clientY,
                ctrlKey,
                metaKey,
                pageX,
                pageY,
                screenX,
                screenY,
                shiftKey,
                pointerId,
                width,
                height,
                pressure,
                tangentialPressure,
                tiltX,
                tiltY,
                twist,
                pointerType,
                isPrimary,
            } = event;
            return {
                alt_key: altKey,
                button: button,
                buttons: buttons,
                client_x: clientX,
                client_y: clientY,
                ctrl_key: ctrlKey,
                meta_key: metaKey,
                page_x: pageX,
                page_y: pageY,
                screen_x: screenX,
                screen_y: screenY,
                shift_key: shiftKey,
                pointer_id: pointerId,
                width: width,
                height: height,
                pressure: pressure,
                tangential_pressure: tangentialPressure,
                tilt_x: tiltX,
                tilt_y: tiltY,
                twist: twist,
                pointer_type: pointerType,
                is_primary: isPrimary,
            };
        }
        case "select": {
            return {};
        }
        case "touchcancel":
        case "touchend":
        case "touchmove":
        case "touchstart": {
            const { altKey, ctrlKey, metaKey, shiftKey } = event;
            return {
                // changed_touches: event.changedTouches,
                // target_touches: event.targetTouches,
                // touches: event.touches,
                alt_key: altKey,
                ctrl_key: ctrlKey,
                meta_key: metaKey,
                shift_key: shiftKey,
            };
        }
        case "scroll": {
            return {};
        }
        case "wheel": {
            const { deltaX, deltaY, deltaZ, deltaMode } = event;
            return {
                delta_x: deltaX,
                delta_y: deltaY,
                delta_z: deltaZ,
                delta_mode: deltaMode,
            };
        }
        case "animationstart":
        case "animationend":
        case "animationiteration": {
            const { animationName, elapsedTime, pseudoElement } = event;
            return {
                animation_name: animationName,
                elapsed_time: elapsedTime,
                pseudo_element: pseudoElement,
            };
        }
        case "transitionend": {
            const { propertyName, elapsedTime, pseudoElement } = event;
            return {
                property_name: propertyName,
                elapsed_time: elapsedTime,
                pseudo_element: pseudoElement,
            };
        }
        case "abort":
        case "canplay":
        case "canplaythrough":
        case "durationchange":
        case "emptied":
        case "encrypted":
        case "ended":
        case "error":
        case "loadeddata":
        case "loadedmetadata":
        case "loadstart":
        case "pause":
        case "play":
        case "playing":
        case "progress":
        case "ratechange":
        case "seeked":
        case "seeking":
        case "stalled":
        case "suspend":
        case "timeupdate":
        case "volumechange":
        case "waiting": {
            return {};
        }
        case "toggle": {
            return {};
        }
        default: {
            return {};
        }
    }
}
function serializeIpcMessage(method: any, params: any = {}) {
    return msgpack.encode({ method, params });
}

const bool_attrs = {
    allowfullscreen: true,
    allowpaymentrequest: true,
    async: true,
    autofocus: true,
    autoplay: true,
    checked: true,
    controls: true,
    default: true,
    defer: true,
    disabled: true,
    formnovalidate: true,
    hidden: true,
    ismap: true,
    itemscope: true,
    loop: true,
    multiple: true,
    muted: true,
    nomodule: true,
    novalidate: true,
    open: true,
    playsinline: true,
    readonly: true,
    required: true,
    reversed: true,
    selected: true,
    truespeed: true,
};

function is_element_node(node: Node) {
    return node.nodeType == 1;
}

function event_bubbles(event: string) {
    return (
        event in
        [
            "copy",
            "cut",
            "paste",
            "compositionend",
            "compositionstart",
            "compositionupdate",
            "keydown",
            "keypress",
            "keyup",
            "focusout",
            "focusin",
            "change",
            "input",
            "invalid",
            "reset",
            "submit",
            "click",
            "contextmenu",
            "doubleclick",
            "dblclick",
            "drag",
            "dragend",
            "dragleave",
            "dragover",
            "dragstart",
            "drop",
            "mousedown",
            "mousemove",
            "mouseout",
            "mouseover",
            "mouseup",
            "pointerdown",
            "pointermove",
            "pointerup",
            "pointercancel",
            "gotpointercapture",
            "lostpointercapture",
            "pointerover",
            "pointerout",
            "select",
            "touchcancel",
            "touchend",
            "touchmove",
            "touchstart",
            "wheel",
            "encrypted",
            "animationstart",
            "animationend",
            "animationiteration",
            "transitionend",
            "toggle",
        ]
    );
}
