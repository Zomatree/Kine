from __future__ import annotations

from typing import (
    Any,
    Callable,
    Generator,
    Iterator,
    Literal,
    TypeAlias,
    TypedDict,
    overload,
    TypeVar,
    Generic,
    TYPE_CHECKING,
)
from typing_extensions import Self

if TYPE_CHECKING:
    from pyodide.ffi import JsProxy

T = TypeVar("T")

class Array(Generic[T], list[T]):
    pass

class Object:
    pass

class EventTarget:
    @overload
    def addEventListener(self, type: str, listener: JsProxy[Any]) -> None: ...
    @overload
    def addEventListener(self, type: str, listener: JsProxy[Any], options: Any) -> None: ...
    @overload
    def addEventListener(self, type: str, listener: JsProxy[Any], useCapture: bool) -> None: ...
    def dispatchEvent(self, event: str) -> bool: ...
    @overload
    def removeEventListener(self, type: str, listener: JsProxy[Any]) -> None: ...
    @overload
    def removeEventListener(self, type: str, listener: JsProxy[Any], options: Any) -> None: ...
    @overload
    def removeEventListener(self, type: str, listener: JsProxy[Any], useCapture: bool) -> None: ...

class NodeList:
    length: int

    def __iter__(self) -> Iterator[Node]: ...
    def __len__(self) -> int: ...
    def entries(self) -> Iterator[Array[Any]]: ...
    @overload
    def forEach(self, callback: Any) -> None: ...
    @overload
    def forEach(self, callback: Any, thisArg: Any) -> None: ...
    def item(self, index: int) -> Node | None: ...
    def keys(self) -> Iterator[int]: ...
    def values(self) -> Iterator[Node]: ...

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
    parentElement: Element | None
    parentNode: Node
    previousSibling: Node | None
    textContent: Node | None

    def appendChild(self, aChild: Node) -> Node: ...
    @overload
    def cloneNode(self) -> Node: ...
    @overload
    def cloneNode(self, deep: bool) -> Node: ...
    def compareDocumentPosition(self, otherNode: Node) -> int: ...
    def contains(self, otherNode: Node) -> bool: ...
    @overload
    def getRootNode(self) -> Node: ...
    @overload
    def getRootNode(self, options: Any) -> Node: ...
    def hasChildNodes(self) -> bool: ...
    def insertBefore(self, newNode: Node, referenceNode: Node) -> Node: ...
    def isDefaultNamespace(self, namespaceURI: str) -> bool: ...
    def isEqualNode(self, otherNode: Node) -> bool: ...
    def isSameNode(self, otherNode: Node) -> bool: ...
    def lookupNamespaceURI(self, prefix: str | None) -> str: ...
    def lookupPrefix(self, namespace: str | None) -> str: ...
    def normalizE(self) -> None: ...
    def removeChild(self, child: Node) -> None: ...
    def replaceChild(self, newChild: Node, oldChild: Node) -> Node: ...

class Attr(Node):
    localName: str
    name: str
    namespaceURI: str | None
    ownerElement: Element | None
    prefix: str | None
    value: str

class NamedNodeMap:
    length: int

    def __getitem__(self, name: str) -> Attr | None: ...
    def getNamedItem(self, name: str) -> Attr | None: ...
    def getNameditemNS(self, namespace: str, localName: str) -> Attr | None: ...
    def removeNamedItem(self, attrName: str) -> Attr | None: ...
    def removeNameditemNS(self, namespace: str, localName: str) -> Attr | None: ...
    def setNamedItem(self, attr: Attr) -> Attr | None: ...
    def setNamedItemNS(self, attr: Attr) -> Attr | None: ...

class HTMLCollection:
    length: int

    def item(self, index: int) -> Node | None: ...
    def namedItem(self, key: str) -> Element | None: ...

class DOMTokenList:
    length: int
    value: str

    def __getitem__(self, index: int) -> str | None: ...
    def add(self, *items: str) -> None: ...
    def contains(self, token: str) -> bool: ...
    def entries(self) -> Iterator[Array[Any]]: ...
    @overload
    def forEach(self, callback: Any) -> None: ...
    @overload
    def forEach(self, callback: Any, thisArg: Any) -> None: ...
    def item(self, index: int) -> str | None: ...
    def keys(self) -> Iterator[int]: ...
    def remove(self, *items: str) -> None: ...
    def replace(self, oldToken: str, newToken: str) -> bool: ...
    def supports(self, token: str) -> bool: ...
    @overload
    def toggle(self, token: str) -> bool: ...
    @overload
    def toggle(self, token: str, force: bool) -> bool: ...
    def values(self) -> Iterator[str]: ...

