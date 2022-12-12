from typing import Any, Callable, Iterator, Literal, TypedDict, overload, TypeVar, Generic
from typing_extensions import NotRequired, Unpack, Self

T = TypeVar("T")

class Array(Generic[T]):
    pass

class EventTarget:
    @overload
    def addEventListener(self, type: str, listener: Any) -> None:
        ...

    @overload
    def addEventListener(self, type: str, listener: Any, options: Any) -> None:
        ...

    @overload
    def addEventListener(self, type: str, listener: Any, useCapture: bool) -> None:
        ...

    def dispatchEvent(self, event: str) -> bool:
        ...

    @overload
    def removeEventListener(self, type: str, listener: Any) -> None:
        ...

    @overload
    def removeEventListener(self, type: str, listener: Any, options: Any) -> None:
        ...

    @overload
    def removeEventListener(self, type: str, listener: Any, useCapture: bool) -> None:
        ...

class NodeList:
    length: int

    def __iter__(self) -> Iterator[Node]:
        ...

    def __len__(self) -> int:
        ...

    def entries(self) -> Iterator[Array[Any[Any]]]:
        ...

    @overload
    def forEach(self, callback: Any) -> None:
        ...

    @overload
    def forEach(self, callback: Any, thisArg: Any) -> None:
        ...

    def item(self, index: int) -> Node | None:
        ...

    def keys(self) -> Iterator[int]:
        ...

    def values(self) -> Iterator[Node]:
        ...

class Node(EventTarget):
    baseURI: str
    childNodes: NodeList
    firstChild: Node | None
    isConnected: bool
    lastChild: Node | None
    nextSibling: Node | None
    nodeName: str
    nodeType: int
    nodeValue: str
    ownerDocument: Document
    parentElement: Element
    parentNode: Node
    previousSibling: Node | None
    textContent: Node | None

    def appendChild(self, aChild: Node) -> Node:
        ...

    @overload
    def cloneNode(self) -> Node:
        ...

    @overload
    def cloneNode(self, deep: bool) -> Node:
        ...

    def compareDocumentPosition(self, otherNode: Node) -> int:
        ...

    def contains(self, otherNode: Node) -> bool:
        ...

    @overload
    def getRootNode(self) -> Node:
        ...

    @overload
    def getRootNode(self, options: Any) -> Node:
        ...

    def hasChildNodes(self) -> bool:
        ...

    def insertBefore(self, newNode: Node, referenceNode: Node) -> Node:
        ...

    def isDefaultNamespace(self, namespaceURI: str) -> bool:
        ...

    def isEqualNode(self, otherNode: Node) -> bool:
        ...

    def isSameNode(self, otherNode: Node) -> bool:
        ...

    def lookupNamespaceURI(self, prefix: str | None) -> str:
        ...

    def lookupPrefix(self, namespace: str | None) -> str:
        ...

    def normalizE(self) -> None:
        ...

    def removeChild(self, child: Node) -> None:
        ...

    def replaceChild(self, newChild: Node, oldChild: Node) -> Node:
        ...

class Attr(Node):
    localName: str
    name: str
    namespaceURI: str | None
    ownerElement: Element | None
    prefix: str | None
    value: str

class NamedNodeMap:
    length: int

    def __getitem__(self, name: str) -> Attr | None:
        ...

    def getNamedItem(self, name: str) -> Attr | None:
        ...

    def getNameditemNS(self, namespace: str, localName: str) -> Attr | None:
        ...

    def removeNamedItem(self, attrName: str) -> Attr | None:
        ...

    def removeNameditemNS(self, namespace: str, localName: str) -> Attr | None:
        ...

    def setNamedItem(self, attr: Attr) -> Attr | None:
        ...

    def setNamedItemNS(self, attr: Attr) -> Attr | None:
        ...

class HTMLCollection:
    length: int

    def item(self, index: int) -> Node | None:
        ...

    def namedItem(self, key: str) -> Element | None:
        ...

class DOMTokenList:
    length: int
    value: str

    def __getitem__(self, index: int) -> str | None:
        ...

    def add(self, *items: str) -> None:
        ...

    def contains(self, token: str) -> bool:
        ...

    def entries(self) -> Iterator[Array[Any]]:
        ...

    @overload
    def forEach(self, callback: Any) -> None:
        ...

    @overload
    def forEach(self, callback: Any, thisArg: Any) -> None:
        ...

    def item(self, index: int) -> str | None:
        ...

    def keys(self) -> Iterator[int]:
        ...

    def remove(self, *items: str) -> None:
        ...

    def replace(self, oldToken: str, newToken: str) -> bool:
        ...

    def supports(self, token: str) -> bool:
        ...

    @overload
    def toggle(self, token: str) -> bool:
        ...

    @overload
    def toggle(self, token: str, force: bool) -> bool:
        ...

    def values(self) -> Iterator[str]:
        ...

class DocumentFragment(Node):
    childElementCount: int
    children: HTMLCollection
    firstElementChild: Element | None
    lastElementChild: Element | None

    def append(self, *param: Node | str) -> None:
        ...

    def prepend(self, *param: Node | str) -> None:
        ...

    def querySelector(self, selectors: str) -> Element | None:
        ...

    def querySelectorAll(self, selectors: str) -> Element | None:
        ...

    def replaceChildren(self, *param: Node | str) -> None:
        ...

class ShadowRoot(DocumentFragment):
    activeElement: Element | None
    delegatesFocus: bool
    fullscreenElement: Element | None
    host: Element
    innerHTML: str
    mode: Literal["open", "closed"]
    pictureInPictureElement: Element | None
    pointerLockElement: Element | None

class Animation:
    pass

