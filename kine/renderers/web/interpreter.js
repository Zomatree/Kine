var __awaiter = (this && this.__awaiter) || function (thisArg, _arguments, P, generator) {
    function adopt(value) { return value instanceof P ? value : new P(function (resolve) { resolve(value); }); }
    return new (P || (P = Promise))(function (resolve, reject) {
        function fulfilled(value) { try { step(generator.next(value)); } catch (e) { reject(e); } }
        function rejected(value) { try { step(generator["throw"](value)); } catch (e) { reject(e); } }
        function step(result) { result.done ? resolve(result.value) : adopt(result.value).then(fulfilled, rejected); }
        step((generator = generator.apply(thisArg, _arguments || [])).next());
    });
};
var __generator = (this && this.__generator) || function (thisArg, body) {
    var _ = { label: 0, sent: function() { if (t[0] & 1) throw t[1]; return t[1]; }, trys: [], ops: [] }, f, y, t, g;
    return g = { next: verb(0), "throw": verb(1), "return": verb(2) }, typeof Symbol === "function" && (g[Symbol.iterator] = function() { return this; }), g;
    function verb(n) { return function (v) { return step([n, v]); }; }
    function step(op) {
        if (f) throw new TypeError("Generator is already executing.");
        while (g && (g = 0, op[0] && (_ = 0)), _) try {
            if (f = 1, y && (t = op[0] & 2 ? y["return"] : op[0] ? y["throw"] || ((t = y["return"]) && t.call(y), 0) : y.next) && !(t = t.call(y, op[1])).done) return t;
            if (y = 0, t) op = [op[0] & 2, t.value];
            switch (op[0]) {
                case 0: case 1: t = op; break;
                case 4: _.label++; return { value: op[1], done: false };
                case 5: _.label++; y = op[1]; op = [0]; continue;
                case 7: op = _.ops.pop(); _.trys.pop(); continue;
                default:
                    if (!(t = _.trys, t = t.length > 0 && t[t.length - 1]) && (op[0] === 6 || op[0] === 2)) { _ = 0; continue; }
                    if (op[0] === 3 && (!t || (op[1] > t[0] && op[1] < t[3]))) { _.label = op[1]; break; }
                    if (op[0] === 6 && _.label < t[1]) { _.label = t[1]; t = op; break; }
                    if (t && _.label < t[2]) { _.label = t[2]; _.ops.push(op); break; }
                    if (t[2]) _.ops.pop();
                    _.trys.pop(); continue;
            }
            op = body.call(thisArg, _);
        } catch (e) { op = [6, e]; y = 0; } finally { f = t = 0; }
        if (op[0] & 5) throw op[1]; return { value: op[0] ? op[1] : void 0, done: true };
    }
};
var __values = (this && this.__values) || function(o) {
    var s = typeof Symbol === "function" && Symbol.iterator, m = s && o[s], i = 0;
    if (m) return m.call(o);
    if (o && typeof o.length === "number") return {
        next: function () {
            if (o && i >= o.length) o = void 0;
            return { value: o && o[i++], done: !o };
        }
    };
    throw new TypeError(s ? "Object is not iterable." : "Symbol.iterator is not defined.");
};
var __read = (this && this.__read) || function (o, n) {
    var m = typeof Symbol === "function" && o[Symbol.iterator];
    if (!m) return o;
    var i = m.call(o), r, ar = [], e;
    try {
        while ((n === void 0 || n-- > 0) && !(r = i.next()).done) ar.push(r.value);
    }
    catch (error) { e = { error: error }; }
    finally {
        try {
            if (r && !r.done && (m = i["return"])) m.call(i);
        }
        finally { if (e) throw e.error; }
    }
    return ar;
};
var __spreadArray = (this && this.__spreadArray) || function (to, from, pack) {
    if (pack || arguments.length === 2) for (var i = 0, l = from.length, ar; i < l; i++) {
        if (ar || !(i in from)) {
            if (!ar) ar = Array.prototype.slice.call(from, 0, i);
            ar[i] = from[i];
        }
    }
    return to.concat(ar || Array.prototype.slice.call(from));
};
// original code is from https://github.com/DioxusLabs/dioxus/blob/master/packages/liveview/src/interpreter.js and is licensed under the MIT license
var ipc;
function main(ws_addr) {
    var root = window.document.getElementById("main");
    if (root != null) {
        ipc = new IPC(root, ws_addr);
    }
}
var IPC = /** @class */ (function () {
    function IPC(root, ws_addr) {
        var _this = this;
        this.interpreter = new Interpreter(root, this);
        this.ws = new WebSocket(ws_addr);
        this.ws.onopen = function () {
            console.log("Connected to the websocket");
            _this.send(serializeIpcMessage("initialize"));
        };
        this.ws.onerror = function (err) {
            console.error("Error: ", err);
        };
        this.ws.onmessage = function (event) { return __awaiter(_this, void 0, void 0, function () {
            var data, view, edits;
            return __generator(this, function (_a) {
                switch (_a.label) {
                    case 0: return [4 /*yield*/, event.data.arrayBuffer()];
                    case 1:
                        data = _a.sent();
                        view = new Uint8Array(data);
                        edits = msgpack.decode(view);
                        this.interpreter.handleEdits(edits);
                        return [2 /*return*/];
                }
            });
        }); };
    }
    IPC.prototype.send = function (msg) {
        this.ws.send(msg);
    };
    return IPC;
}());
var ListenerMap = /** @class */ (function () {
    function ListenerMap(root) {
        // bubbling events can listen at the root element
        this.global = new Map();
        // non bubbling events listen at the element the listener was created at
        this.local = new Map();
        this.root = root;
    }
    ListenerMap.prototype.create = function (event_name, element, handler, bubbles) {
        if (bubbles) {
            var global = this.global.get(event_name);
            if (!global) {
                this.global.set(event_name, {
                    active: 1,
                    callback: handler
                });
                this.root.addEventListener(event_name, handler);
            }
            else {
                global.active++;
            }
        }
        else {
            var id = element.getAttribute("data-kine-id");
            var local = this.local.get(id);
            if (!local) {
                local = new Map();
                this.local.set(id, local);
            }
            local.set(event_name, handler);
            element.addEventListener(event_name, handler);
        }
    };
    ListenerMap.prototype.remove = function (element, event_name, bubbles) {
        if (bubbles) {
            this.global[event_name].active--;
            if (this.global[event_name].active === 0) {
                this.root.removeEventListener(event_name, this.global[event_name].callback);
                delete this.global[event_name];
            }
        }
        else {
            var id = element.getAttribute("data-kine-id");
            var element_listeners = this.local.get(id);
            var handler = element_listeners.get(event_name);
            element_listeners["delete"](event_name);
            if (element_listeners.size === 0) {
                this.local["delete"](id);
            }
            element.removeEventListener(event_name, handler);
        }
    };
    return ListenerMap;
}());
var Interpreter = /** @class */ (function () {
    function Interpreter(root, ipc) {
        this.root = root;
        this.ipc = ipc;
        this.lastNode = root;
        this.listeners = new ListenerMap(root);
        this.nodes = [root];
        this.parents = [];
    }
    Interpreter.prototype.checkAppendParent = function () {
        if (this.parents.length > 0) {
            var lastParent = this.parents[this.parents.length - 1];
            lastParent[1]--;
            if (lastParent[1] === 0) {
                this.parents.pop();
            }
            lastParent[0].appendChild(this.lastNode);
        }
    };
    Interpreter.prototype.AppendChildren = function (root, children) {
        var e_1, _a;
        var node = root != null ? this.nodes[root] : this.lastNode;
        try {
            for (var children_1 = __values(children), children_1_1 = children_1.next(); !children_1_1.done; children_1_1 = children_1.next()) {
                var child = children_1_1.value;
                node.appendChild(this.nodes[child]);
            }
        }
        catch (e_1_1) { e_1 = { error: e_1_1 }; }
        finally {
            try {
                if (children_1_1 && !children_1_1.done && (_a = children_1["return"])) _a.call(children_1);
            }
            finally { if (e_1) throw e_1.error; }
        }
    };
    Interpreter.prototype.ReplaceWith = function (root, nodes) {
        var e_2, _a;
        var node = root != null ? this.nodes[root] : this.lastNode;
        var els = [];
        try {
            for (var nodes_1 = __values(nodes), nodes_1_1 = nodes_1.next(); !nodes_1_1.done; nodes_1_1 = nodes_1.next()) {
                var new_node = nodes_1_1.value;
                els.push(this.nodes[new_node]);
            }
        }
        catch (e_2_1) { e_2 = { error: e_2_1 }; }
        finally {
            try {
                if (nodes_1_1 && !nodes_1_1.done && (_a = nodes_1["return"])) _a.call(nodes_1);
            }
            finally { if (e_2) throw e_2.error; }
        }
        ;
        console.log(node, els);
        node.replaceWith.apply(node, __spreadArray([], __read(els), false));
    };
    Interpreter.prototype.InsertAfter = function (root, nodes) {
        var e_3, _a;
        var node = root != null ? this.nodes[root] : this.lastNode;
        var els = [];
        try {
            for (var nodes_2 = __values(nodes), nodes_2_1 = nodes_2.next(); !nodes_2_1.done; nodes_2_1 = nodes_2.next()) {
                var new_node = nodes_2_1.value;
                els.push(this.nodes[new_node]);
            }
        }
        catch (e_3_1) { e_3 = { error: e_3_1 }; }
        finally {
            try {
                if (nodes_2_1 && !nodes_2_1.done && (_a = nodes_2["return"])) _a.call(nodes_2);
            }
            finally { if (e_3) throw e_3.error; }
        }
        node.after.apply(node, __spreadArray([], __read(els), false));
    };
    Interpreter.prototype.InsertBefore = function (root, nodes) {
        var e_4, _a;
        var node = root != null ? this.nodes[root] : this.lastNode;
        var els = [];
        try {
            for (var nodes_3 = __values(nodes), nodes_3_1 = nodes_3.next(); !nodes_3_1.done; nodes_3_1 = nodes_3.next()) {
                var new_node = nodes_3_1.value;
                els.push(this.nodes[new_node]);
            }
        }
        catch (e_4_1) { e_4 = { error: e_4_1 }; }
        finally {
            try {
                if (nodes_3_1 && !nodes_3_1.done && (_a = nodes_3["return"])) _a.call(nodes_3);
            }
            finally { if (e_4) throw e_4.error; }
        }
        node.before.apply(node, __spreadArray([], __read(els), false));
    };
    Interpreter.prototype.Remove = function (root) {
        var node = root != null ? this.nodes[root] : this.lastNode;
        if (node !== undefined) {
            node.remove();
        }
    };
    Interpreter.prototype.CreateTextNode = function (text, root) {
        var node = document.createTextNode(text);
        this.checkAppendParent();
        if (root != null) {
            this.nodes[root] = node;
        }
    };
    Interpreter.prototype.CreateElement = function (tag, root) {
        this.lastNode = document.createElement(tag);
        this.checkAppendParent();
        if (root != null) {
            this.nodes[root] = this.lastNode;
        }
    };
    Interpreter.prototype.CreatePlaceholder = function (root) {
        this.lastNode = document.createElement("div");
        this.lastNode.hidden = true;
        this.checkAppendParent();
        if (root != null) {
            this.nodes[root] = this.lastNode;
        }
    };
    Interpreter.prototype.NewEventListener = function (event_name, root, handler, bubbles) {
        var node = (root != null ? this.nodes[root] : this.lastNode);
        node.setAttribute("data-kine-id", "".concat(root));
        this.listeners.create(event_name, node, handler, bubbles);
    };
    Interpreter.prototype.RemoveEventListener = function (root, event_name, bubbles) {
        var node = (root != null ? this.nodes[root] : this.lastNode);
        node.removeAttribute("data-kine-id");
        this.listeners.remove(node, event_name, bubbles);
    };
    Interpreter.prototype.SetText = function (root, text) {
        var node = (root != null ? this.nodes[root] : this.lastNode);
        node.data = text;
    };
    Interpreter.prototype.SetAttribute = function (root, field, value) {
        var name = field;
        var node = (root != null ? this.nodes[root] : this.lastNode);
        switch (name) {
            case "value":
                if (value !== node.value) {
                    node.value = value;
                }
                break;
            case "checked":
                node.checked = value === "true";
                break;
            case "selected":
                node.selected = value === "true";
                break;
            case "dangerous_inner_html":
                node.innerHTML = value;
                break;
            default:
                // https://github.com/facebook/react/blob/8b88ac2592c5f555f315f9440cbb665dd1e7457a/packages/react-dom/src/shared/DOMProperty.js#L352-L364
                if (value === "false" && bool_attrs.hasOwnProperty(name)) {
                    node.removeAttribute(name);
                }
                else {
                    node.setAttribute(name, value);
                }
        }
    };
    Interpreter.prototype.RemoveAttribute = function (root, field) {
        var name = field;
        var node = (root != null ? this.nodes[root] : this.lastNode);
        if (name === "value") {
            node.value = "";
        }
        else if (name === "checked") {
            node.checked = false;
        }
        else if (name === "selected") {
            node.selected = false;
        }
        else if (name === "dangerous_inner_html") {
            node.innerHTML = "";
        }
        else {
            node.removeAttribute(name);
        }
    };
    Interpreter.prototype.CloneNode = function (old, new_id) {
        var node = old ? this.nodes[old] : this.lastNode;
        this.nodes[new_id] = node.cloneNode(true);
    };
    Interpreter.prototype.CloneNodeChildren = function (old, new_ids) {
        var e_5, _a;
        var node = old ? this.nodes[old] : this.lastNode;
        var old_node = node.cloneNode(true);
        try {
            for (var _b = __values(Array.from(node.childNodes).entries()), _c = _b.next(); !_c.done; _c = _b.next()) {
                var _d = __read(_c.value, 2), i = _d[0], child = _d[1];
                this.nodes[new_ids[i]] = child;
            }
        }
        catch (e_5_1) { e_5 = { error: e_5_1 }; }
        finally {
            try {
                if (_c && !_c.done && (_a = _b["return"])) _a.call(_b);
            }
            finally { if (e_5) throw e_5.error; }
        }
    };
    Interpreter.prototype.FirstChild = function () {
        this.lastNode = this.lastNode.firstChild;
    };
    Interpreter.prototype.NextSibling = function () {
        this.lastNode = this.lastNode.nextSibling;
    };
    Interpreter.prototype.ParentNode = function () {
        this.lastNode = this.lastNode.parentNode;
    };
    Interpreter.prototype.StoreWithId = function (id) {
        this.nodes[id] = this.lastNode;
    };
    Interpreter.prototype.SetLastNode = function (root) {
        this.lastNode = this.nodes[root];
    };
    Interpreter.prototype.handleEdits = function (edits) {
        var e_6, _a;
        try {
            for (var edits_1 = __values(edits), edits_1_1 = edits_1.next(); !edits_1_1.done; edits_1_1 = edits_1.next()) {
                var edit = edits_1_1.value;
                this.handleEdit(edit);
            }
        }
        catch (e_6_1) { e_6 = { error: e_6_1 }; }
        finally {
            try {
                if (edits_1_1 && !edits_1_1.done && (_a = edits_1["return"])) _a.call(edits_1);
            }
            finally { if (e_6) throw e_6.error; }
        }
    };
    Interpreter.prototype.handleEdit = function (edit) {
        var _this = this;
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
                this.RemoveEventListener(edit.root, edit.event_name, event_bubbles(edit.event_name));
                break;
            case "NewEventListener":
                // this handler is only provided on desktop implementations since this
                // method is not used by the web implementation
                var handler = function (event) {
                    var _a;
                    var target = event.target;
                    if (target != null) {
                        var realId = target.getAttribute("data-kine-id");
                        var shouldPreventDefault = target.getAttribute("kine-prevent-default");
                        if (event.type === "click") {
                            // todo call prevent default if it's the right type of event
                            if (shouldPreventDefault !== "onclick") {
                                if (target.tagName === "A") {
                                    event.preventDefault();
                                    var href = target.getAttribute("href");
                                    if (href !== "" && href !== null && href !== undefined) {
                                        _this.ipc.send(serializeIpcMessage("browser_open", { href: href }));
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
                            realId = target.getAttribute("data-kine-id");
                        }
                        shouldPreventDefault = target.getAttribute("kine-prevent-default");
                        var contents = serialize_event(event);
                        if (shouldPreventDefault === "on".concat(event.type)) {
                            event.preventDefault();
                        }
                        if (event.type === "submit") {
                            event.preventDefault();
                        }
                        if (target.tagName === "FORM" &&
                            (event.type === "submit" || event.type === "input")) {
                            for (var x = 0; x < target.elements.length; x++) {
                                var element = target.elements[x];
                                var name_1 = element.getAttribute("name");
                                if (name_1 != null) {
                                    if (element.getAttribute("type") === "checkbox") {
                                        // @ts-ignore
                                        contents.values[name_1] = element.checked ? "true" : "false";
                                    }
                                    else if (element.getAttribute("type") === "radio") {
                                        if (element.checked) {
                                            contents.values[name_1] = element.value;
                                        }
                                    }
                                    else {
                                        // @ts-ignore
                                        contents.values[name_1] =
                                            (_a = element.value) !== null && _a !== void 0 ? _a : element.textContent;
                                    }
                                }
                            }
                        }
                        if (realId === null) {
                            return;
                        }
                        realId = parseInt(realId);
                        _this.ipc.send(serializeIpcMessage("user_event", {
                            event: edit.event_name,
                            mounted_dom_id: realId,
                            contents: contents
                        }));
                    }
                };
                this.NewEventListener(edit.event_name, edit.root, handler, event_bubbles(edit.event_name));
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
            case "CloneNode":
                this.CloneNode(edit.id, edit.new_id);
                break;
            case "CloneNodeChildren":
                this.CloneNodeChildren(edit.id, edit.new_ids);
                break;
            case "FirstChild":
                this.FirstChild();
                break;
            case "NextSibling":
                this.NextSibling();
                break;
            case "ParentNode":
                this.ParentNode();
                break;
            case "StoreWithId":
                this.StoreWithId(edit.id);
                break;
            case "SetLastNode":
                this.SetLastNode(edit.id);
                break;
            case "EvalMessage":
                eval(edit.code);
                break;
        }
    };
    return Interpreter;
}());
function serialize_event(event) {
    var _a, _b;
    switch (event.type) {
        case "copy":
        case "cut":
        case "paste": {
            return {};
        }
        case "compositionend":
        case "compositionstart":
        case "compositionupdate": {
            var data = event.data;
            return {
                data: data
            };
        }
        case "keydown":
        case "keypress":
        case "keyup": {
            var charCode = event.charCode, key = event.key, altKey = event.altKey, ctrlKey = event.ctrlKey, metaKey = event.metaKey, keyCode = event.keyCode, shiftKey = event.shiftKey, location_1 = event.location, repeat = event.repeat, which = event.which, code = event.code;
            return {
                char_code: charCode,
                key: key,
                alt_key: altKey,
                ctrl_key: ctrlKey,
                meta_key: metaKey,
                key_code: keyCode,
                shift_key: shiftKey,
                location: location_1,
                repeat: repeat,
                which: which,
                code: code
            };
        }
        case "focus":
        case "blur": {
            return {};
        }
        case "change": {
            var target = event.target;
            var value = void 0;
            if (target.type === "checkbox" || target.type === "radio") {
                value = target.checked ? "true" : "false";
            }
            else {
                value = (_a = target.value) !== null && _a !== void 0 ? _a : target.textContent;
            }
            return {
                value: value,
                values: {}
            };
        }
        case "input":
        case "invalid":
        case "reset":
        case "submit": {
            var target = event.target;
            var value = (_b = target.value) !== null && _b !== void 0 ? _b : target.textContent;
            if (target.type === "checkbox") {
                value = target.checked ? "true" : "false";
            }
            return {
                value: value,
                values: {}
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
            var altKey = event.altKey, button = event.button, buttons = event.buttons, clientX = event.clientX, clientY = event.clientY, ctrlKey = event.ctrlKey, metaKey = event.metaKey, offsetX = event.offsetX, offsetY = event.offsetY, pageX = event.pageX, pageY = event.pageY, screenX_1 = event.screenX, screenY_1 = event.screenY, shiftKey = event.shiftKey;
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
                screen_x: screenX_1,
                screen_y: screenY_1,
                shift_key: shiftKey
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
            var altKey = event.altKey, button = event.button, buttons = event.buttons, clientX = event.clientX, clientY = event.clientY, ctrlKey = event.ctrlKey, metaKey = event.metaKey, pageX = event.pageX, pageY = event.pageY, screenX_2 = event.screenX, screenY_2 = event.screenY, shiftKey = event.shiftKey, pointerId = event.pointerId, width = event.width, height = event.height, pressure = event.pressure, tangentialPressure = event.tangentialPressure, tiltX = event.tiltX, tiltY = event.tiltY, twist = event.twist, pointerType = event.pointerType, isPrimary = event.isPrimary;
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
                screen_x: screenX_2,
                screen_y: screenY_2,
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
                is_primary: isPrimary
            };
        }
        case "select": {
            return {};
        }
        case "touchcancel":
        case "touchend":
        case "touchmove":
        case "touchstart": {
            var altKey = event.altKey, ctrlKey = event.ctrlKey, metaKey = event.metaKey, shiftKey = event.shiftKey;
            return {
                // changed_touches: event.changedTouches,
                // target_touches: event.targetTouches,
                // touches: event.touches,
                alt_key: altKey,
                ctrl_key: ctrlKey,
                meta_key: metaKey,
                shift_key: shiftKey
            };
        }
        case "scroll": {
            return {};
        }
        case "wheel": {
            var deltaX = event.deltaX, deltaY = event.deltaY, deltaZ = event.deltaZ, deltaMode = event.deltaMode;
            return {
                delta_x: deltaX,
                delta_y: deltaY,
                delta_z: deltaZ,
                delta_mode: deltaMode
            };
        }
        case "animationstart":
        case "animationend":
        case "animationiteration": {
            var animationName = event.animationName, elapsedTime = event.elapsedTime, pseudoElement = event.pseudoElement;
            return {
                animation_name: animationName,
                elapsed_time: elapsedTime,
                pseudo_element: pseudoElement
            };
        }
        case "transitionend": {
            var propertyName = event.propertyName, elapsedTime = event.elapsedTime, pseudoElement = event.pseudoElement;
            return {
                property_name: propertyName,
                elapsed_time: elapsedTime,
                pseudo_element: pseudoElement
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
function serializeIpcMessage(method, params) {
    if (params === void 0) { params = {}; }
    return msgpack.encode({ method: method, params: params });
}
;
var bool_attrs = {
    allowfullscreen: true,
    allowpaymentrequest: true,
    async: true,
    autofocus: true,
    autoplay: true,
    checked: true,
    controls: true,
    "default": true,
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
    truespeed: true
};
function is_element_node(node) {
    return node.nodeType == 1;
}
function event_bubbles(event) {
    switch (event) {
        case "copy":
            return true;
        case "cut":
            return true;
        case "paste":
            return true;
        case "compositionend":
            return true;
        case "compositionstart":
            return true;
        case "compositionupdate":
            return true;
        case "keydown":
            return true;
        case "keypress":
            return true;
        case "keyup":
            return true;
        case "focus":
            return false;
        case "focusout":
            return true;
        case "focusin":
            return true;
        case "blur":
            return false;
        case "change":
            return true;
        case "input":
            return true;
        case "invalid":
            return true;
        case "reset":
            return true;
        case "submit":
            return true;
        case "click":
            return true;
        case "contextmenu":
            return true;
        case "doubleclick":
            return true;
        case "dblclick":
            return true;
        case "drag":
            return true;
        case "dragend":
            return true;
        case "dragenter":
            return false;
        case "dragexit":
            return false;
        case "dragleave":
            return true;
        case "dragover":
            return true;
        case "dragstart":
            return true;
        case "drop":
            return true;
        case "mousedown":
            return true;
        case "mouseenter":
            return false;
        case "mouseleave":
            return false;
        case "mousemove":
            return true;
        case "mouseout":
            return true;
        case "scroll":
            return false;
        case "mouseover":
            return true;
        case "mouseup":
            return true;
        case "pointerdown":
            return true;
        case "pointermove":
            return true;
        case "pointerup":
            return true;
        case "pointercancel":
            return true;
        case "gotpointercapture":
            return true;
        case "lostpointercapture":
            return true;
        case "pointerenter":
            return false;
        case "pointerleave":
            return false;
        case "pointerover":
            return true;
        case "pointerout":
            return true;
        case "select":
            return true;
        case "touchcancel":
            return true;
        case "touchend":
            return true;
        case "touchmove":
            return true;
        case "touchstart":
            return true;
        case "wheel":
            return true;
        case "abort":
            return false;
        case "canplay":
            return false;
        case "canplaythrough":
            return false;
        case "durationchange":
            return false;
        case "emptied":
            return false;
        case "encrypted":
            return true;
        case "ended":
            return false;
        case "error":
            return false;
        case "loadeddata":
            return false;
        case "loadedmetadata":
            return false;
        case "loadstart":
            return false;
        case "pause":
            return false;
        case "play":
            return false;
        case "playing":
            return false;
        case "progress":
            return false;
        case "ratechange":
            return false;
        case "seeked":
            return false;
        case "seeking":
            return false;
        case "stalled":
            return false;
        case "suspend":
            return false;
        case "timeupdate":
            return false;
        case "volumechange":
            return false;
        case "waiting":
            return false;
        case "animationstart":
            return true;
        case "animationend":
            return true;
        case "animationiteration":
            return true;
        case "transitionend":
            return true;
        case "toggle":
            return true;
        default:
            throw "";
    }
}