class DocumentFragment(Node):
    childElementCount: int
    children: HTMLCollection
    firstElementChild: Element | None
    lastElementChild: Element | None

    def append(self, *param: Node | str) -> None: ...
    def prepend(self, *param: Node | str) -> None: ...
    def querySelector(self, selectors: str) -> Element | None: ...
    def querySelectorAll(self, selectors: str) -> Element | None: ...
    def replaceChildren(self, *param: Node | str) -> None: ...

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

    def after(self, *node: Node) -> None: ...
    def animate(self, keyframes: Array[Any] | Any, options: int | Any) -> Animation: ...
    def append(self, *param: Node) -> None: ...
    def attachShadow(self, options: Any) -> ShadowRoot: ...
    def before(self, *node: Node) -> None: ...
    def closest(self, selectors: str) -> Element | None: ...
    def remove(self) -> None: ...
    def removeAttribute(self, attrName: str) -> None: ...
    def replaceChildren(self, *param: Node) -> None: ...
    def replaceWith(self, *param: Node) -> None: ...
    def setAttribute(self, name: str, value: str) -> bool: ...
    def getAttribute(self, qualifiedName: str) -> str | None: ...

class CharacterData(Node):
    data: str
    length: int

    def appendData(self, data: str) -> None: ...
    def deleteData(self, offset: int, count: int) -> None: ...
    def insertData(self, offset: int, data: str) -> None: ...
    def replaceData(self, offset: int, count: int, data: str) -> None: ...
    def substringData(self, offset: int, count: int) -> str: ...

class Text(CharacterData): ...

class HTMLElement(Element):
    hidden: bool
    innerText: str
    lang: str
    style: Any
    tabIndex: int
    title: str

    def attachInternals(self) -> None: ...
    def blur(self) -> None: ...
    def click(self) -> None: ...
    def focus(self) -> None: ...

class HTMLInputElement(HTMLElement):
    value: str

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

    def assign(self, url: str) -> None: ...
    @overload
    def reload(self) -> None: ...
    @overload
    def reload(self, forceGet: bool) -> None: ...
    def replace(self, url: str) -> None: ...
    def toString(self) -> str: ...

class Document:
    location: Location

    def getElementById(self, id: str) -> Element | None: ...
    @overload
    def createElement(self, tagName: str) -> Element: ...
    @overload
    def createElement(self, tagName: str, options: Any) -> Element: ...
    def createTextNode(self, data: str) -> Text: ...

class _Console:
    def debug(self, *args: Any) -> None: ...
    def error(self, *args: Any) -> None: ...
    def info(self, *args: Any) -> None: ...
    def log(self, *args: Any) -> None: ...
    def warn(self, *args: Any) -> None: ...

class Storage:
    length: int

    def clear(self) -> None: ...
    def getItem(self, keyName: str) -> str | None: ...
    def key(self, index: int) -> str | None: ...
    def removeItem(self, keyName: str) -> None: ...
    def setItem(self, keyName: str, keyValue: str) -> None: ...

class Window:
    closed: bool
    console: _Console
    document: Document
    localStorage: Storage
    sessionStorage: Storage
    history: History
    navigator: Navigator

class ClipboardItemOptions:
    presentationStyle: Literal["unspecified", "inline", "attachment"]

class ClipboardItem:
    def __init__(self, data: Object, options: ClipboardItemOptions) -> None: ...

class Clipboard(EventTarget):
    def read(self) -> Promise[ClipboardItem]: ...
    def readText(self) -> Promise[str]: ...
    def write(self, data: list[ClipboardItem]) -> Promise[None]: ...
    def writeText(self, newClipText: str) -> Promise[None]: ...

class CredentialsContainer:
    @overload
    def create(self) -> Promise[Credential]: ...
    @overload
    def create(self, options: Any) -> Promise[Credential]: ...

    @overload
    def get(self) -> Promise[Credential]: ...
    @overload
    def get(self, options: Any) -> Promise[Credential]: ...

    def preventSilentAccess(self) -> Promise[None]: ...
    def store(self, credentials: Credential) -> Promise[None]: ...