class Element(Node):
    assignedSlot: Element | None
    attributes: NamedNodeMap
    childElementCount: int
    children: HTMLCollection
    classList: DOMTokenList
    className: str
    clientHeight: int
    clientLeft: int
    clientTop: int
    clientWidth: int
    firstElementChild: Element | None
    id: str
    innerHTML: str
    lastElementChild: Element | None
    localName: str
    namespaceURI: str | None
    nextElementSibling: Element | None
    outerHTML: str
    part: DOMTokenList
    prefix: str | None
    previousElementSibling: Element | None
    scrollHeight: int
    scrollLeft: int
    scrollWidth: int
    shadowRoot: ShadowRoot | None
    slot: str
    tagName: str

    def after(self, *node: Node) -> None:
        ...

    def animate(self, keyframes: Array[Any] | Any, options: int | Any) -> Animation:
        ...

    def append(self, *param: Node) -> None:
        ...

    def attachShadow(self, options: Any) -> ShadowRoot:
        ...

    def before(self, *node: Node) -> None:
        ...

    def closest(self, selectors: str) -> Element | None:
        ...

    def remove(self) -> None:
        ...

    def removeAttribute(self, attrName: str) -> None:
        ...

    def replaceChildren(self, *param: Node) -> None:
        ...

    def replaceWith(self, *param: Node) -> None:
        ...

    def setAttribute(self, name: str, value: str) -> bool:
        ...

class CharacterData(Node):
    data: str
    length: int

    def appendData(self, data: str) -> None:
        ...

    def deleteData(self, offset: int, count: int) -> None:
        ...

    def insertData(self, offset: int, data: str) -> None:
        ...

    def replaceData(self, offset: int, count: int, data: str) -> None:
        ...

    def substringData(self, offset: int, count: int) -> str:
        ...

class Text(CharacterData):
    ...

class Location:
    href: str
    protocol: str
    host: str
    hostname: str
    port: str
    pathname: str
    search: str
    hash: str
    origin: str

    def assign(self, url: str) -> None:
        ...

    @overload
    def reload(self) -> None:
        ...

    @overload
    def reload(self, forceGet: bool) -> None:
        ...

    def replace(self, url: str) -> None:
        ...

    def toString(self) -> str:
        ...

class Document:
    location: Location

    def getElementById(self, id: str) -> Element | None:
        ...

    @overload
    def createElement(self, tagName: str) -> Element:
        ...

    @overload
    def createElement(self, tagName: str, options: Any) -> Element:
        ...

    def createTextNode(self, data: str) -> Text:
        ...

class _Console:
    def debug(self, *args: Any) -> None:
        ...

    def error(self, *args: Any) -> None:
        ...

    def info(self, *args: Any) -> None:
        ...

    def log(self, *args: Any) -> None:
        ...

    def warn(self, *args: Any) -> None:
        ...

class Storage:
    length: int

    def clear(self) -> None:
        ...

    def getItem(self, keyName: str) -> str | None:
        ...

    def key(self, index: int) -> str | None:
        ...

    def removeItem(self, keyName: str) -> None:
        ...

    def setItem(self, keyName: str, keyValue: str) -> None:
        ...

class Window:
    closed: bool
    console: _Console
    document: Document
    localStorage: Storage
    sessionStorage: Storage

class ReadableStream:
    locked: bool

    def cancel(self) -> Promise[None]:
        ...

class Response:
    ...

class AbortSigal(EventTarget):
    aborted: bool
    reason: str

    @overload
    @classmethod
    def abort(cls) -> AbortSigal:
        ...

    @overload
    @classmethod
    def abort(cls, reason: str) -> AbortSigal:
        ...

    @classmethod
    def timeout(cls, time: int) -> AbortSigal:
        ...

    def throwIfAborted(self) -> None:
        ...

class FetchOptions(TypedDict):
    method: NotRequired[str]
    headers: NotRequired[dict[str, str]]
    body: NotRequired[Any]
    mode: NotRequired[str]
    credentials: NotRequired[Literal["omit", "same-origin", "include"]]
    cache: NotRequired[Literal["default", "no-store", "reload", "no-cache", "force-cache", "only-if-cached"]]
    redirect: NotRequired[Literal["follow", "error", "manual"]]
    referrer: NotRequired[str]
    referrerPolicy: NotRequired[Literal["no-referrer", "no-referrer-when-downgrade", "same-origin", "origin", "strict-origin", "origin-when-cross-origin", "strict-origin-when-cross-origin", "unsafe-url"]]
    integrity: NotRequired[str]
    keepalive: NotRequired[bool]
    signal: NotRequired[AbortSigal]

T2 = TypeVar("T2")

class Promise[T]:
    @classmethod
    def all(cls, values: Array[Promise[T2]]) -> Promise[T2]:
        ...

    @classmethod
    def race(cls, values: Array[Promise[T2]]) -> Promise[T2]:
        ...

    @overload
    @classmethod
    def reject(cls) -> Promise[T]:
        ...

    @overload
    @classmethod
    def reject(cls, reason: str) -> Promise[T]:
        ...

    @overload
    @classmethod
    def resolve(cls) -> Promise[None]:
        ...

    @overload
    @classmethod
    def resolve(cls, value: T2) -> Promise[T2]:
        ...

    def then(self, onfulfilled: Callable[[T], T2]) -> Promise[T2]:
        ...

    def catch(self, onrejected: Callable[[Any], None]) -> Self:
        ...

    def finally_(self, onfinally: Callable[[], None]) -> Self:
        ...

    def __await__(self) -> T:
        ...

@overload
def fetch(url: str) -> Promise[Response]:
    ...

@overload
def fetch(url: str, **options: Unpack[FetchOptions]) -> Promise[Response]:
    ...

console = _Console()
document = Document()
window = Window()