class Credential:
    id: str
    type: Literal["password", "federated", "public-key"]

class Geolocation:
    def clearWatch(self, id: int) -> None: ...

    @overload
    def getCurrentPosition(self, success: JsProxy[Callable[[GeolocationPosition], Any]]) -> None: ...
    @overload
    def getCurrentPosition(self, success: JsProxy[Callable[[GeolocationPosition], Any]], error: JsProxy[Callable[[GeolocationPositionError], Any]]) -> None: ...
    @overload
    def getCurrentPosition(self, success: JsProxy[Callable[[GeolocationPosition], Any]], error: JsProxy[Callable[[GeolocationPositionError], Any]], options: GeolocationGetCurrentPositionOptions) -> None: ...

class GeolocationGetCurrentPositionOptions:
    maximumAge: int
    timeout: int
    enableHighAccuracy: bool

class GeolocationPosition:
    coords: GeolocationCoords
    timestamp: int

class GeolocationCoords:
    accuracy: float
    altitude: float
    altitudeAccuracy: float
    heading: float
    latitude: float
    longitude: float
    speed: float

class GeolocationPositionError:
    code: Literal[0, 1, 2]
    message: str

class LockManager:
    @overload
    def request(self, name: str, callback: JsProxy[Callable[[], Any]]) -> Promise[None]: ...
    @overload
    def request(self, name: str, options: LockManagerRequestOptions, callback: JsProxy[Callable[[], Any]]) -> Promise[None]: ...

class LockManagerRequestOptions:
    mode: Literal["exclusive", "shared"]
    ifAvailable: bool
    steal: bool
    signal: AbortSigal

class MediaCapabilities:
    def decodingInfo(self, configuration: MediaCapabilitiesDecodinginfoConfiguration) -> Promise[MediaCapabilitiesDecodingInfo]: ...

class MediaCapabilitiesDecodinginfoConfiguration:
    type: Literal["file", "media-source", "webrtc"]
    video: MediaCapabilitiesDecodinginfoVideoConfiguration
    audio: MediaCapabilitiesDecodinginfoAudioConfiguration

class MediaCapabilitiesDecodinginfoVideoConfiguration:
    contentType: str
    width: int
    height: int
    bitrate: int
    framerate: int

class MediaCapabilitiesDecodinginfoAudioConfiguration:
    contentType: str
    channels: int
    bitrate: int
    samplerate: int

class MediaCapabilitiesDecodingInfo:
    supported: bool
    smooth: bool
    powerEfficient: bool

class MediaDeviceInfo:
    deviceId: str
    groupId: str
    kind: Literal["videoinput", "audiosource", "audiooutput"]
    label: str

    def toJSON(self) -> Any: ...

class MediaStream(EventTarget):
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, stream: MediaStream) -> None: ...
    @overload
    def __init__(self, tracks: list[MediaStreamTrack]) -> None: ...

    active: bool
    id: str

    def addTrack(self, track: MediaStreamTrack) -> None: ...
    def clone(self) -> Self: ...
    def getAudioTracks(self) -> list[MediaStreamTrack]: ...
    def getTrackById(self, id: str) -> MediaStreamTrack | None: ...
    def getTracks(self) -> list[MediaStreamTrack]: ...
    def getVideoTracks(self) -> list[MediaStreamTrack]: ...
    def removeTrack(self, track: MediaStreamTrack) -> None: ...

class MediaStreamTrack(EventTarget):
    contentHint: str
    enabled: bool
    id: str
    kind: Literal["audio", "video"]
    label: str
    muted: bool
    readyState: Literal["live", "ended"]

    @overload
    def applyContraints(self) -> Promise[None]: ...
    @overload
    def applyContraints(self, constraints: Any) -> Promise[None]: ...

    def clone(self) -> Self: ...
    def getCapabilities(self) -> Any: ...
    def getConstraints(self) -> Any: ...
    def getSettings(self) -> Any: ...
    def stop(self) -> None: ...

class MediaDevices(EventTarget):
    def enumerateDevices(self) -> Promise[list[MediaDeviceInfo]]: ...

    @overload
    def getDisplayMedia(self) -> Promise[MediaStream]: ...
    @overload
    def getDisplayMedia(self, options: MediaDevicesGetDisplayMediaOptions) -> Promise[MediaStream]: ...


class MediaDevicesGetDisplayMediaOptions:
    video: bool
    audio: bool
    preferCurrentTag: bool
    selfBrowserSurface: Literal["include", "exclude"]
    surfaceSwitching: Literal["include", "exclude"]
    systemAudio: Literal["include", "exclude"]

class MediaSession:
    metadata: MediaMetadata
    playbackState: Literal["none", "paused", "playing"]

    def setActionHandler(self, type: Literal["hangup", "nextslide", "nexttrack", "pause", "play", "previousslide", "previoustrack", "seekbackward", "seekforward", "seekto", "skipad", "stop", "stop", "togglecamera", "togglemicrophone"], callback: JsProxy[Callable[[ActionHandle], None]]) -> None: ...
    def setPositionState(self, stateDict: StateDict) -> None: ...

class MediaMetadata:
    def __init__(self, metadata: MediaMetadata) -> None: ...

    title: str
    artist: str
    album: str
    artwork: list[MediaImage]

class MediaImage:
    src: str
    sizes: list[Any]
    type: str

class ActionHandle:
    action: str
    fastSeek: bool
    seekoffset: float
    seekTime: float

class StateDict:
    duration: float
    playbackRate: float
    position: float

class Permissions:
    def query(self, permissionDescriptor: PermissionDescriptor) -> Promise[PermissionStatus]: ...
    def revoke(self, descriptor: PermissionDescriptor) -> Promise[PermissionStatus]: ...

class PermissionDescriptor:
    name: str
    userVisibleOnly: bool
    sysex: bool

class PermissionStatus(EventTarget):
    name: str
    state: Literal["granted", "denied", "prompt"]
    status: Literal["granted", "denied", "prompt"]

class ServiceWorkerContainer(EventTarget):
    controller: ServiceWorker
    ready: Promise[ServiceWorkerRegistration]

class ServiceWorker(EventTarget):
    scriptURL: str
    state: Literal["parsed", "installing", "installed", "activating", "activated", "redundant"]

    @overload
    def postMessage(self, message: Any) -> None: ...
    @overload
    def postMessage(self, message: Any, options: ServiceWorkerPostMessageOptions) -> None: ...
    @overload
    def postMessage(self, message: Any, transfer: list[ArrayBuffer | MessagePort | ImageBitmap]) -> None: ...

class ArrayBuffer:
    def __init__(self, length: int) -> None: ...

    byteLength: int

    def isView(self, value: Any) -> bool: ...

    @overload
    def slice(self, begin: int) -> Self: ...
    @overload
    def slice(self, begin: int, end: int) -> Self: ...

class MessagePort(EventTarget):
    def postMessage(self, message: Any, transferList: list[Any]) -> None: ...
    def start(self) -> None: ...
    def close(self) -> None: ...

class ImageBitmap:
    height: int
    width: int

    def close(self) -> None: ...

class ServiceWorkerPostMessageOptions:
    transfer: list[ArrayBuffer | MessagePort | ImageBitmap]

class ServiceWorkerRegistration(EventTarget):
    active: Literal["activating", "activated"] | None
    installing: ServiceWorker | None
    navigationPreload: NavigationPreloadManager
    pushManager: PushManager
    waiting: ServiceWorker | None
    updateViaCache: str

    @overload
    def getNotifications(self) -> Promise[list[Notification]]: ...
    @overload
    def getNotifications(self, options: ServiceWorkerRegistrationGetNotificationsOptions) -> Promise[list[Notification]]: ...

    @overload
    def showNotification(self, title: str) -> Promise[None]: ...
    @overload
    def showNotification(self, title: str, options: NotificationOptions) -> Promise[None]: ...

    def unregister(self) -> Promise[bool]: ...
    def update(self) -> Promise[ServiceWorkerRegistration]: ...

class NavigationPreloadManager:
    def enable(self) -> Promise[None]: ...
    def disable(self) -> Promise[None]: ...
    def setHeaderValue(self, value: str) -> Promise[None]: ...
    def getState(self) -> Promise[NavigationPreloadManagerState]: ...

class NavigationPreloadManagerState:
    enabled: bool
    headerValue: str

class PushManager:
    def getSubscription(self) -> Promise[PushSubscription]: ...

    @overload
    def permissionState(self) -> Promise[Literal["granted", "denied", "prompt"]]: ...
    @overload
    def permissionState(self, options: PushOptions) -> Promise[Literal["granted", "denied", "prompt"]]: ...

    def subscribe(self, options: PushOptions) -> Promise[PushSubscription]: ...

class PushOptions:
    userVisibleOnly: bool
    applicationServerKey: str

DOMHighResTimeStamp: TypeAlias = float

class PushSubscription:
    endpoint: str
    expirationtime: DOMHighResTimeStamp
    options: PushOptions

    def getKey(self, name: Literal["p256dh", "auth"]) -> ArrayBuffer: ...
    def toJSON(self) -> Any: ...
    def unsubscribe(self) -> Promise[bool]: ...

class Notification(EventTarget):
    def __init__(self, title: str, options: NotificationOptions) -> None: ...

    permission: Literal["denied", "granted", "default"]
    maxActions: int

    body: str
    dir: Literal["auto", "ltr", "rtl"]
    icon: str
    lang: str
    silent: bool
    tag: str
    timestamp: int
    badge: str
    image: str
    virate: list[int] | int
    renotify: bool
    actions: list[NotificationOptionsAction]

class NotificationOptions:
    body: str
    dir: Literal["auto", "ltr", "rtl"]
    icon: str
    lang: str
    silent: bool
    tag: str
    timestamp: int
    badge: str
    image: str
    virate: list[int] | int
    renotify: bool
    actions: list[NotificationOptionsAction]

class NotificationOptionsAction:
    action: str
    title: str
    icon: str

class ServiceWorkerRegistrationGetNotificationsOptions:
    tag: str

class StorageManager:
    def estimate(self) -> Promise[StorageEstimate]: ...
    def getDirectory(self) -> Promise[FileSystemDirectoryHandle]: ...
    def persist(self) -> Promise[bool]: ...
    def persisted(self) -> Promise[bool]: ...

class FileSystemHandle:
    kind: Literal["file", "directory"]
    name: str

    def isSameEntry(self, fileSystemHandle: FileSystemHandle) -> bool: ...

class FileSystemDirectoryHandle(FileSystemHandle):
    pass

class StorageEstimate:
    quote: int
    usage: int

class Navigator:
    clipboard: Clipboard
    cookieEnabled: bool
    credentials: CredentialsContainer
    geolocation: Geolocation
    hardwareConcurrency: int
    language: str | None
    languages: list[str]
    locks: LockManager
    mediaCapabilities: MediaCapabilities
    mediaDevices: MediaDevices
    mediaSession: MediaSession
    onLine: bool
    pdfPreviewEnabled: bool
    permissions: Permissions
    serviceWorker: ServiceWorkerContainer
    storage: StorageManager
    userActivation: UserActivation
    userAgentData: NavigatorUAData
    userActivation: UserActivation
    userAgent: str
    virtualKeyboard: VirtualKeyboard
    wakeLock: WakeLock
    webdriver: bool
    windowControlsOverlay: WindowControlsOverlay

    @overload
    def canShare(self) -> bool: ...
    @overload
    def canShare(self, data: str | list[File]) -> bool: ...

    def getBattery(self) -> Promise[BatteryManager]: ...
    def getGamepads(self) -> list[Gamepad]: ...

    @overload
    def registerProtocolHandler(self, scheme: str, url: str) -> None: ...
    @overload
    def registerProtocolHandler(self, scheme: str, url: str, title: str) -> None: ...

    def requestMediaKeySystemAccess(self, keySystem: str, supportedConfigurations: list[Any]) -> Promise[MediaKeySystemAccess]: ...

    @overload
    def requestMIDIAccess(self) -> Promise[MIDIAccess]: ...
    @overload
    def requestMIDIAccess(self, MIDIOptions: MIDIOptions) -> Promise[MIDIAccess]: ...

    @overload
    def sendBeacon(self, url: str) -> bool: ...
    @overload
    def sendBeacon(self, url: str, data: ArrayBuffer | TypedArray | DataView | Blob | FormData | URLSearchParams) -> bool: ...

    def share(self, data: str | list[File]) -> Promise[None]: ...
    def unregisterProtocolHandler(self, scheme: str, url: str) -> None: ...
    def vibrate(self, pattern: int | list[int]) -> bool: ...

class MIDIOptions:
    sysex: bool
    software: bool

class History:
    length: int
    scrollRestoration: str
    state: Any

    def back(self) -> None: ...
    def forward(self) -> None: ...
    @overload
    def go(self) -> None: ...
    @overload
    def go(self, delta: int) -> None: ...
    def pushState(self, state: Any, unused: str, url: str) -> None: ...
    def replaceState(self, stateObj: Any, unused: str, url: str) -> None: ...

class ReadableStream:
    locked: bool

    def cancel(self) -> Promise[None]: ...

class Headers:
    def append(self, name: str, value: str) -> None: ...
    def delete(self, name: str) -> None: ...
    def get(self, name: str) -> str | None: ...
    def has(self, name: str) -> bool: ...
    def set(self, name: str, value: str) -> None: ...
    def forEach(
        self,
        callbackfn: JsProxy[Callable[[str], None] | Callable[[str, Self], None] | Callable[[str, str, Self], None]],
    ) -> None: ...

class Blob:
    size: int
    type: str

    def arrayBuffer(self) -> Promise[Any]: ...
    @overload
    def slice(self, start: int) -> Blob: ...
    @overload
    def slice(self, start: int, end: int) -> Blob: ...
    @overload
    def slice(self, start: int, end: int, contentType: str) -> Blob: ...
    def stream(self) -> ReadableStream: ...
    def text(self) -> Promise[str]: ...

class File(Blob):
    lastModified: int
    name: str
    webkitRelativePath: str

FormDataEntryValue = File | str

class FormData:
    @overload
    def append(self, name: str, value: str | Blob) -> None: ...
    @overload
    def append(self, name: str, value: str | Blob, fileName: str) -> None: ...
    def delete(self, name: str) -> None: ...
    def get(self, name: str) -> FormDataEntryValue | None: ...
    def getAll(self, name: str) -> list[FormDataEntryValue]: ...
    def has(self, name: str) -> bool: ...
    @overload
    def set(self, name: str, value: str | Blob) -> None: ...
    @overload
    def set(self, name: str, value: str | Blob, fileName: str) -> None: ...
    def forEach(
        self,
        callbackfn: JsProxy[
            Callable[[FormDataEntryValue], None]
            | Callable[[FormDataEntryValue, str], None]
            | Callable[[FormDataEntryValue, str, Self], None]
        ],
    ) -> None: ...

class Body:
    body: ReadableStream | None
    bodyUsed: bool

    def arrayBuffer(self) -> Promise[Any]: ...
    def blob(self) -> Promise[Blob]: ...
    def formData(self) -> Promise[FormData]: ...
    def json(self) -> Promise[Any]: ...
    def text(self) -> Promise[str]: ...

class Response(Body):
    headers: Headers
    ok: bool
    redirect: bool
    status: int
    statusText: str
    url: str

class AbortSigal(EventTarget):
    aborted: bool
    reason: str

    @overload
    @classmethod
    def abort(cls) -> AbortSigal: ...
    @overload
    @classmethod
    def abort(cls, reason: str) -> AbortSigal: ...
    @classmethod
    def timeout(cls, time: int) -> AbortSigal: ...
    def throwIfAborted(self) -> None: ...

class _FetchOptions(TypedDict, total=False):
    method: str
    headers: dict[str, str]
    body: Any
    mode: str
    credentials: Literal["omit", "same-origin", "include"]
    cache: Literal["default", "no-store", "reload", "no-cache", "force-cache", "only-if-cached"]
    redirect: Literal["follow", "error", "manual"]
    referrer: str
    referrerPolicy:  Literal[
        "no-referrer",
        "no-referrer-when-downgrade",
        "same-origin",
        "origin",
        "strict-origin",
        "origin-when-cross-origin",
        "strict-origin-when-cross-origin",
        "unsafe-url",
    ]

    integrity: str
    keepalive: bool
    signal: AbortSigal

T2 = TypeVar("T2")

class Promise(Generic[T]):
    @classmethod
    def all(cls, values: Array[Promise[T2]]) -> Promise[T2]: ...
    @classmethod
    def race(cls, values: Array[Promise[T2]]) -> Promise[T2]: ...
    @overload
    @classmethod
    def reject(cls) -> Promise[T]: ...
    @overload
    @classmethod
    def reject(cls, reason: str) -> Promise[T]: ...
    @overload
    @classmethod
    def resolve(cls) -> Promise[None]: ...
    @overload
    @classmethod
    def resolve(cls, value: T2) -> Promise[T2]: ...
    def then(self, onfulfilled: JsProxy[Callable[[T], T2]]) -> Promise[T2]: ...
    def catch(self, onrejected: JsProxy[Callable[[Any], None]]) -> Self: ...
    def finally_(self, onfinally: JsProxy[Callable[[], None]]) -> Self: ...
    def __await__(self) -> Generator[Any, Any, T]: ...

class Request(Body):
    cache: Literal["default", "no-store", "reload", "no-cache", "force-cache", "only-if-cached"]
    credentials: Literal["omit", "same-origin", "include"]
    destination: Literal[
        "",
        "audio",
        "audioworklet",
        "document",
        "embed",
        "font",
        "frame",
        "iframe",
        "image",
        "manifest",
        "object",
        "paintworklet",
        "report",
        "script",
        "sharedworker",
        "style",
        "track",
        "video",
        "worker",
        "xslt",
    ]
    headers: Headers
    integrity: str
    keepalive: bool
    method: str
    mode: Literal["cors", "navigate", "no-cors", "same-origin"]
    redirect: Literal["follow", "error", "manual"]
    referrer: str
    referrerPolicy: Literal[
        "no-referrer",
        "no-referrer-when-downgrade",
        "same-origin",
        "origin",
        "strict-origin",
        "origin-when-cross-origin",
        "strict-origin-when-cross-origin",
        "unsafe-url",
    ]
    signal: AbortSigal
    url: str

class URLSearchParams:
    @overload
    def append(self, name: str, value: str | Blob) -> None: ...
    @overload
    def append(self, name: str, value: str | Blob, fileName: str) -> None: ...
    def delete(self, name: str) -> None: ...
    def get(self, name: str) -> str | None: ...
    def getAll(self, name: str) -> list[str]: ...
    def has(self, name: str) -> bool: ...
    @overload
    def set(self, name: str, value: str | Blob) -> None: ...
    @overload
    def set(self, name: str, value: str | Blob, fileName: str) -> None: ...
    def sort(self) -> None: ...
    def forEach(
        self, callbackfn: JsProxy[Callable[[str], None] | Callable[[str, str], None] | Callable[[str, str, Self], None]]
    ) -> None: ...

class URL:
    hash: str
    host: str
    hostname: str
    href: str
    origin: str
    password: str
    pathname: str
    port: str
    protocol: str
    search: str
    searchParams: URLSearchParams
    username: str

    def toJSON(self) -> str: ...

RequestInfo: TypeAlias = Request | str

@overload
def fetch(url: RequestInfo | URL) -> Promise[Response]: ...
@overload
def fetch(url: RequestInfo | URL, options: JsProxy[_FetchOptions]) -> Promise[Response]: ...

class Message:
    seq: int
    type: Literal["request", "response", "event"]

class Event(Message):
    type: str
    event: str
    body: Any | None

class CloseEvent(Event):
    code: int
    reason: str
    wasClean: bool

class MessageEvent(Message, Generic[T]):
    data: T
    lastEventId: str
    origin: str

class WebSocket(EventTarget):
    binaryType: Literal["arraybuffer", "blob"]
    bufferedAmount: int
    extensions: str
    onclose: JsProxy[Callable[[Self, CloseEvent], None]] | None
    onerror: JsProxy[Callable[[Self, Event], None]] | None
    onmessage: JsProxy[Callable[[Self, MessageEvent[Any]], None]] | None
    onopen: JsProxy[Callable[[Self, Event], None]] | None
    protocol: str
    readyState: int
    url: str

    @overload
    def close(self) -> None: ...
    @overload
    def close(self, code: int) -> None: ...
    @overload
    def close(self, code: int, reason: str) -> None: ...
    def send(self, data: str | Array[Any] | Blob) -> None: ...

    CLOSED: int
    CLOSING: int
    CONNECTING: int
    OPEN: int

    @overload
    @classmethod
    def new(cls, url: str | URL) -> Self: ...
    @overload
    @classmethod
    def new(cls, url: str | URL, protocols: str | Array[str]) -> Self: ...


console = _Console()
document = Document()
window = Window()
