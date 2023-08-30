# @formatter:off

from typing import overload, Any, Awaitable, Sequence, Literal, TypedDict, NotRequired, ByteString, Union, Callable, TypeAlias
from .ecmascript import *
SecurityPolicyViolationEventDisposition = Literal["enforce", "report"]

IdentityCredentialRequestOptionsContext = Literal["signin", "signup", "use", "continue"]

EndingType = Literal["transparent", "native"]

IDBRequestReadyState = Literal["pending", "done"]

IDBTransactionDurability = Literal["default", "strict", "relaxed"]

IDBCursorDirection = Literal["next", "nextunique", "prev", "prevunique"]

IDBTransactionMode = Literal["readonly", "readwrite", "versionchange"]

KeyType = Literal["public", "private", "secret"]

KeyUsage = Literal["encrypt", "decrypt", "sign", "verify", "deriveKey", "deriveBits", "wrapKey", "unwrapKey"]

KeyFormat = Literal["raw", "spki", "pkcs8", "jwk"]

AccelerometerLocalCoordinateSystem = Literal["device", "screen"]

AutoplayPolicy = Literal["allowed", "allowed-muted", "disallowed"]

AutoplayPolicyMediaType = Literal["mediaelement", "audiocontext"]

BackgroundFetchResult = Literal["", "success", "failure"]

BackgroundFetchFailureReason = Literal["", "aborted", "bad-status", "fetch-error", "quota-exceeded", "download-total-exceeded"]

PresentationStyle = Literal["unspecified", "inline", "attachment"]

CompressionFormat = Literal["deflate", "deflate-raw", "gzip"]

PressureSource = Literal["thermals", "cpu"]

PressureState = Literal["nominal", "fair", "serious", "critical"]

ContactProperty = Literal["address", "email", "icon", "name", "tel"]

ContentCategory = Literal["", "homepage", "article", "video", "audio"]

CookieSameSite = Literal["strict", "lax", "none"]

CredentialMediationRequirement = Literal["silent", "optional", "conditional", "required"]

ScriptingPolicyViolationType = Literal["externalScript", "inlineScript", "inlineEventHandler", "eval"]

FontFaceLoadStatus = Literal["unloaded", "loading", "loaded", "error"]

FontFaceSetLoadStatus = Literal["loading", "loaded"]

HighlightType = Literal["highlight", "spelling-error", "grammar-error"]

ChildDisplayType = Literal["block", "normal"]

LayoutSizingMode = Literal["block-like", "manual"]

BlockFragmentationType = Literal["none", "page", "column", "region"]

BreakType = Literal["none", "line", "column", "page", "region"]

SpatialNavigationDirection = Literal["up", "down", "left", "right"]

FocusableAreaSearchMode = Literal["visible", "all"]

CSSNumericBaseType = Literal["length", "angle", "time", "frequency", "resolution", "flex", "percent"]

CSSMathOperator = Literal["sum", "product", "negate", "invert", "min", "max", "clamp"]

ScrollBehavior = Literal["auto", "instant", "smooth"]

ScrollLogicalPosition = Literal["start", "center", "end", "nearest"]

CSSBoxType = Literal["margin", "border", "padding", "content"]

DevicePostureType = Literal["continuous", "folded"]

ItemType = Literal["product", "subscription"]

SocketDnsQueryType = Literal["ipv4", "ipv6"]

ShadowRootMode = Literal["open", "closed"]

SlotAssignmentMode = Literal["manual", "named"]

MediaKeysRequirement = Literal["required", "optional", "not-allowed"]

MediaKeySessionType = Literal["temporary", "persistent-license"]

MediaKeySessionClosedReason = Literal["internal-error", "closed-by-application", "release-acknowledged", "hardware-context-reset", "resource-evicted"]

MediaKeyStatus = Literal["usable", "expired", "released", "output-restricted", "output-downscaled", "usable-in-future", "status-pending", "internal-error"]

MediaKeyMessageType = Literal["license-request", "license-renewal", "license-release", "individualization-request"]

OpaqueProperty = Literal["opaque"]

FenceReportingDestination = Literal["buyer", "seller", "component-seller", "direct-seller", "shared-storage-select-url"]

RequestDestination = Literal["", "audio", "audioworklet", "document", "embed", "font", "frame", "iframe", "image", "manifest", "object", "paintworklet", "report", "script", "sharedworker", "style", "track", "video", "worker", "xslt"]

RequestMode = Literal["navigate", "same-origin", "no-cors", "cors"]

RequestCredentials = Literal["omit", "same-origin", "include"]

RequestCache = Literal["default", "no-store", "reload", "no-cache", "force-cache", "only-if-cached"]

RequestRedirect = Literal["follow", "error", "manual"]

RequestDuplex = Literal["half"]

RequestPriority = Literal["high", "low", "auto"]

ResponseType = Literal["basic", "cors", "default", "error", "opaque", "opaqueredirect"]

FileSystemPermissionMode = Literal["read", "readwrite"]

WellKnownDirectory = Literal["desktop", "documents", "downloads", "music", "pictures", "videos"]

FileSystemHandleKind = Literal["file", "directory"]

WriteCommandType = Literal["write", "seek", "truncate"]

FullscreenNavigationUI = Literal["auto", "show", "hide"]

GamepadHand = Literal["", "left", "right"]

GamepadHapticsResult = Literal["complete", "preempted"]

GamepadHapticActuatorType = Literal["vibration", "dual-rumble"]

GamepadHapticEffectType = Literal["dual-rumble"]

GamepadMappingType = Literal["", "standard", "xr-standard"]

MockSensorType = Literal["ambient-light", "accelerometer", "linear-acceleration", "gravity", "gyroscope", "magnetometer", "uncalibrated-magnetometer", "absolute-orientation", "relative-orientation", "geolocation", "proximity"]

GyroscopeLocalCoordinateSystem = Literal["device", "screen"]

DocumentReadyState = Literal["loading", "interactive", "complete"]

DocumentVisibilityState = Literal["visible", "hidden"]

CanPlayTypeResult = Literal["", "maybe", "probably"]

TextTrackMode = Literal["disabled", "hidden", "showing"]

TextTrackKind = Literal["subtitles", "captions", "descriptions", "chapters", "metadata"]

SelectionMode = Literal["select", "start", "end", "preserve"]

PredefinedColorSpace = Literal["srgb", "display-p3"]

CanvasFillRule = Literal["nonzero", "evenodd"]

ImageSmoothingQuality = Literal["low", "medium", "high"]

CanvasLineCap = Literal["butt", "round", "square"]

CanvasLineJoin = Literal["round", "bevel", "miter"]

CanvasTextAlign = Literal["start", "end", "left", "right", "center"]

CanvasTextBaseline = Literal["top", "hanging", "middle", "alphabetic", "ideographic", "bottom"]

CanvasDirection = Literal["ltr", "rtl", "inherit"]

CanvasFontKerning = Literal["auto", "normal", "none"]

CanvasFontStretch = Literal["ultra-condensed", "extra-condensed", "condensed", "semi-condensed", "normal", "semi-expanded", "expanded", "extra-expanded", "ultra-expanded"]

CanvasFontVariantCaps = Literal["normal", "small-caps", "all-small-caps", "petite-caps", "all-petite-caps", "unicase", "titling-caps"]

CanvasTextRendering = Literal["auto", "optimizeSpeed", "optimizeLegibility", "geometricPrecision"]

OffscreenRenderingContextId = Literal["2d", "bitmaprenderer", "webgl", "webgl2", "webgpu"]

ScrollRestoration = Literal["auto", "manual"]

NavigationHistoryBehavior = Literal["auto", "push", "replace"]

NavigationType = Literal["push", "replace", "reload", "traverse"]

NavigationFocusReset = Literal["after-transition", "manual"]

NavigationScrollBehavior = Literal["after-transition", "manual"]

DOMParserSupportedType = Literal["text/html", "text/xml", "application/xml", "application/xhtml+xml", "image/svg+xml"]

ImageOrientation = Literal["from-image", "flipY"]

PremultiplyAlpha = Literal["none", "premultiply", "default"]

ColorSpaceConversion = Literal["none", "default"]

ResizeQuality = Literal["pixelated", "low", "medium", "high"]

WorkerType = Literal["classic", "module"]

UserIdleState = Literal["active", "idle"]

ScreenIdleState = Literal["locked", "unlocked"]

RedEyeReduction = Literal["never", "always", "controllable"]

FillLightMode = Literal["auto", "off", "flash"]

MeteringMode = Literal["none", "manual", "single-shot", "continuous"]

JsonLdErrorCode = Literal["colliding keywords", "conflicting indexes", "context overflow", "cyclic IRI mapping", "invalid @id value", "invalid @import value", "invalid @included value", "invalid @index value", "invalid @nest value", "invalid @prefix value", "invalid @propagate value", "invalid @protected value", "invalid @reverse value", "invalid @version value", "invalid base direction", "invalid base IRI", "invalid container mapping", "invalid context entry", "invalid context nullification", "invalid default language", "invalid IRI mapping", "invalid JSON literal", "invalid keyword alias", "invalid language map value", "invalid language mapping", "invalid language-tagged string", "invalid language-tagged value", "invalid local context", "invalid remote context", "invalid reverse property map", "invalid reverse property value", "invalid reverse property", "invalid scoped context", "invalid script element", "invalid set or list object", "invalid term definition", "invalid type mapping", "invalid type value", "invalid typed value", "invalid value object value", "invalid value object", "invalid vocab mapping", "IRI confused with prefix", "keyword redefinition", "loading document failed", "loading remote context failed", "multiple context link headers", "processing mode conflict", "protected term redefinition"]

JsonLdFramingErrorCode = Literal["invalid frame", "invalid @embed value"]

JsonLdEmbed = Literal["@always", "@once", "@never"]

MagnetometerLocalCoordinateSystem = Literal["device", "screen"]

AppBannerPromptOutcome = Literal["accepted", "dismissed"]

MediaDecodingType = Literal["file", "media-source", "webrtc"]

MediaEncodingType = Literal["record", "webrtc"]

HdrMetadataType = Literal["smpteSt2086", "smpteSt2094-10", "smpteSt2094-40"]

ColorGamut = Literal["srgb", "p3", "rec2020"]

TransferFunction = Literal["srgb", "pq", "hlg"]

ReadyState = Literal["closed", "open", "ended"]

EndOfStreamError = Literal["network", "decode"]

AppendMode = Literal["segments", "sequence"]

MockCapturePromptResult = Literal["granted", "denied"]

CaptureAction = Literal["next", "previous", "first", "last"]

MediaStreamTrackState = Literal["live", "ended"]

VideoFacingModeEnum = Literal["user", "environment", "left", "right"]

VideoResizeModeEnum = Literal["none", "crop-and-scale"]

MediaDeviceKind = Literal["audioinput", "audiooutput", "videoinput"]

MediaSessionPlaybackState = Literal["none", "paused", "playing"]

MediaSessionAction = Literal["play", "pause", "seekbackward", "seekforward", "previoustrack", "nexttrack", "skipad", "stop", "seekto", "togglemicrophone", "togglecamera", "hangup", "previousslide", "nextslide"]

BitrateMode = Literal["constant", "variable"]

RecordingState = Literal["inactive", "recording", "paused"]

RTCDegradationPreference = Literal["maintain-framerate", "maintain-resolution", "balanced"]

NavigationTimingType = Literal["navigate", "reload", "back_forward", "prerender"]

ConnectionType = Literal["bluetooth", "cellular", "ethernet", "mixed", "none", "other", "unknown", "wifi", "wimax"]

EffectiveConnectionType = Literal["2g", "3g", "4g", "slow-2g"]

NotificationPermission = Literal["default", "denied", "granted"]

NotificationDirection = Literal["auto", "ltr", "rtl"]

OrientationSensorLocalCoordinateSystem = Literal["device", "screen"]

ClientLifecycleState = Literal["active", "frozen"]

PaymentDelegation = Literal["shippingAddress", "payerName", "payerPhone", "payerEmail"]

PaymentShippingType = Literal["shipping", "delivery", "pickup"]

PaymentComplete = Literal["fail", "success", "unknown"]

PermissionState = Literal["granted", "denied", "prompt"]

PresentationConnectionState = Literal["connecting", "connected", "closed", "terminated"]

PresentationConnectionCloseReason = Literal["error", "closed", "wentaway"]

RequestTargetAddressSpace = Literal["private", "local"]

PushEncryptionKeyName = Literal["p256dh", "auth"]

ReferrerPolicy = Literal["", "no-referrer", "no-referrer-when-downgrade", "same-origin", "origin", "strict-origin", "origin-when-cross-origin", "strict-origin-when-cross-origin", "unsafe-url"]

RemotePlaybackState = Literal["connecting", "connected", "disconnected"]

ResizeObserverBoxOptions = Literal["border-box", "content-box", "device-pixel-content-box"]

RenderBlockingStatusType = Literal["blocking", "non-blocking"]

TaskPriority = Literal["user-blocking", "user-visible", "background"]

CaptureStartFocusBehavior = Literal["focus-capturing-application", "focus-captured-surface", "no-focus-change"]

SelfCapturePreferenceEnum = Literal["include", "exclude"]

SystemAudioPreferenceEnum = Literal["include", "exclude"]

SurfaceSwitchingPreferenceEnum = Literal["include", "exclude"]

DisplayCaptureSurfaceType = Literal["monitor", "window", "browser"]

CursorCaptureConstraint = Literal["never", "always", "motion"]

OrientationLockType = Literal["any", "natural", "landscape", "portrait", "portrait-primary", "portrait-secondary", "landscape-primary", "landscape-secondary"]

OrientationType = Literal["portrait-primary", "portrait-secondary", "landscape-primary", "landscape-secondary"]

WakeLockType = Literal["screen"]

ScrollAxis = Literal["block", "inline", "x", "y"]

ParityType = Literal["none", "even", "odd"]

FlowControlType = Literal["none", "hardware"]

ServiceWorkerState = Literal["parsed", "installing", "installed", "activating", "activated", "redundant"]

ServiceWorkerUpdateViaCache = Literal["imports", "all", "none"]

FrameType = Literal["auxiliary", "top-level", "nested", "none"]

ClientType = Literal["window", "worker", "sharedworker", "all"]

LandmarkType = Literal["mouth", "eye", "nose"]

BarcodeFormat = Literal["aztec", "code_128", "code_39", "code_93", "codabar", "data_matrix", "ean_13", "ean_8", "itf", "pdf417", "qr_code", "unknown", "upc_a", "upc_e"]

SpeechRecognitionErrorCode = Literal["no-speech", "aborted", "audio-capture", "network", "not-allowed", "service-not-allowed", "bad-grammar", "language-not-supported"]

SpeechSynthesisErrorCode = Literal["canceled", "interrupted", "audio-busy", "audio-hardware", "network", "synthesis-unavailable", "synthesis-failed", "language-unavailable", "voice-unavailable", "text-too-long", "invalid-argument", "not-allowed"]

StorageBucketDurability = Literal["strict", "relaxed"]

ReadableStreamReaderMode = Literal["byob"]

ReadableStreamType = Literal["bytes"]

TouchType = Literal["direct", "stylus"]

RefreshPolicy = Literal["none", "refresh"]

TokenVersion = Literal["1"]

OperationType = Literal["token-request", "send-redemption-record", "token-redemption"]

ImportExportKind = Literal["function", "table", "memory", "global"]

TableKind = Literal["externref", "anyfunc"]

ValueType = Literal["i32", "i64", "f32", "f64", "v128", "externref", "anyfunc"]

IterationCompositeOperation = Literal["replace", "accumulate"]

AnimationPlayState = Literal["idle", "running", "paused", "finished"]

AnimationReplaceState = Literal["active", "removed", "persisted"]

FillMode = Literal["none", "forwards", "backwards", "both", "auto"]

PlaybackDirection = Literal["normal", "reverse", "alternate", "alternate-reverse"]

CompositeOperation = Literal["replace", "add", "accumulate"]

CompositeOperationOrAuto = Literal["replace", "add", "accumulate", "auto"]

LockMode = Literal["shared", "exclusive"]

OTPCredentialTransportType = Literal["sms"]

AudioContextState = Literal["suspended", "running", "closed"]

AudioContextLatencyCategory = Literal["balanced", "interactive", "playback"]

AudioSinkType = Literal["none"]

ChannelCountMode = Literal["max", "clamped-max", "explicit"]

ChannelInterpretation = Literal["speakers", "discrete"]

AutomationRate = Literal["a-rate", "k-rate"]

BiquadFilterType = Literal["lowpass", "highpass", "bandpass", "lowshelf", "highshelf", "peaking", "notch", "allpass"]

OscillatorType = Literal["sine", "square", "sawtooth", "triangle", "custom"]

PanningModelType = Literal["equalpower", "HRTF"]

DistanceModelType = Literal["linear", "inverse", "exponential"]

OverSampleType = Literal["none", "2x", "4x"]

AuthenticatorAttachment = Literal["platform", "cross-platform"]

ResidentKeyRequirement = Literal["discouraged", "preferred", "required"]

AttestationConveyancePreference = Literal["none", "indirect", "direct", "enterprise"]

TokenBindingStatus = Literal["present", "supported"]

PublicKeyCredentialType = Literal["public-key"]

AuthenticatorTransport = Literal["usb", "nfc", "ble", "smart-card", "hybrid", "internal"]

UserVerificationRequirement = Literal["required", "preferred", "discouraged"]

PublicKeyCredentialHints = Literal["security-key", "client-device", "hybrid"]

LargeBlobSupport = Literal["required", "preferred"]

AacBitstreamFormat = Literal["aac", "adts"]

AvcBitstreamFormat = Literal["annexb", "avc"]

HevcBitstreamFormat = Literal["annexb", "hevc"]

OpusBitstreamFormat = Literal["opus", "ogg"]

HardwareAcceleration = Literal["no-preference", "prefer-hardware", "prefer-software"]

AlphaOption = Literal["keep", "discard"]

LatencyMode = Literal["quality", "realtime"]

VideoEncoderBitrateMode = Literal["constant", "variable", "quantizer"]

CodecState = Literal["unconfigured", "configured", "closed"]

EncodedAudioChunkType = Literal["key", "delta"]

EncodedVideoChunkType = Literal["key", "delta"]

AudioSampleFormat = Literal["u8", "s16", "s32", "f32", "u8-planar", "s16-planar", "s32-planar", "f32-planar"]

VideoPixelFormat = Literal["I420", "I420A", "I422", "I444", "NV12", "RGBA", "RGBX", "BGRA", "BGRX"]

VideoColorPrimaries = Literal["bt709", "bt470bg", "smpte170m", "bt2020", "smpte432"]

VideoTransferCharacteristics = Literal["bt709", "smpte170m", "iec61966-2-1", "linear", "pq", "hlg"]

VideoMatrixCoefficients = Literal["rgb", "bt709", "bt470bg", "smpte170m", "bt2020-ncl"]

WebGLPowerPreference = Literal["default", "low-power", "high-performance"]

GPUPowerPreference = Literal["low-power", "high-performance"]

GPUFeatureName = Literal["depth-clip-control", "depth32float-stencil8", "texture-compression-bc", "texture-compression-etc2", "texture-compression-astc", "timestamp-query", "indirect-first-instance", "shader-f16", "rg11b10ufloat-renderable", "bgra8unorm-storage", "float32-filterable"]

GPUBufferMapState = Literal["unmapped", "pending", "mapped"]

GPUTextureDimension = Literal["1d", "2d", "3d"]

GPUTextureViewDimension = Literal["1d", "2d", "2d-array", "cube", "cube-array", "3d"]

GPUTextureAspect = Literal["all", "stencil-only", "depth-only"]

GPUTextureFormat = Literal["r8unorm", "r8snorm", "r8uint", "r8sint", "r16uint", "r16sint", "r16float", "rg8unorm", "rg8snorm", "rg8uint", "rg8sint", "r32uint", "r32sint", "r32float", "rg16uint", "rg16sint", "rg16float", "rgba8unorm", "rgba8unorm-srgb", "rgba8snorm", "rgba8uint", "rgba8sint", "bgra8unorm", "bgra8unorm-srgb", "rgb9e5ufloat", "rgb10a2uint", "rgb10a2unorm", "rg11b10ufloat", "rg32uint", "rg32sint", "rg32float", "rgba16uint", "rgba16sint", "rgba16float", "rgba32uint", "rgba32sint", "rgba32float", "stencil8", "depth16unorm", "depth24plus", "depth24plus-stencil8", "depth32float", "depth32float-stencil8", "bc1-rgba-unorm", "bc1-rgba-unorm-srgb", "bc2-rgba-unorm", "bc2-rgba-unorm-srgb", "bc3-rgba-unorm", "bc3-rgba-unorm-srgb", "bc4-r-unorm", "bc4-r-snorm", "bc5-rg-unorm", "bc5-rg-snorm", "bc6h-rgb-ufloat", "bc6h-rgb-float", "bc7-rgba-unorm", "bc7-rgba-unorm-srgb", "etc2-rgb8unorm", "etc2-rgb8unorm-srgb", "etc2-rgb8a1unorm", "etc2-rgb8a1unorm-srgb", "etc2-rgba8unorm", "etc2-rgba8unorm-srgb", "eac-r11unorm", "eac-r11snorm", "eac-rg11unorm", "eac-rg11snorm", "astc-4x4-unorm", "astc-4x4-unorm-srgb", "astc-5x4-unorm", "astc-5x4-unorm-srgb", "astc-5x5-unorm", "astc-5x5-unorm-srgb", "astc-6x5-unorm", "astc-6x5-unorm-srgb", "astc-6x6-unorm", "astc-6x6-unorm-srgb", "astc-8x5-unorm", "astc-8x5-unorm-srgb", "astc-8x6-unorm", "astc-8x6-unorm-srgb", "astc-8x8-unorm", "astc-8x8-unorm-srgb", "astc-10x5-unorm", "astc-10x5-unorm-srgb", "astc-10x6-unorm", "astc-10x6-unorm-srgb", "astc-10x8-unorm", "astc-10x8-unorm-srgb", "astc-10x10-unorm", "astc-10x10-unorm-srgb", "astc-12x10-unorm", "astc-12x10-unorm-srgb", "astc-12x12-unorm", "astc-12x12-unorm-srgb"]

GPUAddressMode = Literal["clamp-to-edge", "repeat", "mirror-repeat"]

GPUFilterMode = Literal["nearest", "linear"]

GPUMipmapFilterMode = Literal["nearest", "linear"]

GPUCompareFunction = Literal["never", "less", "equal", "less-equal", "greater", "not-equal", "greater-equal", "always"]

GPUBufferBindingType = Literal["uniform", "storage", "read-only-storage"]

GPUSamplerBindingType = Literal["filtering", "non-filtering", "comparison"]

GPUTextureSampleType = Literal["float", "unfilterable-float", "depth", "sint", "uint"]

GPUStorageTextureAccess = Literal["write-only"]

GPUCompilationMessageType = Literal["error", "warning", "info"]

GPUPipelineErrorReason = Literal["validation", "internal"]

GPUAutoLayoutMode = Literal["auto"]

GPUPrimitiveTopology = Literal["point-list", "line-list", "line-strip", "triangle-list", "triangle-strip"]

GPUFrontFace = Literal["ccw", "cw"]

GPUCullMode = Literal["none", "front", "back"]

GPUBlendFactor = Literal["zero", "one", "src", "one-minus-src", "src-alpha", "one-minus-src-alpha", "dst", "one-minus-dst", "dst-alpha", "one-minus-dst-alpha", "src-alpha-saturated", "constant", "one-minus-constant"]

GPUBlendOperation = Literal["add", "subtract", "reverse-subtract", "min", "max"]

GPUStencilOperation = Literal["keep", "zero", "replace", "invert", "increment-clamp", "decrement-clamp", "increment-wrap", "decrement-wrap"]

GPUIndexFormat = Literal["uint16", "uint32"]

GPUVertexFormat = Literal["uint8x2", "uint8x4", "sint8x2", "sint8x4", "unorm8x2", "unorm8x4", "snorm8x2", "snorm8x4", "uint16x2", "uint16x4", "sint16x2", "sint16x4", "unorm16x2", "unorm16x4", "snorm16x2", "snorm16x4", "float16x2", "float16x4", "float32", "float32x2", "float32x3", "float32x4", "uint32", "uint32x2", "uint32x3", "uint32x4", "sint32", "sint32x2", "sint32x3", "sint32x4"]

GPUVertexStepMode = Literal["vertex", "instance"]

GPULoadOp = Literal["load", "clear"]

GPUStoreOp = Literal["store", "discard"]

GPUQueryType = Literal["occlusion", "timestamp"]

GPUCanvasAlphaMode = Literal["opaque", "premultiplied"]

GPUDeviceLostReason = Literal["unknown", "destroyed"]

GPUErrorFilter = Literal["validation", "out-of-memory", "internal"]

HIDUnitSystem = Literal["none", "si-linear", "si-rotation", "english-linear", "english-rotation", "vendor-defined", "reserved"]

MIDIPortType = Literal["input", "output"]

MIDIPortDeviceState = Literal["disconnected", "connected"]

MIDIPortConnectionState = Literal["open", "closed", "pending"]

MLDeviceType = Literal["cpu", "gpu"]

MLPowerPreference = Literal["default", "high-performance", "low-power"]

MLInputOperandLayout = Literal["nchw", "nhwc"]

MLOperandType = Literal["float32", "float16", "int32", "uint32", "int8", "uint8"]

MLConv2dFilterOperandLayout = Literal["oihw", "hwio", "ohwi", "ihwo"]

MLAutoPad = Literal["explicit", "same-upper", "same-lower"]

MLConvTranspose2dFilterOperandLayout = Literal["iohw", "hwoi", "ohwi"]

MLGruWeightLayout = Literal["zrn", "rzn"]

MLRecurrentNetworkDirection = Literal["forward", "backward", "both"]

MLLstmWeightLayout = Literal["iofg", "ifgo"]

MLPaddingMode = Literal["constant", "edge", "reflection", "symmetric"]

MLRoundingType = Literal["floor", "ceil"]

MLInterpolationMode = Literal["nearest-neighbor", "linear"]

SFrameTransformRole = Literal["encrypt", "decrypt"]

SFrameTransformErrorEventType = Literal["authentication", "keyID", "syntax"]

RTCEncodedVideoFrameType = Literal["empty", "key", "delta"]

RTCErrorDetailTypeIdp = Literal["idp-bad-script-failure", "idp-execution-failure", "idp-load-failure", "idp-need-login", "idp-timeout", "idp-tls-failure", "idp-token-expired", "idp-token-invalid"]

RTCPriorityType = Literal["very-low", "low", "medium", "high"]

RTCStatsType = Literal["codec", "inbound-rtp", "outbound-rtp", "remote-inbound-rtp", "remote-outbound-rtp", "media-source", "media-playout", "peer-connection", "data-channel", "transport", "candidate-pair", "local-candidate", "remote-candidate", "certificate"]

RTCQualityLimitationReason = Literal["none", "cpu", "bandwidth", "other"]

RTCDtlsRole = Literal["client", "server", "unknown"]

RTCStatsIceCandidatePairState = Literal["frozen", "waiting", "in-progress", "failed", "succeeded"]

RTCIceTransportPolicy = Literal["relay", "all"]

RTCBundlePolicy = Literal["balanced", "max-compat", "max-bundle"]

RTCRtcpMuxPolicy = Literal["require"]

RTCSignalingState = Literal["stable", "have-local-offer", "have-remote-offer", "have-local-pranswer", "have-remote-pranswer", "closed"]

RTCIceGatheringState = Literal["new", "gathering", "complete"]

RTCPeerConnectionState = Literal["closed", "failed", "disconnected", "new", "connecting", "connected"]

RTCIceConnectionState = Literal["closed", "failed", "disconnected", "new", "checking", "completed", "connected"]

RTCSdpType = Literal["offer", "pranswer", "answer", "rollback"]

RTCIceProtocol = Literal["udp", "tcp"]

RTCIceTcpCandidateType = Literal["active", "passive", "so"]

RTCIceCandidateType = Literal["host", "srflx", "prflx", "relay"]

RTCIceServerTransportProtocol = Literal["udp", "tcp", "tls"]

RTCRtpTransceiverDirection = Literal["sendrecv", "sendonly", "recvonly", "inactive", "stopped"]

RTCDtlsTransportState = Literal["new", "connecting", "connected", "closed", "failed"]

RTCIceGathererState = Literal["new", "gathering", "complete"]

RTCIceTransportState = Literal["closed", "failed", "disconnected", "new", "checking", "completed", "connected"]

RTCIceRole = Literal["unknown", "controlling", "controlled"]

RTCIceComponent = Literal["rtp", "rtcp"]

RTCSctpTransportState = Literal["connecting", "connected", "closed"]

RTCDataChannelState = Literal["connecting", "open", "closing", "closed"]

RTCErrorDetailType = Literal["data-channel-failure", "dtls-failure", "fingerprint-failure", "sctp-failure", "sdp-syntax-error", "hardware-encoder-not-available", "hardware-encoder-error"]

BinaryType = Literal["blob", "arraybuffer"]

WebTransportReliabilityMode = Literal["pending", "reliable-only", "supports-unreliable"]

WebTransportCongestionControl = Literal["default", "throughput", "low-latency"]

WebTransportErrorSource = Literal["stream", "session"]

USBTransferStatus = Literal["ok", "stall", "babble"]

USBRequestType = Literal["standard", "class", "vendor"]

USBRecipient = Literal["device", "interface", "endpoint", "other"]

USBDirection = Literal["in", "out"]

USBEndpointType = Literal["bulk", "interrupt", "isochronous"]

AutoKeyword = Literal["auto"]

DirectionSetting = Literal["", "rl", "lr"]

LineAlignSetting = Literal["start", "center", "end"]

PositionAlignSetting = Literal["line-left", "center", "line-right", "auto"]

AlignSetting = Literal["start", "center", "end", "left", "right"]

ScrollSetting = Literal["", "up"]

XREnvironmentBlendMode = Literal["opaque", "alpha-blend", "additive"]

XRInteractionMode = Literal["screen-space", "world-space"]

XRDepthUsage = Literal["cpu-optimized", "gpu-optimized"]

XRDepthDataFormat = Literal["luminance-alpha", "float32"]

XRDOMOverlayType = Literal["screen", "floating", "head-locked"]

XRHandJoint = Literal["wrist", "thumb-metacarpal", "thumb-phalanx-proximal", "thumb-phalanx-distal", "thumb-tip", "index-finger-metacarpal", "index-finger-phalanx-proximal", "index-finger-phalanx-intermediate", "index-finger-phalanx-distal", "index-finger-tip", "middle-finger-metacarpal", "middle-finger-phalanx-proximal", "middle-finger-phalanx-intermediate", "middle-finger-phalanx-distal", "middle-finger-tip", "ring-finger-metacarpal", "ring-finger-phalanx-proximal", "ring-finger-phalanx-intermediate", "ring-finger-phalanx-distal", "ring-finger-tip", "pinky-finger-metacarpal", "pinky-finger-phalanx-proximal", "pinky-finger-phalanx-intermediate", "pinky-finger-phalanx-distal", "pinky-finger-tip"]

XRHitTestTrackableType = Literal["point", "plane", "mesh"]

XRReflectionFormat = Literal["srgba8", "rgba16f"]

XRSessionMode = Literal["inline", "immersive-vr", "immersive-ar"]

XRVisibilityState = Literal["visible", "visible-blurred", "hidden"]

XRReferenceSpaceType = Literal["viewer", "local", "local-floor", "bounded-floor", "unbounded"]

XREye = Literal["none", "left", "right"]

XRHandedness = Literal["none", "left", "right"]

XRTargetRayMode = Literal["gaze", "tracked-pointer", "screen"]

XRLayerLayout = Literal["default", "mono", "stereo", "stereo-left-right", "stereo-top-bottom"]

XRLayerQuality = Literal["default", "text-optimized", "graphics-optimized"]

XRTextureType = Literal["texture", "texture-array"]

XMLHttpRequestResponseType = Literal["", "arraybuffer", "blob", "document", "json", "text"]

GLuint64EXT: TypeAlias = int

BlobPart: TypeAlias = Union['BufferSource', 'Blob', 'str']

AlgorithmIdentifier: TypeAlias = Union['object', 'str']

HashAlgorithmIdentifier: TypeAlias = AlgorithmIdentifier

BigInteger: TypeAlias = Uint8Array

NamedCurve: TypeAlias = str

ClipboardItemData: TypeAlias = Awaitable[Union['str', 'Blob']]

ClipboardItems: TypeAlias = Sequence[ClipboardItem]

PressureUpdateCallback = Callable[[Sequence[PressureRecord],PressureObserver], None]

CookieList: TypeAlias = Sequence[CookieListItem]

PasswordCredentialInit: TypeAlias = Union['PasswordCredentialData', 'HTMLFormElement']

AnimatorInstanceConstructor = Callable[[Any,Any], Any]

BinaryData: TypeAlias = Union['ArrayBuffer', 'ArrayBufferView']

CSSStringSource: TypeAlias = Union['str', 'ReadableStream']

CSSToken: TypeAlias = Union['str', 'CSSStyleValue', 'CSSParserValue']

CSSUnparsedSegment: TypeAlias = Union['str', 'CSSVariableReferenceValue']

CSSKeywordish: TypeAlias = Union['str', 'CSSKeywordValue']

CSSNumberish: TypeAlias = Union['float', 'CSSNumericValue']

CSSPerspectiveValue: TypeAlias = Union['CSSNumericValue', 'CSSKeywordish']

CSSColorRGBComp: TypeAlias = Union['CSSNumberish', 'CSSKeywordish']

CSSColorPercent: TypeAlias = Union['CSSNumberish', 'CSSKeywordish']

CSSColorNumber: TypeAlias = Union['CSSNumberish', 'CSSKeywordish']

CSSColorAngle: TypeAlias = Union['CSSNumberish', 'CSSKeywordish']

UpdateCallback = Callable[[], Awaitable[Any]]

GeometryNode: TypeAlias = Union['Text', 'Element', 'CSSPseudoElement', 'Document']

EventListener = Callable[[], None]

MutationCallback = Callable[[Sequence[MutationRecord],MutationObserver], None]

NodeFilter = Callable[[], None]

XPathNSResolver = Callable[[], None]

ErrorCallback = Callable[[DOMException], None]

FileSystemEntryCallback = Callable[[FileSystemEntry], None]

FileSystemEntriesCallback = Callable[[Sequence[FileSystemEntry]], None]

FileCallback = Callable[[File], None]

FencedFrameConfigSize: TypeAlias = Union['int', 'OpaqueProperty']

FencedFrameConfigURL: TypeAlias = str

ReportEventType: TypeAlias = Union['FenceEvent', 'str']

HeadersInit: TypeAlias = Union['Sequence[Sequence[ByteString]]', 'ByteString']

XMLHttpRequestBodyInit: TypeAlias = Union['Blob', 'BufferSource', 'FormData', 'URLSearchParams', 'str']

BodyInit: TypeAlias = Union['ReadableStream', 'XMLHttpRequestBodyInit']

RequestInfo: TypeAlias = Union['Request', 'str']

StartInDirectory: TypeAlias = Union['WellKnownDirectory', 'FileSystemHandle']

FileSystemWriteChunkType: TypeAlias = Union['BufferSource', 'Blob', 'str', 'WriteParams']

PositionCallback = Callable[[GeolocationPosition], None]

PositionErrorCallback = Callable[[GeolocationPositionError], None]

DOMHighResTimeStamp: TypeAlias = float

EpochTimeStamp: TypeAlias = int

HTMLOrSVGScriptElement: TypeAlias = Union['HTMLScriptElement', 'SVGScriptElement']

MediaProvider: TypeAlias = Union['MediaStream', 'MediaSource', 'Blob']

RenderingContext: TypeAlias = Union['CanvasRenderingContext2D', 'ImageBitmapRenderingContext', 'WebGLRenderingContext', 'WebGL2RenderingContext', 'GPUCanvasContext']

BlobCallback = Callable[[Union['Blob', 'None']], None]

HTMLOrSVGImageElement: TypeAlias = Union['HTMLImageElement', 'SVGImageElement']

CanvasImageSource: TypeAlias = Union['HTMLOrSVGImageElement', 'HTMLVideoElement', 'HTMLCanvasElement', 'ImageBitmap', 'OffscreenCanvas', 'VideoFrame']

OffscreenRenderingContext: TypeAlias = Union['OffscreenCanvasRenderingContext2D', 'ImageBitmapRenderingContext', 'WebGLRenderingContext', 'WebGL2RenderingContext', 'GPUCanvasContext']

CustomElementConstructor = Callable[[], HTMLElement]

FunctionStringCallback = Callable[[str], None]

NavigationInterceptHandler = Callable[[], Awaitable[None]]

EventHandlerNonNull = Callable[[Event], Any]

EventHandler: TypeAlias = Union['EventHandlerNonNull', 'None']

OnErrorEventHandlerNonNull = Callable[[Union['Event', 'str'],str,int,int,Any], Any]

OnErrorEventHandler: TypeAlias = Union['OnErrorEventHandlerNonNull', 'None']

OnBeforeUnloadEventHandlerNonNull = Callable[[Event], Union['str', 'None']]

OnBeforeUnloadEventHandler: TypeAlias = Union['OnBeforeUnloadEventHandlerNonNull', 'None']

TimerHandler: TypeAlias = Union['str', 'Function']

ImageBitmapSource: TypeAlias = Union['CanvasImageSource', 'Blob', 'ImageData']

FrameRequestCallback = Callable[[DOMHighResTimeStamp], None]

MessageEventSource: TypeAlias = Union['WindowProxy', 'MessagePort', 'ServiceWorker']

ConstrainPoint2D: TypeAlias = Union['Sequence[Point2D]', 'ConstrainPoint2DParameters']

IntersectionObserverCallback = Callable[[Sequence[IntersectionObserverEntry],IntersectionObserver], None]

ProfilerResource: TypeAlias = str

JsonLdRecord: TypeAlias = Any

JsonLdInput: TypeAlias = Union['JsonLdRecord', 'Sequence[JsonLdRecord]', 'str', 'RemoteDocument']

JsonLdContext: TypeAlias = Union['JsonLdRecord', 'Sequence[Union["JsonLdRecord", "str"]]', 'str']

LoadDocumentCallback = Callable[[str,Union['LoadDocumentOptions', 'None']], Awaitable[RemoteDocument]]

NavigatorUserMediaSuccessCallback = Callable[[MediaStream], None]

NavigatorUserMediaErrorCallback = Callable[[DOMException], None]

ConstrainULong: TypeAlias = Union['int', 'ConstrainULongRange']

ConstrainDouble: TypeAlias = Union['float', 'ConstrainDoubleRange']

ConstrainBoolean: TypeAlias = Union['bool', 'ConstrainBooleanParameters']

ConstrainDOMString: TypeAlias = Union['str', 'Sequence[str]', 'ConstrainDOMStringParameters']

MediaSessionActionHandler = Callable[[MediaSessionActionDetails], None]

Megabit: TypeAlias = float

Millisecond: TypeAlias = int

NotificationPermissionCallback = Callable[[NotificationPermission], None]

RotationMatrixType: TypeAlias = Union['Float32Array', 'Float64Array', 'DOMMatrix']

PerformanceEntryList: TypeAlias = Sequence[PerformanceEntry]

PerformanceObserverCallback = Callable[[PerformanceObserverEntryList,PerformanceObserver,PerformanceObserverCallbackOptions], None]

PushMessageDataInit: TypeAlias = Union['BufferSource', 'str']

RemotePlaybackAvailabilityCallback = Callable[[bool], None]

ReportingObserverCallback = Callable[[Sequence[Report],ReportingObserver], None]

ReportList: TypeAlias = Sequence[Report]

IdleRequestCallback = Callable[[IdleDeadline], None]

ResizeObserverCallback = Callable[[Sequence[ResizeObserverEntry],ResizeObserver], None]

AttributeMatchList: TypeAlias = Sequence[str]

SchedulerPostTaskCallback = Callable[[], Any]

SharedStorageOperationConstructor = Callable[[SharedStorageRunOperationMethodOptions], SharedStorageOperation]

SharedStorageResponse: TypeAlias = Union['str', 'FencedFrameConfig']

ReadableStreamReader: TypeAlias = Union['ReadableStreamDefaultReader', 'ReadableStreamBYOBReader']

ReadableStreamController: TypeAlias = Union['ReadableStreamDefaultController', 'ReadableByteStreamController']

UnderlyingSourceStartCallback = Callable[[ReadableStreamController], Any]

UnderlyingSourcePullCallback = Callable[[ReadableStreamController], Awaitable[None]]

UnderlyingSourceCancelCallback = Callable[[Any], Awaitable[None]]

UnderlyingSinkStartCallback = Callable[[WritableStreamDefaultController], Any]

UnderlyingSinkWriteCallback = Callable[[Any,WritableStreamDefaultController], Awaitable[None]]

UnderlyingSinkCloseCallback = Callable[[], Awaitable[None]]

UnderlyingSinkAbortCallback = Callable[[Any], Awaitable[None]]

TransformerStartCallback = Callable[[TransformStreamDefaultController], Any]

TransformerFlushCallback = Callable[[TransformStreamDefaultController], Awaitable[None]]

TransformerTransformCallback = Callable[[Any,TransformStreamDefaultController], Awaitable[None]]

QueuingStrategySize = Callable[[Any], float]

CreateHTMLCallback = Callable[[str,Any], str]

CreateScriptCallback = Callable[[str,Any], str]

CreateScriptURLCallback = Callable[[str,Any], str]

HTMLString: TypeAlias = str

ScriptString: TypeAlias = str

ScriptURLString: TypeAlias = str

TrustedType: TypeAlias = Union['TrustedHTML', 'TrustedScript', 'TrustedScriptURL']

URLPatternInput: TypeAlias = Union['str', 'URLPatternInit']

VibratePattern: TypeAlias = Union['int', 'Sequence[int]']

VideoFrameRequestCallback = Callable[[DOMHighResTimeStamp,VideoFrameCallbackMetadata], None]

EffectCallback = Callable[[Union['float', 'None'],Union['Element', 'CSSPseudoElement'],Animation], None]

LaunchConsumer = Callable[[LaunchParams], Any]

UUID: TypeAlias = str

BluetoothServiceUUID: TypeAlias = Union['str', 'int']

BluetoothCharacteristicUUID: TypeAlias = Union['str', 'int']

BluetoothDescriptorUUID: TypeAlias = Union['str', 'int']

LockGrantedCallback = Callable[[Union['Lock', 'None']], Awaitable[Any]]

NDEFMessageSource: TypeAlias = Union['str', 'BufferSource', 'NDEFMessageInit']

DecodeErrorCallback = Callable[[DOMException], None]

DecodeSuccessCallback = Callable[[AudioBuffer], None]

AudioWorkletProcessorConstructor = Callable[[object], AudioWorkletProcessor]

AudioWorkletProcessCallback = Callable[[Sequence[Sequence[Float32Array]],Sequence[Sequence[Float32Array]],object], bool]

Base64URLString: TypeAlias = str

PublicKeyCredentialJSON: TypeAlias = Union['RegistrationResponseJSON', 'AuthenticationResponseJSON']

COSEAlgorithmIdentifier: TypeAlias = int

UvmEntry: TypeAlias = Sequence[int]

UvmEntries: TypeAlias = Sequence[UvmEntry]

AudioDataOutputCallback = Callable[[AudioData], None]

VideoFrameOutputCallback = Callable[[VideoFrame], None]

EncodedAudioChunkOutputCallback = Callable[[EncodedAudioChunk,EncodedAudioChunkMetadata], None]

EncodedVideoChunkOutputCallback = Callable[[EncodedVideoChunk,EncodedVideoChunkMetadata], None]

WebCodecsErrorCallback = Callable[[DOMException], None]

ImageBufferSource: TypeAlias = Union['BufferSource', 'ReadableStream']

GLenum: TypeAlias = int

GLboolean: TypeAlias = bool

GLbitfield: TypeAlias = int

GLbyte: TypeAlias = int

GLshort: TypeAlias = int

GLint: TypeAlias = int

GLsizei: TypeAlias = int

GLintptr: TypeAlias = int

GLsizeiptr: TypeAlias = int

GLubyte: TypeAlias = int

GLushort: TypeAlias = int

GLuint: TypeAlias = int

GLfloat: TypeAlias = float

GLclampf: TypeAlias = float

TexImageSource: TypeAlias = Union['ImageBitmap', 'ImageData', 'HTMLImageElement', 'HTMLCanvasElement', 'HTMLVideoElement', 'OffscreenCanvas', 'VideoFrame']

Float32List: TypeAlias = Union['Float32Array', 'Sequence[GLfloat]']

Int32List: TypeAlias = Union['Int32Array', 'Sequence[GLint]']

GLint64: TypeAlias = int

GLuint64: TypeAlias = int

Uint32List: TypeAlias = Union['Uint32Array', 'Sequence[GLuint]']

GPUBufferUsageFlags: TypeAlias = int

GPUMapModeFlags: TypeAlias = int

GPUTextureUsageFlags: TypeAlias = int

GPUShaderStageFlags: TypeAlias = int

GPUBindingResource: TypeAlias = Union['GPUSampler', 'GPUTextureView', 'GPUBufferBinding', 'GPUExternalTexture']

GPUPipelineConstantValue: TypeAlias = float

GPUColorWriteFlags: TypeAlias = int

GPUImageCopyExternalImageSource: TypeAlias = Union['ImageBitmap', 'ImageData', 'HTMLImageElement', 'HTMLVideoElement', 'VideoFrame', 'HTMLCanvasElement', 'OffscreenCanvas']

GPUBufferDynamicOffset: TypeAlias = int

GPUStencilValue: TypeAlias = int

GPUSampleMask: TypeAlias = int

GPUDepthBias: TypeAlias = int

GPUSize64: TypeAlias = int

GPUIntegerCoordinate: TypeAlias = int

GPUIndex32: TypeAlias = int

GPUSize32: TypeAlias = int

GPUSignedOffset32: TypeAlias = int

GPUSize64Out: TypeAlias = int

GPUIntegerCoordinateOut: TypeAlias = int

GPUSize32Out: TypeAlias = int

GPUFlagsConstant: TypeAlias = int

GPUColor: TypeAlias = Union['Sequence[float]', 'GPUColorDict']

GPUOrigin2D: TypeAlias = Union['Sequence[GPUIntegerCoordinate]', 'GPUOrigin2DDict']

GPUOrigin3D: TypeAlias = Union['Sequence[GPUIntegerCoordinate]', 'GPUOrigin3DDict']

GPUExtent3D: TypeAlias = Union['Sequence[GPUIntegerCoordinate]', 'GPUExtent3DDict']

ArrayBufferView: TypeAlias = Union['Int8Array', 'Int16Array', 'Int32Array', 'Uint8Array', 'Uint16Array', 'Uint32Array', 'Uint8ClampedArray', 'BigInt64Array', 'BigUint64Array', 'Float32Array', 'Float64Array', 'DataView']

BufferSource: TypeAlias = Union['ArrayBufferView', 'ArrayBuffer']

AllowSharedBufferSource: TypeAlias = Union['ArrayBuffer', 'SharedArrayBuffer', 'ArrayBufferView']

Function = Callable[[Any], Any]

VoidFunction = Callable[[], None]

MLNamedArrayBufferViews: TypeAlias = ArrayBufferView

MLGPUResource: TypeAlias = Union['GPUBuffer', 'GPUTexture']

MLNamedGPUResources: TypeAlias = MLGPUResource

MLNamedOperands: TypeAlias = MLOperand

MLBufferView: TypeAlias = Union['ArrayBufferView', 'MLBufferResourceView']

RTCRtpTransform: TypeAlias = Union['SFrameTransform', 'RTCRtpScriptTransform']

SmallCryptoKeyID: TypeAlias = int

CryptoKeyID: TypeAlias = Union['SmallCryptoKeyID', 'bigint']

GenerateAssertionCallback = Callable[[str,str,RTCIdentityProviderOptions], Awaitable[RTCIdentityAssertionResult]]

ValidateAssertionCallback = Callable[[str,str], Awaitable[RTCIdentityValidationResult]]

RTCPeerConnectionErrorCallback = Callable[[DOMException], None]

RTCSessionDescriptionCallback = Callable[[RTCSessionDescriptionInit], None]

LineAndPositionSetting: TypeAlias = Union['float', 'AutoKeyword']

XRFrameRequestCallback = Callable[[DOMHighResTimeStamp,XRFrame], None]

XRWebGLRenderingContext: TypeAlias = Union['WebGLRenderingContext', 'WebGL2RenderingContext']

FormDataEntryValue: TypeAlias = Union['File', 'str']

class ANGLE_instanced_arrays:
    VERTEX_ATTRIB_ARRAY_DIVISOR_ANGLE = 0x88FE

    def drawArraysInstancedANGLE(self, mode: GLenum, first: GLint, count: GLsizei, primcount: GLsizei) -> None: ...

    def drawElementsInstancedANGLE(self, mode: GLenum, count: GLsizei, type: GLenum, offset: GLintptr, primcount: GLsizei) -> None: ...

    def vertexAttribDivisorANGLE(self, index: GLuint, divisor: GLuint) -> None: ...

class CSPViolationReportBody(ReportBody):

    def toJSON(self) -> object: ...
    documentURL: str
    referrer: Union['str', 'None']
    blockedURL: Union['str', 'None']
    effectiveDirective: str
    originalPolicy: str
    sourceFile: Union['str', 'None']
    sample: Union['str', 'None']
    disposition: SecurityPolicyViolationEventDisposition
    statusCode: int
    lineNumber: Union['int', 'None']
    columnNumber: Union['int', 'None']

class SecurityPolicyViolationEvent(Event):
    @classmethod
    def new(cls, type: str, eventInitDict: Union['SecurityPolicyViolationEventInit', 'None'] = {}) -> SecurityPolicyViolationEvent: ...
    documentURI: str
    referrer: str
    blockedURI: str
    effectiveDirective: str
    violatedDirective: str
    originalPolicy: str
    sourceFile: str
    sample: str
    disposition: SecurityPolicyViolationEventDisposition
    statusCode: int
    lineNumber: int
    columnNumber: int

class SecurityPolicyViolationEventInit(EventInit):
    documentURI: str
    referrer: NotRequired[str]
    blockedURI: NotRequired[str]
    violatedDirective: str
    effectiveDirective: str
    originalPolicy: str
    sourceFile: NotRequired[str]
    sample: NotRequired[str]
    disposition: SecurityPolicyViolationEventDisposition
    statusCode: int
    lineNumber: NotRequired[int]
    columnNumber: NotRequired[int]

class XMLSerializer:
    @classmethod
    def new(cls) -> XMLSerializer: ...

    def serializeToString(self, root: Node) -> str: ...

class InnerHTML:
    innerHTML: str

class Element(Node, InnerHTML, Region, GeometryUtils, ParentNode, NonDocumentTypeChildNode, ChildNode, Slottable, ARIAMixin, Animatable):
    outerHTML: str

    def insertAdjacentHTML(self, position: str, text: str) -> None: ...

    def getSpatialNavigationContainer(self) -> Node: ...

    def focusableAreas(self, option: Union['FocusableAreasOption', 'None'] = {}) -> Sequence[Node]: ...

    def spatialNavigationSearch(self, dir: SpatialNavigationDirection, options: Union['SpatialNavigationSearchOptions', 'None'] = {}) -> Union['Node', 'None']: ...

    def pseudo(self, type: str) -> Union['CSSPseudoElement', 'None']: ...
    part: DOMTokenList

    def computedStyleMap(self) -> StylePropertyMapReadOnly: ...

    def getClientRects(self) -> DOMRectList: ...

    def getBoundingClientRect(self) -> DOMRect: ...

    def checkVisibility(self, options: Union['CheckVisibilityOptions', 'None'] = {}) -> bool: ...

    def scrollIntoView(self, arg: Union['bool', 'ScrollIntoViewOptions', 'None'] = {}) -> None: ...
    @overload
    def scroll(self, options: Union['ScrollToOptions', 'None'] = {}) -> None: ...
    @overload
    def scroll(self, x: float, y: float) -> None: ...
    @overload
    def scrollTo(self, options: Union['ScrollToOptions', 'None'] = {}) -> None: ...
    @overload
    def scrollTo(self, x: float, y: float) -> None: ...
    @overload
    def scrollBy(self, options: Union['ScrollToOptions', 'None'] = {}) -> None: ...
    @overload
    def scrollBy(self, x: float, y: float) -> None: ...
    scrollTop: float
    scrollLeft: float
    scrollWidth: int
    scrollHeight: int
    clientTop: int
    clientLeft: int
    clientWidth: int
    clientHeight: int
    namespaceURI: Union['str', 'None']
    prefix: Union['str', 'None']
    localName: str
    tagName: str
    id: str
    className: str
    classList: DOMTokenList
    slot: str

    def hasAttributes(self) -> bool: ...
    attributes: NamedNodeMap

    def getAttributeNames(self) -> Sequence[str]: ...

    def getAttribute(self, qualifiedName: str) -> Union['str', 'None']: ...

    def getAttributeNS(self, namespace: Union['str', 'None'], localName: str) -> Union['str', 'None']: ...

    def setAttribute(self, qualifiedName: str, value: str) -> None: ...

    def setAttributeNS(self, namespace: Union['str', 'None'], qualifiedName: str, value: str) -> None: ...

    def removeAttribute(self, qualifiedName: str) -> None: ...

    def removeAttributeNS(self, namespace: Union['str', 'None'], localName: str) -> None: ...

    def toggleAttribute(self, qualifiedName: str, force: Union['bool', 'None'] = None) -> bool: ...

    def hasAttribute(self, qualifiedName: str) -> bool: ...

    def hasAttributeNS(self, namespace: Union['str', 'None'], localName: str) -> bool: ...

    def getAttributeNode(self, qualifiedName: str) -> Union['Attr', 'None']: ...

    def getAttributeNodeNS(self, namespace: Union['str', 'None'], localName: str) -> Union['Attr', 'None']: ...

    def setAttributeNode(self, attr: Attr) -> Union['Attr', 'None']: ...

    def setAttributeNodeNS(self, attr: Attr) -> Union['Attr', 'None']: ...

    def removeAttributeNode(self, attr: Attr) -> Attr: ...

    def attachShadow(self, init: ShadowRootInit) -> ShadowRoot: ...
    shadowRoot: Union['ShadowRoot', 'None']

    def closest(self, selectors: str) -> Union['Element', 'None']: ...

    def matches(self, selectors: str) -> bool: ...

    def webkitMatchesSelector(self, selectors: str) -> bool: ...

    def getElementsByTagName(self, qualifiedName: str) -> HTMLCollection: ...

    def getElementsByTagNameNS(self, namespace: Union['str', 'None'], localName: str) -> HTMLCollection: ...

    def getElementsByClassName(self, classNames: str) -> HTMLCollection: ...

    def insertAdjacentElement(self, where: str, element: Element) -> Union['Element', 'None']: ...

    def insertAdjacentText(self, where: str, data: str) -> None: ...
    elementTiming: str

    def requestFullscreen(self, options: Union['FullscreenOptions', 'None'] = {}) -> Awaitable[None]: ...
    onfullscreenchange: EventHandler
    onfullscreenerror: EventHandler

    def setPointerCapture(self, pointerId: int) -> None: ...

    def releasePointerCapture(self, pointerId: int) -> None: ...

    def hasPointerCapture(self, pointerId: int) -> bool: ...

    def requestPointerLock(self) -> None: ...

    def setHTML(self, input: str, options: Union['SetHTMLOptions', 'None'] = {}) -> None: ...

class ShadowRoot(DocumentFragment, InnerHTML, DocumentOrShadowRoot):
    mode: ShadowRootMode
    delegatesFocus: bool
    slotAssignment: SlotAssignmentMode
    host: Element
    onslotchange: EventHandler

class Range(AbstractRange):
    @classmethod
    def new(cls) -> Range: ...

    def createContextualFragment(self, fragment: str) -> DocumentFragment: ...

    def getClientRects(self) -> DOMRectList: ...

    def getBoundingClientRect(self) -> DOMRect: ...
    commonAncestorContainer: Node

    def setStart(self, node: Node, offset: int) -> None: ...

    def setEnd(self, node: Node, offset: int) -> None: ...

    def setStartBefore(self, node: Node) -> None: ...

    def setStartAfter(self, node: Node) -> None: ...

    def setEndBefore(self, node: Node) -> None: ...

    def setEndAfter(self, node: Node) -> None: ...

    def collapse(self, toStart: Union['bool', 'None'] = False) -> None: ...

    def selectNode(self, node: Node) -> None: ...

    def selectNodeContents(self, node: Node) -> None: ...
    START_TO_START = 0
    START_TO_END = 1
    END_TO_END = 2
    END_TO_START = 3

    def compareBoundaryPoints(self, how: int, sourceRange: Range) -> int: ...

    def deleteContents(self) -> None: ...

    def extractContents(self) -> DocumentFragment: ...

    def cloneContents(self) -> DocumentFragment: ...

    def insertNode(self, node: Node) -> None: ...

    def surroundContents(self, newParent: Node) -> None: ...

    def cloneRange(self) -> Range: ...

    def detach(self) -> None: ...

    def isPointInRange(self, node: Node, offset: int) -> bool: ...

    def comparePoint(self, node: Node, offset: int) -> int: ...

    def intersectsNode(self, node: Node) -> bool: ...

class StyleSheet:
    type: Union['str', 'str']
    disabled: bool
    ownerNode: Union['Node', 'Union["Element", "ProcessingInstruction", "None"]']
    parentStyleSheet: Union['StyleSheet', 'Union["CSSStyleSheet", "None"]']
    href: Union['str', 'Union["str", "None"]']
    title: Union['str', 'Union["str", "None"]']
    media: MediaList

class StyleSheetList:
    length: int
    @overload
    def item(self, index: int) -> StyleSheet: ...
    @overload
    def item(self, index: int) -> Union['CSSStyleSheet', 'None']: ...

class MediaList:
    mediaText: Union['str', 'str']
    length: int
    @overload
    def item(self, index: int) -> str: ...
    @overload
    def item(self, index: int) -> Union['str', 'None']: ...
    @overload
    def deleteMedium(self, oldMedium: str) -> None: ...
    @overload
    def deleteMedium(self, medium: str) -> None: ...
    @overload
    def appendMedium(self, newMedium: str) -> None: ...
    @overload
    def appendMedium(self, medium: str) -> None: ...

class LinkStyle:
    sheet: Union['StyleSheet', 'Union["CSSStyleSheet", "None"]']

class DocumentStyle:
    styleSheets: StyleSheetList

class CSSRuleList:
    length: int
    @overload
    def item(self, index: int) -> CSSRule: ...
    @overload
    def item(self, index: int) -> Union['CSSRule', 'None']: ...

class CSSRule:
    UNKNOWN_RULE = 0
    STYLE_RULE = 1
    CHARSET_RULE = 2
    IMPORT_RULE = 3
    MEDIA_RULE = 4
    FONT_FACE_RULE = 5
    PAGE_RULE = 6
    type: int
    cssText: Union['str', 'str']
    parentStyleSheet: Union['CSSStyleSheet', 'Union["CSSStyleSheet", "None"]']
    parentRule: Union['CSSRule', 'Union["CSSRule", "None"]']
    KEYFRAMES_RULE = 7
    KEYFRAME_RULE = 8
    SUPPORTS_RULE = 12
    COUNTER_STYLE_RULE = 11
    FONT_FEATURE_VALUES_RULE = 14
    MARGIN_RULE = 9
    NAMESPACE_RULE = 10

class CSSStyleRule(CSSRule, CSSGroupingRule):
    selectorText: Union['str', 'str']
    style: CSSStyleDeclaration
    styleMap: StylePropertyMap

class CSSFontFaceRule(CSSRule):
    style: CSSStyleDeclaration

class CSSPageRule(CSSRule, CSSGroupingRule):
    selectorText: Union['str', 'str']
    style: CSSStyleDeclaration

class CSSCharsetRule(CSSRule):
    encoding: str

class CSSUnknownRule(CSSRule): ...

class CSSStyleDeclaration:
    cssText: Union['str', 'str']
    @overload
    def getPropertyValue(self, propertyName: str) -> str: ...
    @overload
    def getPropertyValue(self, property: str) -> str: ...

    def getPropertyCSSValue(self, propertyName: str) -> CSSValue: ...
    @overload
    def removeProperty(self, propertyName: str) -> str: ...
    @overload
    def removeProperty(self, property: str) -> str: ...
    @overload
    def getPropertyPriority(self, propertyName: str) -> str: ...
    @overload
    def getPropertyPriority(self, property: str) -> str: ...
    @overload
    def setProperty(self, propertyName: str, value: str, priority: str) -> None: ...
    @overload
    def setProperty(self, property: str, value: str, priority: Union['str', 'None'] = "") -> None: ...
    length: int
    @overload
    def item(self, index: int) -> str: ...
    @overload
    def item(self, index: int) -> str: ...
    parentRule: Union['CSSRule', 'Union["CSSRule", "None"]']
    cssFloat: str
    accentColor: str
    additiveSymbols: str
    alignContent: str
    alignItems: str
    alignSelf: str
    alignmentBaseline: str
    all: str
    animation: str
    animationComposition: str
    animationDelay: str
    animationDirection: str
    animationDuration: str
    animationFillMode: str
    animationIterationCount: str
    animationName: str
    animationPlayState: str
    animationTimingFunction: str
    appRegion: str
    appearance: str
    ascentOverride: str
    aspectRatio: str
    backdropFilter: str
    backfaceVisibility: str
    background: str
    backgroundAttachment: str
    backgroundBlendMode: str
    backgroundClip: str
    backgroundColor: str
    backgroundImage: str
    backgroundOrigin: str
    backgroundPosition: str
    backgroundPositionX: str
    backgroundPositionY: str
    backgroundRepeat: str
    backgroundRepeatX: str
    backgroundRepeatY: str
    backgroundSize: str
    basePalette: str
    baselineShift: str
    baselineSource: str
    blockSize: str
    border: str
    borderBlock: str
    borderBlockColor: str
    borderBlockEnd: str
    borderBlockEndColor: str
    borderBlockEndStyle: str
    borderBlockEndWidth: str
    borderBlockStart: str
    borderBlockStartColor: str
    borderBlockStartStyle: str
    borderBlockStartWidth: str
    borderBlockStyle: str
    borderBlockWidth: str
    borderBottom: str
    borderBottomColor: str
    borderBottomLeftRadius: str
    borderBottomRightRadius: str
    borderBottomStyle: str
    borderBottomWidth: str
    borderCollapse: str
    borderColor: str
    borderEndEndRadius: str
    borderEndStartRadius: str
    borderImage: str
    borderImageOutset: str
    borderImageRepeat: str
    borderImageSlice: str
    borderImageSource: str
    borderImageWidth: str
    borderInline: str
    borderInlineColor: str
    borderInlineEnd: str
    borderInlineEndColor: str
    borderInlineEndStyle: str
    borderInlineEndWidth: str
    borderInlineStart: str
    borderInlineStartColor: str
    borderInlineStartStyle: str
    borderInlineStartWidth: str
    borderInlineStyle: str
    borderInlineWidth: str
    borderLeft: str
    borderLeftColor: str
    borderLeftStyle: str
    borderLeftWidth: str
    borderRadius: str
    borderRight: str
    borderRightColor: str
    borderRightStyle: str
    borderRightWidth: str
    borderSpacing: str
    borderStartEndRadius: str
    borderStartStartRadius: str
    borderStyle: str
    borderTop: str
    borderTopColor: str
    borderTopLeftRadius: str
    borderTopRightRadius: str
    borderTopStyle: str
    borderTopWidth: str
    borderWidth: str
    bottom: str
    boxShadow: str
    boxSizing: str
    breakAfter: str
    breakBefore: str
    breakInside: str
    bufferedRendering: str
    captionSide: str
    caretColor: str
    clear: str
    clip: str
    clipPath: str
    clipRule: str
    color: str
    colorInterpolation: str
    colorInterpolationFilters: str
    colorRendering: str
    colorScheme: str
    columnCount: str
    columnFill: str
    columnGap: str
    columnRule: str
    columnRuleColor: str
    columnRuleStyle: str
    columnRuleWidth: str
    columnSpan: str
    columnWidth: str
    columns: str
    contain: str
    containIntrinsicBlockSize: str
    containIntrinsicHeight: str
    containIntrinsicInlineSize: str
    containIntrinsicSize: str
    containIntrinsicWidth: str
    container: str
    containerName: str
    containerType: str
    content: str
    contentVisibility: str
    counterIncrement: str
    counterReset: str
    counterSet: str
    cursor: str
    cx: str
    cy: str
    descentOverride: str
    direction: str
    display: str
    dominantBaseline: str
    emptyCells: str
    fallback: str
    fill: str
    fillOpacity: str
    fillRule: str
    filter: str
    flex: str
    flexBasis: str
    flexDirection: str
    flexFlow: str
    flexGrow: str
    flexShrink: str
    flexWrap: str
    floodColor: str
    floodOpacity: str
    font: str
    fontDisplay: str
    fontFamily: str
    fontFeatureSettings: str
    fontKerning: str
    fontOpticalSizing: str
    fontPalette: str
    fontSize: str
    fontStretch: str
    fontStyle: str
    fontSynthesis: str
    fontSynthesisSmallCaps: str
    fontSynthesisStyle: str
    fontSynthesisWeight: str
    fontVariant: str
    fontVariantAlternates: str
    fontVariantCaps: str
    fontVariantEastAsian: str
    fontVariantLigatures: str
    fontVariantNumeric: str
    fontVariationSettings: str
    fontWeight: str
    forcedColorAdjust: str
    gap: str
    grid: str
    gridArea: str
    gridAutoColumns: str
    gridAutoFlow: str
    gridAutoRows: str
    gridColumn: str
    gridColumnEnd: str
    gridColumnGap: str
    gridColumnStart: str
    gridGap: str
    gridRow: str
    gridRowEnd: str
    gridRowGap: str
    gridRowStart: str
    gridTemplate: str
    gridTemplateAreas: str
    gridTemplateColumns: str
    gridTemplateRows: str
    height: str
    hyphenateCharacter: str
    hyphenateLimitChars: str
    hyphens: str
    imageOrientation: str
    imageRendering: str
    inherits: str
    initialLetter: str
    initialValue: str
    inlineSize: str
    inset: str
    insetBlock: str
    insetBlockEnd: str
    insetBlockStart: str
    insetInline: str
    insetInlineEnd: str
    insetInlineStart: str
    isolation: str
    justifyContent: str
    justifyItems: str
    justifySelf: str
    left: str
    letterSpacing: str
    lightingColor: str
    lineBreak: str
    lineGapOverride: str
    lineHeight: str
    listStyle: str
    listStyleImage: str
    listStylePosition: str
    listStyleType: str
    margin: str
    marginBlock: str
    marginBlockEnd: str
    marginBlockStart: str
    marginBottom: str
    marginInline: str
    marginInlineEnd: str
    marginInlineStart: str
    marginLeft: str
    marginRight: str
    marginTop: str
    marker: str
    markerEnd: str
    markerMid: str
    markerStart: str
    mask: str
    maskType: str
    mathDepth: str
    mathShift: str
    mathStyle: str
    maxBlockSize: str
    maxHeight: str
    maxInlineSize: str
    maxWidth: str
    minBlockSize: str
    minHeight: str
    minInlineSize: str
    minWidth: str
    mixBlendMode: str
    negative: str
    objectFit: str
    objectPosition: str
    objectViewBox: str
    offset: str
    offsetDistance: str
    offsetPath: str
    offsetRotate: str
    opacity: str
    order: str
    orphans: str
    outline: str
    outlineColor: str
    outlineOffset: str
    outlineStyle: str
    outlineWidth: str
    overflow: str
    overflowAnchor: str
    overflowClipMargin: str
    overflowWrap: str
    overflowX: str
    overflowY: str
    overrideColors: str
    overscrollBehavior: str
    overscrollBehaviorBlock: str
    overscrollBehaviorInline: str
    overscrollBehaviorX: str
    overscrollBehaviorY: str
    pad: str
    padding: str
    paddingBlock: str
    paddingBlockEnd: str
    paddingBlockStart: str
    paddingBottom: str
    paddingInline: str
    paddingInlineEnd: str
    paddingInlineStart: str
    paddingLeft: str
    paddingRight: str
    paddingTop: str
    page: str
    pageBreakAfter: str
    pageBreakBefore: str
    pageBreakInside: str
    pageOrientation: str
    paintOrder: str
    perspective: str
    perspectiveOrigin: str
    placeContent: str
    placeItems: str
    placeSelf: str
    pointerEvents: str
    position: str
    prefix: str
    quotes: str
    range: str
    resize: str
    right: str
    rotate: str
    rowGap: str
    rubyPosition: str
    rx: str
    ry: str
    scale: str
    scrollBehavior: str
    scrollMargin: str
    scrollMarginBlock: str
    scrollMarginBlockEnd: str
    scrollMarginBlockStart: str
    scrollMarginBottom: str
    scrollMarginInline: str
    scrollMarginInlineEnd: str
    scrollMarginInlineStart: str
    scrollMarginLeft: str
    scrollMarginRight: str
    scrollMarginTop: str
    scrollPadding: str
    scrollPaddingBlock: str
    scrollPaddingBlockEnd: str
    scrollPaddingBlockStart: str
    scrollPaddingBottom: str
    scrollPaddingInline: str
    scrollPaddingInlineEnd: str
    scrollPaddingInlineStart: str
    scrollPaddingLeft: str
    scrollPaddingRight: str
    scrollPaddingTop: str
    scrollSnapAlign: str
    scrollSnapStop: str
    scrollSnapType: str
    scrollbarGutter: str
    shapeImageThreshold: str
    shapeMargin: str
    shapeOutside: str
    shapeRendering: str
    size: str
    sizeAdjust: str
    speak: str
    speakAs: str
    src: str
    stopColor: str
    stopOpacity: str
    stroke: str
    strokeDasharray: str
    strokeDashoffset: str
    strokeLinecap: str
    strokeLinejoin: str
    strokeMiterlimit: str
    strokeOpacity: str
    strokeWidth: str
    suffix: str
    symbols: str
    syntax: str
    system: str
    tabSize: str
    tableLayout: str
    textAlign: str
    textAlignLast: str
    textAnchor: str
    textCombineUpright: str
    textDecoration: str
    textDecorationColor: str
    textDecorationLine: str
    textDecorationSkipInk: str
    textDecorationStyle: str
    textDecorationThickness: str
    textEmphasis: str
    textEmphasisColor: str
    textEmphasisPosition: str
    textEmphasisStyle: str
    textIndent: str
    textOrientation: str
    textOverflow: str
    textRendering: str
    textShadow: str
    textSizeAdjust: str
    textTransform: str
    textUnderlineOffset: str
    textUnderlinePosition: str
    top: str
    touchAction: str
    transform: str
    transformBox: str
    transformOrigin: str
    transformStyle: str
    transition: str
    transitionDelay: str
    transitionDuration: str
    transitionProperty: str
    transitionTimingFunction: str
    translate: str
    unicodeBidi: str
    unicodeRange: str
    userSelect: str
    vectorEffect: str
    verticalAlign: str
    viewTransitionName: str
    visibility: str
    whiteSpace: str
    widows: str
    width: str
    willChange: str
    wordBreak: str
    wordSpacing: str
    wordWrap: str
    writingMode: str
    zIndex: str
    zoom: str

class CSSValue:
    CSS_INHERIT = 0
    CSS_PRIMITIVE_VALUE = 1
    CSS_VALUE_LIST = 2
    CSS_CUSTOM = 3
    cssText: str
    cssValueType: int

class CSSPrimitiveValue(CSSValue):
    CSS_UNKNOWN = 0
    CSS_NUMBER = 1
    CSS_PERCENTAGE = 2
    CSS_EMS = 3
    CSS_EXS = 4
    CSS_PX = 5
    CSS_CM = 6
    CSS_MM = 7
    CSS_IN = 8
    CSS_PT = 9
    CSS_PC = 10
    CSS_DEG = 11
    CSS_RAD = 12
    CSS_GRAD = 13
    CSS_MS = 14
    CSS_S = 15
    CSS_HZ = 16
    CSS_KHZ = 17
    CSS_DIMENSION = 18
    CSS_STRING = 19
    CSS_URI = 20
    CSS_IDENT = 21
    CSS_ATTR = 22
    CSS_COUNTER = 23
    CSS_RECT = 24
    CSS_RGBCOLOR = 25
    primitiveType: int

    def setFloatValue(self, unitType: int, floatValue: float) -> None: ...

    def getFloatValue(self, unitType: int) -> float: ...

    def setStringValue(self, stringType: int, stringValue: str) -> None: ...

    def getStringValue(self) -> str: ...

    def getCounterValue(self) -> Counter: ...

    def getRectValue(self) -> Rect: ...

    def getRGBColorValue(self) -> RGBColor: ...

class CSSValueList(CSSValue):
    length: int

    def item(self, index: int) -> CSSValue: ...

class RGBColor:
    red: CSSPrimitiveValue
    green: CSSPrimitiveValue
    blue: CSSPrimitiveValue

class Rect:
    top: CSSPrimitiveValue
    right: CSSPrimitiveValue
    bottom: CSSPrimitiveValue
    left: CSSPrimitiveValue

class Counter:
    identifier: str
    listStyle: str
    separator: str

class DOMImplementationCSS(DOMImplementation):

    def createCSSStyleSheet(self, title: str, media: str) -> CSSStyleSheet: ...

class ElementCSSInlineStyle:
    style: CSSStyleDeclaration
    attributeStyleMap: StylePropertyMap

class CSS2Properties:
    azimuth: str
    background: str
    backgroundAttachment: str
    backgroundColor: str
    backgroundImage: str
    backgroundPosition: str
    backgroundRepeat: str
    border: str
    borderCollapse: str
    borderColor: str
    borderSpacing: str
    borderStyle: str
    borderTop: str
    borderRight: str
    borderBottom: str
    borderLeft: str
    borderTopColor: str
    borderRightColor: str
    borderBottomColor: str
    borderLeftColor: str
    borderTopStyle: str
    borderRightStyle: str
    borderBottomStyle: str
    borderLeftStyle: str
    borderTopWidth: str
    borderRightWidth: str
    borderBottomWidth: str
    borderLeftWidth: str
    borderWidth: str
    bottom: str
    captionSide: str
    clear: str
    clip: str
    color: str
    content: str
    counterIncrement: str
    counterReset: str
    cue: str
    cueAfter: str
    cueBefore: str
    cursor: str
    direction: str
    display: str
    elevation: str
    emptyCells: str
    cssFloat: str
    font: str
    fontFamily: str
    fontSize: str
    fontSizeAdjust: str
    fontStretch: str
    fontStyle: str
    fontVariant: str
    fontWeight: str
    height: str
    left: str
    letterSpacing: str
    lineHeight: str
    listStyle: str
    listStyleImage: str
    listStylePosition: str
    listStyleType: str
    margin: str
    marginTop: str
    marginRight: str
    marginBottom: str
    marginLeft: str
    markerOffset: str
    marks: str
    maxHeight: str
    maxWidth: str
    minHeight: str
    minWidth: str
    orphans: str
    outline: str
    outlineColor: str
    outlineStyle: str
    outlineWidth: str
    overflow: str
    padding: str
    paddingTop: str
    paddingRight: str
    paddingBottom: str
    paddingLeft: str
    page: str
    pageBreakAfter: str
    pageBreakBefore: str
    pageBreakInside: str
    pause: str
    pauseAfter: str
    pauseBefore: str
    pitch: str
    pitchRange: str
    playDuring: str
    position: str
    quotes: str
    richness: str
    right: str
    size: str
    speak: str
    speakHeader: str
    speakNumeral: str
    speakPunctuation: str
    speechRate: str
    stress: str
    tableLayout: str
    textAlign: str
    textDecoration: str
    textIndent: str
    textShadow: str
    textTransform: str
    top: str
    unicodeBidi: str
    verticalAlign: str
    visibility: str
    voiceFamily: str
    volume: str
    whiteSpace: str
    widows: str
    width: str
    wordSpacing: str
    zIndex: str

class EXT_blend_minmax:
    MIN_EXT = 0x8007
    MAX_EXT = 0x8008

class EXT_color_buffer_float: ...

class EXT_color_buffer_half_float:
    RGBA16F_EXT = 0x881A
    RGB16F_EXT = 0x881B
    FRAMEBUFFER_ATTACHMENT_COMPONENT_TYPE_EXT = 0x8211
    UNSIGNED_NORMALIZED_EXT = 0x8C17

class WebGLTimerQueryEXT(WebGLObject): ...

class EXT_disjoint_timer_query:
    QUERY_COUNTER_BITS_EXT = 0x8864
    CURRENT_QUERY_EXT = 0x8865
    QUERY_RESULT_EXT = 0x8866
    QUERY_RESULT_AVAILABLE_EXT = 0x8867
    TIME_ELAPSED_EXT = 0x88BF
    TIMESTAMP_EXT = 0x8E28
    GPU_DISJOINT_EXT = 0x8FBB

    def createQueryEXT(self) -> Union['WebGLTimerQueryEXT', 'None']: ...

    def deleteQueryEXT(self, query: Union['WebGLTimerQueryEXT', 'None']) -> None: ...

    def isQueryEXT(self, query: Union['WebGLTimerQueryEXT', 'None']) -> bool: ...

    def beginQueryEXT(self, target: GLenum, query: WebGLTimerQueryEXT) -> None: ...

    def endQueryEXT(self, target: GLenum) -> None: ...

    def queryCounterEXT(self, query: WebGLTimerQueryEXT, target: GLenum) -> None: ...

    def getQueryEXT(self, target: GLenum, pname: GLenum) -> Any: ...

    def getQueryObjectEXT(self, query: WebGLTimerQueryEXT, pname: GLenum) -> Any: ...

class EXT_disjoint_timer_query_webgl2:
    QUERY_COUNTER_BITS_EXT = 0x8864
    TIME_ELAPSED_EXT = 0x88BF
    TIMESTAMP_EXT = 0x8E28
    GPU_DISJOINT_EXT = 0x8FBB

    def queryCounterEXT(self, query: WebGLQuery, target: GLenum) -> None: ...

class EXT_float_blend: ...

class EXT_frag_depth: ...

class EXT_sRGB:
    SRGB_EXT = 0x8C40
    SRGB_ALPHA_EXT = 0x8C42
    SRGB8_ALPHA8_EXT = 0x8C43
    FRAMEBUFFER_ATTACHMENT_COLOR_ENCODING_EXT = 0x8210

class EXT_shader_texture_lod: ...

class EXT_texture_compression_bptc:
    COMPRESSED_RGBA_BPTC_UNORM_EXT = 0x8E8C
    COMPRESSED_SRGB_ALPHA_BPTC_UNORM_EXT = 0x8E8D
    COMPRESSED_RGB_BPTC_SIGNED_FLOAT_EXT = 0x8E8E
    COMPRESSED_RGB_BPTC_UNSIGNED_FLOAT_EXT = 0x8E8F

class EXT_texture_compression_rgtc:
    COMPRESSED_RED_RGTC1_EXT = 0x8DBB
    COMPRESSED_SIGNED_RED_RGTC1_EXT = 0x8DBC
    COMPRESSED_RED_GREEN_RGTC2_EXT = 0x8DBD
    COMPRESSED_SIGNED_RED_GREEN_RGTC2_EXT = 0x8DBE

class EXT_texture_filter_anisotropic:
    TEXTURE_MAX_ANISOTROPY_EXT = 0x84FE
    MAX_TEXTURE_MAX_ANISOTROPY_EXT = 0x84FF

class EXT_texture_norm16:
    R16_EXT = 0x822A
    RG16_EXT = 0x822C
    RGB16_EXT = 0x8054
    RGBA16_EXT = 0x805B
    R16_SNORM_EXT = 0x8F98
    RG16_SNORM_EXT = 0x8F99
    RGB16_SNORM_EXT = 0x8F9A
    RGBA16_SNORM_EXT = 0x8F9B

class IdentityCredential(Credential):
    token: Union['str', 'None']

class CredentialRequestOptions(TypedDict):
    identity: NotRequired[IdentityCredentialRequestOptions]
    mediation: NotRequired[CredentialMediationRequirement]
    signal: NotRequired[AbortSignal]
    password: NotRequired[bool]
    federated: NotRequired[FederatedCredentialRequestOptions]
    otp: NotRequired[OTPCredentialRequestOptions]
    publicKey: NotRequired[PublicKeyCredentialRequestOptions]

class IdentityCredentialRequestOptions(TypedDict):
    providers: Sequence[IdentityProviderConfig]
    context: NotRequired[IdentityCredentialRequestOptionsContext]

class IdentityProviderConfig(TypedDict):
    configURL: str
    clientId: str
    nonce: NotRequired[str]
    loginHint: NotRequired[str]

class IdentityProviderWellKnown(TypedDict):
    provider_urls: Sequence[str]

class IdentityProviderIcon(TypedDict):
    url: str
    size: NotRequired[int]

class IdentityProviderBranding(TypedDict):
    background_color: NotRequired[str]
    color: NotRequired[str]
    icons: NotRequired[Sequence[IdentityProviderIcon]]
    name: NotRequired[str]

class IdentityProviderAPIConfig(TypedDict):
    accounts_endpoint: str
    client_metadata_endpoint: str
    id_assertion_endpoint: str
    branding: NotRequired[IdentityProviderBranding]

class IdentityProviderAccount(TypedDict):
    id: str
    name: str
    email: str
    given_name: NotRequired[str]
    picture: NotRequired[str]
    approved_clients: NotRequired[Sequence[str]]
    login_hints: NotRequired[Sequence[str]]

class IdentityProviderAccountList(TypedDict):
    accounts: NotRequired[Sequence[IdentityProviderAccount]]

class IdentityProviderToken(TypedDict):
    token: str

class IdentityProviderClientMetadata(TypedDict):
    privacy_policy_url: NotRequired[str]
    terms_of_service_url: NotRequired[str]

class IdentityUserInfo(TypedDict):
    email: NotRequired[str]
    name: NotRequired[str]
    givenName: NotRequired[str]
    picture: NotRequired[str]

class IdentityProvider: ...

class Blob:
    @classmethod
    def new(cls, blobParts: Union['Sequence[BlobPart]', 'None'] = None, options: Union['BlobPropertyBag', 'None'] = {}) -> Blob: ...
    size: int
    type: str

    def slice(self, start: Union['int', 'None'] = None, end: Union['int', 'None'] = None, contentType: Union['str', 'None'] = None) -> Blob: ...

    def stream(self) -> ReadableStream: ...

    def text(self) -> Awaitable[str]: ...

    def arrayBuffer(self) -> Awaitable[ArrayBuffer]: ...

class BlobPropertyBag(TypedDict):
    type: NotRequired[str]
    endings: NotRequired[EndingType]

class File(Blob):
    @classmethod
    def new(cls, fileBits: Sequence[BlobPart], fileName: str, options: Union['FilePropertyBag', 'None'] = {}) -> File: ...
    name: str
    lastModified: int
    webkitRelativePath: str

class FilePropertyBag(BlobPropertyBag):
    lastModified: NotRequired[int]

class FileList:

    def item(self, index: int) -> Union['File', 'None']: ...
    length: int

class FileReader(EventTarget):
    @classmethod
    def new(cls) -> FileReader: ...

    def readAsArrayBuffer(self, blob: Blob) -> None: ...

    def readAsBinaryString(self, blob: Blob) -> None: ...

    def readAsText(self, blob: Blob, encoding: Union['str', 'None'] = None) -> None: ...

    def readAsDataURL(self, blob: Blob) -> None: ...

    def abort(self) -> None: ...
    EMPTY = 0
    LOADING = 1
    DONE = 2
    readyState: int
    result: Union['str', 'ArrayBuffer', 'None']
    error: Union['DOMException', 'None']
    onloadstart: EventHandler
    onprogress: EventHandler
    onload: EventHandler
    onabort: EventHandler
    onerror: EventHandler
    onloadend: EventHandler

class FileReaderSync:
    @classmethod
    def new(cls) -> FileReaderSync: ...

    def readAsArrayBuffer(self, blob: Blob) -> ArrayBuffer: ...

    def readAsBinaryString(self, blob: Blob) -> str: ...

    def readAsText(self, blob: Blob, encoding: Union['str', 'None'] = None) -> str: ...

    def readAsDataURL(self, blob: Blob) -> str: ...

class URL:
    @classmethod
    def new(cls, url: str, base: Union['str', 'None'] = None) -> URL: ...
    href: str
    origin: str
    protocol: str
    username: str
    password: str
    host: str
    hostname: str
    port: str
    pathname: str
    search: str
    searchParams: URLSearchParams
    hash: str

    def toJSON(self) -> str: ...

class IDBRequest(EventTarget):
    result: Any
    error: Union['DOMException', 'None']
    source: Union['IDBObjectStore', 'IDBIndex', 'IDBCursor', 'None']
    transaction: Union['IDBTransaction', 'None']
    readyState: IDBRequestReadyState
    onsuccess: EventHandler
    onerror: EventHandler

class IDBOpenDBRequest(IDBRequest):
    onblocked: EventHandler
    onupgradeneeded: EventHandler

class IDBVersionChangeEvent(Event):
    @classmethod
    def new(cls, type: str, eventInitDict: Union['IDBVersionChangeEventInit', 'None'] = {}) -> IDBVersionChangeEvent: ...
    oldVersion: int
    newVersion: Union['int', 'None']

class IDBVersionChangeEventInit(EventInit):
    oldVersion: NotRequired[int]
    newVersion: NotRequired[Union['int', 'None']]

class WindowOrWorkerGlobalScope:
    indexedDB: IDBFactory
    crypto: Crypto

    def fetch(self, input: RequestInfo, init: Union['RequestInit', 'None'] = {}) -> Awaitable[Response]: ...
    performance: Performance
    origin: str
    isSecureContext: bool
    crossOriginIsolated: bool

    def reportError(self, e: Any) -> None: ...

    def btoa(self, data: str) -> str: ...

    def atob(self, data: str) -> ByteString: ...

    def setTimeout(self, handler: TimerHandler, timeout: Union['int', 'None'] = 0, *arguments: Any) -> int: ...

    def clearTimeout(self, id: Union['int', 'None'] = 0) -> None: ...

    def setInterval(self, handler: TimerHandler, timeout: Union['int', 'None'] = 0, *arguments: Any) -> int: ...

    def clearInterval(self, id: Union['int', 'None'] = 0) -> None: ...

    def queueMicrotask(self, callback: VoidFunction) -> None: ...
    @overload
    def createImageBitmap(self, image: ImageBitmapSource, options: Union['ImageBitmapOptions', 'None'] = {}) -> Awaitable[ImageBitmap]: ...
    @overload
    def createImageBitmap(self, image: ImageBitmapSource, sx: int, sy: int, sw: int, sh: int, options: Union['ImageBitmapOptions', 'None'] = {}) -> Awaitable[ImageBitmap]: ...

    def structuredClone(self, value: Any, options: Union['StructuredSerializeOptions', 'None'] = {}) -> Any: ...
    scheduler: Scheduler
    caches: CacheStorage
    trustedTypes: TrustedTypePolicyFactory

class IDBFactory:

    def open(self, name: str, version: Union['int', 'None'] = None) -> IDBOpenDBRequest: ...

    def deleteDatabase(self, name: str) -> IDBOpenDBRequest: ...

    def databases(self) -> Awaitable[Sequence[IDBDatabaseInfo]]: ...

    def cmp(self, first: Any, second: Any) -> int: ...

class IDBDatabaseInfo(TypedDict):
    name: NotRequired[str]
    version: NotRequired[int]

class IDBDatabase(EventTarget):
    name: str
    version: int
    objectStoreNames: DOMStringList

    def transaction(self, storeNames: Union['str', 'Sequence[str]'], mode: Union['IDBTransactionMode', 'None'] = "readonly", options: Union['IDBTransactionOptions', 'None'] = {}) -> IDBTransaction: ...

    def close(self) -> None: ...

    def createObjectStore(self, name: str, options: Union['IDBObjectStoreParameters', 'None'] = {}) -> IDBObjectStore: ...

    def deleteObjectStore(self, name: str) -> None: ...
    onabort: EventHandler
    onclose: EventHandler
    onerror: EventHandler
    onversionchange: EventHandler

class IDBTransactionOptions(TypedDict):
    durability: NotRequired[IDBTransactionDurability]

class IDBObjectStoreParameters(TypedDict):
    keyPath: NotRequired[Union['str', 'Sequence[str]', 'None']]
    autoIncrement: NotRequired[bool]

class IDBObjectStore:
    name: str
    keyPath: Any
    indexNames: DOMStringList
    transaction: IDBTransaction
    autoIncrement: bool

    def put(self, value: Any, key: Union['Any', 'None'] = None) -> IDBRequest: ...

    def add(self, value: Any, key: Union['Any', 'None'] = None) -> IDBRequest: ...

    def delete(self, query: Any) -> IDBRequest: ...

    def clear(self) -> IDBRequest: ...

    def get(self, query: Any) -> IDBRequest: ...

    def getKey(self, query: Any) -> IDBRequest: ...

    def getAll(self, query: Union['Any', 'None'] = None, count: Union['int', 'None'] = None) -> IDBRequest: ...

    def getAllKeys(self, query: Union['Any', 'None'] = None, count: Union['int', 'None'] = None) -> IDBRequest: ...

    def count(self, query: Union['Any', 'None'] = None) -> IDBRequest: ...

    def openCursor(self, query: Union['Any', 'None'] = None, direction: Union['IDBCursorDirection', 'None'] = "next") -> IDBRequest: ...

    def openKeyCursor(self, query: Union['Any', 'None'] = None, direction: Union['IDBCursorDirection', 'None'] = "next") -> IDBRequest: ...

    def index(self, name: str) -> IDBIndex: ...

    def createIndex(self, name: str, keyPath: Union['str', 'Sequence[str]'], options: Union['IDBIndexParameters', 'None'] = {}) -> IDBIndex: ...

    def deleteIndex(self, name: str) -> None: ...

class IDBIndexParameters(TypedDict):
    unique: NotRequired[bool]
    multiEntry: NotRequired[bool]

class IDBIndex:
    name: str
    objectStore: IDBObjectStore
    keyPath: Any
    multiEntry: bool
    unique: bool

    def get(self, query: Any) -> IDBRequest: ...

    def getKey(self, query: Any) -> IDBRequest: ...

    def getAll(self, query: Union['Any', 'None'] = None, count: Union['int', 'None'] = None) -> IDBRequest: ...

    def getAllKeys(self, query: Union['Any', 'None'] = None, count: Union['int', 'None'] = None) -> IDBRequest: ...

    def count(self, query: Union['Any', 'None'] = None) -> IDBRequest: ...

    def openCursor(self, query: Union['Any', 'None'] = None, direction: Union['IDBCursorDirection', 'None'] = "next") -> IDBRequest: ...

    def openKeyCursor(self, query: Union['Any', 'None'] = None, direction: Union['IDBCursorDirection', 'None'] = "next") -> IDBRequest: ...

class IDBKeyRange:
    lower: Any
    upper: Any
    lowerOpen: bool
    upperOpen: bool

    def includes(self, key: Any) -> bool: ...

class IDBCursor:
    source: Union['IDBObjectStore', 'IDBIndex']
    direction: IDBCursorDirection
    key: Any
    primaryKey: Any
    request: IDBRequest

    def advance(self, count: int) -> None: ...

    def continue_(self, key: Union['Any', 'None'] = None) -> None: ...

    def continuePrimaryKey(self, key: Any, primaryKey: Any) -> None: ...

    def update(self, value: Any) -> IDBRequest: ...

    def delete(self) -> IDBRequest: ...

class IDBCursorWithValue(IDBCursor):
    value: Any

class IDBTransaction(EventTarget):
    objectStoreNames: DOMStringList
    mode: IDBTransactionMode
    durability: IDBTransactionDurability
    db: IDBDatabase
    error: Union['DOMException', 'None']

    def objectStore(self, name: str) -> IDBObjectStore: ...

    def commit(self) -> None: ...

    def abort(self) -> None: ...
    onabort: EventHandler
    oncomplete: EventHandler
    onerror: EventHandler

class KHR_parallel_shader_compile:
    COMPLETION_STATUS_KHR = 0x91B1

class OES_draw_buffers_indexed:

    def enableiOES(self, target: GLenum, index: GLuint) -> None: ...

    def disableiOES(self, target: GLenum, index: GLuint) -> None: ...

    def blendEquationiOES(self, buf: GLuint, mode: GLenum) -> None: ...

    def blendEquationSeparateiOES(self, buf: GLuint, modeRGB: GLenum, modeAlpha: GLenum) -> None: ...

    def blendFunciOES(self, buf: GLuint, src: GLenum, dst: GLenum) -> None: ...

    def blendFuncSeparateiOES(self, buf: GLuint, srcRGB: GLenum, dstRGB: GLenum, srcAlpha: GLenum, dstAlpha: GLenum) -> None: ...

    def colorMaskiOES(self, buf: GLuint, r: GLboolean, g: GLboolean, b: GLboolean, a: GLboolean) -> None: ...

class OES_element_index_uint: ...

class OES_fbo_render_mipmap: ...

class OES_standard_derivatives:
    FRAGMENT_SHADER_DERIVATIVE_HINT_OES = 0x8B8B

class OES_texture_float: ...

class OES_texture_float_linear: ...

class OES_texture_half_float:
    HALF_FLOAT_OES = 0x8D61

class OES_texture_half_float_linear: ...

class WebGLVertexArrayObjectOES(WebGLObject): ...

class OES_vertex_array_object:
    VERTEX_ARRAY_BINDING_OES = 0x85B5

    def createVertexArrayOES(self) -> Union['WebGLVertexArrayObjectOES', 'None']: ...

    def deleteVertexArrayOES(self, arrayObject: Union['WebGLVertexArrayObjectOES', 'None']) -> None: ...

    def isVertexArrayOES(self, arrayObject: Union['WebGLVertexArrayObjectOES', 'None']) -> GLboolean: ...

    def bindVertexArrayOES(self, arrayObject: Union['WebGLVertexArrayObjectOES', 'None']) -> None: ...

class OVR_multiview2:
    FRAMEBUFFER_ATTACHMENT_TEXTURE_NUM_VIEWS_OVR = 0x9630
    FRAMEBUFFER_ATTACHMENT_TEXTURE_BASE_VIEW_INDEX_OVR = 0x9632
    MAX_VIEWS_OVR = 0x9631
    FRAMEBUFFER_INCOMPLETE_VIEW_TARGETS_OVR = 0x9633

    def framebufferTextureMultiviewOVR(self, target: GLenum, attachment: GLenum, texture: Union['WebGLTexture', 'None'], level: GLint, baseViewIndex: GLint, numViews: GLsizei) -> None: ...

class SVGElement(Element, GlobalEventHandlers, SVGElementInstance, HTMLOrSVGElement, ElementCSSInlineStyle):
    className: SVGAnimatedString
    ownerSVGElement: Union['SVGSVGElement', 'None']
    viewportElement: Union['SVGElement', 'None']

class SVGBoundingBoxOptions(TypedDict):
    fill: NotRequired[bool]
    stroke: NotRequired[bool]
    markers: NotRequired[bool]
    clipped: NotRequired[bool]

class SVGGraphicsElement(SVGElement, SVGTests):
    transform: SVGAnimatedTransformList

    def getBBox(self, options: Union['SVGBoundingBoxOptions', 'None'] = {}) -> DOMRect: ...

    def getCTM(self) -> Union['DOMMatrix', 'None']: ...

    def getScreenCTM(self) -> Union['DOMMatrix', 'None']: ...

class SVGGeometryElement(SVGGraphicsElement):
    pathLength: SVGAnimatedNumber

    def isPointInFill(self, point: Union['DOMPointInit', 'None'] = {}) -> bool: ...

    def isPointInStroke(self, point: Union['DOMPointInit', 'None'] = {}) -> bool: ...

    def getTotalLength(self) -> float: ...

    def getPointAtLength(self, distance: float) -> DOMPoint: ...

class SVGNumber:
    value: float

class SVGLength:
    SVG_LENGTHTYPE_UNKNOWN = 0
    SVG_LENGTHTYPE_NUMBER = 1
    SVG_LENGTHTYPE_PERCENTAGE = 2
    SVG_LENGTHTYPE_EMS = 3
    SVG_LENGTHTYPE_EXS = 4
    SVG_LENGTHTYPE_PX = 5
    SVG_LENGTHTYPE_CM = 6
    SVG_LENGTHTYPE_MM = 7
    SVG_LENGTHTYPE_IN = 8
    SVG_LENGTHTYPE_PT = 9
    SVG_LENGTHTYPE_PC = 10
    unitType: int
    value: float
    valueInSpecifiedUnits: float
    valueAsString: str

    def newValueSpecifiedUnits(self, unitType: int, valueInSpecifiedUnits: float) -> None: ...

    def convertToSpecifiedUnits(self, unitType: int) -> None: ...

class SVGAngle:
    SVG_ANGLETYPE_UNKNOWN = 0
    SVG_ANGLETYPE_UNSPECIFIED = 1
    SVG_ANGLETYPE_DEG = 2
    SVG_ANGLETYPE_RAD = 3
    SVG_ANGLETYPE_GRAD = 4
    unitType: int
    value: float
    valueInSpecifiedUnits: float
    valueAsString: str

    def newValueSpecifiedUnits(self, unitType: int, valueInSpecifiedUnits: float) -> None: ...

    def convertToSpecifiedUnits(self, unitType: int) -> None: ...

class SVGNumberList:
    length: int
    numberOfItems: int

    def clear(self) -> None: ...

    def initialize(self, newItem: SVGNumber) -> SVGNumber: ...

    def getItem(self, index: int) -> SVGNumber: ...

    def insertItemBefore(self, newItem: SVGNumber, index: int) -> SVGNumber: ...

    def replaceItem(self, newItem: SVGNumber, index: int) -> SVGNumber: ...

    def removeItem(self, index: int) -> SVGNumber: ...

    def appendItem(self, newItem: SVGNumber) -> SVGNumber: ...

    def __setter__(self, index: int, newItem: SVGNumber) -> None: ...

class SVGLengthList:
    length: int
    numberOfItems: int

    def clear(self) -> None: ...

    def initialize(self, newItem: SVGLength) -> SVGLength: ...

    def getItem(self, index: int) -> SVGLength: ...

    def insertItemBefore(self, newItem: SVGLength, index: int) -> SVGLength: ...

    def replaceItem(self, newItem: SVGLength, index: int) -> SVGLength: ...

    def removeItem(self, index: int) -> SVGLength: ...

    def appendItem(self, newItem: SVGLength) -> SVGLength: ...

    def __setter__(self, index: int, newItem: SVGLength) -> None: ...

class SVGStringList:
    length: int
    numberOfItems: int

    def clear(self) -> None: ...

    def initialize(self, newItem: str) -> str: ...

    def getItem(self, index: int) -> str: ...

    def insertItemBefore(self, newItem: str, index: int) -> str: ...

    def replaceItem(self, newItem: str, index: int) -> str: ...

    def removeItem(self, index: int) -> str: ...

    def appendItem(self, newItem: str) -> str: ...

    def __setter__(self, index: int, newItem: str) -> None: ...

class SVGAnimatedBoolean:
    baseVal: bool
    animVal: bool

class SVGAnimatedEnumeration:
    baseVal: int
    animVal: int

class SVGAnimatedInteger:
    baseVal: int
    animVal: int

class SVGAnimatedNumber:
    baseVal: float
    animVal: float

class SVGAnimatedLength:
    baseVal: SVGLength
    animVal: SVGLength

class SVGAnimatedAngle:
    baseVal: SVGAngle
    animVal: SVGAngle

class SVGAnimatedString:
    baseVal: str
    animVal: str

class SVGAnimatedRect:
    baseVal: DOMRect
    animVal: DOMRectReadOnly

class SVGAnimatedNumberList:
    baseVal: SVGNumberList
    animVal: SVGNumberList

class SVGAnimatedLengthList:
    baseVal: SVGLengthList
    animVal: SVGLengthList

class SVGUnitTypes:
    SVG_UNIT_TYPE_UNKNOWN = 0
    SVG_UNIT_TYPE_USERSPACEONUSE = 1
    SVG_UNIT_TYPE_OBJECTBOUNDINGBOX = 2

class SVGTests:
    requiredExtensions: SVGStringList
    systemLanguage: SVGStringList

class SVGFitToViewBox:
    viewBox: SVGAnimatedRect
    preserveAspectRatio: SVGAnimatedPreserveAspectRatio

class SVGURIReference:
    href: SVGAnimatedString

class Document(Node, FontFaceSource, GeometryUtils, NonElementParentNode, DocumentOrShadowRoot, ParentNode, XPathEvaluatorBase, GlobalEventHandlers):
    @classmethod
    def new(cls) -> Document: ...
    rootElement: Union['SVGSVGElement', 'None']
    namedFlows: NamedFlowMap

    def startViewTransition(self, updateCallback: Union['UpdateCallback', 'None'] = None) -> ViewTransition: ...

    def elementFromPoint(self, x: float, y: float) -> Union['Element', 'None']: ...

    def elementsFromPoint(self, x: float, y: float) -> Sequence[Element]: ...

    def caretPositionFromPoint(self, x: float, y: float) -> Union['CaretPosition', 'None']: ...
    scrollingElement: Union['Element', 'None']
    implementation: DOMImplementation
    URL: str
    documentURI: str
    compatMode: str
    characterSet: str
    charset: str
    inputEncoding: str
    contentType: str
    doctype: Union['DocumentType', 'None']
    documentElement: Union['Element', 'None']

    def getElementsByTagName(self, qualifiedName: str) -> HTMLCollection: ...

    def getElementsByTagNameNS(self, namespace: Union['str', 'None'], localName: str) -> HTMLCollection: ...

    def getElementsByClassName(self, classNames: str) -> HTMLCollection: ...

    def createElement(self, localName: str, options: Union['str', 'ElementCreationOptions', 'None'] = {}) -> Element: ...

    def createElementNS(self, namespace: Union['str', 'None'], qualifiedName: str, options: Union['str', 'ElementCreationOptions', 'None'] = {}) -> Element: ...

    def createDocumentFragment(self) -> DocumentFragment: ...

    def createTextNode(self, data: str) -> Text: ...

    def createCDATASection(self, data: str) -> CDATASection: ...

    def createComment(self, data: str) -> Comment: ...

    def createProcessingInstruction(self, target: str, data: str) -> ProcessingInstruction: ...

    def importNode(self, node: Node, deep: Union['bool', 'None'] = False) -> Node: ...

    def adoptNode(self, node: Node) -> Node: ...

    def createAttribute(self, localName: str) -> Attr: ...

    def createAttributeNS(self, namespace: Union['str', 'None'], qualifiedName: str) -> Attr: ...

    def createEvent(self, interface: str) -> Event: ...

    def createRange(self) -> Range: ...

    def createNodeIterator(self, root: Node, whatToShow: Union['int', 'None'] = 0xFFFFFFFF, filter: Union['NodeFilter', 'None'] = None) -> NodeIterator: ...

    def createTreeWalker(self, root: Node, whatToShow: Union['int', 'None'] = 0xFFFFFFFF, filter: Union['NodeFilter', 'None'] = None) -> TreeWalker: ...

    def measureElement(self, element: Element) -> FontMetrics: ...

    def measureText(self, text: str, styleMap: StylePropertyMapReadOnly) -> FontMetrics: ...
    fullscreenEnabled: bool
    fullscreen: bool

    def exitFullscreen(self) -> Awaitable[None]: ...
    onfullscreenchange: EventHandler
    onfullscreenerror: EventHandler
    location: Union['Location', 'None']
    domain: str
    referrer: str
    cookie: str
    lastModified: str
    readyState: DocumentReadyState

    def __getter__(self, name: str) -> object: ...
    title: str
    dir: str
    body: Union['HTMLElement', 'None']
    head: Union['HTMLHeadElement', 'None']
    images: HTMLCollection
    embeds: HTMLCollection
    plugins: HTMLCollection
    links: HTMLCollection
    forms: HTMLCollection
    scripts: HTMLCollection

    def getElementsByName(self, elementName: str) -> NodeList: ...
    currentScript: Union['HTMLOrSVGScriptElement', 'None']
    @overload
    def open(self, unused1: Union['str', 'None'] = None, unused2: Union['str', 'None'] = None) -> Document: ...
    @overload
    def open(self, url: str, name: str, features: str) -> Union['WindowProxy', 'None']: ...

    def close(self) -> None: ...

    def write(self, *text: str) -> None: ...

    def writeln(self, *text: str) -> None: ...
    defaultView: Union['WindowProxy', 'None']

    def hasFocus(self) -> bool: ...
    designMode: str

    def execCommand(self, commandId: str, showUI: Union['bool', 'None'] = False, value: Union['str', 'None'] = "") -> bool: ...

    def queryCommandEnabled(self, commandId: str) -> bool: ...

    def queryCommandIndeterm(self, commandId: str) -> bool: ...

    def queryCommandState(self, commandId: str) -> bool: ...

    def queryCommandSupported(self, commandId: str) -> bool: ...

    def queryCommandValue(self, commandId: str) -> str: ...
    hidden: bool
    visibilityState: DocumentVisibilityState
    onreadystatechange: EventHandler
    onvisibilitychange: EventHandler
    fgColor: str
    linkColor: str
    vlinkColor: str
    alinkColor: str
    bgColor: str
    anchors: HTMLCollection
    applets: HTMLCollection

    def clear(self) -> None: ...

    def captureEvents(self) -> None: ...

    def releaseEvents(self) -> None: ...
    all: HTMLAllCollection
    onfreeze: EventHandler
    onresume: EventHandler
    wasDiscarded: bool
    permissionsPolicy: PermissionsPolicy
    pictureInPictureEnabled: bool

    def exitPictureInPicture(self) -> Awaitable[None]: ...
    onpointerlockchange: EventHandler
    onpointerlockerror: EventHandler

    def exitPointerLock(self) -> None: ...
    prerendering: bool
    onprerenderingchange: EventHandler

    def requestStorageAccessFor(self, requestedOrigin: str) -> Awaitable[None]: ...
    fragmentDirective: FragmentDirective

    def getSelection(self) -> Union['Selection', 'None']: ...

    def hasStorageAccess(self) -> Awaitable[bool]: ...

    def requestStorageAccess(self) -> Awaitable[None]: ...

    def browsingTopics(self, options: Union['BrowsingTopicsOptions', 'None'] = {}) -> Awaitable[Sequence[BrowsingTopic]]: ...

    def hasPrivateTokens(self, issuer: str) -> Awaitable[bool]: ...

    def hasRedemptionRecord(self, issuer: str) -> Awaitable[bool]: ...
    timeline: DocumentTimeline

class SVGSVGElement(SVGGraphicsElement, SVGFitToViewBox, WindowEventHandlers):
    x: SVGAnimatedLength
    y: SVGAnimatedLength
    width: SVGAnimatedLength
    height: SVGAnimatedLength
    currentScale: float
    currentTranslate: DOMPointReadOnly

    def getIntersectionList(self, rect: DOMRectReadOnly, referenceElement: Union['SVGElement', 'None']) -> NodeList: ...

    def getEnclosureList(self, rect: DOMRectReadOnly, referenceElement: Union['SVGElement', 'None']) -> NodeList: ...

    def checkIntersection(self, element: SVGElement, rect: DOMRectReadOnly) -> bool: ...

    def checkEnclosure(self, element: SVGElement, rect: DOMRectReadOnly) -> bool: ...

    def deselectAll(self) -> None: ...

    def createSVGNumber(self) -> SVGNumber: ...

    def createSVGLength(self) -> SVGLength: ...

    def createSVGAngle(self) -> SVGAngle: ...

    def createSVGPoint(self) -> DOMPoint: ...

    def createSVGMatrix(self) -> DOMMatrix: ...

    def createSVGRect(self) -> DOMRect: ...

    def createSVGTransform(self) -> SVGTransform: ...

    def createSVGTransformFromMatrix(self, matrix: Union['DOMMatrix2DInit', 'None'] = {}) -> SVGTransform: ...

    def getElementById(self, elementId: str) -> Element: ...

    def suspendRedraw(self, maxWaitMilliseconds: int) -> int: ...

    def unsuspendRedraw(self, suspendHandleID: int) -> None: ...

    def unsuspendRedrawAll(self) -> None: ...

    def forceRedraw(self) -> None: ...

    def pauseAnimations(self) -> None: ...

    def unpauseAnimations(self) -> None: ...

    def animationsPaused(self) -> bool: ...

    def getCurrentTime(self) -> float: ...

    def setCurrentTime(self, seconds: float) -> None: ...

class SVGGElement(SVGGraphicsElement): ...

class SVGDefsElement(SVGGraphicsElement): ...

class SVGDescElement(SVGElement): ...

class SVGMetadataElement(SVGElement): ...

class SVGTitleElement(SVGElement): ...

class SVGSymbolElement(SVGGraphicsElement, SVGFitToViewBox): ...

class SVGUseElement(SVGGraphicsElement, SVGURIReference):
    x: SVGAnimatedLength
    y: SVGAnimatedLength
    width: SVGAnimatedLength
    height: SVGAnimatedLength
    instanceRoot: Union['SVGElement', 'None']
    animatedInstanceRoot: Union['SVGElement', 'None']

class SVGUseElementShadowRoot(ShadowRoot): ...

class SVGElementInstance:
    correspondingElement: Union['SVGElement', 'None']
    correspondingUseElement: Union['SVGUseElement', 'None']

class ShadowAnimation(Animation):
    @classmethod
    def new(cls, source: Animation, newTarget: Union['Element', 'CSSPseudoElement']) -> ShadowAnimation: ...
    sourceAnimation: Animation

class SVGSwitchElement(SVGGraphicsElement): ...

class GetSVGDocument:

    def getSVGDocument(self) -> Document: ...

class SVGStyleElement(SVGElement, LinkStyle):
    type: str
    media: str
    title: str

class SVGTransform:
    SVG_TRANSFORM_UNKNOWN = 0
    SVG_TRANSFORM_MATRIX = 1
    SVG_TRANSFORM_TRANSLATE = 2
    SVG_TRANSFORM_SCALE = 3
    SVG_TRANSFORM_ROTATE = 4
    SVG_TRANSFORM_SKEWX = 5
    SVG_TRANSFORM_SKEWY = 6
    type: int
    matrix: DOMMatrix
    angle: float

    def setMatrix(self, matrix: Union['DOMMatrix2DInit', 'None'] = {}) -> None: ...

    def setTranslate(self, tx: float, ty: float) -> None: ...

    def setScale(self, sx: float, sy: float) -> None: ...

    def setRotate(self, angle: float, cx: float, cy: float) -> None: ...

    def setSkewX(self, angle: float) -> None: ...

    def setSkewY(self, angle: float) -> None: ...

class SVGTransformList:
    length: int
    numberOfItems: int

    def clear(self) -> None: ...

    def initialize(self, newItem: SVGTransform) -> SVGTransform: ...

    def getItem(self, index: int) -> SVGTransform: ...

    def insertItemBefore(self, newItem: SVGTransform, index: int) -> SVGTransform: ...

    def replaceItem(self, newItem: SVGTransform, index: int) -> SVGTransform: ...

    def removeItem(self, index: int) -> SVGTransform: ...

    def appendItem(self, newItem: SVGTransform) -> SVGTransform: ...

    def __setter__(self, index: int, newItem: SVGTransform) -> None: ...

    def createSVGTransformFromMatrix(self, matrix: Union['DOMMatrix2DInit', 'None'] = {}) -> SVGTransform: ...

    def consolidate(self) -> Union['SVGTransform', 'None']: ...

class SVGAnimatedTransformList:
    baseVal: SVGTransformList
    animVal: SVGTransformList

class SVGPreserveAspectRatio:
    SVG_PRESERVEASPECTRATIO_UNKNOWN = 0
    SVG_PRESERVEASPECTRATIO_NONE = 1
    SVG_PRESERVEASPECTRATIO_XMINYMIN = 2
    SVG_PRESERVEASPECTRATIO_XMIDYMIN = 3
    SVG_PRESERVEASPECTRATIO_XMAXYMIN = 4
    SVG_PRESERVEASPECTRATIO_XMINYMID = 5
    SVG_PRESERVEASPECTRATIO_XMIDYMID = 6
    SVG_PRESERVEASPECTRATIO_XMAXYMID = 7
    SVG_PRESERVEASPECTRATIO_XMINYMAX = 8
    SVG_PRESERVEASPECTRATIO_XMIDYMAX = 9
    SVG_PRESERVEASPECTRATIO_XMAXYMAX = 10
    SVG_MEETORSLICE_UNKNOWN = 0
    SVG_MEETORSLICE_MEET = 1
    SVG_MEETORSLICE_SLICE = 2
    align: int
    meetOrSlice: int

class SVGAnimatedPreserveAspectRatio:
    baseVal: SVGPreserveAspectRatio
    animVal: SVGPreserveAspectRatio

class SVGPathElement(SVGGeometryElement): ...

class SVGRectElement(SVGGeometryElement):
    x: SVGAnimatedLength
    y: SVGAnimatedLength
    width: SVGAnimatedLength
    height: SVGAnimatedLength
    rx: SVGAnimatedLength
    ry: SVGAnimatedLength

class SVGCircleElement(SVGGeometryElement):
    cx: SVGAnimatedLength
    cy: SVGAnimatedLength
    r: SVGAnimatedLength

class SVGEllipseElement(SVGGeometryElement):
    cx: SVGAnimatedLength
    cy: SVGAnimatedLength
    rx: SVGAnimatedLength
    ry: SVGAnimatedLength

class SVGLineElement(SVGGeometryElement):
    x1: SVGAnimatedLength
    y1: SVGAnimatedLength
    x2: SVGAnimatedLength
    y2: SVGAnimatedLength

class SVGAnimatedPoints:
    points: SVGPointList
    animatedPoints: SVGPointList

class SVGPointList:
    length: int
    numberOfItems: int

    def clear(self) -> None: ...

    def initialize(self, newItem: DOMPoint) -> DOMPoint: ...

    def getItem(self, index: int) -> DOMPoint: ...

    def insertItemBefore(self, newItem: DOMPoint, index: int) -> DOMPoint: ...

    def replaceItem(self, newItem: DOMPoint, index: int) -> DOMPoint: ...

    def removeItem(self, index: int) -> DOMPoint: ...

    def appendItem(self, newItem: DOMPoint) -> DOMPoint: ...

    def __setter__(self, index: int, newItem: DOMPoint) -> None: ...

class SVGPolylineElement(SVGGeometryElement, SVGAnimatedPoints): ...

class SVGPolygonElement(SVGGeometryElement, SVGAnimatedPoints): ...

class SVGTextContentElement(SVGGraphicsElement):
    LENGTHADJUST_UNKNOWN = 0
    LENGTHADJUST_SPACING = 1
    LENGTHADJUST_SPACINGANDGLYPHS = 2
    textLength: SVGAnimatedLength
    lengthAdjust: SVGAnimatedEnumeration

    def getNumberOfChars(self) -> int: ...

    def getComputedTextLength(self) -> float: ...

    def getSubStringLength(self, charnum: int, nchars: int) -> float: ...

    def getStartPositionOfChar(self, charnum: int) -> DOMPoint: ...

    def getEndPositionOfChar(self, charnum: int) -> DOMPoint: ...

    def getExtentOfChar(self, charnum: int) -> DOMRect: ...

    def getRotationOfChar(self, charnum: int) -> float: ...

    def getCharNumAtPosition(self, point: Union['DOMPointInit', 'None'] = {}) -> int: ...

    def selectSubString(self, charnum: int, nchars: int) -> None: ...

class SVGTextPositioningElement(SVGTextContentElement):
    x: SVGAnimatedLengthList
    y: SVGAnimatedLengthList
    dx: SVGAnimatedLengthList
    dy: SVGAnimatedLengthList
    rotate: SVGAnimatedNumberList

class SVGTextElement(SVGTextPositioningElement): ...

class SVGTSpanElement(SVGTextPositioningElement): ...

class SVGTextPathElement(SVGTextContentElement, SVGURIReference):
    TEXTPATH_METHODTYPE_UNKNOWN = 0
    TEXTPATH_METHODTYPE_ALIGN = 1
    TEXTPATH_METHODTYPE_STRETCH = 2
    TEXTPATH_SPACINGTYPE_UNKNOWN = 0
    TEXTPATH_SPACINGTYPE_AUTO = 1
    TEXTPATH_SPACINGTYPE_EXACT = 2
    startOffset: SVGAnimatedLength
    method: SVGAnimatedEnumeration
    spacing: SVGAnimatedEnumeration

class SVGImageElement(SVGGraphicsElement, SVGURIReference):
    x: SVGAnimatedLength
    y: SVGAnimatedLength
    width: SVGAnimatedLength
    height: SVGAnimatedLength
    preserveAspectRatio: SVGAnimatedPreserveAspectRatio
    crossOrigin: Union['str', 'None']

class SVGForeignObjectElement(SVGGraphicsElement):
    x: SVGAnimatedLength
    y: SVGAnimatedLength
    width: SVGAnimatedLength
    height: SVGAnimatedLength

class SVGMarkerElement(SVGElement, SVGFitToViewBox):
    SVG_MARKERUNITS_UNKNOWN = 0
    SVG_MARKERUNITS_USERSPACEONUSE = 1
    SVG_MARKERUNITS_STROKEWIDTH = 2
    SVG_MARKER_ORIENT_UNKNOWN = 0
    SVG_MARKER_ORIENT_AUTO = 1
    SVG_MARKER_ORIENT_ANGLE = 2
    refX: SVGAnimatedLength
    refY: SVGAnimatedLength
    markerUnits: SVGAnimatedEnumeration
    markerWidth: SVGAnimatedLength
    markerHeight: SVGAnimatedLength
    orientType: SVGAnimatedEnumeration
    orientAngle: SVGAnimatedAngle
    orient: str

    def setOrientToAuto(self) -> None: ...

    def setOrientToAngle(self, angle: SVGAngle) -> None: ...

class SVGGradientElement(SVGElement, SVGURIReference):
    SVG_SPREADMETHOD_UNKNOWN = 0
    SVG_SPREADMETHOD_PAD = 1
    SVG_SPREADMETHOD_REFLECT = 2
    SVG_SPREADMETHOD_REPEAT = 3
    gradientUnits: SVGAnimatedEnumeration
    gradientTransform: SVGAnimatedTransformList
    spreadMethod: SVGAnimatedEnumeration

class SVGLinearGradientElement(SVGGradientElement):
    x1: SVGAnimatedLength
    y1: SVGAnimatedLength
    x2: SVGAnimatedLength
    y2: SVGAnimatedLength

class SVGRadialGradientElement(SVGGradientElement):
    cx: SVGAnimatedLength
    cy: SVGAnimatedLength
    r: SVGAnimatedLength
    fx: SVGAnimatedLength
    fy: SVGAnimatedLength
    fr: SVGAnimatedLength

class SVGStopElement(SVGElement):
    offset: SVGAnimatedNumber

class SVGPatternElement(SVGElement, SVGFitToViewBox, SVGURIReference):
    patternUnits: SVGAnimatedEnumeration
    patternContentUnits: SVGAnimatedEnumeration
    patternTransform: SVGAnimatedTransformList
    x: SVGAnimatedLength
    y: SVGAnimatedLength
    width: SVGAnimatedLength
    height: SVGAnimatedLength

class SVGScriptElement(SVGElement, SVGURIReference):
    type: str
    crossOrigin: Union['str', 'None']

class SVGAElement(SVGGraphicsElement, SVGURIReference):
    target: SVGAnimatedString
    download: str
    ping: str
    rel: str
    relList: DOMTokenList
    hreflang: str
    type: str
    text: str
    referrerPolicy: str
    origin: str
    protocol: str
    username: str
    password: str
    host: str
    hostname: str
    port: str
    pathname: str
    search: str
    hash: str

class SVGViewElement(SVGElement, SVGFitToViewBox): ...

class WEBGL_blend_equation_advanced_coherent:
    MULTIPLY = 0x9294
    SCREEN = 0x9295
    OVERLAY = 0x9296
    DARKEN = 0x9297
    LIGHTEN = 0x9298
    COLORDODGE = 0x9299
    COLORBURN = 0x929A
    HARDLIGHT = 0x929B
    SOFTLIGHT = 0x929C
    DIFFERENCE = 0x929E
    EXCLUSION = 0x92A0
    HSL_HUE = 0x92AD
    HSL_SATURATION = 0x92AE
    HSL_COLOR = 0x92AF
    HSL_LUMINOSITY = 0x92B0

class WEBGL_clip_cull_distance:
    MAX_CLIP_DISTANCES_WEBGL = 0x0D32
    MAX_CULL_DISTANCES_WEBGL = 0x82F9
    MAX_COMBINED_CLIP_AND_CULL_DISTANCES_WEBGL = 0x82FA
    CLIP_DISTANCE0_WEBGL = 0x3000
    CLIP_DISTANCE1_WEBGL = 0x3001
    CLIP_DISTANCE2_WEBGL = 0x3002
    CLIP_DISTANCE3_WEBGL = 0x3003
    CLIP_DISTANCE4_WEBGL = 0x3004
    CLIP_DISTANCE5_WEBGL = 0x3005
    CLIP_DISTANCE6_WEBGL = 0x3006
    CLIP_DISTANCE7_WEBGL = 0x3007

class WEBGL_color_buffer_float:
    RGBA32F_EXT = 0x8814
    FRAMEBUFFER_ATTACHMENT_COMPONENT_TYPE_EXT = 0x8211
    UNSIGNED_NORMALIZED_EXT = 0x8C17

class WEBGL_compressed_texture_astc:
    COMPRESSED_RGBA_ASTC_4x4_KHR = 0x93B0
    COMPRESSED_RGBA_ASTC_5x4_KHR = 0x93B1
    COMPRESSED_RGBA_ASTC_5x5_KHR = 0x93B2
    COMPRESSED_RGBA_ASTC_6x5_KHR = 0x93B3
    COMPRESSED_RGBA_ASTC_6x6_KHR = 0x93B4
    COMPRESSED_RGBA_ASTC_8x5_KHR = 0x93B5
    COMPRESSED_RGBA_ASTC_8x6_KHR = 0x93B6
    COMPRESSED_RGBA_ASTC_8x8_KHR = 0x93B7
    COMPRESSED_RGBA_ASTC_10x5_KHR = 0x93B8
    COMPRESSED_RGBA_ASTC_10x6_KHR = 0x93B9
    COMPRESSED_RGBA_ASTC_10x8_KHR = 0x93BA
    COMPRESSED_RGBA_ASTC_10x10_KHR = 0x93BB
    COMPRESSED_RGBA_ASTC_12x10_KHR = 0x93BC
    COMPRESSED_RGBA_ASTC_12x12_KHR = 0x93BD
    COMPRESSED_SRGB8_ALPHA8_ASTC_4x4_KHR = 0x93D0
    COMPRESSED_SRGB8_ALPHA8_ASTC_5x4_KHR = 0x93D1
    COMPRESSED_SRGB8_ALPHA8_ASTC_5x5_KHR = 0x93D2
    COMPRESSED_SRGB8_ALPHA8_ASTC_6x5_KHR = 0x93D3
    COMPRESSED_SRGB8_ALPHA8_ASTC_6x6_KHR = 0x93D4
    COMPRESSED_SRGB8_ALPHA8_ASTC_8x5_KHR = 0x93D5
    COMPRESSED_SRGB8_ALPHA8_ASTC_8x6_KHR = 0x93D6
    COMPRESSED_SRGB8_ALPHA8_ASTC_8x8_KHR = 0x93D7
    COMPRESSED_SRGB8_ALPHA8_ASTC_10x5_KHR = 0x93D8
    COMPRESSED_SRGB8_ALPHA8_ASTC_10x6_KHR = 0x93D9
    COMPRESSED_SRGB8_ALPHA8_ASTC_10x8_KHR = 0x93DA
    COMPRESSED_SRGB8_ALPHA8_ASTC_10x10_KHR = 0x93DB
    COMPRESSED_SRGB8_ALPHA8_ASTC_12x10_KHR = 0x93DC
    COMPRESSED_SRGB8_ALPHA8_ASTC_12x12_KHR = 0x93DD

    def getSupportedProfiles(self) -> Sequence[str]: ...

class WEBGL_compressed_texture_etc:
    COMPRESSED_R11_EAC = 0x9270
    COMPRESSED_SIGNED_R11_EAC = 0x9271
    COMPRESSED_RG11_EAC = 0x9272
    COMPRESSED_SIGNED_RG11_EAC = 0x9273
    COMPRESSED_RGB8_ETC2 = 0x9274
    COMPRESSED_SRGB8_ETC2 = 0x9275
    COMPRESSED_RGB8_PUNCHTHROUGH_ALPHA1_ETC2 = 0x9276
    COMPRESSED_SRGB8_PUNCHTHROUGH_ALPHA1_ETC2 = 0x9277
    COMPRESSED_RGBA8_ETC2_EAC = 0x9278
    COMPRESSED_SRGB8_ALPHA8_ETC2_EAC = 0x9279

class WEBGL_compressed_texture_etc1:
    COMPRESSED_RGB_ETC1_WEBGL = 0x8D64

class WEBGL_compressed_texture_pvrtc:
    COMPRESSED_RGB_PVRTC_4BPPV1_IMG = 0x8C00
    COMPRESSED_RGB_PVRTC_2BPPV1_IMG = 0x8C01
    COMPRESSED_RGBA_PVRTC_4BPPV1_IMG = 0x8C02
    COMPRESSED_RGBA_PVRTC_2BPPV1_IMG = 0x8C03

class WEBGL_compressed_texture_s3tc:
    COMPRESSED_RGB_S3TC_DXT1_EXT = 0x83F0
    COMPRESSED_RGBA_S3TC_DXT1_EXT = 0x83F1
    COMPRESSED_RGBA_S3TC_DXT3_EXT = 0x83F2
    COMPRESSED_RGBA_S3TC_DXT5_EXT = 0x83F3

class WEBGL_compressed_texture_s3tc_srgb:
    COMPRESSED_SRGB_S3TC_DXT1_EXT = 0x8C4C
    COMPRESSED_SRGB_ALPHA_S3TC_DXT1_EXT = 0x8C4D
    COMPRESSED_SRGB_ALPHA_S3TC_DXT3_EXT = 0x8C4E
    COMPRESSED_SRGB_ALPHA_S3TC_DXT5_EXT = 0x8C4F

class WEBGL_debug_renderer_info:
    UNMASKED_VENDOR_WEBGL = 0x9245
    UNMASKED_RENDERER_WEBGL = 0x9246

class WEBGL_debug_shaders:

    def getTranslatedShaderSource(self, shader: WebGLShader) -> str: ...

class WEBGL_depth_texture:
    UNSIGNED_INT_24_8_WEBGL = 0x84FA

class WEBGL_draw_buffers:
    COLOR_ATTACHMENT0_WEBGL = 0x8CE0
    COLOR_ATTACHMENT1_WEBGL = 0x8CE1
    COLOR_ATTACHMENT2_WEBGL = 0x8CE2
    COLOR_ATTACHMENT3_WEBGL = 0x8CE3
    COLOR_ATTACHMENT4_WEBGL = 0x8CE4
    COLOR_ATTACHMENT5_WEBGL = 0x8CE5
    COLOR_ATTACHMENT6_WEBGL = 0x8CE6
    COLOR_ATTACHMENT7_WEBGL = 0x8CE7
    COLOR_ATTACHMENT8_WEBGL = 0x8CE8
    COLOR_ATTACHMENT9_WEBGL = 0x8CE9
    COLOR_ATTACHMENT10_WEBGL = 0x8CEA
    COLOR_ATTACHMENT11_WEBGL = 0x8CEB
    COLOR_ATTACHMENT12_WEBGL = 0x8CEC
    COLOR_ATTACHMENT13_WEBGL = 0x8CED
    COLOR_ATTACHMENT14_WEBGL = 0x8CEE
    COLOR_ATTACHMENT15_WEBGL = 0x8CEF
    DRAW_BUFFER0_WEBGL = 0x8825
    DRAW_BUFFER1_WEBGL = 0x8826
    DRAW_BUFFER2_WEBGL = 0x8827
    DRAW_BUFFER3_WEBGL = 0x8828
    DRAW_BUFFER4_WEBGL = 0x8829
    DRAW_BUFFER5_WEBGL = 0x882A
    DRAW_BUFFER6_WEBGL = 0x882B
    DRAW_BUFFER7_WEBGL = 0x882C
    DRAW_BUFFER8_WEBGL = 0x882D
    DRAW_BUFFER9_WEBGL = 0x882E
    DRAW_BUFFER10_WEBGL = 0x882F
    DRAW_BUFFER11_WEBGL = 0x8830
    DRAW_BUFFER12_WEBGL = 0x8831
    DRAW_BUFFER13_WEBGL = 0x8832
    DRAW_BUFFER14_WEBGL = 0x8833
    DRAW_BUFFER15_WEBGL = 0x8834
    MAX_COLOR_ATTACHMENTS_WEBGL = 0x8CDF
    MAX_DRAW_BUFFERS_WEBGL = 0x8824

    def drawBuffersWEBGL(self, buffers: Sequence[GLenum]) -> None: ...

class WEBGL_draw_instanced_base_vertex_base_instance:

    def drawArraysInstancedBaseInstanceWEBGL(self, mode: GLenum, first: GLint, count: GLsizei, instanceCount: GLsizei, baseInstance: GLuint) -> None: ...

    def drawElementsInstancedBaseVertexBaseInstanceWEBGL(self, mode: GLenum, count: GLsizei, type: GLenum, offset: GLintptr, instanceCount: GLsizei, baseVertex: GLint, baseInstance: GLuint) -> None: ...

class WEBGL_lose_context:

    def loseContext(self) -> None: ...

    def restoreContext(self) -> None: ...

class WEBGL_multi_draw:

    def multiDrawArraysWEBGL(self, mode: GLenum, firstsList: Union['Int32Array', 'Sequence[GLint]'], firstsOffset: GLuint, countsList: Union['Int32Array', 'Sequence[GLsizei]'], countsOffset: GLuint, drawcount: GLsizei) -> None: ...

    def multiDrawElementsWEBGL(self, mode: GLenum, countsList: Union['Int32Array', 'Sequence[GLsizei]'], countsOffset: GLuint, type: GLenum, offsetsList: Union['Int32Array', 'Sequence[GLsizei]'], offsetsOffset: GLuint, drawcount: GLsizei) -> None: ...

    def multiDrawArraysInstancedWEBGL(self, mode: GLenum, firstsList: Union['Int32Array', 'Sequence[GLint]'], firstsOffset: GLuint, countsList: Union['Int32Array', 'Sequence[GLsizei]'], countsOffset: GLuint, instanceCountsList: Union['Int32Array', 'Sequence[GLsizei]'], instanceCountsOffset: GLuint, drawcount: GLsizei) -> None: ...

    def multiDrawElementsInstancedWEBGL(self, mode: GLenum, countsList: Union['Int32Array', 'Sequence[GLsizei]'], countsOffset: GLuint, type: GLenum, offsetsList: Union['Int32Array', 'Sequence[GLsizei]'], offsetsOffset: GLuint, instanceCountsList: Union['Int32Array', 'Sequence[GLsizei]'], instanceCountsOffset: GLuint, drawcount: GLsizei) -> None: ...

class WEBGL_multi_draw_instanced_base_vertex_base_instance:

    def multiDrawArraysInstancedBaseInstanceWEBGL(self, mode: GLenum, firstsList: Union['Int32Array', 'Sequence[GLint]'], firstsOffset: GLuint, countsList: Union['Int32Array', 'Sequence[GLsizei]'], countsOffset: GLuint, instanceCountsList: Union['Int32Array', 'Sequence[GLsizei]'], instanceCountsOffset: GLuint, baseInstancesList: Union['Uint32Array', 'Sequence[GLuint]'], baseInstancesOffset: GLuint, drawcount: GLsizei) -> None: ...

    def multiDrawElementsInstancedBaseVertexBaseInstanceWEBGL(self, mode: GLenum, countsList: Union['Int32Array', 'Sequence[GLsizei]'], countsOffset: GLuint, type: GLenum, offsetsList: Union['Int32Array', 'Sequence[GLsizei]'], offsetsOffset: GLuint, instanceCountsList: Union['Int32Array', 'Sequence[GLsizei]'], instanceCountsOffset: GLuint, baseVerticesList: Union['Int32Array', 'Sequence[GLint]'], baseVerticesOffset: GLuint, baseInstancesList: Union['Uint32Array', 'Sequence[GLuint]'], baseInstancesOffset: GLuint, drawcount: GLsizei) -> None: ...

class WEBGL_provoking_vertex:
    FIRST_VERTEX_CONVENTION_WEBGL = 0x8E4D
    LAST_VERTEX_CONVENTION_WEBGL = 0x8E4E
    PROVOKING_VERTEX_WEBGL = 0x8E4F

    def provokingVertexWEBGL(self, provokeMode: GLenum) -> None: ...

class Crypto:
    subtle: SubtleCrypto

    def getRandomValues(self, array: ArrayBufferView) -> ArrayBufferView: ...

    def randomUUID(self) -> str: ...

class Algorithm(TypedDict):
    name: str

class KeyAlgorithm(TypedDict):
    name: str

class CryptoKey:
    type: KeyType
    extractable: bool
    algorithm: object
    usages: object

class SubtleCrypto:

    def encrypt(self, algorithm: AlgorithmIdentifier, key: CryptoKey, data: BufferSource) -> Awaitable[Any]: ...

    def decrypt(self, algorithm: AlgorithmIdentifier, key: CryptoKey, data: BufferSource) -> Awaitable[Any]: ...

    def sign(self, algorithm: AlgorithmIdentifier, key: CryptoKey, data: BufferSource) -> Awaitable[Any]: ...

    def verify(self, algorithm: AlgorithmIdentifier, key: CryptoKey, signature: BufferSource, data: BufferSource) -> Awaitable[Any]: ...

    def digest(self, algorithm: AlgorithmIdentifier, data: BufferSource) -> Awaitable[Any]: ...

    def generateKey(self, algorithm: AlgorithmIdentifier, extractable: bool, keyUsages: Sequence[KeyUsage]) -> Awaitable[Any]: ...

    def deriveKey(self, algorithm: AlgorithmIdentifier, baseKey: CryptoKey, derivedKeyType: AlgorithmIdentifier, extractable: bool, keyUsages: Sequence[KeyUsage]) -> Awaitable[Any]: ...

    def deriveBits(self, algorithm: AlgorithmIdentifier, baseKey: CryptoKey, length: int) -> Awaitable[ArrayBuffer]: ...

    def importKey(self, format: KeyFormat, keyData: Union['BufferSource', 'JsonWebKey'], algorithm: AlgorithmIdentifier, extractable: bool, keyUsages: Sequence[KeyUsage]) -> Awaitable[CryptoKey]: ...

    def exportKey(self, format: KeyFormat, key: CryptoKey) -> Awaitable[Any]: ...

    def wrapKey(self, format: KeyFormat, key: CryptoKey, wrappingKey: CryptoKey, wrapAlgorithm: AlgorithmIdentifier) -> Awaitable[Any]: ...

    def unwrapKey(self, format: KeyFormat, wrappedKey: BufferSource, unwrappingKey: CryptoKey, unwrapAlgorithm: AlgorithmIdentifier, unwrappedKeyAlgorithm: AlgorithmIdentifier, extractable: bool, keyUsages: Sequence[KeyUsage]) -> Awaitable[CryptoKey]: ...

class RsaOtherPrimesInfo(TypedDict):
    r: NotRequired[str]
    d: NotRequired[str]
    t: NotRequired[str]

class JsonWebKey(TypedDict):
    kty: NotRequired[str]
    use: NotRequired[str]
    key_ops: NotRequired[Sequence[str]]
    alg: NotRequired[str]
    ext: NotRequired[bool]
    crv: NotRequired[str]
    x: NotRequired[str]
    y: NotRequired[str]
    d: NotRequired[str]
    n: NotRequired[str]
    e: NotRequired[str]
    p: NotRequired[str]
    q: NotRequired[str]
    dp: NotRequired[str]
    dq: NotRequired[str]
    qi: NotRequired[str]
    oth: NotRequired[Sequence[RsaOtherPrimesInfo]]
    k: NotRequired[str]

class CryptoKeyPair(TypedDict):
    publicKey: NotRequired[CryptoKey]
    privateKey: NotRequired[CryptoKey]

class RsaKeyGenParams(Algorithm):
    modulusLength: int
    publicExponent: BigInteger

class RsaHashedKeyGenParams(RsaKeyGenParams):
    hash: HashAlgorithmIdentifier

class RsaKeyAlgorithm(KeyAlgorithm):
    modulusLength: int
    publicExponent: BigInteger

class RsaHashedKeyAlgorithm(RsaKeyAlgorithm):
    hash: KeyAlgorithm

class RsaHashedImportParams(Algorithm):
    hash: HashAlgorithmIdentifier

class RsaPssParams(Algorithm):
    saltLength: int

class RsaOaepParams(Algorithm):
    label: NotRequired[BufferSource]

class EcdsaParams(Algorithm):
    hash: HashAlgorithmIdentifier

class EcKeyGenParams(Algorithm):
    namedCurve: NamedCurve

class EcKeyAlgorithm(KeyAlgorithm):
    namedCurve: NamedCurve

class EcKeyImportParams(Algorithm):
    namedCurve: NamedCurve

class EcdhKeyDeriveParams(Algorithm):
    public: CryptoKey

class AesCtrParams(Algorithm):
    counter: BufferSource
    length: int

class AesKeyAlgorithm(KeyAlgorithm):
    length: int

class AesKeyGenParams(Algorithm):
    length: int

class AesDerivedKeyParams(Algorithm):
    length: int

class AesCbcParams(Algorithm):
    iv: BufferSource

class AesGcmParams(Algorithm):
    iv: BufferSource
    additionalData: NotRequired[BufferSource]
    tagLength: NotRequired[int]

class HmacImportParams(Algorithm):
    hash: HashAlgorithmIdentifier
    length: NotRequired[int]

class HmacKeyAlgorithm(KeyAlgorithm):
    hash: KeyAlgorithm
    length: int

class HmacKeyGenParams(Algorithm):
    hash: HashAlgorithmIdentifier
    length: NotRequired[int]

class HkdfParams(Algorithm):
    hash: HashAlgorithmIdentifier
    salt: BufferSource
    info: BufferSource

class Pbkdf2Params(Algorithm):
    salt: BufferSource
    iterations: int
    hash: HashAlgorithmIdentifier

class Accelerometer(Sensor):
    @classmethod
    def new(cls, options: Union['AccelerometerSensorOptions', 'None'] = {}) -> Accelerometer: ...
    x: Union['float', 'None']
    y: Union['float', 'None']
    z: Union['float', 'None']

class AccelerometerSensorOptions(SensorOptions):
    referenceFrame: NotRequired[AccelerometerLocalCoordinateSystem]

class LinearAccelerationSensor(Accelerometer):
    @classmethod
    def new(cls, options: Union['AccelerometerSensorOptions', 'None'] = {}) -> LinearAccelerationSensor: ...

class GravitySensor(Accelerometer):
    @classmethod
    def new(cls, options: Union['AccelerometerSensorOptions', 'None'] = {}) -> GravitySensor: ...

class AccelerometerReadingValues(TypedDict):
    x: Union['float', 'None']
    y: Union['float', 'None']
    z: Union['float', 'None']

class LinearAccelerationReadingValues(AccelerometerReadingValues): ...

class GravityReadingValues(AccelerometerReadingValues): ...

class AmbientLightSensor(Sensor):
    @classmethod
    def new(cls, sensorOptions: Union['SensorOptions', 'None'] = {}) -> AmbientLightSensor: ...
    illuminance: Union['float', 'None']

class AmbientLightReadingValues(TypedDict):
    illuminance: Union['float', 'None']

class XRAnchor:
    anchorSpace: XRSpace

    def requestPersistentHandle(self) -> Awaitable[str]: ...

    def delete(self) -> None: ...

class XRFrame:

    def createAnchor(self, pose: XRRigidTransform, space: XRSpace) -> Awaitable[XRAnchor]: ...
    trackedAnchors: XRAnchorSet
    detectedMeshes: XRMeshSet

    def getDepthInformation(self, view: XRView) -> Union['XRCPUDepthInformation', 'None']: ...

    def getJointPose(self, joint: XRJointSpace, baseSpace: XRSpace) -> Union['XRJointPose', 'None']: ...

    def fillJointRadii(self, jointSpaces: Sequence[XRJointSpace], radii: Float32Array) -> bool: ...

    def fillPoses(self, spaces: Sequence[XRSpace], baseSpace: XRSpace, transforms: Float32Array) -> bool: ...

    def getHitTestResults(self, hitTestSource: XRHitTestSource) -> Sequence[XRHitTestResult]: ...

    def getHitTestResultsForTransientInput(self, hitTestSource: XRTransientInputHitTestSource) -> Sequence[XRTransientInputHitTestResult]: ...

    def getLightEstimate(self, lightProbe: XRLightProbe) -> Union['XRLightEstimate', 'None']: ...
    session: XRSession
    predictedDisplayTime: DOMHighResTimeStamp

    def getViewerPose(self, referenceSpace: XRReferenceSpace) -> Union['XRViewerPose', 'None']: ...

    def getPose(self, space: XRSpace, baseSpace: XRSpace) -> Union['XRPose', 'None']: ...

class XRSession(EventTarget):
    persistentAnchors: Sequence[str]

    def restorePersistentAnchor(self, uuid: str) -> Awaitable[XRAnchor]: ...

    def deletePersistentAnchor(self, uuid: str) -> Awaitable[None]: ...
    environmentBlendMode: XREnvironmentBlendMode
    interactionMode: XRInteractionMode
    depthUsage: XRDepthUsage
    depthDataFormat: XRDepthDataFormat
    domOverlayState: Union['XRDOMOverlayState', 'None']

    def requestHitTestSource(self, options: XRHitTestOptionsInit) -> Awaitable[XRHitTestSource]: ...

    def requestHitTestSourceForTransientInput(self, options: XRTransientInputHitTestOptionsInit) -> Awaitable[XRTransientInputHitTestSource]: ...

    def requestLightProbe(self, options: Union['XRLightProbeInit', 'None'] = {}) -> Awaitable[XRLightProbe]: ...
    preferredReflectionFormat: XRReflectionFormat
    visibilityState: XRVisibilityState
    frameRate: Union['float', 'None']
    supportedFrameRates: Float32Array
    renderState: XRRenderState
    inputSources: XRInputSourceArray
    enabledFeatures: Sequence[str]
    isSystemKeyboardSupported: bool

    def updateRenderState(self, state: Union['XRRenderStateInit', 'None'] = {}) -> None: ...

    def updateTargetFrameRate(self, rate: float) -> Awaitable[None]: ...

    def requestReferenceSpace(self, type: XRReferenceSpaceType) -> Awaitable[XRReferenceSpace]: ...

    def requestAnimationFrame(self, callback: XRFrameRequestCallback) -> int: ...

    def cancelAnimationFrame(self, handle: int) -> None: ...

    def end(self) -> Awaitable[None]: ...
    onend: EventHandler
    oninputsourceschange: EventHandler
    onselect: EventHandler
    onselectstart: EventHandler
    onselectend: EventHandler
    onsqueeze: EventHandler
    onsqueezestart: EventHandler
    onsqueezeend: EventHandler
    onvisibilitychange: EventHandler
    onframeratechange: EventHandler

class XRHitTestResult:

    def createAnchor(self) -> Awaitable[XRAnchor]: ...

    def getPose(self, baseSpace: XRSpace) -> Union['XRPose', 'None']: ...

class XRAnchorSet: ...

class HTMLAttributionSrcElementUtils:
    attributionSrc: str

class HTMLAnchorElement(HTMLElement, HTMLAttributionSrcElementUtils, HTMLHyperlinkElementUtils):
    @classmethod
    def new(cls) -> HTMLAnchorElement: ...
    target: str
    download: str
    ping: str
    rel: str
    relList: DOMTokenList
    hreflang: str
    type: str
    text: str
    referrerPolicy: str
    coords: str
    charset: str
    name: str
    rev: str
    shape: str
    attributionSourceId: int

class HTMLImageElement(HTMLElement, HTMLAttributionSrcElementUtils):
    @classmethod
    def new(cls) -> HTMLImageElement: ...
    x: int
    y: int
    alt: str
    src: str
    srcset: str
    sizes: str
    crossOrigin: Union['str', 'None']
    useMap: str
    isMap: bool
    width: int
    height: int
    naturalWidth: int
    naturalHeight: int
    complete: bool
    currentSrc: str
    referrerPolicy: str
    decoding: str
    loading: str
    fetchPriority: str

    def decode(self) -> Awaitable[None]: ...
    name: str
    lowsrc: str
    align: str
    hspace: int
    vspace: int
    longDesc: str
    border: str
    """ # GIgnoredStmt
    LegacyFactoryFunction=Image(optional unsigned long width, optional unsigned long height)
    """

class HTMLScriptElement(HTMLElement, HTMLAttributionSrcElementUtils):
    @classmethod
    def new(cls) -> HTMLScriptElement: ...
    src: str
    type: str
    noModule: bool
    async_: bool
    defer: bool
    crossOrigin: Union['str', 'None']
    text: str
    integrity: str
    referrerPolicy: str
    blocking: DOMTokenList
    fetchPriority: str
    charset: str
    event: str
    htmlFor: str

class AttributionReportingRequestOptions(TypedDict):
    eventSourceEligible: bool
    triggerEligible: bool

class RequestInit(TypedDict):
    attributionReporting: NotRequired[AttributionReportingRequestOptions]
    method: NotRequired[ByteString]
    headers: NotRequired[HeadersInit]
    body: NotRequired[Union['BodyInit', 'None']]
    referrer: NotRequired[str]
    referrerPolicy: NotRequired[ReferrerPolicy]
    mode: NotRequired[RequestMode]
    credentials: NotRequired[RequestCredentials]
    cache: NotRequired[RequestCache]
    redirect: NotRequired[RequestRedirect]
    integrity: NotRequired[str]
    keepalive: NotRequired[bool]
    signal: NotRequired[Union['AbortSignal', 'None']]
    duplex: NotRequired[RequestDuplex]
    priority: NotRequired[RequestPriority]
    window: NotRequired[Any]
    targetAddressSpace: NotRequired[RequestTargetAddressSpace]
    browsingTopics: NotRequired[bool]
    privateToken: NotRequired[PrivateToken]

class XMLHttpRequest(XMLHttpRequestEventTarget):
    @classmethod
    def new(cls) -> XMLHttpRequest: ...

    def setAttributionReporting(self, options: AttributionReportingRequestOptions) -> None: ...

    def setPrivateToken(self, privateToken: PrivateToken) -> None: ...
    onreadystatechange: EventHandler
    UNSENT = 0
    OPENED = 1
    HEADERS_RECEIVED = 2
    LOADING = 3
    DONE = 4
    readyState: int
    @overload
    def open(self, method: ByteString, url: str) -> None: ...
    @overload
    def open(self, method: ByteString, url: str, async_: bool, username: Union['str', 'None'] = None, password: Union['str', 'None'] = None) -> None: ...

    def setRequestHeader(self, name: ByteString, value: ByteString) -> None: ...
    timeout: int
    withCredentials: bool
    upload: XMLHttpRequestUpload

    def send(self, body: Union['Document', 'XMLHttpRequestBodyInit', 'None'] = None) -> None: ...

    def abort(self) -> None: ...
    responseURL: str
    status: int
    statusText: ByteString

    def getResponseHeader(self, name: ByteString) -> Union['ByteString', 'None']: ...

    def getAllResponseHeaders(self) -> ByteString: ...

    def overrideMimeType(self, mime: str) -> None: ...
    responseType: XMLHttpRequestResponseType
    response: Any
    responseText: str
    responseXML: Union['Document', 'None']

class HTMLMediaElement(HTMLElement):
    sinkId: str

    def setSinkId(self, sinkId: str) -> Awaitable[None]: ...
    mediaKeys: Union['MediaKeys', 'None']
    onencrypted: EventHandler
    onwaitingforkey: EventHandler

    def setMediaKeys(self, mediaKeys: Union['MediaKeys', 'None']) -> Awaitable[None]: ...
    error: Union['MediaError', 'None']
    src: str
    srcObject: Union['MediaProvider', 'None']
    currentSrc: str
    crossOrigin: Union['str', 'None']
    NETWORK_EMPTY = 0
    NETWORK_IDLE = 1
    NETWORK_LOADING = 2
    NETWORK_NO_SOURCE = 3
    networkState: int
    preload: str
    buffered: TimeRanges

    def load(self) -> None: ...

    def canPlayType(self, type: str) -> CanPlayTypeResult: ...
    HAVE_NOTHING = 0
    HAVE_METADATA = 1
    HAVE_CURRENT_DATA = 2
    HAVE_FUTURE_DATA = 3
    HAVE_ENOUGH_DATA = 4
    readyState: int
    seeking: bool
    currentTime: float

    def fastSeek(self, time: float) -> None: ...
    duration: float

    def getStartDate(self) -> object: ...
    paused: bool
    defaultPlaybackRate: float
    playbackRate: float
    preservesPitch: bool
    played: TimeRanges
    seekable: TimeRanges
    ended: bool
    autoplay: bool
    loop: bool

    def play(self) -> Awaitable[None]: ...

    def pause(self) -> None: ...
    controls: bool
    volume: float
    muted: bool
    defaultMuted: bool
    audioTracks: AudioTrackList
    videoTracks: VideoTrackList
    textTracks: TextTrackList

    def addTextTrack(self, kind: TextTrackKind, label: Union['str', 'None'] = "", language: Union['str', 'None'] = "") -> TextTrack: ...

    def captureStream(self) -> MediaStream: ...
    remote: RemotePlayback
    disableRemotePlayback: bool

class MediaDevices(EventTarget):

    def selectAudioOutput(self, options: Union['AudioOutputOptions', 'None'] = {}) -> Awaitable[MediaDeviceInfo]: ...

    def setCaptureHandleConfig(self, config: Union['CaptureHandleConfig', 'None'] = {}) -> None: ...

    def setSupportedCaptureActions(self, actions: Sequence[str]) -> None: ...
    oncaptureaction: EventHandler
    ondevicechange: EventHandler

    def enumerateDevices(self) -> Awaitable[Sequence[MediaDeviceInfo]]: ...

    def getSupportedConstraints(self) -> MediaTrackSupportedConstraints: ...

    def getUserMedia(self, constraints: Union['MediaStreamConstraints', 'None'] = {}) -> Awaitable[MediaStream]: ...

    def getViewportMedia(self, constraints: Union['ViewportMediaStreamConstraints', 'None'] = {}) -> Awaitable[MediaStream]: ...

    def getDisplayMedia(self, options: Union['DisplayMediaStreamOptions', 'None'] = {}) -> Awaitable[MediaStream]: ...

class AudioOutputOptions(TypedDict):
    deviceId: NotRequired[str]

class Navigator(NavigatorBadge, NavigatorDeviceMemory, GlobalPrivacyControl, NavigatorID, NavigatorLanguage, NavigatorOnLine, NavigatorContentUtils, NavigatorCookies, NavigatorPlugins, NavigatorConcurrentHardware, NavigatorNetworkInformation, NavigatorStorageBuckets, NavigatorStorage, NavigatorUA, NavigatorLocks, NavigatorAutomationInformation, NavigatorGPU, NavigatorML):
    @overload
    def getAutoplayPolicy(self, type: AutoplayPolicyMediaType) -> AutoplayPolicy: ...
    @overload
    def getAutoplayPolicy(self, element: HTMLMediaElement) -> AutoplayPolicy: ...
    @overload
    def getAutoplayPolicy(self, context: AudioContext) -> AutoplayPolicy: ...

    def getBattery(self) -> Awaitable[BatteryManager]: ...

    def sendBeacon(self, url: str, data: Union['BodyInit', 'None'] = None) -> bool: ...
    clipboard: Clipboard
    contacts: ContactsManager
    credentials: CredentialsContainer
    devicePosture: DevicePosture

    def requestMediaKeySystemAccess(self, keySystem: str, supportedConfigurations: Sequence[MediaKeySystemConfiguration]) -> Awaitable[MediaKeySystemAccess]: ...
    epubReadingSystem: EpubReadingSystem

    def getGamepads(self) -> Sequence[Union['Gamepad', 'None']]: ...
    geolocation: Geolocation

    def getInstalledRelatedApps(self) -> Awaitable[Sequence[RelatedApplication]]: ...
    userActivation: UserActivation
    ink: Ink
    scheduling: Scheduling
    keyboard: Keyboard
    mediaCapabilities: MediaCapabilities
    mediaDevices: MediaDevices

    def getUserMedia(self, constraints: MediaStreamConstraints, successCallback: NavigatorUserMediaSuccessCallback, errorCallback: NavigatorUserMediaErrorCallback) -> None: ...
    mediaSession: MediaSession
    permissions: Permissions
    maxTouchPoints: int
    presentation: Presentation
    wakeLock: WakeLock
    serial: Serial
    serviceWorker: ServiceWorkerContainer

    def joinAdInterestGroup(self, group: AuctionAdInterestGroup) -> Awaitable[None]: ...

    def leaveAdInterestGroup(self, group: Union['AuctionAdInterestGroupKey', 'None'] = {}) -> Awaitable[None]: ...

    def runAdAuction(self, config: AuctionAdConfig) -> Awaitable[Union['str', 'FencedFrameConfig', 'None']]: ...

    def updateAdInterestGroups(self) -> None: ...

    def vibrate(self, pattern: VibratePattern) -> bool: ...
    virtualKeyboard: VirtualKeyboard
    bluetooth: Bluetooth

    def share(self, data: Union['ShareData', 'None'] = {}) -> Awaitable[None]: ...

    def canShare(self, data: Union['ShareData', 'None'] = {}) -> bool: ...
    hid: HID

    def requestMIDIAccess(self, options: Union['MIDIOptions', 'None'] = {}) -> Awaitable[MIDIAccess]: ...
    usb: USB
    xr: XRSystem
    windowControlsOverlay: WindowControlsOverlay

class ServiceWorkerGlobalScope(WorkerGlobalScope):
    onbackgroundfetchsuccess: EventHandler
    onbackgroundfetchfail: EventHandler
    onbackgroundfetchabort: EventHandler
    onbackgroundfetchclick: EventHandler
    onsync: EventHandler
    oncontentdelete: EventHandler
    cookieStore: CookieStore
    oncookiechange: EventHandler
    onnotificationclick: EventHandler
    onnotificationclose: EventHandler
    oncanmakepayment: EventHandler
    onpaymentrequest: EventHandler
    onperiodicsync: EventHandler
    onpush: EventHandler
    onpushsubscriptionchange: EventHandler
    clients: Clients
    registration: ServiceWorkerRegistration
    serviceWorker: ServiceWorker

    def skipWaiting(self) -> Awaitable[None]: ...
    oninstall: EventHandler
    onactivate: EventHandler
    onfetch: EventHandler
    onmessage: EventHandler
    onmessageerror: EventHandler

class ServiceWorkerRegistration(EventTarget):
    backgroundFetch: BackgroundFetchManager
    sync: SyncManager
    index: ContentIndex
    cookies: CookieStoreManager

    def showNotification(self, title: str, options: Union['NotificationOptions', 'None'] = {}) -> Awaitable[None]: ...

    def getNotifications(self, filter: Union['GetNotificationOptions', 'None'] = {}) -> Awaitable[Sequence[Notification]]: ...
    paymentManager: PaymentManager
    periodicSync: PeriodicSyncManager
    pushManager: PushManager
    installing: Union['ServiceWorker', 'None']
    waiting: Union['ServiceWorker', 'None']
    active: Union['ServiceWorker', 'None']
    navigationPreload: NavigationPreloadManager
    scope: str
    updateViaCache: ServiceWorkerUpdateViaCache

    def update(self) -> Awaitable[None]: ...

    def unregister(self) -> Awaitable[bool]: ...
    onupdatefound: EventHandler

class BackgroundFetchManager:

    def fetch(self, id: str, requests: Union['RequestInfo', 'Sequence[RequestInfo]'], options: Union['BackgroundFetchOptions', 'None'] = {}) -> Awaitable[BackgroundFetchRegistration]: ...

    def get(self, id: str) -> Awaitable[Union['BackgroundFetchRegistration', 'None']]: ...

    def getIds(self) -> Awaitable[Sequence[str]]: ...

class BackgroundFetchUIOptions(TypedDict):
    icons: NotRequired[Sequence[ImageResource]]
    title: NotRequired[str]

class BackgroundFetchOptions(BackgroundFetchUIOptions):
    downloadTotal: NotRequired[int]

class BackgroundFetchRegistration(EventTarget):
    id: str
    uploadTotal: int
    uploaded: int
    downloadTotal: int
    downloaded: int
    result: BackgroundFetchResult
    failureReason: BackgroundFetchFailureReason
    recordsAvailable: bool
    onprogress: EventHandler

    def abort(self) -> Awaitable[bool]: ...

    def match(self, request: RequestInfo, options: Union['CacheQueryOptions', 'None'] = {}) -> Awaitable[BackgroundFetchRecord]: ...

    def matchAll(self, request: Union['RequestInfo', 'None'] = None, options: Union['CacheQueryOptions', 'None'] = {}) -> Awaitable[Sequence[BackgroundFetchRecord]]: ...

class BackgroundFetchRecord:
    request: Request
    responseReady: Awaitable[Response]

class BackgroundFetchEvent(ExtendableEvent):
    @classmethod
    def new(cls, type: str, init: BackgroundFetchEventInit) -> BackgroundFetchEvent: ...
    registration: BackgroundFetchRegistration

class BackgroundFetchEventInit(ExtendableEventInit):
    registration: BackgroundFetchRegistration

class BackgroundFetchUpdateUIEvent(BackgroundFetchEvent):
    @classmethod
    def new(cls, type: str, init: BackgroundFetchEventInit) -> BackgroundFetchUpdateUIEvent: ...

    def updateUI(self, options: Union['BackgroundFetchUIOptions', 'None'] = {}) -> Awaitable[None]: ...

class SyncManager:

    def register(self, tag: str) -> Awaitable[None]: ...

    def getTags(self) -> Awaitable[Sequence[str]]: ...

class SyncEvent(ExtendableEvent):
    @classmethod
    def new(cls, type: str, init: SyncEventInit) -> SyncEvent: ...
    tag: str
    lastChance: bool

class SyncEventInit(ExtendableEventInit):
    tag: str
    lastChance: NotRequired[bool]

class NavigatorBadge:

    def setAppBadge(self, contents: Union['int', 'None'] = None) -> Awaitable[None]: ...

    def clearAppBadge(self) -> Awaitable[None]: ...

class WorkerNavigator(NavigatorBadge, NavigatorDeviceMemory, GlobalPrivacyControl, NavigatorID, NavigatorLanguage, NavigatorOnLine, NavigatorConcurrentHardware, NavigatorNetworkInformation, NavigatorStorageBuckets, NavigatorStorage, NavigatorUA, NavigatorLocks, NavigatorGPU, NavigatorML):
    mediaCapabilities: MediaCapabilities
    permissions: Permissions
    serial: Serial
    serviceWorker: ServiceWorkerContainer
    hid: HID
    usb: USB

class BatteryManager(EventTarget):
    charging: bool
    chargingTime: float
    dischargingTime: float
    level: float
    onchargingchange: EventHandler
    onchargingtimechange: EventHandler
    ondischargingtimechange: EventHandler
    onlevelchange: EventHandler

class CaptureHandleConfig(TypedDict):
    exposeOrigin: NotRequired[bool]
    handle: NotRequired[str]
    permittedOrigins: NotRequired[Sequence[str]]

class CaptureHandle(TypedDict):
    origin: NotRequired[str]
    handle: NotRequired[str]

class MediaStreamTrack(EventTarget):

    def getCaptureHandle(self) -> Union['CaptureHandle', 'None']: ...
    oncapturehandlechange: EventHandler

    def getSupportedCaptureActions(self) -> Sequence[str]: ...

    def sendCaptureAction(self, action: CaptureAction) -> Awaitable[None]: ...
    kind: str
    id: str
    label: str
    enabled: bool
    muted: bool
    onmute: EventHandler
    onunmute: EventHandler
    readyState: MediaStreamTrackState
    onended: EventHandler

    def clone(self) -> MediaStreamTrack: ...

    def stop(self) -> None: ...

    def getCapabilities(self) -> MediaTrackCapabilities: ...

    def getConstraints(self) -> MediaTrackConstraints: ...

    def getSettings(self) -> MediaTrackSettings: ...

    def applyConstraints(self, constraints: Union['MediaTrackConstraints', 'None'] = {}) -> Awaitable[None]: ...
    contentHint: str
    isolated: bool
    onisolationchange: EventHandler

class CapturedMouseEvent(Event):
    @classmethod
    def new(cls, type: str, eventInitDict: Union['CapturedMouseEventInit', 'None'] = {}) -> CapturedMouseEvent: ...
    surfaceX: int
    surfaceY: int

class CapturedMouseEventInit(EventInit):
    surfaceX: NotRequired[int]
    surfaceY: NotRequired[int]

class CaptureController(EventTarget):
    @classmethod
    def new(cls) -> CaptureController: ...
    oncapturedmousechange: EventHandler

    def setFocusBehavior(self, focusBehavior: CaptureStartFocusBehavior) -> None: ...

class ClipboardEventInit(EventInit):
    clipboardData: NotRequired[Union['DataTransfer', 'None']]

class ClipboardEvent(Event):
    @classmethod
    def new(cls, type: str, eventInitDict: Union['ClipboardEventInit', 'None'] = {}) -> ClipboardEvent: ...
    clipboardData: Union['DataTransfer', 'None']

class ClipboardItem:
    @classmethod
    def new(cls, items: ClipboardItemData, options: Union['ClipboardItemOptions', 'None'] = {}) -> ClipboardItem: ...
    presentationStyle: PresentationStyle
    types: Sequence[str]

    def getType(self, type: str) -> Awaitable[Blob]: ...

class ClipboardItemOptions(TypedDict):
    presentationStyle: NotRequired[PresentationStyle]

class Clipboard(EventTarget):

    def read(self) -> Awaitable[ClipboardItems]: ...

    def readText(self) -> Awaitable[str]: ...

    def write(self, data: ClipboardItems) -> Awaitable[None]: ...

    def writeText(self, data: str) -> Awaitable[None]: ...

class ClipboardPermissionDescriptor(PermissionDescriptor):
    allowWithoutGesture: NotRequired[bool]

class Window(EventTarget, GlobalEventHandlers, WindowEventHandlers, WindowOrWorkerGlobalScope, AnimationFrameProvider, WindowSessionStorage, WindowLocalStorage):
    orientation: int
    onorientationchange: EventHandler
    cookieStore: CookieStore

    def navigate(self, dir: SpatialNavigationDirection) -> None: ...

    def matchMedia(self, query: str) -> MediaQueryList: ...
    screen: Screen
    visualViewport: Union['VisualViewport', 'None']

    def moveTo(self, x: int, y: int) -> None: ...

    def moveBy(self, x: int, y: int) -> None: ...

    def resizeTo(self, width: int, height: int) -> None: ...

    def resizeBy(self, x: int, y: int) -> None: ...
    innerWidth: int
    innerHeight: int
    scrollX: float
    pageXOffset: float
    scrollY: float
    pageYOffset: float
    @overload
    def scroll(self, options: Union['ScrollToOptions', 'None'] = {}) -> None: ...
    @overload
    def scroll(self, x: float, y: float) -> None: ...
    @overload
    def scrollTo(self, options: Union['ScrollToOptions', 'None'] = {}) -> None: ...
    @overload
    def scrollTo(self, x: float, y: float) -> None: ...
    @overload
    def scrollBy(self, options: Union['ScrollToOptions', 'None'] = {}) -> None: ...
    @overload
    def scrollBy(self, x: float, y: float) -> None: ...
    screenX: int
    screenLeft: int
    screenY: int
    screenTop: int
    outerWidth: int
    outerHeight: int
    devicePixelRatio: float

    def getComputedStyle(self, elt: Element, pseudoElt: Union['str', 'None'] = None) -> CSSStyleDeclaration: ...

    def getDigitalGoodsService(self, serviceProvider: str) -> Awaitable[DigitalGoodsService]: ...
    documentPictureInPicture: DocumentPictureInPicture
    event: Union['Event', 'None']
    fence: Union['Fence', 'None']

    def showOpenFilePicker(self, options: Union['OpenFilePickerOptions', 'None'] = {}) -> Awaitable[Sequence[FileSystemFileHandle]]: ...

    def showSaveFilePicker(self, options: Union['SaveFilePickerOptions', 'None'] = {}) -> Awaitable[FileSystemFileHandle]: ...

    def showDirectoryPicker(self, options: Union['DirectoryPickerOptions', 'None'] = {}) -> Awaitable[FileSystemDirectoryHandle]: ...
    window: WindowProxy
    self: WindowProxy
    document: Document
    name: str
    location: Location
    history: History
    navigation: Navigation
    customElements: CustomElementRegistry
    locationbar: BarProp
    menubar: BarProp
    personalbar: BarProp
    scrollbars: BarProp
    statusbar: BarProp
    toolbar: BarProp
    status: str

    def close(self) -> None: ...
    closed: bool

    def stop(self) -> None: ...

    def focus(self) -> None: ...

    def blur(self) -> None: ...
    frames: WindowProxy
    length: int
    top: Union['WindowProxy', 'None']
    opener: Any
    parent: Union['WindowProxy', 'None']
    frameElement: Union['Element', 'None']

    def open(self, url: Union['str', 'None'] = "", target: Union['str', 'None'] = "_blank", features: Union['str', 'None'] = "") -> Union['WindowProxy', 'None']: ...

    def __getter__(self, name: str) -> object: ...
    navigator: Navigator
    clientInformation: Navigator
    originAgentCluster: bool
    @overload
    def alert(self) -> None: ...
    @overload
    def alert(self, message: str) -> None: ...

    def confirm(self, message: Union['str', 'None'] = "") -> bool: ...

    def prompt(self, message: Union['str', 'None'] = "", default: Union['str', 'None'] = "") -> Union['str', 'None']: ...

    def print(self) -> None: ...
    @overload
    def postMessage(self, message: Any, targetOrigin: str, transfer: Union['Sequence[object]', 'None'] = []) -> None: ...
    @overload
    def postMessage(self, message: Any, options: Union['WindowPostMessageOptions', 'None'] = {}) -> None: ...

    def captureEvents(self) -> None: ...

    def releaseEvents(self) -> None: ...
    external: External

    def queryLocalFonts(self, options: Union['QueryOptions', 'None'] = {}) -> Awaitable[Sequence[FontData]]: ...
    onappinstalled: EventHandler
    onbeforeinstallprompt: EventHandler
    ondeviceorientation: EventHandler
    ondeviceorientationabsolute: EventHandler
    ondevicemotion: EventHandler
    portalHost: Union['PortalHost', 'None']

    def requestIdleCallback(self, callback: IdleRequestCallback, options: Union['IdleRequestOptions', 'None'] = {}) -> int: ...

    def cancelIdleCallback(self, handle: int) -> None: ...

    def getSelection(self) -> Union['Selection', 'None']: ...
    sharedStorage: Union['WindowSharedStorage', 'None']
    speechSynthesis: SpeechSynthesis
    launchQueue: LaunchQueue

    def getScreenDetails(self) -> Awaitable[ScreenDetails]: ...

class HTMLBodyElement(HTMLElement, WindowEventHandlers):
    @classmethod
    def new(cls) -> HTMLBodyElement: ...
    onorientationchange: EventHandler
    text: str
    link: str
    vLink: str
    aLink: str
    bgColor: str
    background: str

class CompressionStream(GenericTransformStream):
    @classmethod
    def new(cls, format: CompressionFormat) -> CompressionStream: ...

class DecompressionStream(GenericTransformStream):
    @classmethod
    def new(cls, format: CompressionFormat) -> DecompressionStream: ...

class PressureObserver:
    @classmethod
    def new(cls, callback: PressureUpdateCallback, options: Union['PressureObserverOptions', 'None'] = {}) -> PressureObserver: ...

    def observe(self, source: PressureSource) -> Awaitable[None]: ...

    def unobserve(self, source: PressureSource) -> None: ...

    def disconnect(self) -> None: ...

    def takeRecords(self) -> Sequence[PressureRecord]: ...

class PressureRecord:
    source: PressureSource
    state: PressureState
    time: DOMHighResTimeStamp

    def toJSON(self) -> object: ...

class PressureObserverOptions(TypedDict):
    sampleRate: NotRequired[float]

class ConsoleNamespace:

    def assert_(self, condition: Union['bool', 'None'] = False, *data: Any) -> None: ...

    def clear(self) -> None: ...

    def debug(self, *data: Any) -> None: ...

    def error(self, *data: Any) -> None: ...

    def info(self, *data: Any) -> None: ...

    def log(self, *data: Any) -> None: ...

    def table(self, tabularData: Union['Any', 'None'] = None, properties: Union['Sequence[str]', 'None'] = None) -> None: ...

    def trace(self, *data: Any) -> None: ...

    def warn(self, *data: Any) -> None: ...

    def dir(self, item: Union['Any', 'None'] = None, options: Union['object', 'None'] = None) -> None: ...

    def dirxml(self, *data: Any) -> None: ...

    def count(self, label: Union['str', 'None'] = "default") -> None: ...

    def countReset(self, label: Union['str', 'None'] = "default") -> None: ...

    def group(self, *data: Any) -> None: ...

    def groupCollapsed(self, *data: Any) -> None: ...

    def groupEnd(self) -> None: ...

    def time(self, label: Union['str', 'None'] = "default") -> None: ...

    def timeLog(self, label: Union['str', 'None'] = "default", *data: Any) -> None: ...

    def timeEnd(self, label: Union['str', 'None'] = "default") -> None: ...

class ContactAddress:

    def toJSON(self) -> object: ...
    city: str
    country: str
    dependentLocality: str
    organization: str
    phone: str
    postalCode: str
    recipient: str
    region: str
    sortingCode: str
    addressLine: Sequence[str]

class ContactInfo(TypedDict):
    address: NotRequired[Sequence[ContactAddress]]
    email: NotRequired[Sequence[str]]
    icon: NotRequired[Sequence[Blob]]
    name: NotRequired[Sequence[str]]
    tel: NotRequired[Sequence[str]]

class ContactsSelectOptions(TypedDict):
    multiple: NotRequired[bool]

class ContactsManager:

    def getProperties(self) -> Awaitable[Sequence[ContactProperty]]: ...

    def select(self, properties: Sequence[ContactProperty], options: Union['ContactsSelectOptions', 'None'] = {}) -> Awaitable[Sequence[ContactInfo]]: ...

class ContentDescription(TypedDict):
    id: str
    title: str
    description: str
    category: NotRequired[ContentCategory]
    icons: NotRequired[Sequence[ImageResource]]
    url: str

class ContentIndex:

    def add(self, description: ContentDescription) -> Awaitable[None]: ...

    def delete(self, id: str) -> Awaitable[None]: ...

    def getAll(self) -> Awaitable[Sequence[ContentDescription]]: ...

class ContentIndexEventInit(ExtendableEventInit):
    id: str

class ContentIndexEvent(ExtendableEvent):
    @classmethod
    def new(cls, type: str, init: ContentIndexEventInit) -> ContentIndexEvent: ...
    id: str

class CookieStore(EventTarget):
    @overload
    def get(self, name: str) -> Awaitable[Union['CookieListItem', 'None']]: ...
    @overload
    def get(self, options: Union['CookieStoreGetOptions', 'None'] = {}) -> Awaitable[Union['CookieListItem', 'None']]: ...
    @overload
    def getAll(self, name: str) -> Awaitable[CookieList]: ...
    @overload
    def getAll(self, options: Union['CookieStoreGetOptions', 'None'] = {}) -> Awaitable[CookieList]: ...
    @overload
    def set(self, name: str, value: str) -> Awaitable[None]: ...
    @overload
    def set(self, options: CookieInit) -> Awaitable[None]: ...
    @overload
    def delete(self, name: str) -> Awaitable[None]: ...
    @overload
    def delete(self, options: CookieStoreDeleteOptions) -> Awaitable[None]: ...
    onchange: EventHandler

class CookieStoreGetOptions(TypedDict):
    name: NotRequired[str]
    url: NotRequired[str]

class CookieInit(TypedDict):
    name: str
    value: str
    expires: NotRequired[Union['DOMHighResTimeStamp', 'None']]
    domain: NotRequired[Union['str', 'None']]
    path: NotRequired[str]
    sameSite: NotRequired[CookieSameSite]
    partitioned: NotRequired[bool]

class CookieStoreDeleteOptions(TypedDict):
    name: str
    domain: NotRequired[Union['str', 'None']]
    path: NotRequired[str]
    partitioned: NotRequired[bool]

class CookieListItem(TypedDict):
    name: NotRequired[str]
    value: NotRequired[str]
    domain: NotRequired[Union['str', 'None']]
    path: NotRequired[str]
    expires: NotRequired[Union['DOMHighResTimeStamp', 'None']]
    secure: NotRequired[bool]
    sameSite: NotRequired[CookieSameSite]
    partitioned: NotRequired[bool]

class CookieStoreManager:

    def subscribe(self, subscriptions: Sequence[CookieStoreGetOptions]) -> Awaitable[None]: ...

    def getSubscriptions(self) -> Awaitable[Sequence[CookieStoreGetOptions]]: ...

    def unsubscribe(self, subscriptions: Sequence[CookieStoreGetOptions]) -> Awaitable[None]: ...

class CookieChangeEvent(Event):
    @classmethod
    def new(cls, type: str, eventInitDict: Union['CookieChangeEventInit', 'None'] = {}) -> CookieChangeEvent: ...
    changed: Sequence[CookieListItem]
    deleted: Sequence[CookieListItem]

class CookieChangeEventInit(EventInit):
    changed: NotRequired[CookieList]
    deleted: NotRequired[CookieList]

class ExtendableCookieChangeEvent(ExtendableEvent):
    @classmethod
    def new(cls, type: str, eventInitDict: Union['ExtendableCookieChangeEventInit', 'None'] = {}) -> ExtendableCookieChangeEvent: ...
    changed: Sequence[CookieListItem]
    deleted: Sequence[CookieListItem]

class ExtendableCookieChangeEventInit(ExtendableEventInit):
    changed: NotRequired[CookieList]
    deleted: NotRequired[CookieList]

class CrashReportBody(ReportBody):

    def toJSON(self) -> object: ...
    reason: Union['str', 'None']

class Credential:
    id: str
    type: str

class CredentialUserData:
    name: str
    iconURL: str

class CredentialsContainer:

    def get(self, options: Union['CredentialRequestOptions', 'None'] = {}) -> Awaitable[Union['Credential', 'None']]: ...

    def store(self, credential: Credential) -> Awaitable[None]: ...

    def create(self, options: Union['CredentialCreationOptions', 'None'] = {}) -> Awaitable[Union['Credential', 'None']]: ...

    def preventSilentAccess(self) -> Awaitable[None]: ...

class CredentialData(TypedDict):
    id: str

class CredentialCreationOptions(TypedDict):
    signal: NotRequired[AbortSignal]
    password: NotRequired[PasswordCredentialInit]
    federated: NotRequired[FederatedCredentialInit]
    publicKey: NotRequired[PublicKeyCredentialCreationOptions]

class PasswordCredential(Credential, CredentialUserData):
    @overload
    @classmethod
    def new(cls, form: HTMLFormElement) -> PasswordCredential: ...
    @overload
    @classmethod
    def new(cls, data: PasswordCredentialData) -> PasswordCredential: ...
    password: str

class PasswordCredentialData(CredentialData):
    name: NotRequired[str]
    iconURL: NotRequired[str]
    origin: str
    password: str

class FederatedCredential(Credential, CredentialUserData):
    @classmethod
    def new(cls, data: FederatedCredentialInit) -> FederatedCredential: ...
    provider: str
    protocol: Union['str', 'None']

class FederatedCredentialRequestOptions(TypedDict):
    providers: NotRequired[Sequence[str]]
    protocols: NotRequired[Sequence[str]]

class FederatedCredentialInit(CredentialData):
    name: NotRequired[str]
    iconURL: NotRequired[str]
    origin: str
    provider: str
    protocol: NotRequired[str]

class HTMLIFrameElement(HTMLElement):
    @classmethod
    def new(cls) -> HTMLIFrameElement: ...
    csp: str
    src: str
    srcdoc: str
    name: str
    sandbox: DOMTokenList
    allow: str
    allowFullscreen: bool
    width: str
    height: str
    referrerPolicy: str
    loading: str
    contentDocument: Union['Document', 'None']
    contentWindow: Union['WindowProxy', 'None']

    def getSVGDocument(self) -> Union['Document', 'None']: ...
    align: str
    scrolling: str
    frameBorder: str
    longDesc: str
    marginHeight: str
    marginWidth: str
    permissionsPolicy: PermissionsPolicy
    browsingTopics: bool
    privateToken: str

class ScriptingPolicyReportBody(ReportBody):

    def toJSON(self) -> object: ...
    violationType: str
    violationURL: Union['str', 'None']
    violationSample: Union['str', 'None']
    lineno: int
    colno: int

class CSSPositionFallbackRule(CSSGroupingRule):
    name: str

class CSSTryRule(CSSRule):
    style: CSSStyleDeclaration

class AnimationWorkletGlobalScope(WorkletGlobalScope):

    def registerAnimator(self, name: str, animatorCtor: AnimatorInstanceConstructor) -> None: ...

class WorkletAnimationEffect:

    def getTiming(self) -> EffectTiming: ...

    def getComputedTiming(self) -> ComputedEffectTiming: ...
    localTime: Union['float', 'None']

class WorkletAnimation(Animation):
    @classmethod
    def new(cls, animatorName: str, effects: Union['AnimationEffect', 'Sequence[AnimationEffect]', 'None'] = None, timeline: Union['AnimationTimeline', 'None'] = None, options: Union['Any', 'None'] = None) -> WorkletAnimation: ...
    animatorName: str

class WorkletGroupEffect:

    def getChildren(self) -> Sequence[WorkletAnimationEffect]: ...

class CSSAnimation(Animation):
    animationName: str

class AnimationEvent(Event):
    @classmethod
    def new(cls, type: str, animationEventInitDict: Union['AnimationEventInit', 'None'] = {}) -> AnimationEvent: ...
    animationName: str
    elapsedTime: float
    pseudoElement: str

class AnimationEventInit(EventInit):
    animationName: NotRequired[str]
    elapsedTime: NotRequired[float]
    pseudoElement: NotRequired[str]

class CSSKeyframeRule(CSSRule):
    keyText: str
    style: CSSStyleDeclaration

class CSSKeyframesRule(CSSRule):
    name: str
    cssRules: CSSRuleList
    length: int

    def __getter__(self, index: int) -> CSSKeyframeRule: ...

    def appendRule(self, rule: str) -> None: ...

    def deleteRule(self, select: str) -> None: ...

    def findRule(self, select: str) -> Union['CSSKeyframeRule', 'None']: ...

class GlobalEventHandlers:
    onanimationstart: EventHandler
    onanimationiteration: EventHandler
    onanimationend: EventHandler
    onanimationcancel: EventHandler
    ontransitionrun: EventHandler
    ontransitionstart: EventHandler
    ontransitionend: EventHandler
    ontransitioncancel: EventHandler
    onabort: EventHandler
    onauxclick: EventHandler
    onbeforeinput: EventHandler
    onbeforematch: EventHandler
    onbeforetoggle: EventHandler
    onblur: EventHandler
    oncancel: EventHandler
    oncanplay: EventHandler
    oncanplaythrough: EventHandler
    onchange: EventHandler
    onclick: EventHandler
    onclose: EventHandler
    oncontextlost: EventHandler
    oncontextmenu: EventHandler
    oncontextrestored: EventHandler
    oncopy: EventHandler
    oncuechange: EventHandler
    oncut: EventHandler
    ondblclick: EventHandler
    ondrag: EventHandler
    ondragend: EventHandler
    ondragenter: EventHandler
    ondragleave: EventHandler
    ondragover: EventHandler
    ondragstart: EventHandler
    ondrop: EventHandler
    ondurationchange: EventHandler
    onemptied: EventHandler
    onended: EventHandler
    onerror: OnErrorEventHandler
    onfocus: EventHandler
    onformdata: EventHandler
    oninput: EventHandler
    oninvalid: EventHandler
    onkeydown: EventHandler
    onkeypress: EventHandler
    onkeyup: EventHandler
    onload: EventHandler
    onloadeddata: EventHandler
    onloadedmetadata: EventHandler
    onloadstart: EventHandler
    onmousedown: EventHandler
    onmouseenter: EventHandler
    onmouseleave: EventHandler
    onmousemove: EventHandler
    onmouseout: EventHandler
    onmouseover: EventHandler
    onmouseup: EventHandler
    onpaste: EventHandler
    onpause: EventHandler
    onplay: EventHandler
    onplaying: EventHandler
    onprogress: EventHandler
    onratechange: EventHandler
    onreset: EventHandler
    onresize: EventHandler
    onscroll: EventHandler
    onscrollend: EventHandler
    onsecuritypolicyviolation: EventHandler
    onseeked: EventHandler
    onseeking: EventHandler
    onselect: EventHandler
    onslotchange: EventHandler
    onstalled: EventHandler
    onsubmit: EventHandler
    onsuspend: EventHandler
    ontimeupdate: EventHandler
    ontoggle: EventHandler
    onvolumechange: EventHandler
    onwaiting: EventHandler
    onwebkitanimationend: EventHandler
    onwebkitanimationiteration: EventHandler
    onwebkitanimationstart: EventHandler
    onwebkittransitionend: EventHandler
    onwheel: EventHandler
    onpointerover: EventHandler
    onpointerenter: EventHandler
    onpointerdown: EventHandler
    onpointermove: EventHandler
    onpointerrawupdate: EventHandler
    onpointerup: EventHandler
    onpointercancel: EventHandler
    onpointerout: EventHandler
    onpointerleave: EventHandler
    ongotpointercapture: EventHandler
    onlostpointercapture: EventHandler
    onselectstart: EventHandler
    onselectionchange: EventHandler
    ontouchstart: EventHandler
    ontouchend: EventHandler
    ontouchmove: EventHandler
    ontouchcancel: EventHandler
    onbeforexrselect: EventHandler

class CSSScopeRule(CSSGroupingRule):
    start: Union['str', 'None']
    end: Union['str', 'None']

class CSSLayerBlockRule(CSSGroupingRule):
    name: str

class CSSLayerStatementRule(CSSRule):
    nameList: Sequence[str]

class CSSColorProfileRule(CSSRule):
    name: str
    src: str
    renderingIntent: str
    components: str

class CSSConditionRule(CSSGroupingRule):
    conditionText: str

class CSSMediaRule(CSSConditionRule):
    media: MediaList

class CSSSupportsRule(CSSConditionRule): ...

class CssNamespace:
    @overload
    def supports(self, property: str, value: str) -> bool: ...
    @overload
    def supports(self, conditionText: str) -> bool: ...

    def parseStylesheet(self, css: CSSStringSource, options: Union['CSSParserOptions', 'None'] = {}) -> Awaitable[Sequence[CSSParserRule]]: ...

    def parseRuleList(self, css: CSSStringSource, options: Union['CSSParserOptions', 'None'] = {}) -> Awaitable[Sequence[CSSParserRule]]: ...

    def parseRule(self, css: CSSStringSource, options: Union['CSSParserOptions', 'None'] = {}) -> Awaitable[CSSParserRule]: ...

    def parseDeclarationList(self, css: CSSStringSource, options: Union['CSSParserOptions', 'None'] = {}) -> Awaitable[Sequence[CSSParserRule]]: ...

    def parseDeclaration(self, css: str, options: Union['CSSParserOptions', 'None'] = {}) -> CSSParserDeclaration: ...

    def parseValue(self, css: str) -> CSSToken: ...

    def parseValueList(self, css: str) -> Sequence[CSSToken]: ...

    def parseCommaValueList(self, css: str) -> Sequence[Sequence[CSSToken]]: ...

    def registerProperty(self, definition: PropertyDefinition) -> None: ...

    def number(self, value: float) -> CSSUnitValue: ...

    def percent(self, value: float) -> CSSUnitValue: ...

    def em(self, value: float) -> CSSUnitValue: ...

    def ex(self, value: float) -> CSSUnitValue: ...

    def ch(self, value: float) -> CSSUnitValue: ...

    def ic(self, value: float) -> CSSUnitValue: ...

    def rem(self, value: float) -> CSSUnitValue: ...

    def lh(self, value: float) -> CSSUnitValue: ...

    def rlh(self, value: float) -> CSSUnitValue: ...

    def vw(self, value: float) -> CSSUnitValue: ...

    def vh(self, value: float) -> CSSUnitValue: ...

    def vi(self, value: float) -> CSSUnitValue: ...

    def vb(self, value: float) -> CSSUnitValue: ...

    def vmin(self, value: float) -> CSSUnitValue: ...

    def vmax(self, value: float) -> CSSUnitValue: ...

    def svw(self, value: float) -> CSSUnitValue: ...

    def svh(self, value: float) -> CSSUnitValue: ...

    def svi(self, value: float) -> CSSUnitValue: ...

    def svb(self, value: float) -> CSSUnitValue: ...

    def svmin(self, value: float) -> CSSUnitValue: ...

    def svmax(self, value: float) -> CSSUnitValue: ...

    def lvw(self, value: float) -> CSSUnitValue: ...

    def lvh(self, value: float) -> CSSUnitValue: ...

    def lvi(self, value: float) -> CSSUnitValue: ...

    def lvb(self, value: float) -> CSSUnitValue: ...

    def lvmin(self, value: float) -> CSSUnitValue: ...

    def lvmax(self, value: float) -> CSSUnitValue: ...

    def dvw(self, value: float) -> CSSUnitValue: ...

    def dvh(self, value: float) -> CSSUnitValue: ...

    def dvi(self, value: float) -> CSSUnitValue: ...

    def dvb(self, value: float) -> CSSUnitValue: ...

    def dvmin(self, value: float) -> CSSUnitValue: ...

    def dvmax(self, value: float) -> CSSUnitValue: ...

    def cqw(self, value: float) -> CSSUnitValue: ...

    def cqh(self, value: float) -> CSSUnitValue: ...

    def cqi(self, value: float) -> CSSUnitValue: ...

    def cqb(self, value: float) -> CSSUnitValue: ...

    def cqmin(self, value: float) -> CSSUnitValue: ...

    def cqmax(self, value: float) -> CSSUnitValue: ...

    def cm(self, value: float) -> CSSUnitValue: ...

    def mm(self, value: float) -> CSSUnitValue: ...

    def Q(self, value: float) -> CSSUnitValue: ...

    def in_(self, value: float) -> CSSUnitValue: ...

    def pt(self, value: float) -> CSSUnitValue: ...

    def pc(self, value: float) -> CSSUnitValue: ...

    def px(self, value: float) -> CSSUnitValue: ...

    def deg(self, value: float) -> CSSUnitValue: ...

    def grad(self, value: float) -> CSSUnitValue: ...

    def rad(self, value: float) -> CSSUnitValue: ...

    def turn(self, value: float) -> CSSUnitValue: ...

    def s(self, value: float) -> CSSUnitValue: ...

    def ms(self, value: float) -> CSSUnitValue: ...

    def Hz(self, value: float) -> CSSUnitValue: ...

    def kHz(self, value: float) -> CSSUnitValue: ...

    def dpi(self, value: float) -> CSSUnitValue: ...

    def dpcm(self, value: float) -> CSSUnitValue: ...

    def dppx(self, value: float) -> CSSUnitValue: ...

    def fr(self, value: float) -> CSSUnitValue: ...

    def escape(self, ident: str) -> str: ...

class CSSContainerRule(CSSConditionRule):
    containerName: str
    containerQuery: str

class ContentVisibilityAutoStateChangeEvent(Event):
    @classmethod
    def new(cls, type: str, eventInitDict: Union['ContentVisibilityAutoStateChangeEventInit', 'None'] = {}) -> ContentVisibilityAutoStateChangeEvent: ...
    skipped: bool

class ContentVisibilityAutoStateChangeEventInit(EventInit):
    skipped: NotRequired[bool]

class CSSCounterStyleRule(CSSRule):
    name: str
    system: str
    symbols: str
    additiveSymbols: str
    negative: str
    prefix: str
    suffix: str
    range: str
    pad: str
    speakAs: str
    fallback: str

class FontFaceDescriptors(TypedDict):
    style: NotRequired[str]
    weight: NotRequired[str]
    stretch: NotRequired[str]
    unicodeRange: NotRequired[str]
    variant: NotRequired[str]
    featureSettings: NotRequired[str]
    variationSettings: NotRequired[str]
    display: NotRequired[str]
    ascentOverride: NotRequired[str]
    descentOverride: NotRequired[str]
    lineGapOverride: NotRequired[str]

class FontFace:
    @classmethod
    def new(cls, family: str, source: Union['str', 'BinaryData'], descriptors: Union['FontFaceDescriptors', 'None'] = {}) -> FontFace: ...
    family: str
    style: str
    weight: str
    stretch: str
    unicodeRange: str
    variant: str
    featureSettings: str
    variationSettings: str
    display: str
    ascentOverride: str
    descentOverride: str
    lineGapOverride: str
    status: FontFaceLoadStatus

    def load(self) -> Awaitable[FontFace]: ...
    loaded: Awaitable[FontFace]
    features: FontFaceFeatures
    variations: FontFaceVariations
    palettes: FontFacePalettes

class FontFaceFeatures: ...

class FontFaceVariationAxis:
    name: str
    axisTag: str
    minimumValue: float
    maximumValue: float
    defaultValue: float

class FontFaceVariations: ...

class FontFacePalette:
    length: int

    def __getter__(self, index: int) -> str: ...
    usableWithLightBackground: bool
    usableWithDarkBackground: bool

class FontFacePalettes:
    length: int

    def __getter__(self, index: int) -> FontFacePalette: ...

class FontFaceSetLoadEventInit(EventInit):
    fontfaces: NotRequired[Sequence[FontFace]]

class FontFaceSetLoadEvent(Event):
    @classmethod
    def new(cls, type: str, eventInitDict: Union['FontFaceSetLoadEventInit', 'None'] = {}) -> FontFaceSetLoadEvent: ...
    fontfaces: Sequence[FontFace]

class FontFaceSet(EventTarget):
    @classmethod
    def new(cls, initialFaces: Sequence[FontFace]) -> FontFaceSet: ...

    def add(self, font: FontFace) -> FontFaceSet: ...

    def delete(self, font: FontFace) -> bool: ...

    def clear(self) -> None: ...
    onloading: EventHandler
    onloadingdone: EventHandler
    onloadingerror: EventHandler

    def load(self, font: str, text: Union['str', 'None'] = " ") -> Awaitable[Sequence[FontFace]]: ...

    def check(self, font: str, text: Union['str', 'None'] = " ") -> bool: ...
    ready: Awaitable[FontFaceSet]
    status: FontFaceSetLoadStatus

class FontFaceSource:
    fonts: FontFaceSet

class WorkerGlobalScope(EventTarget, FontFaceSource, WindowOrWorkerGlobalScope):
    self: WorkerGlobalScope
    location: WorkerLocation
    navigator: WorkerNavigator

    def importScripts(self, *urls: str) -> None: ...
    onerror: OnErrorEventHandler
    onlanguagechange: EventHandler
    onoffline: EventHandler
    ononline: EventHandler
    onrejectionhandled: EventHandler
    onunhandledrejection: EventHandler

class CSSFontFeatureValuesRule(CSSRule):
    fontFamily: str
    annotation: CSSFontFeatureValuesMap
    ornaments: CSSFontFeatureValuesMap
    stylistic: CSSFontFeatureValuesMap
    swash: CSSFontFeatureValuesMap
    characterVariant: CSSFontFeatureValuesMap
    styleset: CSSFontFeatureValuesMap

class CSSFontFeatureValuesMap:

    def set(self, featureValueName: str, values: Union['int', 'Sequence[int]']) -> None: ...

class CSSFontPaletteValuesRule(CSSRule):
    name: str
    fontFamily: str
    basePalette: str
    overrideColors: str

class Highlight:
    @classmethod
    def new(cls, *initialRanges: AbstractRange) -> Highlight: ...
    priority: int
    type: HighlightType

class HighlightRegistry: ...

class LayoutWorkletGlobalScope(WorkletGlobalScope):

    def registerLayout(self, name: str, layoutCtor: VoidFunction) -> None: ...

class LayoutOptions(TypedDict):
    childDisplay: NotRequired[ChildDisplayType]
    sizing: NotRequired[LayoutSizingMode]

class LayoutChild:
    styleMap: StylePropertyMapReadOnly

    def intrinsicSizes(self) -> Awaitable[IntrinsicSizes]: ...

    def layoutNextFragment(self, constraints: LayoutConstraintsOptions, breakToken: ChildBreakToken) -> Awaitable[LayoutFragment]: ...

class LayoutFragment:
    inlineSize: float
    blockSize: float
    inlineOffset: float
    blockOffset: float
    data: Any
    breakToken: Union['ChildBreakToken', 'None']

class IntrinsicSizes:
    minContentSize: float
    maxContentSize: float

class LayoutConstraints:
    availableInlineSize: float
    availableBlockSize: float
    fixedInlineSize: Union['float', 'None']
    fixedBlockSize: Union['float', 'None']
    percentageInlineSize: float
    percentageBlockSize: float
    blockFragmentationOffset: Union['float', 'None']
    blockFragmentationType: BlockFragmentationType
    data: Any

class LayoutConstraintsOptions(TypedDict):
    availableInlineSize: NotRequired[float]
    availableBlockSize: NotRequired[float]
    fixedInlineSize: NotRequired[float]
    fixedBlockSize: NotRequired[float]
    percentageInlineSize: NotRequired[float]
    percentageBlockSize: NotRequired[float]
    blockFragmentationOffset: NotRequired[float]
    blockFragmentationType: NotRequired[BlockFragmentationType]
    data: NotRequired[Any]

class ChildBreakToken:
    breakType: BreakType
    child: LayoutChild

class BreakToken:
    childBreakTokens: Sequence[ChildBreakToken]
    data: Any

class BreakTokenOptions(TypedDict):
    childBreakTokens: NotRequired[Sequence[ChildBreakToken]]
    data: NotRequired[Any]

class LayoutEdges:
    inlineStart: float
    inlineEnd: float
    blockStart: float
    blockEnd: float
    inline: float
    block: float

class FragmentResultOptions(TypedDict):
    inlineSize: NotRequired[float]
    blockSize: NotRequired[float]
    autoBlockSize: NotRequired[float]
    childFragments: NotRequired[Sequence[LayoutFragment]]
    data: NotRequired[Any]
    breakToken: NotRequired[BreakTokenOptions]

class FragmentResult:
    @classmethod
    def new(cls, options: Union['FragmentResultOptions', 'None'] = {}) -> FragmentResult: ...
    inlineSize: float
    blockSize: float

class IntrinsicSizesResultOptions(TypedDict):
    maxContentSize: NotRequired[float]
    minContentSize: NotRequired[float]

class SVGClipPathElement(SVGElement):
    clipPathUnits: SVGAnimatedEnumeration
    transform: SVGAnimatedTransformList

class SVGMaskElement(SVGElement):
    maskUnits: SVGAnimatedEnumeration
    maskContentUnits: SVGAnimatedEnumeration
    x: SVGAnimatedLength
    y: SVGAnimatedLength
    width: SVGAnimatedLength
    height: SVGAnimatedLength

class FocusableAreasOption(TypedDict):
    mode: NotRequired[FocusableAreaSearchMode]

class SpatialNavigationSearchOptions(TypedDict):
    candidates: NotRequired[Sequence[Node]]
    container: NotRequired[Union['Node', 'None']]

class NavigationEvent(UIEvent):
    @classmethod
    def new(cls, type: str, eventInitDict: Union['NavigationEventInit', 'None'] = {}) -> NavigationEvent: ...
    dir: SpatialNavigationDirection
    relatedTarget: Union['EventTarget', 'None']

class NavigationEventInit(UIEventInit):
    dir: NotRequired[SpatialNavigationDirection]
    relatedTarget: NotRequired[Union['EventTarget', 'None']]

class PaintWorkletGlobalScope(WorkletGlobalScope):

    def registerPaint(self, name: str, paintCtor: VoidFunction) -> None: ...
    devicePixelRatio: float

class PaintRenderingContext2DSettings(TypedDict):
    alpha: NotRequired[bool]

class PaintRenderingContext2D(CanvasState, CanvasTransform, CanvasCompositing, CanvasImageSmoothing, CanvasFillStrokeStyles, CanvasShadowStyles, CanvasRect, CanvasDrawPath, CanvasDrawImage, CanvasPathDrawingStyles, CanvasPath): ...

class PaintSize:
    width: float
    height: float

class CSSParserOptions(TypedDict):
    atRules: NotRequired[object]

class CSSParserRule: ...

class CSSParserAtRule(CSSParserRule):
    @classmethod
    def new(cls, name: str, prelude: Sequence[CSSToken], body: Union['Sequence[CSSParserRule]', 'None'] = None) -> CSSParserAtRule: ...
    name: str
    prelude: Sequence[CSSParserValue]
    body: Sequence[CSSParserRule]

class CSSParserQualifiedRule(CSSParserRule):
    @classmethod
    def new(cls, prelude: Sequence[CSSToken], body: Union['Sequence[CSSParserRule]', 'None'] = None) -> CSSParserQualifiedRule: ...
    prelude: Sequence[CSSParserValue]
    body: Sequence[CSSParserRule]

class CSSParserDeclaration(CSSParserRule):
    @classmethod
    def new(cls, name: str, body: Union['Sequence[CSSParserRule]', 'None'] = None) -> CSSParserDeclaration: ...
    name: str
    body: Sequence[CSSParserValue]

class CSSParserValue: ...

class CSSParserBlock(CSSParserValue):
    @classmethod
    def new(cls, name: str, body: Sequence[CSSParserValue]) -> CSSParserBlock: ...
    name: str
    body: Sequence[CSSParserValue]

class CSSParserFunction(CSSParserValue):
    @classmethod
    def new(cls, name: str, args: Sequence[Sequence[CSSParserValue]]) -> CSSParserFunction: ...
    name: str
    args: Sequence[Sequence[CSSParserValue]]

class PropertyDefinition(TypedDict):
    name: str
    syntax: NotRequired[str]
    inherits: bool
    initialValue: NotRequired[str]

class CSSPropertyRule(CSSRule):
    name: str
    syntax: str
    inherits: bool
    initialValue: Union['str', 'None']

class CSSPseudoElement(EventTarget, GeometryUtils):
    type: str
    element: Element
    parent: Union['Element', 'CSSPseudoElement']

    def pseudo(self, type: str) -> Union['CSSPseudoElement', 'None']: ...

class NamedFlowMap: ...

class NamedFlow(EventTarget):
    name: str
    overset: bool

    def getRegions(self) -> Sequence[Element]: ...
    firstEmptyRegionIndex: int

    def getContent(self) -> Sequence[Node]: ...

    def getRegionsByContent(self, node: Node) -> Sequence[Element]: ...

class Region:
    regionOverset: str

    def getRegionFlowRanges(self) -> Sequence[Range]: ...

class CSSStartingStyleRule(CSSGroupingRule): ...

class CSSTransition(Animation):
    transitionProperty: str

class TransitionEvent(Event):
    @classmethod
    def new(cls, type: str, transitionEventInitDict: Union['TransitionEventInit', 'None'] = {}) -> TransitionEvent: ...
    propertyName: str
    elapsedTime: float
    pseudoElement: str

class TransitionEventInit(EventInit):
    propertyName: NotRequired[str]
    elapsedTime: NotRequired[float]
    pseudoElement: NotRequired[str]

class CSSStyleValue: ...

class StylePropertyMapReadOnly:

    def get(self, property: str) -> Union['None', 'CSSStyleValue']: ...

    def getAll(self, property: str) -> Sequence[CSSStyleValue]: ...

    def has(self, property: str) -> bool: ...
    size: int

class StylePropertyMap(StylePropertyMapReadOnly):

    def set(self, property: str, *values: Union['CSSStyleValue', 'str']) -> None: ...

    def append(self, property: str, *values: Union['CSSStyleValue', 'str']) -> None: ...

    def delete(self, property: str) -> None: ...

    def clear(self) -> None: ...

class CSSUnparsedValue(CSSStyleValue):
    @classmethod
    def new(cls, members: Sequence[CSSUnparsedSegment]) -> CSSUnparsedValue: ...
    length: int

    def __getter__(self, index: int) -> CSSUnparsedSegment: ...

    def __setter__(self, index: int, val: CSSUnparsedSegment) -> CSSUnparsedSegment: ...

class CSSVariableReferenceValue:
    @classmethod
    def new(cls, variable: str, fallback: Union['CSSUnparsedValue', 'None'] = None) -> CSSVariableReferenceValue: ...
    variable: str
    fallback: Union['CSSUnparsedValue', 'None']

class CSSKeywordValue(CSSStyleValue):
    @classmethod
    def new(cls, value: str) -> CSSKeywordValue: ...
    value: str

class CSSNumericType(TypedDict):
    length: NotRequired[int]
    angle: NotRequired[int]
    time: NotRequired[int]
    frequency: NotRequired[int]
    resolution: NotRequired[int]
    flex: NotRequired[int]
    percent: NotRequired[int]
    percentHint: NotRequired[CSSNumericBaseType]

class CSSNumericValue(CSSStyleValue):

    def add(self, *values: CSSNumberish) -> CSSNumericValue: ...

    def sub(self, *values: CSSNumberish) -> CSSNumericValue: ...

    def mul(self, *values: CSSNumberish) -> CSSNumericValue: ...

    def div(self, *values: CSSNumberish) -> CSSNumericValue: ...

    def min(self, *values: CSSNumberish) -> CSSNumericValue: ...

    def max(self, *values: CSSNumberish) -> CSSNumericValue: ...

    def equals(self, *value: CSSNumberish) -> bool: ...

    def to(self, unit: str) -> CSSUnitValue: ...

    def toSum(self, *units: str) -> CSSMathSum: ...

    def type(self) -> CSSNumericType: ...

class CSSUnitValue(CSSNumericValue):
    @classmethod
    def new(cls, value: float, unit: str) -> CSSUnitValue: ...
    value: float
    unit: str

class CSSMathValue(CSSNumericValue):
    operator: CSSMathOperator

class CSSMathSum(CSSMathValue):
    @classmethod
    def new(cls, *args: CSSNumberish) -> CSSMathSum: ...
    values: CSSNumericArray

class CSSMathProduct(CSSMathValue):
    @classmethod
    def new(cls, *args: CSSNumberish) -> CSSMathProduct: ...
    values: CSSNumericArray

class CSSMathNegate(CSSMathValue):
    @classmethod
    def new(cls, arg: CSSNumberish) -> CSSMathNegate: ...
    value: CSSNumericValue

class CSSMathInvert(CSSMathValue):
    @classmethod
    def new(cls, arg: CSSNumberish) -> CSSMathInvert: ...
    value: CSSNumericValue

class CSSMathMin(CSSMathValue):
    @classmethod
    def new(cls, *args: CSSNumberish) -> CSSMathMin: ...
    values: CSSNumericArray

class CSSMathMax(CSSMathValue):
    @classmethod
    def new(cls, *args: CSSNumberish) -> CSSMathMax: ...
    values: CSSNumericArray

class CSSMathClamp(CSSMathValue):
    @classmethod
    def new(cls, lower: CSSNumberish, value: CSSNumberish, upper: CSSNumberish) -> CSSMathClamp: ...
    lower: CSSNumericValue
    value: CSSNumericValue
    upper: CSSNumericValue

class CSSNumericArray:
    length: int

    def __getter__(self, index: int) -> CSSNumericValue: ...

class CSSTransformValue(CSSStyleValue):
    @classmethod
    def new(cls, transforms: Sequence[CSSTransformComponent]) -> CSSTransformValue: ...
    length: int

    def __getter__(self, index: int) -> CSSTransformComponent: ...

    def __setter__(self, index: int, val: CSSTransformComponent) -> CSSTransformComponent: ...
    is2D: bool

    def toMatrix(self) -> DOMMatrix: ...

class CSSTransformComponent:
    is2D: bool

    def toMatrix(self) -> DOMMatrix: ...

class CSSTranslate(CSSTransformComponent):
    @classmethod
    def new(cls, x: CSSNumericValue, y: CSSNumericValue, z: Union['CSSNumericValue', 'None'] = None) -> CSSTranslate: ...
    x: CSSNumericValue
    y: CSSNumericValue
    z: CSSNumericValue

class CSSRotate(CSSTransformComponent):
    @overload
    @classmethod
    def new(cls, angle: CSSNumericValue) -> CSSRotate: ...
    @overload
    @classmethod
    def new(cls, x: CSSNumberish, y: CSSNumberish, z: CSSNumberish, angle: CSSNumericValue) -> CSSRotate: ...
    x: CSSNumberish
    y: CSSNumberish
    z: CSSNumberish
    angle: CSSNumericValue

class CSSScale(CSSTransformComponent):
    @classmethod
    def new(cls, x: CSSNumberish, y: CSSNumberish, z: Union['CSSNumberish', 'None'] = None) -> CSSScale: ...
    x: CSSNumberish
    y: CSSNumberish
    z: CSSNumberish

class CSSSkew(CSSTransformComponent):
    @classmethod
    def new(cls, ax: CSSNumericValue, ay: CSSNumericValue) -> CSSSkew: ...
    ax: CSSNumericValue
    ay: CSSNumericValue

class CSSSkewX(CSSTransformComponent):
    @classmethod
    def new(cls, ax: CSSNumericValue) -> CSSSkewX: ...
    ax: CSSNumericValue

class CSSSkewY(CSSTransformComponent):
    @classmethod
    def new(cls, ay: CSSNumericValue) -> CSSSkewY: ...
    ay: CSSNumericValue

class CSSPerspective(CSSTransformComponent):
    @classmethod
    def new(cls, length: CSSPerspectiveValue) -> CSSPerspective: ...
    length: CSSPerspectiveValue

class CSSMatrixComponent(CSSTransformComponent):
    @classmethod
    def new(cls, matrix: DOMMatrixReadOnly, options: Union['CSSMatrixComponentOptions', 'None'] = {}) -> CSSMatrixComponent: ...
    matrix: DOMMatrix

class CSSMatrixComponentOptions(TypedDict):
    is2D: NotRequired[bool]

class CSSImageValue(CSSStyleValue): ...

class CSSColorValue(CSSStyleValue): ...

class CSSRGB(CSSColorValue):
    @classmethod
    def new(cls, r: CSSColorRGBComp, g: CSSColorRGBComp, b: CSSColorRGBComp, alpha: Union['CSSColorPercent', 'None'] = 1) -> CSSRGB: ...
    r: CSSColorRGBComp
    g: CSSColorRGBComp
    b: CSSColorRGBComp
    alpha: CSSColorPercent

class CSSHSL(CSSColorValue):
    @classmethod
    def new(cls, h: CSSColorAngle, s: CSSColorPercent, l: CSSColorPercent, alpha: Union['CSSColorPercent', 'None'] = 1) -> CSSHSL: ...
    h: CSSColorAngle
    s: CSSColorPercent
    l: CSSColorPercent
    alpha: CSSColorPercent

class CSSHWB(CSSColorValue):
    @classmethod
    def new(cls, h: CSSNumericValue, w: CSSNumberish, b: CSSNumberish, alpha: Union['CSSNumberish', 'None'] = 1) -> CSSHWB: ...
    h: CSSNumericValue
    w: CSSNumberish
    b: CSSNumberish
    alpha: CSSNumberish

class CSSLab(CSSColorValue):
    @classmethod
    def new(cls, l: CSSColorPercent, a: CSSColorNumber, b: CSSColorNumber, alpha: Union['CSSColorPercent', 'None'] = 1) -> CSSLab: ...
    l: CSSColorPercent
    a: CSSColorNumber
    b: CSSColorNumber
    alpha: CSSColorPercent

class CSSLCH(CSSColorValue):
    @classmethod
    def new(cls, l: CSSColorPercent, c: CSSColorPercent, h: CSSColorAngle, alpha: Union['CSSColorPercent', 'None'] = 1) -> CSSLCH: ...
    l: CSSColorPercent
    c: CSSColorPercent
    h: CSSColorAngle
    alpha: CSSColorPercent

class CSSOKLab(CSSColorValue):
    @classmethod
    def new(cls, l: CSSColorPercent, a: CSSColorNumber, b: CSSColorNumber, alpha: Union['CSSColorPercent', 'None'] = 1) -> CSSOKLab: ...
    l: CSSColorPercent
    a: CSSColorNumber
    b: CSSColorNumber
    alpha: CSSColorPercent

class CSSOKLCH(CSSColorValue):
    @classmethod
    def new(cls, l: CSSColorPercent, c: CSSColorPercent, h: CSSColorAngle, alpha: Union['CSSColorPercent', 'None'] = 1) -> CSSOKLCH: ...
    l: CSSColorPercent
    c: CSSColorPercent
    h: CSSColorAngle
    alpha: CSSColorPercent

class CSSColor(CSSColorValue):
    @classmethod
    def new(cls, colorSpace: CSSKeywordish, channels: Sequence[CSSColorPercent], alpha: Union['CSSNumberish', 'None'] = 1) -> CSSColor: ...
    colorSpace: CSSKeywordish
    channels: Sequence[CSSColorPercent]
    alpha: CSSNumberish

class ViewTransition:
    updateCallbackDone: Awaitable[None]
    ready: Awaitable[None]
    finished: Awaitable[None]

    def skipTransition(self) -> None: ...

class ScrollOptions(TypedDict):
    behavior: NotRequired[ScrollBehavior]

class ScrollToOptions(ScrollOptions):
    left: NotRequired[float]
    top: NotRequired[float]

class MediaQueryList(EventTarget):
    media: str
    matches: bool

    def addListener(self, callback: Union['EventListener', 'None']) -> None: ...

    def removeListener(self, callback: Union['EventListener', 'None']) -> None: ...
    onchange: EventHandler

class MediaQueryListEvent(Event):
    @classmethod
    def new(cls, type: str, eventInitDict: Union['MediaQueryListEventInit', 'None'] = {}) -> MediaQueryListEvent: ...
    media: str
    matches: bool

class MediaQueryListEventInit(EventInit):
    media: NotRequired[str]
    matches: NotRequired[bool]

class Screen:
    availWidth: int
    availHeight: int
    width: int
    height: int
    colorDepth: int
    pixelDepth: int
    orientation: ScreenOrientation
    isExtended: bool
    onchange: EventHandler

class CaretPosition:
    offsetNode: Node
    offset: int

    def getClientRect(self) -> Union['DOMRect', 'None']: ...

class ScrollIntoViewOptions(ScrollOptions):
    block: NotRequired[ScrollLogicalPosition]
    inline: NotRequired[ScrollLogicalPosition]

class CheckVisibilityOptions(TypedDict):
    checkOpacity: NotRequired[bool]
    checkVisibilityCSS: NotRequired[bool]

class HTMLElement(Element, ElementCSSInlineStyle, GlobalEventHandlers, ElementContentEditable, HTMLOrSVGElement):
    @classmethod
    def new(cls) -> HTMLElement: ...
    offsetParent: Union['Element', 'None']
    offsetTop: int
    offsetLeft: int
    offsetWidth: int
    offsetHeight: int
    editContext: Union['EditContext', 'None']
    title: str
    lang: str
    translate: bool
    dir: str
    hidden: Union['bool', 'float', 'str', 'None']
    inert: bool

    def click(self) -> None: ...
    accessKey: str
    accessKeyLabel: str
    draggable: bool
    spellcheck: bool
    autocapitalize: str
    innerText: str
    outerText: str

    def attachInternals(self) -> ElementInternals: ...

    def showPopover(self) -> None: ...

    def hidePopover(self) -> None: ...

    def togglePopover(self, force: Union['bool', 'None'] = None) -> bool: ...
    popover: Union['str', 'None']

class MouseEvent(UIEvent):
    @classmethod
    def new(cls, type: str, eventInitDict: Union['MouseEventInit', 'None'] = {}) -> MouseEvent: ...
    pageX: float
    pageY: float
    x: float
    y: float
    offsetX: float
    offsetY: float
    movementX: float
    movementY: float
    screenX: int
    screenY: int
    clientX: int
    clientY: int
    ctrlKey: bool
    shiftKey: bool
    altKey: bool
    metaKey: bool
    button: int
    buttons: int
    relatedTarget: Union['EventTarget', 'None']

    def getModifierState(self, keyArg: str) -> bool: ...

    def initMouseEvent(self, typeArg: str, bubblesArg: Union['bool', 'None'] = False, cancelableArg: Union['bool', 'None'] = False, viewArg: Union['Window', 'None'] = None, detailArg: Union['int', 'None'] = 0, screenXArg: Union['int', 'None'] = 0, screenYArg: Union['int', 'None'] = 0, clientXArg: Union['int', 'None'] = 0, clientYArg: Union['int', 'None'] = 0, ctrlKeyArg: Union['bool', 'None'] = False, altKeyArg: Union['bool', 'None'] = False, shiftKeyArg: Union['bool', 'None'] = False, metaKeyArg: Union['bool', 'None'] = False, buttonArg: Union['int', 'None'] = 0, relatedTargetArg: Union['EventTarget', 'None'] = None) -> None: ...

class BoxQuadOptions(TypedDict):
    box: NotRequired[CSSBoxType]
    relativeTo: NotRequired[GeometryNode]

class ConvertCoordinateOptions(TypedDict):
    fromBox: NotRequired[CSSBoxType]
    toBox: NotRequired[CSSBoxType]

class GeometryUtils:

    def getBoxQuads(self, options: Union['BoxQuadOptions', 'None'] = {}) -> Sequence[DOMQuad]: ...

    def convertQuadFromNode(self, quad: DOMQuadInit, from_: GeometryNode, options: Union['ConvertCoordinateOptions', 'None'] = {}) -> DOMQuad: ...

    def convertRectFromNode(self, rect: DOMRectReadOnly, from_: GeometryNode, options: Union['ConvertCoordinateOptions', 'None'] = {}) -> DOMQuad: ...

    def convertPointFromNode(self, point: DOMPointInit, from_: GeometryNode, options: Union['ConvertCoordinateOptions', 'None'] = {}) -> DOMPoint: ...

class Text(CharacterData, GeometryUtils, Slottable):
    @classmethod
    def new(cls, data: Union['str', 'None'] = "") -> Text: ...

    def splitText(self, offset: int) -> Text: ...
    wholeText: str

class VisualViewport(EventTarget):
    offsetLeft: float
    offsetTop: float
    pageLeft: float
    pageTop: float
    width: float
    height: float
    scale: float
    onresize: EventHandler
    onscroll: EventHandler
    onscrollend: EventHandler

class CSSStyleSheet(StyleSheet):
    @classmethod
    def new(cls, options: Union['CSSStyleSheetInit', 'None'] = {}) -> CSSStyleSheet: ...
    ownerRule: Union['CSSRule', 'None']
    cssRules: CSSRuleList

    def insertRule(self, rule: str, index: Union['int', 'None'] = 0) -> int: ...

    def deleteRule(self, index: int) -> None: ...

    def replace(self, text: str) -> Awaitable[CSSStyleSheet]: ...

    def replaceSync(self, text: str) -> None: ...
    rules: CSSRuleList

    def addRule(self, selector: Union['str', 'None'] = "undefined", style: Union['str', 'None'] = "undefined", index: Union['int', 'None'] = None) -> int: ...

    def removeRule(self, index: Union['int', 'None'] = 0) -> None: ...

class CSSStyleSheetInit(TypedDict):
    baseURL: NotRequired[str]
    media: NotRequired[Union['MediaList', 'str']]
    disabled: NotRequired[bool]

class DocumentOrShadowRoot:
    styleSheets: StyleSheetList
    adoptedStyleSheets: Sequence[CSSStyleSheet]
    fullscreenElement: Union['Element', 'None']
    activeElement: Union['Element', 'None']
    pictureInPictureElement: Union['Element', 'None']
    pointerLockElement: Union['Element', 'None']

    def getAnimations(self) -> Sequence[Animation]: ...

class ProcessingInstruction(CharacterData, LinkStyle):
    target: str

class CSSImportRule(CSSRule):
    href: str
    media: MediaList
    styleSheet: Union['CSSStyleSheet', 'None']
    layerName: Union['str', 'None']
    supportsText: Union['str', 'None']

class CSSGroupingRule(CSSRule):
    cssRules: CSSRuleList

    def insertRule(self, rule: str, index: Union['int', 'None'] = 0) -> int: ...

    def deleteRule(self, index: int) -> None: ...

class CSSMarginRule(CSSRule):
    name: str
    style: CSSStyleDeclaration

class CSSNamespaceRule(CSSRule):
    namespaceURI: str
    prefix: str

class MathMLElement(Element, ElementCSSInlineStyle, GlobalEventHandlers, HTMLOrSVGElement): ...

class ElementInternals(ARIAMixin):
    states: CustomStateSet
    shadowRoot: Union['ShadowRoot', 'None']

    def setFormValue(self, value: Union['File', 'str', 'FormData', 'None'], state: Union['File', 'str', 'FormData', 'None'] = None) -> None: ...
    form: Union['HTMLFormElement', 'None']

    def setValidity(self, flags: Union['ValidityStateFlags', 'None'] = {}, message: Union['str', 'None'] = None, anchor: Union['HTMLElement', 'None'] = None) -> None: ...
    willValidate: bool
    validity: ValidityState
    validationMessage: str

    def checkValidity(self) -> bool: ...

    def reportValidity(self) -> bool: ...
    labels: NodeList

class CustomStateSet:

    def add(self, value: str) -> None: ...

class DataCue(TextTrackCue):
    @classmethod
    def new(cls, startTime: float, endTime: float, value: Any, type: Union['str', 'None'] = None) -> DataCue: ...
    value: Any
    type: str

class DeprecationReportBody(ReportBody):

    def toJSON(self) -> object: ...
    id: str
    anticipatedRemoval: Union['object', 'None']
    message: str
    sourceFile: Union['str', 'None']
    lineNumber: Union['int', 'None']
    columnNumber: Union['int', 'None']

class NavigatorDeviceMemory:
    deviceMemory: float

class DevicePosture(EventTarget):
    type: DevicePostureType
    onchange: EventHandler

class DigitalGoodsService:

    def getDetails(self, itemIds: Sequence[str]) -> Awaitable[Sequence[ItemDetails]]: ...

    def listPurchases(self) -> Awaitable[Sequence[PurchaseDetails]]: ...

    def listPurchaseHistory(self) -> Awaitable[Sequence[PurchaseDetails]]: ...

    def consume(self, purchaseToken: str) -> Awaitable[None]: ...

class ItemDetails(TypedDict):
    itemId: str
    title: str
    price: PaymentCurrencyAmount
    type: NotRequired[ItemType]
    description: NotRequired[str]
    iconURLs: NotRequired[Sequence[str]]
    subscriptionPeriod: NotRequired[str]
    freeTrialPeriod: NotRequired[str]
    introductoryPrice: NotRequired[PaymentCurrencyAmount]
    introductoryPricePeriod: NotRequired[str]
    introductoryPriceCycles: NotRequired[int]

class PurchaseDetails(TypedDict):
    itemId: str
    purchaseToken: str

class TCPSocket:
    @classmethod
    def new(cls, remoteAddress: str, remotePort: int, options: Union['TCPSocketOptions', 'None'] = {}) -> TCPSocket: ...
    opened: Awaitable[TCPSocketOpenInfo]
    closed: Awaitable[None]

    def close(self) -> Awaitable[None]: ...

class TCPSocketOptions(TypedDict):
    sendBufferSize: NotRequired[int]
    receiveBufferSize: NotRequired[int]
    noDelay: NotRequired[bool]
    keepAliveDelay: NotRequired[int]
    dnsQueryType: NotRequired[SocketDnsQueryType]

class TCPSocketOpenInfo(TypedDict):
    readable: NotRequired[ReadableStream]
    writable: NotRequired[WritableStream]
    remoteAddress: NotRequired[str]
    remotePort: NotRequired[int]
    localAddress: NotRequired[str]
    localPort: NotRequired[int]

class UDPSocket:
    @classmethod
    def new(cls, options: Union['UDPSocketOptions', 'None'] = {}) -> UDPSocket: ...
    opened: Awaitable[UDPSocketOpenInfo]
    closed: Awaitable[None]

    def close(self) -> Awaitable[None]: ...

class UDPSocketOptions(TypedDict):
    remoteAddress: NotRequired[str]
    remotePort: NotRequired[int]
    localAddress: NotRequired[str]
    localPort: NotRequired[int]
    sendBufferSize: NotRequired[int]
    receiveBufferSize: NotRequired[int]
    dnsQueryType: NotRequired[SocketDnsQueryType]
    ipv6Only: NotRequired[bool]

class UDPMessage(TypedDict):
    data: NotRequired[BufferSource]
    remoteAddress: NotRequired[str]
    remotePort: NotRequired[int]
    dnsQueryType: NotRequired[SocketDnsQueryType]

class UDPSocketOpenInfo(TypedDict):
    readable: NotRequired[ReadableStream]
    writable: NotRequired[WritableStream]
    remoteAddress: NotRequired[str]
    remotePort: NotRequired[int]
    localAddress: NotRequired[str]
    localPort: NotRequired[int]

class TCPServerSocket:
    @classmethod
    def new(cls, localAddress: str, options: Union['TCPServerSocketOptions', 'None'] = {}) -> TCPServerSocket: ...
    opened: Awaitable[TCPServerSocketOpenInfo]
    closed: Awaitable[None]

    def close(self) -> Awaitable[None]: ...

class TCPServerSocketOptions(TypedDict):
    localPort: NotRequired[int]
    backlog: NotRequired[int]
    ipv6Only: NotRequired[bool]

class TCPServerSocketOpenInfo(TypedDict):
    readable: NotRequired[ReadableStream]
    localAddress: NotRequired[str]
    localPort: NotRequired[int]

class DocumentPictureInPicture(EventTarget):

    def requestWindow(self, options: Union['DocumentPictureInPictureOptions', 'None'] = {}) -> Awaitable[Window]: ...
    window: Window
    onenter: EventHandler

class DocumentPictureInPictureOptions(TypedDict):
    width: NotRequired[int]
    height: NotRequired[int]

class DocumentPictureInPictureEvent(Event):
    @classmethod
    def new(cls, type: str, eventInitDict: DocumentPictureInPictureEventInit) -> DocumentPictureInPictureEvent: ...
    window: Window

class DocumentPictureInPictureEventInit(EventInit):
    window: Window

class Event:
    @classmethod
    def new(cls, type: str, eventInitDict: Union['EventInit', 'None'] = {}) -> Event: ...
    type: str
    target: Union['EventTarget', 'None']
    srcElement: Union['EventTarget', 'None']
    currentTarget: Union['EventTarget', 'None']

    def composedPath(self) -> Sequence[EventTarget]: ...
    NONE = 0
    CAPTURING_PHASE = 1
    AT_TARGET = 2
    BUBBLING_PHASE = 3
    eventPhase: int

    def stopPropagation(self) -> None: ...
    cancelBubble: bool

    def stopImmediatePropagation(self) -> None: ...
    bubbles: bool
    cancelable: bool
    returnValue: bool

    def preventDefault(self) -> None: ...
    defaultPrevented: bool
    composed: bool
    isTrusted: bool
    timeStamp: DOMHighResTimeStamp

    def initEvent(self, type: str, bubbles: Union['bool', 'None'] = False, cancelable: Union['bool', 'None'] = False) -> None: ...

class EventInit(TypedDict):
    bubbles: NotRequired[bool]
    cancelable: NotRequired[bool]
    composed: NotRequired[bool]

class CustomEvent(Event):
    @classmethod
    def new(cls, type: str, eventInitDict: Union['CustomEventInit', 'None'] = {}) -> CustomEvent: ...
    detail: Any

    def initCustomEvent(self, type: str, bubbles: Union['bool', 'None'] = False, cancelable: Union['bool', 'None'] = False, detail: Union['Any', 'None'] = None) -> None: ...

class CustomEventInit(EventInit):
    detail: NotRequired[Any]

class EventTarget:
    @classmethod
    def new(cls) -> EventTarget: ...

    def addEventListener(self, type: str, callback: Union['EventListener', 'None'], options: Union['AddEventListenerOptions', 'bool', 'None'] = {}) -> None: ...

    def removeEventListener(self, type: str, callback: Union['EventListener', 'None'], options: Union['EventListenerOptions', 'bool', 'None'] = {}) -> None: ...

    def dispatchEvent(self, event: Event) -> bool: ...

class EventListenerOptions(TypedDict):
    capture: NotRequired[bool]

class AddEventListenerOptions(EventListenerOptions):
    passive: NotRequired[bool]
    once: NotRequired[bool]
    signal: NotRequired[AbortSignal]

class AbortController:
    @classmethod
    def new(cls) -> AbortController: ...
    signal: AbortSignal

    def abort(self, reason: Union['Any', 'None'] = None) -> None: ...

class AbortSignal(EventTarget):
    aborted: bool
    reason: Any

    def throwIfAborted(self) -> None: ...
    onabort: EventHandler

class NonElementParentNode:

    def getElementById(self, elementId: str) -> Union['Element', 'None']: ...

class DocumentFragment(Node, NonElementParentNode, ParentNode):
    @classmethod
    def new(cls) -> DocumentFragment: ...

class ParentNode:
    children: HTMLCollection
    firstElementChild: Union['Element', 'None']
    lastElementChild: Union['Element', 'None']
    childElementCount: int

    def prepend(self, *nodes: Union['Node', 'str']) -> None: ...

    def append(self, *nodes: Union['Node', 'str']) -> None: ...

    def replaceChildren(self, *nodes: Union['Node', 'str']) -> None: ...

    def querySelector(self, selectors: str) -> Union['Element', 'None']: ...

    def querySelectorAll(self, selectors: str) -> NodeList: ...

class NonDocumentTypeChildNode:
    previousElementSibling: Union['Element', 'None']
    nextElementSibling: Union['Element', 'None']

class CharacterData(Node, NonDocumentTypeChildNode, ChildNode):
    data: str
    length: int

    def substringData(self, offset: int, count: int) -> str: ...

    def appendData(self, data: str) -> None: ...

    def insertData(self, offset: int, data: str) -> None: ...

    def deleteData(self, offset: int, count: int) -> None: ...

    def replaceData(self, offset: int, count: int, data: str) -> None: ...

class ChildNode:

    def before(self, *nodes: Union['Node', 'str']) -> None: ...

    def after(self, *nodes: Union['Node', 'str']) -> None: ...

    def replaceWith(self, *nodes: Union['Node', 'str']) -> None: ...

    def remove(self) -> None: ...

class DocumentType(Node, ChildNode):
    name: str
    publicId: str
    systemId: str

class Slottable:
    assignedSlot: Union['HTMLSlotElement', 'None']

class NodeList:

    def item(self, index: int) -> Union['Node', 'None']: ...
    length: int

class HTMLCollection:
    length: int

    def item(self, index: int) -> Union['Element', 'None']: ...

    def namedItem(self, name: str) -> Union['Element', 'None']: ...

class MutationObserver:
    @classmethod
    def new(cls, callback: MutationCallback) -> MutationObserver: ...

    def observe(self, target: Node, options: Union['MutationObserverInit', 'None'] = {}) -> None: ...

    def disconnect(self) -> None: ...

    def takeRecords(self) -> Sequence[MutationRecord]: ...

class MutationObserverInit(TypedDict):
    childList: NotRequired[bool]
    attributes: NotRequired[bool]
    characterData: NotRequired[bool]
    subtree: NotRequired[bool]
    attributeOldValue: NotRequired[bool]
    characterDataOldValue: NotRequired[bool]
    attributeFilter: NotRequired[Sequence[str]]

class MutationRecord:
    type: str
    target: Node
    addedNodes: NodeList
    removedNodes: NodeList
    previousSibling: Union['Node', 'None']
    nextSibling: Union['Node', 'None']
    attributeName: Union['str', 'None']
    attributeNamespace: Union['str', 'None']
    oldValue: Union['str', 'None']

class Node(EventTarget):
    ELEMENT_NODE = 1
    ATTRIBUTE_NODE = 2
    TEXT_NODE = 3
    CDATA_SECTION_NODE = 4
    ENTITY_REFERENCE_NODE = 5
    ENTITY_NODE = 6
    PROCESSING_INSTRUCTION_NODE = 7
    COMMENT_NODE = 8
    DOCUMENT_NODE = 9
    DOCUMENT_TYPE_NODE = 10
    DOCUMENT_FRAGMENT_NODE = 11
    NOTATION_NODE = 12
    nodeType: int
    nodeName: str
    baseURI: str
    isConnected: bool
    ownerDocument: Union['Document', 'None']

    def getRootNode(self, options: Union['GetRootNodeOptions', 'None'] = {}) -> Node: ...
    parentNode: Union['Node', 'None']
    parentElement: Union['Element', 'None']

    def hasChildNodes(self) -> bool: ...
    childNodes: NodeList
    firstChild: Union['Node', 'None']
    lastChild: Union['Node', 'None']
    previousSibling: Union['Node', 'None']
    nextSibling: Union['Node', 'None']
    nodeValue: Union['str', 'None']
    textContent: Union['str', 'None']

    def normalize(self) -> None: ...

    def cloneNode(self, deep: Union['bool', 'None'] = False) -> Node: ...

    def isEqualNode(self, otherNode: Union['Node', 'None']) -> bool: ...

    def isSameNode(self, otherNode: Union['Node', 'None']) -> bool: ...
    DOCUMENT_POSITION_DISCONNECTED = 0x01
    DOCUMENT_POSITION_PRECEDING = 0x02
    DOCUMENT_POSITION_FOLLOWING = 0x04
    DOCUMENT_POSITION_CONTAINS = 0x08
    DOCUMENT_POSITION_CONTAINED_BY = 0x10
    DOCUMENT_POSITION_IMPLEMENTATION_SPECIFIC = 0x20

    def compareDocumentPosition(self, other: Node) -> int: ...

    def contains(self, other: Union['Node', 'None']) -> bool: ...

    def lookupPrefix(self, namespace: Union['str', 'None']) -> Union['str', 'None']: ...

    def lookupNamespaceURI(self, prefix: Union['str', 'None']) -> Union['str', 'None']: ...

    def isDefaultNamespace(self, namespace: Union['str', 'None']) -> bool: ...

    def insertBefore(self, node: Node, child: Union['Node', 'None']) -> Node: ...

    def appendChild(self, node: Node) -> Node: ...

    def replaceChild(self, node: Node, child: Node) -> Node: ...

    def removeChild(self, child: Node) -> Node: ...

class GetRootNodeOptions(TypedDict):
    composed: NotRequired[bool]

class XMLDocument(Document): ...

class ElementCreationOptions(TypedDict): ...

class DOMImplementation:

    def createDocumentType(self, qualifiedName: str, publicId: str, systemId: str) -> DocumentType: ...

    def createDocument(self, namespace: Union['str', 'None'], qualifiedName: str, doctype: Union['DocumentType', 'None'] = None) -> XMLDocument: ...

    def createHTMLDocument(self, title: Union['str', 'None'] = None) -> Document: ...

    def hasFeature(self) -> bool: ...

class ShadowRootInit(TypedDict):
    mode: ShadowRootMode
    delegatesFocus: NotRequired[bool]
    slotAssignment: NotRequired[SlotAssignmentMode]

class NamedNodeMap:
    length: int

    def item(self, index: int) -> Union['Attr', 'None']: ...

    def getNamedItem(self, qualifiedName: str) -> Union['Attr', 'None']: ...

    def getNamedItemNS(self, namespace: Union['str', 'None'], localName: str) -> Union['Attr', 'None']: ...

    def setNamedItem(self, attr: Attr) -> Union['Attr', 'None']: ...

    def setNamedItemNS(self, attr: Attr) -> Union['Attr', 'None']: ...

    def removeNamedItem(self, qualifiedName: str) -> Attr: ...

    def removeNamedItemNS(self, namespace: Union['str', 'None'], localName: str) -> Attr: ...

class Attr(Node):
    namespaceURI: Union['str', 'None']
    prefix: Union['str', 'None']
    localName: str
    name: str
    value: str
    ownerElement: Union['Element', 'None']
    specified: bool

class CDATASection(Text): ...

class Comment(CharacterData):
    @classmethod
    def new(cls, data: Union['str', 'None'] = "") -> Comment: ...

class AbstractRange:
    startContainer: Node
    startOffset: int
    endContainer: Node
    endOffset: int
    collapsed: bool

class StaticRangeInit(TypedDict):
    startContainer: Node
    startOffset: int
    endContainer: Node
    endOffset: int

class StaticRange(AbstractRange):
    @classmethod
    def new(cls, init: StaticRangeInit) -> StaticRange: ...

class NodeIterator:
    root: Node
    referenceNode: Node
    pointerBeforeReferenceNode: bool
    whatToShow: int
    filter: Union['NodeFilter', 'None']

    def nextNode(self) -> Union['Node', 'None']: ...

    def previousNode(self) -> Union['Node', 'None']: ...

    def detach(self) -> None: ...

class TreeWalker:
    root: Node
    whatToShow: int
    filter: Union['NodeFilter', 'None']
    currentNode: Node

    def parentNode(self) -> Union['Node', 'None']: ...

    def firstChild(self) -> Union['Node', 'None']: ...

    def lastChild(self) -> Union['Node', 'None']: ...

    def previousSibling(self) -> Union['Node', 'None']: ...

    def nextSibling(self) -> Union['Node', 'None']: ...

    def previousNode(self) -> Union['Node', 'None']: ...

    def nextNode(self) -> Union['Node', 'None']: ...

class DOMTokenList:
    length: int

    def item(self, index: int) -> Union['str', 'None']: ...

    def contains(self, token: str) -> bool: ...

    def add(self, *tokens: str) -> None: ...

    def remove(self, *tokens: str) -> None: ...

    def toggle(self, token: str, force: Union['bool', 'None'] = None) -> bool: ...

    def replace(self, token: str, newToken: str) -> bool: ...

    def supports(self, token: str) -> bool: ...
    value: str

class XPathResult:
    ANY_TYPE = 0
    NUMBER_TYPE = 1
    STRING_TYPE = 2
    BOOLEAN_TYPE = 3
    UNORDERED_NODE_ITERATOR_TYPE = 4
    ORDERED_NODE_ITERATOR_TYPE = 5
    UNORDERED_NODE_SNAPSHOT_TYPE = 6
    ORDERED_NODE_SNAPSHOT_TYPE = 7
    ANY_UNORDERED_NODE_TYPE = 8
    FIRST_ORDERED_NODE_TYPE = 9
    resultType: int
    numberValue: float
    stringValue: str
    booleanValue: bool
    singleNodeValue: Union['Node', 'None']
    invalidIteratorState: bool
    snapshotLength: int

    def iterateNext(self) -> Union['Node', 'None']: ...

    def snapshotItem(self, index: int) -> Union['Node', 'None']: ...

class XPathExpression:

    def evaluate(self, contextNode: Node, type: Union['int', 'None'] = 0, result: Union['XPathResult', 'None'] = None) -> XPathResult: ...

class XPathEvaluatorBase:

    def createExpression(self, expression: str, resolver: Union['XPathNSResolver', 'None'] = None) -> XPathExpression: ...

    def createNSResolver(self, nodeResolver: Node) -> Node: ...

    def evaluate(self, expression: str, contextNode: Node, resolver: Union['XPathNSResolver', 'None'] = None, type: Union['int', 'None'] = 0, result: Union['XPathResult', 'None'] = None) -> XPathResult: ...

class XPathEvaluator(XPathEvaluatorBase):
    @classmethod
    def new(cls) -> XPathEvaluator: ...

class XSLTProcessor:
    @classmethod
    def new(cls) -> XSLTProcessor: ...

    def importStylesheet(self, style: Node) -> None: ...

    def transformToFragment(self, source: Node, output: Document) -> DocumentFragment: ...

    def transformToDocument(self, source: Node) -> Document: ...

    def setParameter(self, namespaceURI: str, localName: str, value: Any) -> None: ...

    def getParameter(self, namespaceURI: str, localName: str) -> Any: ...

    def removeParameter(self, namespaceURI: str, localName: str) -> None: ...

    def clearParameters(self) -> None: ...

    def reset(self) -> None: ...

class EditContextInit(TypedDict):
    text: NotRequired[str]
    selectionStart: NotRequired[int]
    selectionEnd: NotRequired[int]

class EditContext(EventTarget):
    @classmethod
    def new(cls, options: Union['EditContextInit', 'None'] = {}) -> EditContext: ...

    def updateText(self, rangeStart: int, rangeEnd: int, text: str) -> None: ...

    def updateSelection(self, start: int, end: int) -> None: ...

    def updateControlBounds(self, controlBounds: DOMRect) -> None: ...

    def updateSelectionBounds(self, selectionBounds: DOMRect) -> None: ...

    def updateCharacterBounds(self, rangeStart: int, characterBounds: Sequence[DOMRect]) -> None: ...

    def attachedElements(self) -> Sequence[Element]: ...
    text: str
    selectionStart: int
    selectionEnd: int
    compositionRangeStart: int
    compositionRangeEnd: int
    isComposing: bool
    controlBounds: DOMRect
    selectionBounds: DOMRect
    characterBoundsRangeStart: int

    def characterBounds(self) -> Sequence[DOMRect]: ...
    ontextupdate: EventHandler
    ontextformatupdate: EventHandler
    oncharacterboundsupdate: EventHandler
    oncompositionstart: EventHandler
    oncompositionend: EventHandler

class TextUpdateEventInit(EventInit):
    updateRangeStart: NotRequired[int]
    updateRangeEnd: NotRequired[int]
    text: NotRequired[str]
    selectionStart: NotRequired[int]
    selectionEnd: NotRequired[int]
    compositionStart: NotRequired[int]
    compositionEnd: NotRequired[int]

class TextUpdateEvent(Event):
    @classmethod
    def new(cls, type: str, options: Union['TextUpdateEventInit', 'None'] = {}) -> TextUpdateEvent: ...
    updateRangeStart: int
    updateRangeEnd: int
    text: str
    selectionStart: int
    selectionEnd: int
    compositionStart: int
    compositionEnd: int

class TextFormatInit(TypedDict):
    rangeStart: NotRequired[int]
    rangeEnd: NotRequired[int]
    underlineStyle: NotRequired[str]
    underlineThickness: NotRequired[str]

class TextFormat:
    @classmethod
    def new(cls, options: Union['TextFormatInit', 'None'] = {}) -> TextFormat: ...
    rangeStart: int
    rangeEnd: int
    underlineStyle: str
    underlineThickness: str

class TextFormatUpdateEventInit(EventInit):
    textFormats: NotRequired[Sequence[TextFormat]]

class TextFormatUpdateEvent(Event):
    @classmethod
    def new(cls, type: str, options: Union['TextFormatUpdateEventInit', 'None'] = {}) -> TextFormatUpdateEvent: ...

    def getTextFormats(self) -> Sequence[TextFormat]: ...

class CharacterBoundsUpdateEventInit(EventInit):
    rangeStart: NotRequired[int]
    rangeEnd: NotRequired[int]

class CharacterBoundsUpdateEvent(Event):
    @classmethod
    def new(cls, type: str, options: Union['CharacterBoundsUpdateEventInit', 'None'] = {}) -> CharacterBoundsUpdateEvent: ...
    rangeStart: int
    rangeEnd: int

class RestrictionTarget: ...

class BrowserCaptureMediaStreamTrack(MediaStreamTrack):

    def restrictTo(self, RestrictionTarget: Union['RestrictionTarget', 'None']) -> Awaitable[None]: ...

    def cropTo(self, cropTarget: Union['CropTarget', 'None']) -> Awaitable[None]: ...

    def clone(self) -> BrowserCaptureMediaStreamTrack: ...

class PerformanceElementTiming(PerformanceEntry):
    renderTime: DOMHighResTimeStamp
    loadTime: DOMHighResTimeStamp
    intersectionRect: DOMRectReadOnly
    identifier: str
    naturalWidth: int
    naturalHeight: int
    id: str
    element: Union['Element', 'None']
    url: str

    def toJSON(self) -> object: ...

class TextDecoderCommon:
    encoding: str
    fatal: bool
    ignoreBOM: bool

class TextDecoderOptions(TypedDict):
    fatal: NotRequired[bool]
    ignoreBOM: NotRequired[bool]

class TextDecodeOptions(TypedDict):
    stream: NotRequired[bool]

class TextDecoder(TextDecoderCommon):
    @classmethod
    def new(cls, label: Union['str', 'None'] = "utf-8", options: Union['TextDecoderOptions', 'None'] = {}) -> TextDecoder: ...

    def decode(self, input: Union['AllowSharedBufferSource', 'None'] = None, options: Union['TextDecodeOptions', 'None'] = {}) -> str: ...

class TextEncoderCommon:
    encoding: str

class TextEncoderEncodeIntoResult(TypedDict):
    read: NotRequired[int]
    written: NotRequired[int]

class TextEncoder(TextEncoderCommon):
    @classmethod
    def new(cls) -> TextEncoder: ...

    def encode(self, input: Union['str', 'None'] = "") -> Uint8Array: ...

    def encodeInto(self, source: str, destination: Uint8Array) -> TextEncoderEncodeIntoResult: ...

class TextDecoderStream(TextDecoderCommon, GenericTransformStream):
    @classmethod
    def new(cls, label: Union['str', 'None'] = "utf-8", options: Union['TextDecoderOptions', 'None'] = {}) -> TextDecoderStream: ...

class TextEncoderStream(TextEncoderCommon, GenericTransformStream):
    @classmethod
    def new(cls) -> TextEncoderStream: ...

class MediaKeySystemConfiguration(TypedDict):
    label: NotRequired[str]
    initDataTypes: NotRequired[Sequence[str]]
    audioCapabilities: NotRequired[Sequence[MediaKeySystemMediaCapability]]
    videoCapabilities: NotRequired[Sequence[MediaKeySystemMediaCapability]]
    distinctiveIdentifier: NotRequired[MediaKeysRequirement]
    persistentState: NotRequired[MediaKeysRequirement]
    sessionTypes: NotRequired[Sequence[str]]

class MediaKeySystemMediaCapability(TypedDict):
    contentType: NotRequired[str]
    encryptionScheme: NotRequired[Union['str', 'None']]
    robustness: NotRequired[str]

class MediaKeySystemAccess:
    keySystem: str

    def getConfiguration(self) -> MediaKeySystemConfiguration: ...

    def createMediaKeys(self) -> Awaitable[MediaKeys]: ...

class MediaKeys:

    def createSession(self, sessionType: Union['MediaKeySessionType', 'None'] = "temporary") -> MediaKeySession: ...

    def setServerCertificate(self, serverCertificate: BufferSource) -> Awaitable[bool]: ...

class MediaKeySession(EventTarget):
    sessionId: str
    expiration: float
    closed: Awaitable[MediaKeySessionClosedReason]
    keyStatuses: MediaKeyStatusMap
    onkeystatuseschange: EventHandler
    onmessage: EventHandler

    def generateRequest(self, initDataType: str, initData: BufferSource) -> Awaitable[None]: ...

    def load(self, sessionId: str) -> Awaitable[bool]: ...

    def update(self, response: BufferSource) -> Awaitable[None]: ...

    def close(self) -> Awaitable[None]: ...

    def remove(self) -> Awaitable[None]: ...

class MediaKeyStatusMap:
    size: int

    def has(self, keyId: BufferSource) -> bool: ...

    def get(self, keyId: BufferSource) -> Union['MediaKeyStatus', 'None']: ...

class MediaKeyMessageEvent(Event):
    @classmethod
    def new(cls, type: str, eventInitDict: MediaKeyMessageEventInit) -> MediaKeyMessageEvent: ...
    messageType: MediaKeyMessageType
    message: ArrayBuffer

class MediaKeyMessageEventInit(EventInit):
    messageType: MediaKeyMessageType
    message: ArrayBuffer

class MediaEncryptedEvent(Event):
    @classmethod
    def new(cls, type: str, eventInitDict: Union['MediaEncryptedEventInit', 'None'] = {}) -> MediaEncryptedEvent: ...
    initDataType: str
    initData: ArrayBuffer

class MediaEncryptedEventInit(EventInit):
    initDataType: NotRequired[str]
    initData: NotRequired[ArrayBuffer]

class HTMLInputElement(HTMLElement, PopoverInvokerElement):
    @classmethod
    def new(cls) -> HTMLInputElement: ...
    webkitdirectory: bool
    webkitEntries: Sequence[FileSystemEntry]
    capture: str
    accept: str
    alt: str
    autocomplete: str
    defaultChecked: bool
    checked: bool
    dirName: str
    disabled: bool
    form: Union['HTMLFormElement', 'None']
    files: Union['FileList', 'None']
    formAction: str
    formEnctype: str
    formMethod: str
    formNoValidate: bool
    formTarget: str
    height: int
    indeterminate: bool
    list: Union['HTMLDataListElement', 'None']
    max: str
    maxLength: int
    min: str
    minLength: int
    multiple: bool
    name: str
    pattern: str
    placeholder: str
    readOnly: bool
    required: bool
    size: int
    src: str
    step: str
    type: str
    defaultValue: str
    value: str
    valueAsDate: Union['object', 'None']
    valueAsNumber: float
    width: int

    def stepUp(self, n: Union['int', 'None'] = 1) -> None: ...

    def stepDown(self, n: Union['int', 'None'] = 1) -> None: ...
    willValidate: bool
    validity: ValidityState
    validationMessage: str

    def checkValidity(self) -> bool: ...

    def reportValidity(self) -> bool: ...

    def setCustomValidity(self, error: str) -> None: ...
    labels: Union['NodeList', 'None']

    def select(self) -> None: ...
    selectionStart: Union['int', 'None']
    selectionEnd: Union['int', 'None']
    selectionDirection: Union['str', 'None']
    @overload
    def setRangeText(self, replacement: str) -> None: ...
    @overload
    def setRangeText(self, replacement: str, start: int, end: int, selectionMode: Union['SelectionMode', 'None'] = "preserve") -> None: ...

    def setSelectionRange(self, start: int, end: int, direction: Union['str', 'None'] = None) -> None: ...

    def showPicker(self) -> None: ...
    align: str
    useMap: str

class DataTransferItem:

    def webkitGetAsEntry(self) -> Union['FileSystemEntry', 'None']: ...

    def getAsFileSystemHandle(self) -> Awaitable[Union['FileSystemHandle', 'None']]: ...
    kind: str
    type: str

    def getAsString(self, callback: Union['FunctionStringCallback', 'None']) -> None: ...

    def getAsFile(self) -> Union['File', 'None']: ...

class FileSystemEntry:
    isFile: bool
    isDirectory: bool
    name: str
    fullPath: str
    filesystem: FileSystem

    def getParent(self, successCallback: Union['FileSystemEntryCallback', 'None'] = None, errorCallback: Union['ErrorCallback', 'None'] = None) -> None: ...

class FileSystemDirectoryEntry(FileSystemEntry):

    def createReader(self) -> FileSystemDirectoryReader: ...

    def getFile(self, path: Union['str', 'None'] = None, options: Union['FileSystemFlags', 'None'] = {}, successCallback: Union['FileSystemEntryCallback', 'None'] = None, errorCallback: Union['ErrorCallback', 'None'] = None) -> None: ...

    def getDirectory(self, path: Union['str', 'None'] = None, options: Union['FileSystemFlags', 'None'] = {}, successCallback: Union['FileSystemEntryCallback', 'None'] = None, errorCallback: Union['ErrorCallback', 'None'] = None) -> None: ...

class FileSystemFlags(TypedDict):
    create: NotRequired[bool]
    exclusive: NotRequired[bool]

class FileSystemDirectoryReader:

    def readEntries(self, successCallback: FileSystemEntriesCallback, errorCallback: Union['ErrorCallback', 'None'] = None) -> None: ...

class FileSystemFileEntry(FileSystemEntry):

    def file(self, successCallback: FileCallback, errorCallback: Union['ErrorCallback', 'None'] = None) -> None: ...

class FileSystem:
    name: str
    root: FileSystemDirectoryEntry

class EpubReadingSystem:

    def hasFeature(self, feature: str, version: Union['str', 'None'] = None) -> bool: ...

class PerformanceEventTiming(PerformanceEntry):
    processingStart: DOMHighResTimeStamp
    processingEnd: DOMHighResTimeStamp
    cancelable: bool
    target: Union['Node', 'None']
    interactionId: int

    def toJSON(self) -> object: ...

class EventCounts: ...

class Performance(EventTarget):
    eventCounts: EventCounts
    interactionCount: int

    def now(self) -> DOMHighResTimeStamp: ...
    timeOrigin: DOMHighResTimeStamp

    def toJSON(self) -> object: ...
    timing: PerformanceTiming
    navigation: PerformanceNavigation

    def measureUserAgentSpecificMemory(self) -> Awaitable[MemoryMeasurement]: ...

    def getEntries(self) -> PerformanceEntryList: ...

    def getEntriesByType(self, type: str) -> PerformanceEntryList: ...

    def getEntriesByName(self, name: str, type: Union['str', 'None'] = None) -> PerformanceEntryList: ...

    def clearResourceTimings(self) -> None: ...

    def setResourceTimingBufferSize(self, maxSize: int) -> None: ...
    onresourcetimingbufferfull: EventHandler

    def mark(self, markName: str, markOptions: Union['PerformanceMarkOptions', 'None'] = {}) -> PerformanceMark: ...

    def clearMarks(self, markName: Union['str', 'None'] = None) -> None: ...

    def measure(self, measureName: str, startOrMeasureOptions: Union['str', 'PerformanceMeasureOptions', 'None'] = {}, endMark: Union['str', 'None'] = None) -> PerformanceMeasure: ...

    def clearMeasures(self, measureName: Union['str', 'None'] = None) -> None: ...

class PerformanceObserverInit(TypedDict):
    durationThreshold: NotRequired[DOMHighResTimeStamp]
    entryTypes: NotRequired[Sequence[str]]
    type: NotRequired[str]
    buffered: NotRequired[bool]

class ColorSelectionResult(TypedDict):
    sRGBHex: NotRequired[str]

class ColorSelectionOptions(TypedDict):
    signal: NotRequired[AbortSignal]

class EyeDropper:
    @classmethod
    def new(cls) -> EyeDropper: ...

    def open(self, options: Union['ColorSelectionOptions', 'None'] = {}) -> Awaitable[ColorSelectionResult]: ...

class HTMLFencedFrameElement(HTMLElement):
    @classmethod
    def new(cls) -> HTMLFencedFrameElement: ...
    config: Union['FencedFrameConfig', 'None']
    width: str
    height: str
    allow: str

class FencedFrameConfig:
    containerWidth: Union['FencedFrameConfigSize', 'None']
    containerHeight: Union['FencedFrameConfigSize', 'None']
    contentWidth: Union['FencedFrameConfigSize', 'None']
    contentHeight: Union['FencedFrameConfigSize', 'None']

    def setSharedStorageContext(self, contextString: str) -> None: ...

class FenceEvent(TypedDict):
    eventType: str
    eventData: str
    destination: Sequence[FenceReportingDestination]
    once: NotRequired[bool]

class Fence:

    def reportEvent(self, event: ReportEventType) -> None: ...

    def setReportEventDataForAutomaticBeacons(self, event: FenceEvent) -> None: ...

    def getNestedConfigs(self) -> Sequence[FencedFrameConfig]: ...

class Headers:
    @classmethod
    def new(cls, init: Union['HeadersInit', 'None'] = None) -> Headers: ...

    def append(self, name: ByteString, value: ByteString) -> None: ...

    def delete(self, name: ByteString) -> None: ...

    def get(self, name: ByteString) -> Union['ByteString', 'None']: ...

    def getSetCookie(self) -> Sequence[ByteString]: ...

    def has(self, name: ByteString) -> bool: ...

    def set(self, name: ByteString, value: ByteString) -> None: ...

class Body:
    body: Union['ReadableStream', 'None']
    bodyUsed: bool

    def arrayBuffer(self) -> Awaitable[ArrayBuffer]: ...

    def blob(self) -> Awaitable[Blob]: ...

    def formData(self) -> Awaitable[FormData]: ...

    def json(self) -> Awaitable[Any]: ...

    def text(self) -> Awaitable[str]: ...

class Request(Body):
    @classmethod
    def new(cls, input: RequestInfo, init: Union['RequestInit', 'None'] = {}) -> Request: ...
    method: ByteString
    url: str
    headers: Headers
    destination: RequestDestination
    referrer: str
    referrerPolicy: ReferrerPolicy
    mode: RequestMode
    credentials: RequestCredentials
    cache: RequestCache
    redirect: RequestRedirect
    integrity: str
    keepalive: bool
    isReloadNavigation: bool
    isHistoryNavigation: bool
    signal: AbortSignal
    duplex: RequestDuplex

    def clone(self) -> Request: ...

class Response(Body):
    @classmethod
    def new(cls, body: Union['BodyInit', 'None'] = None, init: Union['ResponseInit', 'None'] = {}) -> Response: ...
    type: ResponseType
    url: str
    redirected: bool
    status: int
    ok: bool
    statusText: ByteString
    headers: Headers

    def clone(self) -> Response: ...

class ResponseInit(TypedDict):
    status: NotRequired[int]
    statusText: NotRequired[ByteString]
    headers: NotRequired[HeadersInit]

class AuthenticationExtensionsClientInputs(TypedDict):
    credentialProtectionPolicy: NotRequired[str]
    enforceCredentialProtectionPolicy: NotRequired[bool]
    credBlob: NotRequired[ArrayBuffer]
    getCredBlob: NotRequired[bool]
    minPinLength: NotRequired[bool]
    hmacCreateSecret: NotRequired[bool]
    hmacGetSecret: NotRequired[HMACGetSecretInput]
    payment: NotRequired[AuthenticationExtensionsPaymentInputs]
    appid: NotRequired[str]
    appidExclude: NotRequired[str]
    credProps: NotRequired[bool]
    prf: NotRequired[AuthenticationExtensionsPRFInputs]
    largeBlob: NotRequired[AuthenticationExtensionsLargeBlobInputs]
    uvm: NotRequired[bool]
    devicePubKey: NotRequired[AuthenticationExtensionsDevicePublicKeyInputs]

class HMACGetSecretInput(TypedDict):
    salt1: ArrayBuffer
    salt2: NotRequired[ArrayBuffer]

class AuthenticationExtensionsClientOutputs(TypedDict):
    hmacCreateSecret: NotRequired[bool]
    hmacGetSecret: NotRequired[HMACGetSecretOutput]
    appid: NotRequired[bool]
    appidExclude: NotRequired[bool]
    credProps: NotRequired[CredentialPropertiesOutput]
    prf: NotRequired[AuthenticationExtensionsPRFOutputs]
    largeBlob: NotRequired[AuthenticationExtensionsLargeBlobOutputs]
    uvm: NotRequired[UvmEntries]
    devicePubKey: NotRequired[AuthenticationExtensionsDevicePublicKeyOutputs]

class HMACGetSecretOutput(TypedDict):
    output1: ArrayBuffer
    output2: NotRequired[ArrayBuffer]

class FileSystemPermissionDescriptor(PermissionDescriptor):
    handle: FileSystemHandle
    mode: NotRequired[FileSystemPermissionMode]

class FileSystemHandlePermissionDescriptor(TypedDict):
    mode: NotRequired[FileSystemPermissionMode]

class FileSystemHandle:

    def queryPermission(self, descriptor: Union['FileSystemHandlePermissionDescriptor', 'None'] = {}) -> Awaitable[PermissionState]: ...

    def requestPermission(self, descriptor: Union['FileSystemHandlePermissionDescriptor', 'None'] = {}) -> Awaitable[PermissionState]: ...
    kind: FileSystemHandleKind
    name: str

    def isSameEntry(self, other: FileSystemHandle) -> Awaitable[bool]: ...

class FilePickerAcceptType(TypedDict):
    description: NotRequired[str]
    accept: NotRequired[Union['str', 'Sequence[str]']]

class FilePickerOptions(TypedDict):
    types: NotRequired[Sequence[FilePickerAcceptType]]
    excludeAcceptAllOption: NotRequired[bool]
    id: NotRequired[str]
    startIn: NotRequired[StartInDirectory]

class OpenFilePickerOptions(FilePickerOptions):
    multiple: NotRequired[bool]

class SaveFilePickerOptions(FilePickerOptions):
    suggestedName: NotRequired[Union['str', 'None']]

class DirectoryPickerOptions(TypedDict):
    id: NotRequired[str]
    startIn: NotRequired[StartInDirectory]
    mode: NotRequired[FileSystemPermissionMode]

class SVGFilterElement(SVGElement, SVGURIReference):
    filterUnits: SVGAnimatedEnumeration
    primitiveUnits: SVGAnimatedEnumeration
    x: SVGAnimatedLength
    y: SVGAnimatedLength
    width: SVGAnimatedLength
    height: SVGAnimatedLength

class SVGFilterPrimitiveStandardAttributes:
    x: SVGAnimatedLength
    y: SVGAnimatedLength
    width: SVGAnimatedLength
    height: SVGAnimatedLength
    result: SVGAnimatedString

class SVGFEBlendElement(SVGElement, SVGFilterPrimitiveStandardAttributes):
    SVG_FEBLEND_MODE_UNKNOWN = 0
    SVG_FEBLEND_MODE_NORMAL = 1
    SVG_FEBLEND_MODE_MULTIPLY = 2
    SVG_FEBLEND_MODE_SCREEN = 3
    SVG_FEBLEND_MODE_DARKEN = 4
    SVG_FEBLEND_MODE_LIGHTEN = 5
    SVG_FEBLEND_MODE_OVERLAY = 6
    SVG_FEBLEND_MODE_COLOR_DODGE = 7
    SVG_FEBLEND_MODE_COLOR_BURN = 8
    SVG_FEBLEND_MODE_HARD_LIGHT = 9
    SVG_FEBLEND_MODE_SOFT_LIGHT = 10
    SVG_FEBLEND_MODE_DIFFERENCE = 11
    SVG_FEBLEND_MODE_EXCLUSION = 12
    SVG_FEBLEND_MODE_HUE = 13
    SVG_FEBLEND_MODE_SATURATION = 14
    SVG_FEBLEND_MODE_COLOR = 15
    SVG_FEBLEND_MODE_LUMINOSITY = 16
    in1: SVGAnimatedString
    in2: SVGAnimatedString
    mode: SVGAnimatedEnumeration

class SVGFEColorMatrixElement(SVGElement, SVGFilterPrimitiveStandardAttributes):
    SVG_FECOLORMATRIX_TYPE_UNKNOWN = 0
    SVG_FECOLORMATRIX_TYPE_MATRIX = 1
    SVG_FECOLORMATRIX_TYPE_SATURATE = 2
    SVG_FECOLORMATRIX_TYPE_HUEROTATE = 3
    SVG_FECOLORMATRIX_TYPE_LUMINANCETOALPHA = 4
    in1: SVGAnimatedString
    type: SVGAnimatedEnumeration
    values: SVGAnimatedNumberList

class SVGFEComponentTransferElement(SVGElement, SVGFilterPrimitiveStandardAttributes):
    in1: SVGAnimatedString

class SVGComponentTransferFunctionElement(SVGElement):
    SVG_FECOMPONENTTRANSFER_TYPE_UNKNOWN = 0
    SVG_FECOMPONENTTRANSFER_TYPE_IDENTITY = 1
    SVG_FECOMPONENTTRANSFER_TYPE_TABLE = 2
    SVG_FECOMPONENTTRANSFER_TYPE_DISCRETE = 3
    SVG_FECOMPONENTTRANSFER_TYPE_LINEAR = 4
    SVG_FECOMPONENTTRANSFER_TYPE_GAMMA = 5
    type: SVGAnimatedEnumeration
    tableValues: SVGAnimatedNumberList
    slope: SVGAnimatedNumber
    intercept: SVGAnimatedNumber
    amplitude: SVGAnimatedNumber
    exponent: SVGAnimatedNumber
    offset: SVGAnimatedNumber

class SVGFEFuncRElement(SVGComponentTransferFunctionElement): ...

class SVGFEFuncGElement(SVGComponentTransferFunctionElement): ...

class SVGFEFuncBElement(SVGComponentTransferFunctionElement): ...

class SVGFEFuncAElement(SVGComponentTransferFunctionElement): ...

class SVGFECompositeElement(SVGElement, SVGFilterPrimitiveStandardAttributes):
    SVG_FECOMPOSITE_OPERATOR_UNKNOWN = 0
    SVG_FECOMPOSITE_OPERATOR_OVER = 1
    SVG_FECOMPOSITE_OPERATOR_IN = 2
    SVG_FECOMPOSITE_OPERATOR_OUT = 3
    SVG_FECOMPOSITE_OPERATOR_ATOP = 4
    SVG_FECOMPOSITE_OPERATOR_XOR = 5
    SVG_FECOMPOSITE_OPERATOR_ARITHMETIC = 6
    in1: SVGAnimatedString
    in2: SVGAnimatedString
    operator: SVGAnimatedEnumeration
    k1: SVGAnimatedNumber
    k2: SVGAnimatedNumber
    k3: SVGAnimatedNumber
    k4: SVGAnimatedNumber

class SVGFEConvolveMatrixElement(SVGElement, SVGFilterPrimitiveStandardAttributes):
    SVG_EDGEMODE_UNKNOWN = 0
    SVG_EDGEMODE_DUPLICATE = 1
    SVG_EDGEMODE_WRAP = 2
    SVG_EDGEMODE_NONE = 3
    in1: SVGAnimatedString
    orderX: SVGAnimatedInteger
    orderY: SVGAnimatedInteger
    kernelMatrix: SVGAnimatedNumberList
    divisor: SVGAnimatedNumber
    bias: SVGAnimatedNumber
    targetX: SVGAnimatedInteger
    targetY: SVGAnimatedInteger
    edgeMode: SVGAnimatedEnumeration
    kernelUnitLengthX: SVGAnimatedNumber
    kernelUnitLengthY: SVGAnimatedNumber
    preserveAlpha: SVGAnimatedBoolean

class SVGFEDiffuseLightingElement(SVGElement, SVGFilterPrimitiveStandardAttributes):
    in1: SVGAnimatedString
    surfaceScale: SVGAnimatedNumber
    diffuseConstant: SVGAnimatedNumber
    kernelUnitLengthX: SVGAnimatedNumber
    kernelUnitLengthY: SVGAnimatedNumber

class SVGFEDistantLightElement(SVGElement):
    azimuth: SVGAnimatedNumber
    elevation: SVGAnimatedNumber

class SVGFEPointLightElement(SVGElement):
    x: SVGAnimatedNumber
    y: SVGAnimatedNumber
    z: SVGAnimatedNumber

class SVGFESpotLightElement(SVGElement):
    x: SVGAnimatedNumber
    y: SVGAnimatedNumber
    z: SVGAnimatedNumber
    pointsAtX: SVGAnimatedNumber
    pointsAtY: SVGAnimatedNumber
    pointsAtZ: SVGAnimatedNumber
    specularExponent: SVGAnimatedNumber
    limitingConeAngle: SVGAnimatedNumber

class SVGFEDisplacementMapElement(SVGElement, SVGFilterPrimitiveStandardAttributes):
    SVG_CHANNEL_UNKNOWN = 0
    SVG_CHANNEL_R = 1
    SVG_CHANNEL_G = 2
    SVG_CHANNEL_B = 3
    SVG_CHANNEL_A = 4
    in1: SVGAnimatedString
    in2: SVGAnimatedString
    scale: SVGAnimatedNumber
    xChannelSelector: SVGAnimatedEnumeration
    yChannelSelector: SVGAnimatedEnumeration

class SVGFEDropShadowElement(SVGElement, SVGFilterPrimitiveStandardAttributes):
    in1: SVGAnimatedString
    dx: SVGAnimatedNumber
    dy: SVGAnimatedNumber
    stdDeviationX: SVGAnimatedNumber
    stdDeviationY: SVGAnimatedNumber

    def setStdDeviation(self, stdDeviationX: float, stdDeviationY: float) -> None: ...

class SVGFEFloodElement(SVGElement, SVGFilterPrimitiveStandardAttributes): ...

class SVGFEGaussianBlurElement(SVGElement, SVGFilterPrimitiveStandardAttributes):
    SVG_EDGEMODE_UNKNOWN = 0
    SVG_EDGEMODE_DUPLICATE = 1
    SVG_EDGEMODE_WRAP = 2
    SVG_EDGEMODE_NONE = 3
    in1: SVGAnimatedString
    stdDeviationX: SVGAnimatedNumber
    stdDeviationY: SVGAnimatedNumber
    edgeMode: SVGAnimatedEnumeration

    def setStdDeviation(self, stdDeviationX: float, stdDeviationY: float) -> None: ...

class SVGFEImageElement(SVGElement, SVGFilterPrimitiveStandardAttributes, SVGURIReference):
    preserveAspectRatio: SVGAnimatedPreserveAspectRatio
    crossOrigin: SVGAnimatedString

class SVGFEMergeElement(SVGElement, SVGFilterPrimitiveStandardAttributes): ...

class SVGFEMergeNodeElement(SVGElement):
    in1: SVGAnimatedString

class SVGFEMorphologyElement(SVGElement, SVGFilterPrimitiveStandardAttributes):
    SVG_MORPHOLOGY_OPERATOR_UNKNOWN = 0
    SVG_MORPHOLOGY_OPERATOR_ERODE = 1
    SVG_MORPHOLOGY_OPERATOR_DILATE = 2
    in1: SVGAnimatedString
    operator: SVGAnimatedEnumeration
    radiusX: SVGAnimatedNumber
    radiusY: SVGAnimatedNumber

class SVGFEOffsetElement(SVGElement, SVGFilterPrimitiveStandardAttributes):
    in1: SVGAnimatedString
    dx: SVGAnimatedNumber
    dy: SVGAnimatedNumber

class SVGFESpecularLightingElement(SVGElement, SVGFilterPrimitiveStandardAttributes):
    in1: SVGAnimatedString
    surfaceScale: SVGAnimatedNumber
    specularConstant: SVGAnimatedNumber
    specularExponent: SVGAnimatedNumber
    kernelUnitLengthX: SVGAnimatedNumber
    kernelUnitLengthY: SVGAnimatedNumber

class SVGFETileElement(SVGElement, SVGFilterPrimitiveStandardAttributes):
    in1: SVGAnimatedString

class SVGFETurbulenceElement(SVGElement, SVGFilterPrimitiveStandardAttributes):
    SVG_TURBULENCE_TYPE_UNKNOWN = 0
    SVG_TURBULENCE_TYPE_FRACTALNOISE = 1
    SVG_TURBULENCE_TYPE_TURBULENCE = 2
    SVG_STITCHTYPE_UNKNOWN = 0
    SVG_STITCHTYPE_STITCH = 1
    SVG_STITCHTYPE_NOSTITCH = 2
    baseFrequencyX: SVGAnimatedNumber
    baseFrequencyY: SVGAnimatedNumber
    numOctaves: SVGAnimatedInteger
    seed: SVGAnimatedNumber
    stitchTiles: SVGAnimatedEnumeration
    type: SVGAnimatedEnumeration

class FontMetrics:
    width: float
    advances: Sequence[float]
    boundingBoxLeft: float
    boundingBoxRight: float
    height: float
    emHeightAscent: float
    emHeightDescent: float
    boundingBoxAscent: float
    boundingBoxDescent: float
    fontBoundingBoxAscent: float
    fontBoundingBoxDescent: float
    dominantBaseline: Baseline
    baselines: Sequence[Baseline]
    fonts: Sequence[Font]

class Baseline:
    name: str
    value: float

class Font:
    name: str
    glyphsRendered: int

class FileSystemCreateWritableOptions(TypedDict):
    keepExistingData: NotRequired[bool]

class FileSystemFileHandle(FileSystemHandle):

    def getFile(self) -> Awaitable[File]: ...

    def createWritable(self, options: Union['FileSystemCreateWritableOptions', 'None'] = {}) -> Awaitable[FileSystemWritableFileStream]: ...

    def createSyncAccessHandle(self) -> Awaitable[FileSystemSyncAccessHandle]: ...

class FileSystemGetFileOptions(TypedDict):
    create: NotRequired[bool]

class FileSystemGetDirectoryOptions(TypedDict):
    create: NotRequired[bool]

class FileSystemRemoveOptions(TypedDict):
    recursive: NotRequired[bool]

class FileSystemDirectoryHandle(FileSystemHandle):

    def getFileHandle(self, name: str, options: Union['FileSystemGetFileOptions', 'None'] = {}) -> Awaitable[FileSystemFileHandle]: ...

    def getDirectoryHandle(self, name: str, options: Union['FileSystemGetDirectoryOptions', 'None'] = {}) -> Awaitable[FileSystemDirectoryHandle]: ...

    def removeEntry(self, name: str, options: Union['FileSystemRemoveOptions', 'None'] = {}) -> Awaitable[None]: ...

    def resolve(self, possibleDescendant: FileSystemHandle) -> Awaitable[Sequence[str]]: ...

class WriteParams(TypedDict):
    type: WriteCommandType
    size: NotRequired[Union['int', 'None']]
    position: NotRequired[Union['int', 'None']]
    data: NotRequired[Union['BufferSource', 'Blob', 'str', 'None']]

class FileSystemWritableFileStream(WritableStream):

    def write(self, data: FileSystemWriteChunkType) -> Awaitable[None]: ...

    def seek(self, position: int) -> Awaitable[None]: ...

    def truncate(self, size: int) -> Awaitable[None]: ...

class FileSystemReadWriteOptions(TypedDict):
    at: NotRequired[int]

class FileSystemSyncAccessHandle:

    def read(self, buffer: AllowSharedBufferSource, options: Union['FileSystemReadWriteOptions', 'None'] = {}) -> int: ...

    def write(self, buffer: AllowSharedBufferSource, options: Union['FileSystemReadWriteOptions', 'None'] = {}) -> int: ...

    def truncate(self, newSize: int) -> None: ...

    def getSize(self) -> int: ...

    def flush(self) -> None: ...

    def close(self) -> None: ...

class StorageManager:

    def getDirectory(self) -> Awaitable[FileSystemDirectoryHandle]: ...

    def persisted(self) -> Awaitable[bool]: ...

    def persist(self) -> Awaitable[bool]: ...

    def estimate(self) -> Awaitable[StorageEstimate]: ...

class FullscreenOptions(TypedDict):
    navigationUI: NotRequired[FullscreenNavigationUI]
    screen: NotRequired[ScreenDetailed]

class GamepadHapticActuator:
    type: GamepadHapticActuatorType

    def canPlayEffectType(self, type: GamepadHapticEffectType) -> bool: ...

    def playEffect(self, type: GamepadHapticEffectType, params: Union['GamepadEffectParameters', 'None'] = {}) -> Awaitable[GamepadHapticsResult]: ...

    def pulse(self, value: float, duration: float) -> Awaitable[bool]: ...

    def reset(self) -> Awaitable[GamepadHapticsResult]: ...

class GamepadEffectParameters(TypedDict):
    duration: NotRequired[float]
    startDelay: NotRequired[float]
    strongMagnitude: NotRequired[float]
    weakMagnitude: NotRequired[float]

class GamepadPose:
    hasOrientation: bool
    hasPosition: bool
    position: Float32Array
    linearVelocity: Float32Array
    linearAcceleration: Float32Array
    orientation: Float32Array
    angularVelocity: Float32Array
    angularAcceleration: Float32Array

class GamepadTouch:
    touchId: int
    surfaceId: int
    position: Float32Array
    surfaceDimensions: Uint32Array

class Gamepad:
    hand: GamepadHand
    hapticActuators: Sequence[GamepadHapticActuator]
    pose: Union['GamepadPose', 'None']
    touchEvents: Sequence[GamepadTouch]
    vibrationActuator: Union['GamepadHapticActuator', 'None']
    id: str
    index: int
    connected: bool
    timestamp: DOMHighResTimeStamp
    mapping: GamepadMappingType
    axes: Sequence[float]
    buttons: Sequence[GamepadButton]

class GamepadButton:
    pressed: bool
    touched: bool
    value: float

class GamepadEvent(Event):
    @classmethod
    def new(cls, type: str, eventInitDict: GamepadEventInit) -> GamepadEvent: ...
    gamepad: Gamepad

class GamepadEventInit(EventInit):
    gamepad: Gamepad

class WindowEventHandlers:
    ongamepadconnected: EventHandler
    ongamepaddisconnected: EventHandler
    onafterprint: EventHandler
    onbeforeprint: EventHandler
    onbeforeunload: OnBeforeUnloadEventHandler
    onhashchange: EventHandler
    onlanguagechange: EventHandler
    onmessage: EventHandler
    onmessageerror: EventHandler
    onoffline: EventHandler
    ononline: EventHandler
    onpagehide: EventHandler
    onpageshow: EventHandler
    onpopstate: EventHandler
    onrejectionhandled: EventHandler
    onstorage: EventHandler
    onunhandledrejection: EventHandler
    onunload: EventHandler
    onportalactivate: EventHandler

class Sensor(EventTarget):
    activated: bool
    hasReading: bool
    timestamp: Union['DOMHighResTimeStamp', 'None']

    def start(self) -> None: ...

    def stop(self) -> None: ...
    onreading: EventHandler
    onactivate: EventHandler
    onerror: EventHandler

class SensorOptions(TypedDict):
    frequency: NotRequired[float]

class SensorErrorEvent(Event):
    @classmethod
    def new(cls, type: str, errorEventInitDict: SensorErrorEventInit) -> SensorErrorEvent: ...
    error: DOMException

class SensorErrorEventInit(EventInit):
    error: DOMException

class MockSensorConfiguration(TypedDict):
    mockSensorType: MockSensorType
    connected: NotRequired[bool]
    maxSamplingFrequency: NotRequired[Union['float', 'None']]
    minSamplingFrequency: NotRequired[Union['float', 'None']]

class MockSensor(TypedDict):
    maxSamplingFrequency: NotRequired[float]
    minSamplingFrequency: NotRequired[float]
    requestedSamplingFrequency: NotRequired[float]

class MockSensorReadingValues(TypedDict): ...

class GeolocationSensor(Sensor):
    @classmethod
    def new(cls, options: Union['GeolocationSensorOptions', 'None'] = {}) -> GeolocationSensor: ...
    latitude: Union['float', 'None']
    longitude: Union['float', 'None']
    altitude: Union['float', 'None']
    accuracy: Union['float', 'None']
    altitudeAccuracy: Union['float', 'None']
    heading: Union['float', 'None']
    speed: Union['float', 'None']

class GeolocationSensorOptions(SensorOptions): ...

class ReadOptions(GeolocationSensorOptions):
    signal: NotRequired[Union['AbortSignal', 'None']]

class GeolocationSensorReading(TypedDict):
    timestamp: NotRequired[Union['DOMHighResTimeStamp', 'None']]
    latitude: NotRequired[Union['float', 'None']]
    longitude: NotRequired[Union['float', 'None']]
    altitude: NotRequired[Union['float', 'None']]
    accuracy: NotRequired[Union['float', 'None']]
    altitudeAccuracy: NotRequired[Union['float', 'None']]
    heading: NotRequired[Union['float', 'None']]
    speed: NotRequired[Union['float', 'None']]

class GeolocationReadingValues(TypedDict):
    latitude: Union['float', 'None']
    longitude: Union['float', 'None']
    altitude: Union['float', 'None']
    accuracy: Union['float', 'None']
    altitudeAccuracy: Union['float', 'None']
    heading: Union['float', 'None']
    speed: Union['float', 'None']

class Geolocation:

    def getCurrentPosition(self, successCallback: PositionCallback, errorCallback: Union['PositionErrorCallback', 'None'] = None, options: Union['PositionOptions', 'None'] = {}) -> None: ...

    def watchPosition(self, successCallback: PositionCallback, errorCallback: Union['PositionErrorCallback', 'None'] = None, options: Union['PositionOptions', 'None'] = {}) -> int: ...

    def clearWatch(self, watchId: int) -> None: ...

class PositionOptions(TypedDict):
    enableHighAccuracy: NotRequired[bool]
    timeout: NotRequired[int]
    maximumAge: NotRequired[int]

class GeolocationPosition:
    coords: GeolocationCoordinates
    timestamp: EpochTimeStamp

class GeolocationCoordinates:
    accuracy: float
    latitude: float
    longitude: float
    altitude: Union['float', 'None']
    altitudeAccuracy: Union['float', 'None']
    heading: Union['float', 'None']
    speed: Union['float', 'None']

class GeolocationPositionError:
    PERMISSION_DENIED = 1
    POSITION_UNAVAILABLE = 2
    TIMEOUT = 3
    code: int
    message: str

class DOMPointReadOnly:
    @classmethod
    def new(cls, x: Union['float', 'None'] = 0, y: Union['float', 'None'] = 0, z: Union['float', 'None'] = 0, w: Union['float', 'None'] = 1) -> DOMPointReadOnly: ...
    x: float
    y: float
    z: float
    w: float

    def matrixTransform(self, matrix: Union['DOMMatrixInit', 'None'] = {}) -> DOMPoint: ...

    def toJSON(self) -> object: ...

class DOMPoint(DOMPointReadOnly):
    @classmethod
    def new(cls, x: Union['float', 'None'] = 0, y: Union['float', 'None'] = 0, z: Union['float', 'None'] = 0, w: Union['float', 'None'] = 1) -> DOMPoint: ...
    x: float
    y: float
    z: float
    w: float

class DOMPointInit(TypedDict):
    x: NotRequired[float]
    y: NotRequired[float]
    z: NotRequired[float]
    w: NotRequired[float]

class DOMRectReadOnly:
    @classmethod
    def new(cls, x: Union['float', 'None'] = 0, y: Union['float', 'None'] = 0, width: Union['float', 'None'] = 0, height: Union['float', 'None'] = 0) -> DOMRectReadOnly: ...
    x: float
    y: float
    width: float
    height: float
    top: float
    right: float
    bottom: float
    left: float

    def toJSON(self) -> object: ...

class DOMRect(DOMRectReadOnly):
    @classmethod
    def new(cls, x: Union['float', 'None'] = 0, y: Union['float', 'None'] = 0, width: Union['float', 'None'] = 0, height: Union['float', 'None'] = 0) -> DOMRect: ...
    x: float
    y: float
    width: float
    height: float

class DOMRectInit(TypedDict):
    x: NotRequired[float]
    y: NotRequired[float]
    width: NotRequired[float]
    height: NotRequired[float]

class DOMRectList:
    length: int

    def item(self, index: int) -> Union['DOMRect', 'None']: ...

class DOMQuad:
    @classmethod
    def new(cls, p1: Union['DOMPointInit', 'None'] = {}, p2: Union['DOMPointInit', 'None'] = {}, p3: Union['DOMPointInit', 'None'] = {}, p4: Union['DOMPointInit', 'None'] = {}) -> DOMQuad: ...
    p1: DOMPoint
    p2: DOMPoint
    p3: DOMPoint
    p4: DOMPoint

    def getBounds(self) -> DOMRect: ...

    def toJSON(self) -> object: ...

class DOMQuadInit(TypedDict):
    p1: NotRequired[DOMPointInit]
    p2: NotRequired[DOMPointInit]
    p3: NotRequired[DOMPointInit]
    p4: NotRequired[DOMPointInit]

class DOMMatrixReadOnly:
    @classmethod
    def new(cls, init: Union['str', 'Sequence[float]', 'None'] = None) -> DOMMatrixReadOnly: ...
    a: float
    b: float
    c: float
    d: float
    e: float
    f: float
    m11: float
    m12: float
    m13: float
    m14: float
    m21: float
    m22: float
    m23: float
    m24: float
    m31: float
    m32: float
    m33: float
    m34: float
    m41: float
    m42: float
    m43: float
    m44: float
    is2D: bool
    isIdentity: bool

    def translate(self, tx: Union['float', 'None'] = 0, ty: Union['float', 'None'] = 0, tz: Union['float', 'None'] = 0) -> DOMMatrix: ...

    def scale(self, scaleX: Union['float', 'None'] = 1, scaleY: Union['float', 'None'] = None, scaleZ: Union['float', 'None'] = 1, originX: Union['float', 'None'] = 0, originY: Union['float', 'None'] = 0, originZ: Union['float', 'None'] = 0) -> DOMMatrix: ...

    def scaleNonUniform(self, scaleX: Union['float', 'None'] = 1, scaleY: Union['float', 'None'] = 1) -> DOMMatrix: ...

    def scale3d(self, scale: Union['float', 'None'] = 1, originX: Union['float', 'None'] = 0, originY: Union['float', 'None'] = 0, originZ: Union['float', 'None'] = 0) -> DOMMatrix: ...

    def rotate(self, rotX: Union['float', 'None'] = 0, rotY: Union['float', 'None'] = None, rotZ: Union['float', 'None'] = None) -> DOMMatrix: ...

    def rotateFromVector(self, x: Union['float', 'None'] = 0, y: Union['float', 'None'] = 0) -> DOMMatrix: ...

    def rotateAxisAngle(self, x: Union['float', 'None'] = 0, y: Union['float', 'None'] = 0, z: Union['float', 'None'] = 0, angle: Union['float', 'None'] = 0) -> DOMMatrix: ...

    def skewX(self, sx: Union['float', 'None'] = 0) -> DOMMatrix: ...

    def skewY(self, sy: Union['float', 'None'] = 0) -> DOMMatrix: ...

    def multiply(self, other: Union['DOMMatrixInit', 'None'] = {}) -> DOMMatrix: ...

    def flipX(self) -> DOMMatrix: ...

    def flipY(self) -> DOMMatrix: ...

    def inverse(self) -> DOMMatrix: ...

    def transformPoint(self, point: Union['DOMPointInit', 'None'] = {}) -> DOMPoint: ...

    def toFloat32Array(self) -> Float32Array: ...

    def toFloat64Array(self) -> Float64Array: ...

    def toJSON(self) -> object: ...

class DOMMatrix(DOMMatrixReadOnly):
    @classmethod
    def new(cls, init: Union['str', 'Sequence[float]', 'None'] = None) -> DOMMatrix: ...
    a: float
    b: float
    c: float
    d: float
    e: float
    f: float
    m11: float
    m12: float
    m13: float
    m14: float
    m21: float
    m22: float
    m23: float
    m24: float
    m31: float
    m32: float
    m33: float
    m34: float
    m41: float
    m42: float
    m43: float
    m44: float

    def multiplySelf(self, other: Union['DOMMatrixInit', 'None'] = {}) -> DOMMatrix: ...

    def preMultiplySelf(self, other: Union['DOMMatrixInit', 'None'] = {}) -> DOMMatrix: ...

    def translateSelf(self, tx: Union['float', 'None'] = 0, ty: Union['float', 'None'] = 0, tz: Union['float', 'None'] = 0) -> DOMMatrix: ...

    def scaleSelf(self, scaleX: Union['float', 'None'] = 1, scaleY: Union['float', 'None'] = None, scaleZ: Union['float', 'None'] = 1, originX: Union['float', 'None'] = 0, originY: Union['float', 'None'] = 0, originZ: Union['float', 'None'] = 0) -> DOMMatrix: ...

    def scale3dSelf(self, scale: Union['float', 'None'] = 1, originX: Union['float', 'None'] = 0, originY: Union['float', 'None'] = 0, originZ: Union['float', 'None'] = 0) -> DOMMatrix: ...

    def rotateSelf(self, rotX: Union['float', 'None'] = 0, rotY: Union['float', 'None'] = None, rotZ: Union['float', 'None'] = None) -> DOMMatrix: ...

    def rotateFromVectorSelf(self, x: Union['float', 'None'] = 0, y: Union['float', 'None'] = 0) -> DOMMatrix: ...

    def rotateAxisAngleSelf(self, x: Union['float', 'None'] = 0, y: Union['float', 'None'] = 0, z: Union['float', 'None'] = 0, angle: Union['float', 'None'] = 0) -> DOMMatrix: ...

    def skewXSelf(self, sx: Union['float', 'None'] = 0) -> DOMMatrix: ...

    def skewYSelf(self, sy: Union['float', 'None'] = 0) -> DOMMatrix: ...

    def invertSelf(self) -> DOMMatrix: ...

    def setMatrixValue(self, transformList: str) -> DOMMatrix: ...

class DOMMatrix2DInit(TypedDict):
    a: NotRequired[float]
    b: NotRequired[float]
    c: NotRequired[float]
    d: NotRequired[float]
    e: NotRequired[float]
    f: NotRequired[float]
    m11: NotRequired[float]
    m12: NotRequired[float]
    m21: NotRequired[float]
    m22: NotRequired[float]
    m41: NotRequired[float]
    m42: NotRequired[float]

class DOMMatrixInit(DOMMatrix2DInit):
    m13: NotRequired[float]
    m14: NotRequired[float]
    m23: NotRequired[float]
    m24: NotRequired[float]
    m31: NotRequired[float]
    m32: NotRequired[float]
    m33: NotRequired[float]
    m34: NotRequired[float]
    m43: NotRequired[float]
    m44: NotRequired[float]
    is2D: NotRequired[bool]

class RelatedApplication(TypedDict):
    platform: str
    url: NotRequired[str]
    id: NotRequired[str]
    version: NotRequired[str]

class GlobalPrivacyControl:
    globalPrivacyControl: bool

class Gyroscope(Sensor):
    @classmethod
    def new(cls, sensorOptions: Union['GyroscopeSensorOptions', 'None'] = {}) -> Gyroscope: ...
    x: Union['float', 'None']
    y: Union['float', 'None']
    z: Union['float', 'None']

class GyroscopeSensorOptions(SensorOptions):
    referenceFrame: NotRequired[GyroscopeLocalCoordinateSystem]

class GyroscopeReadingValues(TypedDict):
    x: Union['float', 'None']
    y: Union['float', 'None']
    z: Union['float', 'None']

class HTMLAllCollection:
    length: int

    def __getter__(self, index: int) -> Element: ...

    def namedItem(self, name: str) -> Union['HTMLCollection', 'Element', 'None']: ...

    def item(self, nameOrIndex: Union['str', 'None'] = None) -> Union['HTMLCollection', 'Element', 'None']: ...

class HTMLFormControlsCollection(HTMLCollection):

    def namedItem(self, name: str) -> Union['RadioNodeList', 'Element', 'None']: ...

class RadioNodeList(NodeList):
    value: str

class HTMLOptionsCollection(HTMLCollection):
    length: int

    def __setter__(self, index: int, option: Union['HTMLOptionElement', 'None']) -> None: ...

    def add(self, element: Union['HTMLOptionElement', 'HTMLOptGroupElement'], before: Union['HTMLElement', 'int', 'None'] = None) -> None: ...

    def remove(self, index: int) -> None: ...
    selectedIndex: int

class DOMStringList:
    length: int

    def item(self, index: int) -> Union['str', 'None']: ...

    def contains(self, string: str) -> bool: ...

class HTMLUnknownElement(HTMLElement): ...

class HTMLOrSVGElement:
    dataset: DOMStringMap
    nonce: str
    autofocus: bool
    tabIndex: int

    def focus(self, options: Union['FocusOptions', 'None'] = {}) -> None: ...

    def blur(self) -> None: ...

class DOMStringMap:

    def __getter__(self, name: str) -> str: ...

    def __setter__(self, name: str, value: str) -> None: ...

    def __deleter__(self, name: str) -> None: ...

class HTMLHtmlElement(HTMLElement):
    @classmethod
    def new(cls) -> HTMLHtmlElement: ...
    version: str

class HTMLHeadElement(HTMLElement):
    @classmethod
    def new(cls) -> HTMLHeadElement: ...

class HTMLTitleElement(HTMLElement):
    @classmethod
    def new(cls) -> HTMLTitleElement: ...
    text: str

class HTMLBaseElement(HTMLElement):
    @classmethod
    def new(cls) -> HTMLBaseElement: ...
    href: str
    target: str

class HTMLLinkElement(HTMLElement, LinkStyle):
    @classmethod
    def new(cls) -> HTMLLinkElement: ...
    href: str
    crossOrigin: Union['str', 'None']
    rel: str
    relList: DOMTokenList
    media: str
    integrity: str
    hreflang: str
    type: str
    sizes: DOMTokenList
    imageSrcset: str
    imageSizes: str
    referrerPolicy: str
    blocking: DOMTokenList
    disabled: bool
    fetchPriority: str
    charset: str
    rev: str
    target: str

class HTMLMetaElement(HTMLElement):
    @classmethod
    def new(cls) -> HTMLMetaElement: ...
    name: str
    httpEquiv: str
    content: str
    media: str
    scheme: str

class HTMLStyleElement(HTMLElement, LinkStyle):
    @classmethod
    def new(cls) -> HTMLStyleElement: ...
    disabled: bool
    media: str
    blocking: DOMTokenList
    type: str

class HTMLHeadingElement(HTMLElement):
    @classmethod
    def new(cls) -> HTMLHeadingElement: ...
    align: str

class HTMLParagraphElement(HTMLElement):
    @classmethod
    def new(cls) -> HTMLParagraphElement: ...
    align: str

class HTMLHRElement(HTMLElement):
    @classmethod
    def new(cls) -> HTMLHRElement: ...
    align: str
    color: str
    noShade: bool
    size: str
    width: str

class HTMLPreElement(HTMLElement):
    @classmethod
    def new(cls) -> HTMLPreElement: ...
    width: int

class HTMLQuoteElement(HTMLElement):
    @classmethod
    def new(cls) -> HTMLQuoteElement: ...
    cite: str

class HTMLOListElement(HTMLElement):
    @classmethod
    def new(cls) -> HTMLOListElement: ...
    reversed: bool
    start: int
    type: str
    compact: bool

class HTMLUListElement(HTMLElement):
    @classmethod
    def new(cls) -> HTMLUListElement: ...
    compact: bool
    type: str

class HTMLMenuElement(HTMLElement):
    @classmethod
    def new(cls) -> HTMLMenuElement: ...
    compact: bool

class HTMLLIElement(HTMLElement):
    @classmethod
    def new(cls) -> HTMLLIElement: ...
    value: int
    type: str

class HTMLDListElement(HTMLElement):
    @classmethod
    def new(cls) -> HTMLDListElement: ...
    compact: bool

class HTMLDivElement(HTMLElement):
    @classmethod
    def new(cls) -> HTMLDivElement: ...
    align: str

class HTMLDataElement(HTMLElement):
    @classmethod
    def new(cls) -> HTMLDataElement: ...
    value: str

class HTMLTimeElement(HTMLElement):
    @classmethod
    def new(cls) -> HTMLTimeElement: ...
    dateTime: str

class HTMLSpanElement(HTMLElement):
    @classmethod
    def new(cls) -> HTMLSpanElement: ...

class HTMLBRElement(HTMLElement):
    @classmethod
    def new(cls) -> HTMLBRElement: ...
    clear: str

class HTMLHyperlinkElementUtils:
    href: str
    origin: str
    protocol: str
    username: str
    password: str
    host: str
    hostname: str
    port: str
    pathname: str
    search: str
    hash: str

class HTMLModElement(HTMLElement):
    @classmethod
    def new(cls) -> HTMLModElement: ...
    cite: str
    dateTime: str

class HTMLPictureElement(HTMLElement):
    @classmethod
    def new(cls) -> HTMLPictureElement: ...

class HTMLSourceElement(HTMLElement):
    @classmethod
    def new(cls) -> HTMLSourceElement: ...
    src: str
    type: str
    srcset: str
    sizes: str
    media: str
    width: int
    height: int

class HTMLEmbedElement(HTMLElement):
    @classmethod
    def new(cls) -> HTMLEmbedElement: ...
    src: str
    type: str
    width: str
    height: str

    def getSVGDocument(self) -> Union['Document', 'None']: ...
    align: str
    name: str

class HTMLObjectElement(HTMLElement):
    @classmethod
    def new(cls) -> HTMLObjectElement: ...
    data: str
    type: str
    name: str
    form: Union['HTMLFormElement', 'None']
    width: str
    height: str
    contentDocument: Union['Document', 'None']
    contentWindow: Union['WindowProxy', 'None']

    def getSVGDocument(self) -> Union['Document', 'None']: ...
    willValidate: bool
    validity: ValidityState
    validationMessage: str

    def checkValidity(self) -> bool: ...

    def reportValidity(self) -> bool: ...

    def setCustomValidity(self, error: str) -> None: ...
    align: str
    archive: str
    code: str
    declare: bool
    hspace: int
    standby: str
    vspace: int
    codeBase: str
    codeType: str
    useMap: str
    border: str

class HTMLVideoElement(HTMLMediaElement):
    @classmethod
    def new(cls) -> HTMLVideoElement: ...
    width: int
    height: int
    videoWidth: int
    videoHeight: int
    poster: str
    playsInline: bool

    def getVideoPlaybackQuality(self) -> VideoPlaybackQuality: ...

    def requestPictureInPicture(self) -> Awaitable[PictureInPictureWindow]: ...
    onenterpictureinpicture: EventHandler
    onleavepictureinpicture: EventHandler
    disablePictureInPicture: bool

    def requestVideoFrameCallback(self, callback: VideoFrameRequestCallback) -> int: ...

    def cancelVideoFrameCallback(self, handle: int) -> None: ...

class HTMLAudioElement(HTMLMediaElement):
    @classmethod
    def new(cls) -> HTMLAudioElement: ...
    """ # GIgnoredStmt
    LegacyFactoryFunction=Audio(optional DOMString src)
    """

class HTMLTrackElement(HTMLElement):
    @classmethod
    def new(cls) -> HTMLTrackElement: ...
    kind: str
    src: str
    srclang: str
    label: str
    default: bool
    NONE = 0
    LOADING = 1
    LOADED = 2
    ERROR = 3
    readyState: int
    track: TextTrack

class MediaError:
    MEDIA_ERR_ABORTED = 1
    MEDIA_ERR_NETWORK = 2
    MEDIA_ERR_DECODE = 3
    MEDIA_ERR_SRC_NOT_SUPPORTED = 4
    code: int
    message: str

class AudioTrackList(EventTarget):
    length: int

    def __getter__(self, index: int) -> AudioTrack: ...

    def getTrackById(self, id: str) -> Union['AudioTrack', 'None']: ...
    onchange: EventHandler
    onaddtrack: EventHandler
    onremovetrack: EventHandler

class AudioTrack:
    id: str
    kind: str
    label: str
    language: str
    enabled: bool
    sourceBuffer: Union['SourceBuffer', 'None']

class VideoTrackList(EventTarget):
    length: int

    def __getter__(self, index: int) -> VideoTrack: ...

    def getTrackById(self, id: str) -> Union['VideoTrack', 'None']: ...
    selectedIndex: int
    onchange: EventHandler
    onaddtrack: EventHandler
    onremovetrack: EventHandler

class VideoTrack:
    id: str
    kind: str
    label: str
    language: str
    selected: bool
    sourceBuffer: Union['SourceBuffer', 'None']

class TextTrackList(EventTarget):
    length: int

    def __getter__(self, index: int) -> TextTrack: ...

    def getTrackById(self, id: str) -> Union['TextTrack', 'None']: ...
    onchange: EventHandler
    onaddtrack: EventHandler
    onremovetrack: EventHandler

class TextTrack(EventTarget):
    kind: TextTrackKind
    label: str
    language: str
    id: str
    inBandMetadataTrackDispatchType: str
    mode: TextTrackMode
    cues: Union['TextTrackCueList', 'None']
    activeCues: Union['TextTrackCueList', 'None']

    def addCue(self, cue: TextTrackCue) -> None: ...

    def removeCue(self, cue: TextTrackCue) -> None: ...
    oncuechange: EventHandler
    sourceBuffer: Union['SourceBuffer', 'None']

class TextTrackCueList:
    length: int

    def __getter__(self, index: int) -> TextTrackCue: ...

    def getCueById(self, id: str) -> Union['TextTrackCue', 'None']: ...

class TextTrackCue(EventTarget):
    track: Union['TextTrack', 'None']
    id: str
    startTime: float
    endTime: float
    pauseOnExit: bool
    onenter: EventHandler
    onexit: EventHandler

class TimeRanges:
    length: int

    def start(self, index: int) -> float: ...

    def end(self, index: int) -> float: ...

class TrackEvent(Event):
    @classmethod
    def new(cls, type: str, eventInitDict: Union['TrackEventInit', 'None'] = {}) -> TrackEvent: ...
    track: Union['VideoTrack', 'AudioTrack', 'TextTrack', 'None']

class TrackEventInit(EventInit):
    track: NotRequired[Union['VideoTrack', 'AudioTrack', 'TextTrack', 'None']]

class HTMLMapElement(HTMLElement):
    @classmethod
    def new(cls) -> HTMLMapElement: ...
    name: str
    areas: HTMLCollection

class HTMLAreaElement(HTMLElement, HTMLHyperlinkElementUtils):
    @classmethod
    def new(cls) -> HTMLAreaElement: ...
    alt: str
    coords: str
    shape: str
    target: str
    download: str
    ping: str
    rel: str
    relList: DOMTokenList
    referrerPolicy: str
    noHref: bool

class HTMLTableElement(HTMLElement):
    @classmethod
    def new(cls) -> HTMLTableElement: ...
    caption: Union['HTMLTableCaptionElement', 'None']

    def createCaption(self) -> HTMLTableCaptionElement: ...

    def deleteCaption(self) -> None: ...
    tHead: Union['HTMLTableSectionElement', 'None']

    def createTHead(self) -> HTMLTableSectionElement: ...

    def deleteTHead(self) -> None: ...
    tFoot: Union['HTMLTableSectionElement', 'None']

    def createTFoot(self) -> HTMLTableSectionElement: ...

    def deleteTFoot(self) -> None: ...
    tBodies: HTMLCollection

    def createTBody(self) -> HTMLTableSectionElement: ...
    rows: HTMLCollection

    def insertRow(self, index: Union['int', 'None'] = -1) -> HTMLTableRowElement: ...

    def deleteRow(self, index: int) -> None: ...
    align: str
    border: str
    frame: str
    rules: str
    summary: str
    width: str
    bgColor: str
    cellPadding: str
    cellSpacing: str

class HTMLTableCaptionElement(HTMLElement):
    @classmethod
    def new(cls) -> HTMLTableCaptionElement: ...
    align: str

class HTMLTableColElement(HTMLElement):
    @classmethod
    def new(cls) -> HTMLTableColElement: ...
    span: int
    align: str
    ch: str
    chOff: str
    vAlign: str
    width: str

class HTMLTableSectionElement(HTMLElement):
    @classmethod
    def new(cls) -> HTMLTableSectionElement: ...
    rows: HTMLCollection

    def insertRow(self, index: Union['int', 'None'] = -1) -> HTMLTableRowElement: ...

    def deleteRow(self, index: int) -> None: ...
    align: str
    ch: str
    chOff: str
    vAlign: str

class HTMLTableRowElement(HTMLElement):
    @classmethod
    def new(cls) -> HTMLTableRowElement: ...
    rowIndex: int
    sectionRowIndex: int
    cells: HTMLCollection

    def insertCell(self, index: Union['int', 'None'] = -1) -> HTMLTableCellElement: ...

    def deleteCell(self, index: int) -> None: ...
    align: str
    ch: str
    chOff: str
    vAlign: str
    bgColor: str

class HTMLTableCellElement(HTMLElement):
    @classmethod
    def new(cls) -> HTMLTableCellElement: ...
    colSpan: int
    rowSpan: int
    headers: str
    cellIndex: int
    scope: str
    abbr: str
    align: str
    axis: str
    height: str
    width: str
    ch: str
    chOff: str
    noWrap: bool
    vAlign: str
    bgColor: str

class HTMLFormElement(HTMLElement):
    @classmethod
    def new(cls) -> HTMLFormElement: ...
    acceptCharset: str
    action: str
    autocomplete: str
    enctype: str
    encoding: str
    method: str
    name: str
    noValidate: bool
    target: str
    rel: str
    relList: DOMTokenList
    elements: HTMLFormControlsCollection
    length: int
    @overload
    def __getter__(self, index: int) -> Element: ...
    @overload
    def __getter__(self, name: str) -> Union['RadioNodeList', 'Element']: ...

    def submit(self) -> None: ...

    def requestSubmit(self, submitter: Union['HTMLElement', 'None'] = None) -> None: ...

    def reset(self) -> None: ...

    def checkValidity(self) -> bool: ...

    def reportValidity(self) -> bool: ...

class HTMLLabelElement(HTMLElement):
    @classmethod
    def new(cls) -> HTMLLabelElement: ...
    form: Union['HTMLFormElement', 'None']
    htmlFor: str
    control: Union['HTMLElement', 'None']

class HTMLButtonElement(HTMLElement, PopoverInvokerElement):
    @classmethod
    def new(cls) -> HTMLButtonElement: ...
    disabled: bool
    form: Union['HTMLFormElement', 'None']
    formAction: str
    formEnctype: str
    formMethod: str
    formNoValidate: bool
    formTarget: str
    name: str
    type: str
    value: str
    willValidate: bool
    validity: ValidityState
    validationMessage: str

    def checkValidity(self) -> bool: ...

    def reportValidity(self) -> bool: ...

    def setCustomValidity(self, error: str) -> None: ...
    labels: NodeList

class HTMLSelectElement(HTMLElement):
    @classmethod
    def new(cls) -> HTMLSelectElement: ...
    autocomplete: str
    disabled: bool
    form: Union['HTMLFormElement', 'None']
    multiple: bool
    name: str
    required: bool
    size: int
    type: str
    options: HTMLOptionsCollection
    length: int

    def item(self, index: int) -> Union['HTMLOptionElement', 'None']: ...

    def namedItem(self, name: str) -> Union['HTMLOptionElement', 'None']: ...

    def add(self, element: Union['HTMLOptionElement', 'HTMLOptGroupElement'], before: Union['HTMLElement', 'int', 'None'] = None) -> None: ...
    @overload
    def remove(self) -> None: ...
    @overload
    def remove(self, index: int) -> None: ...

    def __setter__(self, index: int, option: Union['HTMLOptionElement', 'None']) -> None: ...
    selectedOptions: HTMLCollection
    selectedIndex: int
    value: str
    willValidate: bool
    validity: ValidityState
    validationMessage: str

    def checkValidity(self) -> bool: ...

    def reportValidity(self) -> bool: ...

    def setCustomValidity(self, error: str) -> None: ...
    labels: NodeList

class HTMLDataListElement(HTMLElement):
    @classmethod
    def new(cls) -> HTMLDataListElement: ...
    options: HTMLCollection

class HTMLOptGroupElement(HTMLElement):
    @classmethod
    def new(cls) -> HTMLOptGroupElement: ...
    disabled: bool
    label: str

class HTMLOptionElement(HTMLElement):
    @classmethod
    def new(cls) -> HTMLOptionElement: ...
    disabled: bool
    form: Union['HTMLFormElement', 'None']
    label: str
    defaultSelected: bool
    selected: bool
    value: str
    text: str
    index: int
    """ # GIgnoredStmt
    LegacyFactoryFunction=Option(optional DOMString text = "", optional DOMString value, optional boolean defaultSelected = false, optional boolean selected = false)
    """

class HTMLTextAreaElement(HTMLElement):
    @classmethod
    def new(cls) -> HTMLTextAreaElement: ...
    autocomplete: str
    cols: int
    dirName: str
    disabled: bool
    form: Union['HTMLFormElement', 'None']
    maxLength: int
    minLength: int
    name: str
    placeholder: str
    readOnly: bool
    required: bool
    rows: int
    wrap: str
    type: str
    defaultValue: str
    value: str
    textLength: int
    willValidate: bool
    validity: ValidityState
    validationMessage: str

    def checkValidity(self) -> bool: ...

    def reportValidity(self) -> bool: ...

    def setCustomValidity(self, error: str) -> None: ...
    labels: NodeList

    def select(self) -> None: ...
    selectionStart: int
    selectionEnd: int
    selectionDirection: str
    @overload
    def setRangeText(self, replacement: str) -> None: ...
    @overload
    def setRangeText(self, replacement: str, start: int, end: int, selectionMode: Union['SelectionMode', 'None'] = "preserve") -> None: ...

    def setSelectionRange(self, start: int, end: int, direction: Union['str', 'None'] = None) -> None: ...

class HTMLOutputElement(HTMLElement):
    @classmethod
    def new(cls) -> HTMLOutputElement: ...
    htmlFor: DOMTokenList
    form: Union['HTMLFormElement', 'None']
    name: str
    type: str
    defaultValue: str
    value: str
    willValidate: bool
    validity: ValidityState
    validationMessage: str

    def checkValidity(self) -> bool: ...

    def reportValidity(self) -> bool: ...

    def setCustomValidity(self, error: str) -> None: ...
    labels: NodeList

class HTMLProgressElement(HTMLElement):
    @classmethod
    def new(cls) -> HTMLProgressElement: ...
    value: float
    max: float
    position: float
    labels: NodeList

class HTMLMeterElement(HTMLElement):
    @classmethod
    def new(cls) -> HTMLMeterElement: ...
    value: float
    min: float
    max: float
    low: float
    high: float
    optimum: float
    labels: NodeList

class HTMLFieldSetElement(HTMLElement):
    @classmethod
    def new(cls) -> HTMLFieldSetElement: ...
    disabled: bool
    form: Union['HTMLFormElement', 'None']
    name: str
    type: str
    elements: HTMLCollection
    willValidate: bool
    validity: ValidityState
    validationMessage: str

    def checkValidity(self) -> bool: ...

    def reportValidity(self) -> bool: ...

    def setCustomValidity(self, error: str) -> None: ...

class HTMLLegendElement(HTMLElement):
    @classmethod
    def new(cls) -> HTMLLegendElement: ...
    form: Union['HTMLFormElement', 'None']
    align: str

class ValidityState:
    valueMissing: bool
    typeMismatch: bool
    patternMismatch: bool
    tooLong: bool
    tooShort: bool
    rangeUnderflow: bool
    rangeOverflow: bool
    stepMismatch: bool
    badInput: bool
    customError: bool
    valid: bool

class SubmitEvent(Event):
    @classmethod
    def new(cls, type: str, eventInitDict: Union['SubmitEventInit', 'None'] = {}) -> SubmitEvent: ...
    submitter: Union['HTMLElement', 'None']

class SubmitEventInit(EventInit):
    submitter: NotRequired[Union['HTMLElement', 'None']]

class FormDataEvent(Event):
    @classmethod
    def new(cls, type: str, eventInitDict: FormDataEventInit) -> FormDataEvent: ...
    formData: FormData

class FormDataEventInit(EventInit):
    formData: FormData

class HTMLDetailsElement(HTMLElement):
    @classmethod
    def new(cls) -> HTMLDetailsElement: ...
    open: bool

class HTMLDialogElement(HTMLElement):
    @classmethod
    def new(cls) -> HTMLDialogElement: ...
    open: bool
    returnValue: str

    def show(self) -> None: ...

    def showModal(self) -> None: ...

    def close(self, returnValue: Union['str', 'None'] = None) -> None: ...

class HTMLTemplateElement(HTMLElement):
    @classmethod
    def new(cls) -> HTMLTemplateElement: ...
    content: DocumentFragment

class HTMLSlotElement(HTMLElement):
    @classmethod
    def new(cls) -> HTMLSlotElement: ...
    name: str

    def assignedNodes(self, options: Union['AssignedNodesOptions', 'None'] = {}) -> Sequence[Node]: ...

    def assignedElements(self, options: Union['AssignedNodesOptions', 'None'] = {}) -> Sequence[Element]: ...

    def assign(self, *nodes: Union['Element', 'Text']) -> None: ...

class AssignedNodesOptions(TypedDict):
    flatten: NotRequired[bool]

class HTMLCanvasElement(HTMLElement):
    @classmethod
    def new(cls) -> HTMLCanvasElement: ...
    width: int
    height: int

    def getContext(self, contextId: str, options: Union['Any', 'None'] = None) -> Union['RenderingContext', 'None']: ...

    def toDataURL(self, type: Union['str', 'None'] = "image/png", quality: Union['Any', 'None'] = None) -> str: ...

    def toBlob(self, callback: BlobCallback, type: Union['str', 'None'] = "image/png", quality: Union['Any', 'None'] = None) -> None: ...

    def transferControlToOffscreen(self) -> OffscreenCanvas: ...

    def captureStream(self, frameRequestRate: Union['float', 'None'] = None) -> MediaStream: ...

class CanvasRenderingContext2DSettings(TypedDict):
    alpha: NotRequired[bool]
    desynchronized: NotRequired[bool]
    colorSpace: NotRequired[PredefinedColorSpace]
    willReadFrequently: NotRequired[bool]

class CanvasRenderingContext2D(CanvasState, CanvasTransform, CanvasCompositing, CanvasImageSmoothing, CanvasFillStrokeStyles, CanvasShadowStyles, CanvasFilters, CanvasRect, CanvasDrawPath, CanvasUserInterface, CanvasText, CanvasDrawImage, CanvasImageData, CanvasPathDrawingStyles, CanvasTextDrawingStyles, CanvasPath):
    canvas: HTMLCanvasElement

    def getContextAttributes(self) -> CanvasRenderingContext2DSettings: ...

class CanvasState:

    def save(self) -> None: ...

    def restore(self) -> None: ...

    def reset(self) -> None: ...

    def isContextLost(self) -> bool: ...

class CanvasTransform:

    def scale(self, x: float, y: float) -> None: ...

    def rotate(self, angle: float) -> None: ...

    def translate(self, x: float, y: float) -> None: ...

    def transform(self, a: float, b: float, c: float, d: float, e: float, f: float) -> None: ...

    def getTransform(self) -> DOMMatrix: ...
    @overload
    def setTransform(self, a: float, b: float, c: float, d: float, e: float, f: float) -> None: ...
    @overload
    def setTransform(self, transform: Union['DOMMatrix2DInit', 'None'] = {}) -> None: ...

    def resetTransform(self) -> None: ...

class CanvasCompositing:
    globalAlpha: float
    globalCompositeOperation: str

class CanvasImageSmoothing:
    imageSmoothingEnabled: bool
    imageSmoothingQuality: ImageSmoothingQuality

class CanvasFillStrokeStyles:
    strokeStyle: Union['str', 'CanvasGradient', 'CanvasPattern']
    fillStyle: Union['str', 'CanvasGradient', 'CanvasPattern']

    def createLinearGradient(self, x0: float, y0: float, x1: float, y1: float) -> CanvasGradient: ...

    def createRadialGradient(self, x0: float, y0: float, r0: float, x1: float, y1: float, r1: float) -> CanvasGradient: ...

    def createConicGradient(self, startAngle: float, x: float, y: float) -> CanvasGradient: ...

    def createPattern(self, image: CanvasImageSource, repetition: str) -> Union['CanvasPattern', 'None']: ...

class CanvasShadowStyles:
    shadowOffsetX: float
    shadowOffsetY: float
    shadowBlur: float
    shadowColor: str

class CanvasFilters:
    filter: str

class CanvasRect:

    def clearRect(self, x: float, y: float, w: float, h: float) -> None: ...

    def fillRect(self, x: float, y: float, w: float, h: float) -> None: ...

    def strokeRect(self, x: float, y: float, w: float, h: float) -> None: ...

class CanvasDrawPath:

    def beginPath(self) -> None: ...
    @overload
    def fill(self, fillRule: Union['CanvasFillRule', 'None'] = "nonzero") -> None: ...
    @overload
    def fill(self, path: Path2D, fillRule: Union['CanvasFillRule', 'None'] = "nonzero") -> None: ...
    @overload
    def stroke(self) -> None: ...
    @overload
    def stroke(self, path: Path2D) -> None: ...
    @overload
    def clip(self, fillRule: Union['CanvasFillRule', 'None'] = "nonzero") -> None: ...
    @overload
    def clip(self, path: Path2D, fillRule: Union['CanvasFillRule', 'None'] = "nonzero") -> None: ...
    @overload
    def isPointInPath(self, x: float, y: float, fillRule: Union['CanvasFillRule', 'None'] = "nonzero") -> bool: ...
    @overload
    def isPointInPath(self, path: Path2D, x: float, y: float, fillRule: Union['CanvasFillRule', 'None'] = "nonzero") -> bool: ...
    @overload
    def isPointInStroke(self, x: float, y: float) -> bool: ...
    @overload
    def isPointInStroke(self, path: Path2D, x: float, y: float) -> bool: ...

class CanvasUserInterface:
    @overload
    def drawFocusIfNeeded(self, element: Element) -> None: ...
    @overload
    def drawFocusIfNeeded(self, path: Path2D, element: Element) -> None: ...
    @overload
    def scrollPathIntoView(self) -> None: ...
    @overload
    def scrollPathIntoView(self, path: Path2D) -> None: ...

class CanvasText:

    def fillText(self, text: str, x: float, y: float, maxWidth: Union['float', 'None'] = None) -> None: ...

    def strokeText(self, text: str, x: float, y: float, maxWidth: Union['float', 'None'] = None) -> None: ...

    def measureText(self, text: str) -> TextMetrics: ...

class CanvasDrawImage:
    @overload
    def drawImage(self, image: CanvasImageSource, dx: float, dy: float) -> None: ...
    @overload
    def drawImage(self, image: CanvasImageSource, dx: float, dy: float, dw: float, dh: float) -> None: ...
    @overload
    def drawImage(self, image: CanvasImageSource, sx: float, sy: float, sw: float, sh: float, dx: float, dy: float, dw: float, dh: float) -> None: ...

class CanvasImageData:
    @overload
    def createImageData(self, sw: int, sh: int, settings: Union['ImageDataSettings', 'None'] = {}) -> ImageData: ...
    @overload
    def createImageData(self, imagedata: ImageData) -> ImageData: ...

    def getImageData(self, sx: int, sy: int, sw: int, sh: int, settings: Union['ImageDataSettings', 'None'] = {}) -> ImageData: ...
    @overload
    def putImageData(self, imagedata: ImageData, dx: int, dy: int) -> None: ...
    @overload
    def putImageData(self, imagedata: ImageData, dx: int, dy: int, dirtyX: int, dirtyY: int, dirtyWidth: int, dirtyHeight: int) -> None: ...

class CanvasPathDrawingStyles:
    lineWidth: float
    lineCap: CanvasLineCap
    lineJoin: CanvasLineJoin
    miterLimit: float

    def setLineDash(self, segments: Sequence[float]) -> None: ...

    def getLineDash(self) -> Sequence[float]: ...
    lineDashOffset: float

class CanvasTextDrawingStyles:
    font: str
    textAlign: CanvasTextAlign
    textBaseline: CanvasTextBaseline
    direction: CanvasDirection
    letterSpacing: str
    fontKerning: CanvasFontKerning
    fontStretch: CanvasFontStretch
    fontVariantCaps: CanvasFontVariantCaps
    textRendering: CanvasTextRendering
    wordSpacing: str

class CanvasPath:

    def closePath(self) -> None: ...

    def moveTo(self, x: float, y: float) -> None: ...

    def lineTo(self, x: float, y: float) -> None: ...

    def quadraticCurveTo(self, cpx: float, cpy: float, x: float, y: float) -> None: ...

    def bezierCurveTo(self, cp1x: float, cp1y: float, cp2x: float, cp2y: float, x: float, y: float) -> None: ...

    def arcTo(self, x1: float, y1: float, x2: float, y2: float, radius: float) -> None: ...

    def rect(self, x: float, y: float, w: float, h: float) -> None: ...

    def roundRect(self, x: float, y: float, w: float, h: float, radii: Union['float', 'DOMPointInit', 'Sequence[Union["float", "DOMPointInit"]]', 'None'] = 0) -> None: ...

    def arc(self, x: float, y: float, radius: float, startAngle: float, endAngle: float, counterclockwise: Union['bool', 'None'] = False) -> None: ...

    def ellipse(self, x: float, y: float, radiusX: float, radiusY: float, rotation: float, startAngle: float, endAngle: float, counterclockwise: Union['bool', 'None'] = False) -> None: ...

class CanvasGradient:

    def addColorStop(self, offset: float, color: str) -> None: ...

class CanvasPattern:

    def setTransform(self, transform: Union['DOMMatrix2DInit', 'None'] = {}) -> None: ...

class TextMetrics:
    width: float
    actualBoundingBoxLeft: float
    actualBoundingBoxRight: float
    fontBoundingBoxAscent: float
    fontBoundingBoxDescent: float
    actualBoundingBoxAscent: float
    actualBoundingBoxDescent: float
    emHeightAscent: float
    emHeightDescent: float
    hangingBaseline: float
    alphabeticBaseline: float
    ideographicBaseline: float

class ImageDataSettings(TypedDict):
    colorSpace: NotRequired[PredefinedColorSpace]

class ImageData:
    @overload
    @classmethod
    def new(cls, sw: int, sh: int, settings: Union['ImageDataSettings', 'None'] = {}) -> ImageData: ...
    @overload
    @classmethod
    def new(cls, data: Uint8ClampedArray, sw: int, sh: Union['int', 'None'] = None, settings: Union['ImageDataSettings', 'None'] = {}) -> ImageData: ...
    width: int
    height: int
    data: Uint8ClampedArray
    colorSpace: PredefinedColorSpace

class Path2D(CanvasPath):
    @classmethod
    def new(cls, path: Union['Path2D', 'str', 'None'] = None) -> Path2D: ...

    def addPath(self, path: Path2D, transform: Union['DOMMatrix2DInit', 'None'] = {}) -> None: ...

class ImageBitmapRenderingContext:
    canvas: Union['HTMLCanvasElement', 'OffscreenCanvas']

    def transferFromImageBitmap(self, bitmap: Union['ImageBitmap', 'None']) -> None: ...

class ImageBitmapRenderingContextSettings(TypedDict):
    alpha: NotRequired[bool]

class ImageEncodeOptions(TypedDict):
    type: NotRequired[str]
    quality: NotRequired[float]

class OffscreenCanvas(EventTarget):
    @classmethod
    def new(cls, width: int, height: int) -> OffscreenCanvas: ...
    width: int
    height: int

    def getContext(self, contextId: OffscreenRenderingContextId, options: Union['Any', 'None'] = None) -> Union['OffscreenRenderingContext', 'None']: ...

    def transferToImageBitmap(self) -> ImageBitmap: ...

    def convertToBlob(self, options: Union['ImageEncodeOptions', 'None'] = {}) -> Awaitable[Blob]: ...
    oncontextlost: EventHandler
    oncontextrestored: EventHandler

class OffscreenCanvasRenderingContext2D(CanvasState, CanvasTransform, CanvasCompositing, CanvasImageSmoothing, CanvasFillStrokeStyles, CanvasShadowStyles, CanvasFilters, CanvasRect, CanvasDrawPath, CanvasText, CanvasDrawImage, CanvasImageData, CanvasPathDrawingStyles, CanvasTextDrawingStyles, CanvasPath):

    def commit(self) -> None: ...
    canvas: OffscreenCanvas

class CustomElementRegistry:

    def define(self, name: str, constructor: CustomElementConstructor, options: Union['ElementDefinitionOptions', 'None'] = {}) -> None: ...

    def get(self, name: str) -> Union['CustomElementConstructor', 'None']: ...

    def getName(self, constructor: CustomElementConstructor) -> Union['str', 'None']: ...

    def whenDefined(self, name: str) -> Awaitable[CustomElementConstructor]: ...

    def upgrade(self, root: Node) -> None: ...

class ElementDefinitionOptions(TypedDict):
    extends: NotRequired[str]

class ValidityStateFlags(TypedDict):
    valueMissing: NotRequired[bool]
    typeMismatch: NotRequired[bool]
    patternMismatch: NotRequired[bool]
    tooLong: NotRequired[bool]
    tooShort: NotRequired[bool]
    rangeUnderflow: NotRequired[bool]
    rangeOverflow: NotRequired[bool]
    stepMismatch: NotRequired[bool]
    badInput: NotRequired[bool]
    customError: NotRequired[bool]

class VisibilityStateEntry(PerformanceEntry):
    name: str
    entryType: str
    startTime: DOMHighResTimeStamp
    duration: int

class UserActivation:
    hasBeenActive: bool
    isActive: bool

class ToggleEvent(Event):
    @classmethod
    def new(cls, type: str, eventInitDict: Union['ToggleEventInit', 'None'] = {}) -> ToggleEvent: ...
    oldState: str
    newState: str

class ToggleEventInit(EventInit):
    oldState: NotRequired[str]
    newState: NotRequired[str]

class FocusOptions(TypedDict):
    preventScroll: NotRequired[bool]
    focusVisible: NotRequired[bool]

class ElementContentEditable:
    contentEditable: str
    enterKeyHint: str
    isContentEditable: bool
    inputMode: str
    virtualKeyboardPolicy: str

class DataTransfer:
    @classmethod
    def new(cls) -> DataTransfer: ...
    dropEffect: str
    effectAllowed: str
    items: DataTransferItemList

    def setDragImage(self, image: Element, x: int, y: int) -> None: ...
    types: Sequence[str]

    def getData(self, format: str) -> str: ...

    def setData(self, format: str, data: str) -> None: ...

    def clearData(self, format: Union['str', 'None'] = None) -> None: ...
    files: FileList

class DataTransferItemList:
    length: int

    def __getter__(self, index: int) -> DataTransferItem: ...
    @overload
    def add(self, data: str, type: str) -> Union['DataTransferItem', 'None']: ...
    @overload
    def add(self, data: File) -> Union['DataTransferItem', 'None']: ...

    def remove(self, index: int) -> None: ...

    def clear(self) -> None: ...

class DragEvent(MouseEvent):
    @classmethod
    def new(cls, type: str, eventInitDict: Union['DragEventInit', 'None'] = {}) -> DragEvent: ...
    dataTransfer: Union['DataTransfer', 'None']

class DragEventInit(MouseEventInit):
    dataTransfer: NotRequired[Union['DataTransfer', 'None']]

class PopoverInvokerElement:
    popoverTargetElement: Union['Element', 'None']
    popoverTargetAction: str

class WindowPostMessageOptions(StructuredSerializeOptions):
    targetOrigin: NotRequired[str]

class BarProp:
    visible: bool

class Location:
    href: str
    origin: str
    protocol: str
    host: str
    hostname: str
    port: str
    pathname: str
    search: str
    hash: str

    def assign(self, url: str) -> None: ...

    def replace(self, url: str) -> None: ...

    def reload(self) -> None: ...
    ancestorOrigins: DOMStringList

class History:
    length: int
    scrollRestoration: ScrollRestoration
    state: Any

    def go(self, delta: Union['int', 'None'] = 0) -> None: ...

    def back(self) -> None: ...

    def forward(self) -> None: ...

    def pushState(self, data: Any, unused: str, url: Union['str', 'None'] = None) -> None: ...

    def replaceState(self, data: Any, unused: str, url: Union['str', 'None'] = None) -> None: ...

class Navigation(EventTarget):

    def entries(self) -> Sequence[NavigationHistoryEntry]: ...
    currentEntry: Union['NavigationHistoryEntry', 'None']

    def updateCurrentEntry(self, options: NavigationUpdateCurrentEntryOptions) -> None: ...
    transition: Union['NavigationTransition', 'None']
    canGoBack: bool
    canGoForward: bool

    def navigate(self, url: str, options: Union['NavigationNavigateOptions', 'None'] = {}) -> NavigationResult: ...

    def reload(self, options: Union['NavigationReloadOptions', 'None'] = {}) -> NavigationResult: ...

    def traverseTo(self, key: str, options: Union['NavigationOptions', 'None'] = {}) -> NavigationResult: ...

    def back(self, options: Union['NavigationOptions', 'None'] = {}) -> NavigationResult: ...

    def forward(self, options: Union['NavigationOptions', 'None'] = {}) -> NavigationResult: ...
    onnavigate: EventHandler
    onnavigatesuccess: EventHandler
    onnavigateerror: EventHandler
    oncurrententrychange: EventHandler

class NavigationUpdateCurrentEntryOptions(TypedDict):
    state: Any

class NavigationOptions(TypedDict):
    info: NotRequired[Any]

class NavigationNavigateOptions(NavigationOptions):
    state: NotRequired[Any]
    history: NotRequired[NavigationHistoryBehavior]

class NavigationReloadOptions(NavigationOptions):
    state: NotRequired[Any]

class NavigationResult(TypedDict):
    committed: NotRequired[Awaitable[NavigationHistoryEntry]]
    finished: NotRequired[Awaitable[NavigationHistoryEntry]]

class NavigationHistoryEntry(EventTarget):
    url: Union['str', 'None']
    key: str
    id: str
    index: int
    sameDocument: bool

    def getState(self) -> Any: ...
    ondispose: EventHandler

class NavigationTransition:
    navigationType: NavigationType
    from_: NavigationHistoryEntry
    finished: Awaitable[None]

class NavigateEvent(Event):
    @classmethod
    def new(cls, type: str, eventInitDict: NavigateEventInit) -> NavigateEvent: ...
    navigationType: NavigationType
    destination: NavigationDestination
    canIntercept: bool
    userInitiated: bool
    hashChange: bool
    signal: AbortSignal
    formData: Union['FormData', 'None']
    downloadRequest: Union['str', 'None']
    info: Any
    hasUAVisualTransition: bool

    def intercept(self, options: Union['NavigationInterceptOptions', 'None'] = {}) -> None: ...

    def scroll(self) -> None: ...

class NavigateEventInit(EventInit):
    navigationType: NotRequired[NavigationType]
    destination: NavigationDestination
    canIntercept: NotRequired[bool]
    userInitiated: NotRequired[bool]
    hashChange: NotRequired[bool]
    signal: AbortSignal
    formData: NotRequired[Union['FormData', 'None']]
    downloadRequest: NotRequired[Union['str', 'None']]
    info: NotRequired[Any]
    hasUAVisualTransition: NotRequired[bool]

class NavigationInterceptOptions(TypedDict):
    handler: NotRequired[NavigationInterceptHandler]
    focusReset: NotRequired[NavigationFocusReset]
    scroll: NotRequired[NavigationScrollBehavior]

class NavigationDestination:
    url: str
    key: str
    id: str
    index: int
    sameDocument: bool

    def getState(self) -> Any: ...

class NavigationCurrentEntryChangeEvent(Event):
    @classmethod
    def new(cls, type: str, eventInitDict: NavigationCurrentEntryChangeEventInit) -> NavigationCurrentEntryChangeEvent: ...
    navigationType: Union['NavigationType', 'None']
    from_: NavigationHistoryEntry

class NavigationCurrentEntryChangeEventInit(EventInit):
    navigationType: NotRequired[Union['NavigationType', 'None']]

class PopStateEvent(Event):
    @classmethod
    def new(cls, type: str, eventInitDict: Union['PopStateEventInit', 'None'] = {}) -> PopStateEvent: ...
    state: Any
    hasUAVisualTransition: bool

class PopStateEventInit(EventInit):
    state: NotRequired[Any]
    hasUAVisualTransition: NotRequired[bool]

class HashChangeEvent(Event):
    @classmethod
    def new(cls, type: str, eventInitDict: Union['HashChangeEventInit', 'None'] = {}) -> HashChangeEvent: ...
    oldURL: str
    newURL: str

class HashChangeEventInit(EventInit):
    oldURL: NotRequired[str]
    newURL: NotRequired[str]

class PageTransitionEvent(Event):
    @classmethod
    def new(cls, type: str, eventInitDict: Union['PageTransitionEventInit', 'None'] = {}) -> PageTransitionEvent: ...
    persisted: bool

class PageTransitionEventInit(EventInit):
    persisted: NotRequired[bool]

class BeforeUnloadEvent(Event):
    returnValue: str

class ErrorEvent(Event):
    @classmethod
    def new(cls, type: str, eventInitDict: Union['ErrorEventInit', 'None'] = {}) -> ErrorEvent: ...
    message: str
    filename: str
    lineno: int
    colno: int
    error: Any

class ErrorEventInit(EventInit):
    message: NotRequired[str]
    filename: NotRequired[str]
    lineno: NotRequired[int]
    colno: NotRequired[int]
    error: NotRequired[Any]

class PromiseRejectionEvent(Event):
    @classmethod
    def new(cls, type: str, eventInitDict: PromiseRejectionEventInit) -> PromiseRejectionEvent: ...
    promise: Awaitable[Any]
    reason: Any

class PromiseRejectionEventInit(EventInit):
    promise: Awaitable[Any]
    reason: NotRequired[Any]

class DOMParser:
    @classmethod
    def new(cls) -> DOMParser: ...

    def parseFromString(self, string: str, type: DOMParserSupportedType) -> Document: ...

class NavigatorID:
    appCodeName: str
    appName: str
    appVersion: str
    platform: str
    product: str
    productSub: str
    userAgent: str
    vendor: str
    vendorSub: str

    def taintEnabled(self) -> bool: ...
    oscpu: str

class NavigatorLanguage:
    language: str
    languages: Sequence[str]

class NavigatorOnLine:
    onLine: bool

class NavigatorContentUtils:

    def registerProtocolHandler(self, scheme: str, url: str) -> None: ...

    def unregisterProtocolHandler(self, scheme: str, url: str) -> None: ...

class NavigatorCookies:
    cookieEnabled: bool

class NavigatorPlugins:
    plugins: PluginArray
    mimeTypes: MimeTypeArray

    def javaEnabled(self) -> bool: ...
    pdfViewerEnabled: bool

class PluginArray:

    def refresh(self) -> None: ...
    length: int

    def item(self, index: int) -> Union['Plugin', 'None']: ...

    def namedItem(self, name: str) -> Union['Plugin', 'None']: ...

class MimeTypeArray:
    length: int

    def item(self, index: int) -> Union['MimeType', 'None']: ...

    def namedItem(self, name: str) -> Union['MimeType', 'None']: ...

class Plugin:
    name: str
    description: str
    filename: str
    length: int

    def item(self, index: int) -> Union['MimeType', 'None']: ...

    def namedItem(self, name: str) -> Union['MimeType', 'None']: ...

class MimeType:
    type: str
    description: str
    suffixes: str
    enabledPlugin: Plugin

class ImageBitmap:
    width: int
    height: int

    def close(self) -> None: ...

class ImageBitmapOptions(TypedDict):
    imageOrientation: NotRequired[ImageOrientation]
    premultiplyAlpha: NotRequired[PremultiplyAlpha]
    colorSpaceConversion: NotRequired[ColorSpaceConversion]
    resizeWidth: NotRequired[int]
    resizeHeight: NotRequired[int]
    resizeQuality: NotRequired[ResizeQuality]

class AnimationFrameProvider:

    def requestAnimationFrame(self, callback: FrameRequestCallback) -> int: ...

    def cancelAnimationFrame(self, handle: int) -> None: ...

class DedicatedWorkerGlobalScope(WorkerGlobalScope, AnimationFrameProvider):
    name: str
    @overload
    def postMessage(self, message: Any, transfer: Sequence[object]) -> None: ...
    @overload
    def postMessage(self, message: Any, options: Union['StructuredSerializeOptions', 'None'] = {}) -> None: ...

    def close(self) -> None: ...
    onmessage: EventHandler
    onmessageerror: EventHandler
    onrtctransform: EventHandler

class MessageEvent(Event):
    @classmethod
    def new(cls, type: str, eventInitDict: Union['MessageEventInit', 'None'] = {}) -> MessageEvent: ...
    data: Any
    origin: str
    lastEventId: str
    source: Union['MessageEventSource', 'None']
    ports: Sequence[MessagePort]

    def initMessageEvent(self, type: str, bubbles: Union['bool', 'None'] = False, cancelable: Union['bool', 'None'] = False, data: Union['Any', 'None'] = None, origin: Union['str', 'None'] = "", lastEventId: Union['str', 'None'] = "", source: Union['MessageEventSource', 'None'] = None, ports: Union['Sequence[MessagePort]', 'None'] = []) -> None: ...

class MessageEventInit(EventInit):
    data: NotRequired[Any]
    origin: NotRequired[str]
    lastEventId: NotRequired[str]
    source: NotRequired[Union['MessageEventSource', 'None']]
    ports: NotRequired[Sequence[MessagePort]]

class EventSource(EventTarget):
    @classmethod
    def new(cls, url: str, eventSourceInitDict: Union['EventSourceInit', 'None'] = {}) -> EventSource: ...
    url: str
    withCredentials: bool
    CONNECTING = 0
    OPEN = 1
    CLOSED = 2
    readyState: int
    onopen: EventHandler
    onmessage: EventHandler
    onerror: EventHandler

    def close(self) -> None: ...

class EventSourceInit(TypedDict):
    withCredentials: NotRequired[bool]

class MessageChannel:
    @classmethod
    def new(cls) -> MessageChannel: ...
    port1: MessagePort
    port2: MessagePort

class MessagePort(EventTarget):
    @overload
    def postMessage(self, message: Any, transfer: Sequence[object]) -> None: ...
    @overload
    def postMessage(self, message: Any, options: Union['StructuredSerializeOptions', 'None'] = {}) -> None: ...

    def start(self) -> None: ...

    def close(self) -> None: ...
    onmessage: EventHandler
    onmessageerror: EventHandler

class StructuredSerializeOptions(TypedDict):
    transfer: NotRequired[Sequence[object]]

class BroadcastChannel(EventTarget):
    @classmethod
    def new(cls, name: str) -> BroadcastChannel: ...
    name: str

    def postMessage(self, message: Any) -> None: ...

    def close(self) -> None: ...
    onmessage: EventHandler
    onmessageerror: EventHandler

class SharedWorkerGlobalScope(WorkerGlobalScope):
    name: str

    def close(self) -> None: ...
    onconnect: EventHandler

class AbstractWorker:
    onerror: EventHandler

class Worker(EventTarget, AbstractWorker):
    @classmethod
    def new(cls, scriptURL: str, options: Union['WorkerOptions', 'None'] = {}) -> Worker: ...

    def terminate(self) -> None: ...
    @overload
    def postMessage(self, message: Any, transfer: Sequence[object]) -> None: ...
    @overload
    def postMessage(self, message: Any, options: Union['StructuredSerializeOptions', 'None'] = {}) -> None: ...
    onmessage: EventHandler
    onmessageerror: EventHandler

class WorkerOptions(TypedDict):
    type: NotRequired[WorkerType]
    credentials: NotRequired[RequestCredentials]
    name: NotRequired[str]

class SharedWorker(EventTarget, AbstractWorker):
    @classmethod
    def new(cls, scriptURL: str, options: Union['str', 'WorkerOptions', 'None'] = {}) -> SharedWorker: ...
    port: MessagePort

class NavigatorConcurrentHardware:
    hardwareConcurrency: int

class WorkerLocation:
    href: str
    origin: str
    protocol: str
    host: str
    hostname: str
    port: str
    pathname: str
    search: str
    hash: str

class WorkletGlobalScope: ...

class Worklet:

    def addModule(self, moduleURL: str, options: Union['WorkletOptions', 'None'] = {}) -> Awaitable[None]: ...

class WorkletOptions(TypedDict):
    credentials: NotRequired[RequestCredentials]

class Storage:
    length: int

    def key(self, index: int) -> Union['str', 'None']: ...

    def getItem(self, key: str) -> Union['str', 'None']: ...

    def setItem(self, key: str, value: str) -> None: ...

    def removeItem(self, key: str) -> None: ...

    def clear(self) -> None: ...

class WindowSessionStorage:
    sessionStorage: Storage

class WindowLocalStorage:
    localStorage: Storage

class StorageEvent(Event):
    @classmethod
    def new(cls, type: str, eventInitDict: Union['StorageEventInit', 'None'] = {}) -> StorageEvent: ...
    key: Union['str', 'None']
    oldValue: Union['str', 'None']
    newValue: Union['str', 'None']
    url: str
    storageArea: Union['Storage', 'None']

    def initStorageEvent(self, type: str, bubbles: Union['bool', 'None'] = False, cancelable: Union['bool', 'None'] = False, key: Union['str', 'None'] = None, oldValue: Union['str', 'None'] = None, newValue: Union['str', 'None'] = None, url: Union['str', 'None'] = "", storageArea: Union['Storage', 'None'] = None) -> None: ...

class StorageEventInit(EventInit):
    key: NotRequired[Union['str', 'None']]
    oldValue: NotRequired[Union['str', 'None']]
    newValue: NotRequired[Union['str', 'None']]
    url: NotRequired[str]
    storageArea: NotRequired[Union['Storage', 'None']]

class HTMLMarqueeElement(HTMLElement):
    @classmethod
    def new(cls) -> HTMLMarqueeElement: ...
    behavior: str
    bgColor: str
    direction: str
    height: str
    hspace: int
    loop: int
    scrollAmount: int
    scrollDelay: int
    trueSpeed: bool
    vspace: int
    width: str

    def start(self) -> None: ...

    def stop(self) -> None: ...

class HTMLFrameSetElement(HTMLElement, WindowEventHandlers):
    @classmethod
    def new(cls) -> HTMLFrameSetElement: ...
    cols: str
    rows: str

class HTMLFrameElement(HTMLElement):
    @classmethod
    def new(cls) -> HTMLFrameElement: ...
    name: str
    scrolling: str
    src: str
    frameBorder: str
    longDesc: str
    noResize: bool
    contentDocument: Union['Document', 'None']
    contentWindow: Union['WindowProxy', 'None']
    marginHeight: str
    marginWidth: str

class HTMLDirectoryElement(HTMLElement):
    @classmethod
    def new(cls) -> HTMLDirectoryElement: ...
    compact: bool

class HTMLFontElement(HTMLElement):
    @classmethod
    def new(cls) -> HTMLFontElement: ...
    color: str
    face: str
    size: str

class HTMLParamElement(HTMLElement):
    @classmethod
    def new(cls) -> HTMLParamElement: ...
    name: str
    value: str
    type: str
    valueType: str

class External:

    def AddSearchProvider(self) -> None: ...

    def IsSearchProviderInstalled(self) -> None: ...

class IdleOptions(TypedDict):
    threshold: NotRequired[int]
    signal: NotRequired[AbortSignal]

class IdleDetector(EventTarget):
    @classmethod
    def new(cls) -> IdleDetector: ...
    userState: Union['UserIdleState', 'None']
    screenState: Union['ScreenIdleState', 'None']
    onchange: EventHandler

    def start(self, options: Union['IdleOptions', 'None'] = {}) -> Awaitable[None]: ...

class ImageCapture:
    @classmethod
    def new(cls, videoTrack: MediaStreamTrack) -> ImageCapture: ...

    def takePhoto(self, photoSettings: Union['PhotoSettings', 'None'] = {}) -> Awaitable[Blob]: ...

    def getPhotoCapabilities(self) -> Awaitable[PhotoCapabilities]: ...

    def getPhotoSettings(self) -> Awaitable[PhotoSettings]: ...

    def grabFrame(self) -> Awaitable[ImageBitmap]: ...
    track: MediaStreamTrack

class PhotoCapabilities(TypedDict):
    redEyeReduction: NotRequired[RedEyeReduction]
    imageHeight: NotRequired[MediaSettingsRange]
    imageWidth: NotRequired[MediaSettingsRange]
    fillLightMode: NotRequired[Sequence[FillLightMode]]

class PhotoSettings(TypedDict):
    fillLightMode: NotRequired[FillLightMode]
    imageHeight: NotRequired[float]
    imageWidth: NotRequired[float]
    redEyeReduction: NotRequired[bool]

class MediaSettingsRange(TypedDict):
    max: NotRequired[float]
    min: NotRequired[float]
    step: NotRequired[float]

class MediaTrackSupportedConstraints(TypedDict):
    whiteBalanceMode: NotRequired[bool]
    exposureMode: NotRequired[bool]
    focusMode: NotRequired[bool]
    pointsOfInterest: NotRequired[bool]
    exposureCompensation: NotRequired[bool]
    exposureTime: NotRequired[bool]
    colorTemperature: NotRequired[bool]
    iso: NotRequired[bool]
    brightness: NotRequired[bool]
    contrast: NotRequired[bool]
    pan: NotRequired[bool]
    saturation: NotRequired[bool]
    sharpness: NotRequired[bool]
    focusDistance: NotRequired[bool]
    tilt: NotRequired[bool]
    zoom: NotRequired[bool]
    torch: NotRequired[bool]
    width: NotRequired[bool]
    height: NotRequired[bool]
    aspectRatio: NotRequired[bool]
    frameRate: NotRequired[bool]
    facingMode: NotRequired[bool]
    resizeMode: NotRequired[bool]
    sampleRate: NotRequired[bool]
    sampleSize: NotRequired[bool]
    echoCancellation: NotRequired[bool]
    autoGainControl: NotRequired[bool]
    noiseSuppression: NotRequired[bool]
    latency: NotRequired[bool]
    channelCount: NotRequired[bool]
    deviceId: NotRequired[bool]
    groupId: NotRequired[bool]
    displaySurface: NotRequired[bool]
    logicalSurface: NotRequired[bool]
    cursor: NotRequired[bool]
    restrictOwnAudio: NotRequired[bool]
    suppressLocalAudioPlayback: NotRequired[bool]

class MediaTrackCapabilities(TypedDict):
    whiteBalanceMode: NotRequired[Sequence[str]]
    exposureMode: NotRequired[Sequence[str]]
    focusMode: NotRequired[Sequence[str]]
    exposureCompensation: NotRequired[MediaSettingsRange]
    exposureTime: NotRequired[MediaSettingsRange]
    colorTemperature: NotRequired[MediaSettingsRange]
    iso: NotRequired[MediaSettingsRange]
    brightness: NotRequired[MediaSettingsRange]
    contrast: NotRequired[MediaSettingsRange]
    saturation: NotRequired[MediaSettingsRange]
    sharpness: NotRequired[MediaSettingsRange]
    focusDistance: NotRequired[MediaSettingsRange]
    pan: NotRequired[MediaSettingsRange]
    tilt: NotRequired[MediaSettingsRange]
    zoom: NotRequired[MediaSettingsRange]
    torch: NotRequired[bool]
    width: NotRequired[ULongRange]
    height: NotRequired[ULongRange]
    aspectRatio: NotRequired[DoubleRange]
    frameRate: NotRequired[DoubleRange]
    facingMode: NotRequired[Sequence[str]]
    resizeMode: NotRequired[Sequence[str]]
    sampleRate: NotRequired[ULongRange]
    sampleSize: NotRequired[ULongRange]
    echoCancellation: NotRequired[Sequence[bool]]
    autoGainControl: NotRequired[Sequence[bool]]
    noiseSuppression: NotRequired[Sequence[bool]]
    latency: NotRequired[DoubleRange]
    channelCount: NotRequired[ULongRange]
    deviceId: NotRequired[str]
    groupId: NotRequired[str]
    displaySurface: NotRequired[str]
    logicalSurface: NotRequired[bool]
    cursor: NotRequired[Sequence[str]]

class MediaTrackConstraintSet(TypedDict):
    whiteBalanceMode: NotRequired[ConstrainDOMString]
    exposureMode: NotRequired[ConstrainDOMString]
    focusMode: NotRequired[ConstrainDOMString]
    pointsOfInterest: NotRequired[ConstrainPoint2D]
    exposureCompensation: NotRequired[ConstrainDouble]
    exposureTime: NotRequired[ConstrainDouble]
    colorTemperature: NotRequired[ConstrainDouble]
    iso: NotRequired[ConstrainDouble]
    brightness: NotRequired[ConstrainDouble]
    contrast: NotRequired[ConstrainDouble]
    saturation: NotRequired[ConstrainDouble]
    sharpness: NotRequired[ConstrainDouble]
    focusDistance: NotRequired[ConstrainDouble]
    pan: NotRequired[Union['bool', 'ConstrainDouble']]
    tilt: NotRequired[Union['bool', 'ConstrainDouble']]
    zoom: NotRequired[Union['bool', 'ConstrainDouble']]
    torch: NotRequired[ConstrainBoolean]
    width: NotRequired[ConstrainULong]
    height: NotRequired[ConstrainULong]
    aspectRatio: NotRequired[ConstrainDouble]
    frameRate: NotRequired[ConstrainDouble]
    facingMode: NotRequired[ConstrainDOMString]
    resizeMode: NotRequired[ConstrainDOMString]
    sampleRate: NotRequired[ConstrainULong]
    sampleSize: NotRequired[ConstrainULong]
    echoCancellation: NotRequired[ConstrainBoolean]
    autoGainControl: NotRequired[ConstrainBoolean]
    noiseSuppression: NotRequired[ConstrainBoolean]
    latency: NotRequired[ConstrainDouble]
    channelCount: NotRequired[ConstrainULong]
    deviceId: NotRequired[ConstrainDOMString]
    groupId: NotRequired[ConstrainDOMString]
    displaySurface: NotRequired[ConstrainDOMString]
    logicalSurface: NotRequired[ConstrainBoolean]
    cursor: NotRequired[ConstrainDOMString]
    restrictOwnAudio: NotRequired[ConstrainBoolean]
    suppressLocalAudioPlayback: NotRequired[ConstrainBoolean]

class MediaTrackSettings(TypedDict):
    whiteBalanceMode: NotRequired[str]
    exposureMode: NotRequired[str]
    focusMode: NotRequired[str]
    pointsOfInterest: NotRequired[Sequence[Point2D]]
    exposureCompensation: NotRequired[float]
    exposureTime: NotRequired[float]
    colorTemperature: NotRequired[float]
    iso: NotRequired[float]
    brightness: NotRequired[float]
    contrast: NotRequired[float]
    saturation: NotRequired[float]
    sharpness: NotRequired[float]
    focusDistance: NotRequired[float]
    pan: NotRequired[float]
    tilt: NotRequired[float]
    zoom: NotRequired[float]
    torch: NotRequired[bool]
    width: NotRequired[int]
    height: NotRequired[int]
    aspectRatio: NotRequired[float]
    frameRate: NotRequired[float]
    facingMode: NotRequired[str]
    resizeMode: NotRequired[str]
    sampleRate: NotRequired[int]
    sampleSize: NotRequired[int]
    echoCancellation: NotRequired[bool]
    autoGainControl: NotRequired[bool]
    noiseSuppression: NotRequired[bool]
    latency: NotRequired[float]
    channelCount: NotRequired[int]
    deviceId: NotRequired[str]
    groupId: NotRequired[str]
    displaySurface: NotRequired[str]
    logicalSurface: NotRequired[bool]
    cursor: NotRequired[str]
    restrictOwnAudio: NotRequired[bool]
    suppressLocalAudioPlayback: NotRequired[bool]

class ConstrainPoint2DParameters(TypedDict):
    exact: NotRequired[Sequence[Point2D]]
    ideal: NotRequired[Sequence[Point2D]]

class Point2D(TypedDict):
    x: NotRequired[float]
    y: NotRequired[float]

class ImageResource(TypedDict):
    src: str
    sizes: NotRequired[str]
    type: NotRequired[str]
    label: NotRequired[str]

class Ink:

    def requestPresenter(self, param: Union['InkPresenterParam', 'None'] = {}) -> Awaitable[InkPresenter]: ...

class InkPresenterParam(TypedDict):
    presentationArea: NotRequired[Union['Element', 'None']]

class InkPresenter:
    presentationArea: Union['Element', 'None']
    expectedImprovement: int

    def updateInkTrailStartPoint(self, event: PointerEvent, style: InkTrailStyle) -> None: ...

class InkTrailStyle(TypedDict):
    color: str
    diameter: float

class InputDeviceCapabilities:
    @classmethod
    def new(cls, deviceInitDict: Union['InputDeviceCapabilitiesInit', 'None'] = {}) -> InputDeviceCapabilities: ...
    firesTouchEvents: bool
    pointerMovementScrolls: bool

class InputDeviceCapabilitiesInit(TypedDict):
    firesTouchEvents: NotRequired[bool]
    pointerMovementScrolls: NotRequired[bool]

class UIEvent(Event):
    @classmethod
    def new(cls, type: str, eventInitDict: Union['UIEventInit', 'None'] = {}) -> UIEvent: ...
    sourceCapabilities: Union['InputDeviceCapabilities', 'None']
    view: Union['Window', 'None']
    detail: int

    def initUIEvent(self, typeArg: str, bubblesArg: Union['bool', 'None'] = False, cancelableArg: Union['bool', 'None'] = False, viewArg: Union['Window', 'None'] = None, detailArg: Union['int', 'None'] = 0) -> None: ...
    which: int

class UIEventInit(TypedDict, EventInit):
    sourceCapabilities: NotRequired[Union['InputDeviceCapabilities', 'None']]
    view: NotRequired[Union['Window', 'None']]
    detail: NotRequired[int]
    which: NotRequired[int]

class InputEvent(UIEvent):
    @classmethod
    def new(cls, type: str, eventInitDict: Union['InputEventInit', 'None'] = {}) -> InputEvent: ...
    dataTransfer: Union['DataTransfer', 'None']

    def getTargetRanges(self) -> Sequence[StaticRange]: ...
    data: Union['str', 'None']
    isComposing: bool
    inputType: str

class InputEventInit(TypedDict, UIEventInit):
    dataTransfer: NotRequired[Union['DataTransfer', 'None']]
    targetRanges: NotRequired[Sequence[StaticRange]]
    data: NotRequired[Union['str', 'None']]
    isComposing: NotRequired[bool]
    inputType: NotRequired[str]

class IntersectionObserver:
    @classmethod
    def new(cls, callback: IntersectionObserverCallback, options: Union['IntersectionObserverInit', 'None'] = {}) -> IntersectionObserver: ...
    root: Union['Element', 'Document', 'None']
    rootMargin: str
    thresholds: Sequence[float]

    def observe(self, target: Element) -> None: ...

    def unobserve(self, target: Element) -> None: ...

    def disconnect(self) -> None: ...

    def takeRecords(self) -> Sequence[IntersectionObserverEntry]: ...

class IntersectionObserverEntry:
    @classmethod
    def new(cls, intersectionObserverEntryInit: IntersectionObserverEntryInit) -> IntersectionObserverEntry: ...
    time: DOMHighResTimeStamp
    rootBounds: Union['DOMRectReadOnly', 'None']
    boundingClientRect: DOMRectReadOnly
    intersectionRect: DOMRectReadOnly
    isIntersecting: bool
    intersectionRatio: float
    target: Element

class IntersectionObserverEntryInit(TypedDict):
    time: DOMHighResTimeStamp
    rootBounds: Union['DOMRectInit', 'None']
    boundingClientRect: DOMRectInit
    intersectionRect: DOMRectInit
    isIntersecting: bool
    intersectionRatio: float
    target: Element

class IntersectionObserverInit(TypedDict):
    root: NotRequired[Union['Element', 'Document', 'None']]
    rootMargin: NotRequired[str]
    threshold: NotRequired[Union['float', 'Sequence[float]']]

class InterventionReportBody(ReportBody):

    def toJSON(self) -> object: ...
    id: str
    message: str
    sourceFile: Union['str', 'None']
    lineNumber: Union['int', 'None']
    columnNumber: Union['int', 'None']

class IsInputPendingOptions(TypedDict):
    includeContinuous: NotRequired[bool]

class Scheduling:

    def isInputPending(self, isInputPendingOptions: Union['IsInputPendingOptions', 'None'] = {}) -> bool: ...

class Profiler(EventTarget):
    @classmethod
    def new(cls, options: ProfilerInitOptions) -> Profiler: ...
    sampleInterval: DOMHighResTimeStamp
    stopped: bool

    def stop(self) -> Awaitable[ProfilerTrace]: ...

class ProfilerTrace(TypedDict):
    resources: Sequence[ProfilerResource]
    frames: Sequence[ProfilerFrame]
    stacks: Sequence[ProfilerStack]
    samples: Sequence[ProfilerSample]

class ProfilerSample(TypedDict):
    timestamp: DOMHighResTimeStamp
    stackId: NotRequired[int]

class ProfilerStack(TypedDict):
    parentId: NotRequired[int]
    frameId: int

class ProfilerFrame(TypedDict):
    name: str
    resourceId: NotRequired[int]
    line: NotRequired[int]
    column: NotRequired[int]

class ProfilerInitOptions(TypedDict):
    sampleInterval: DOMHighResTimeStamp
    maxBufferSize: int

class JsonLd: ...

class JsonLdProcessor:
    @classmethod
    def new(cls) -> JsonLdProcessor: ...

class RdfDataset:
    @classmethod
    def new(cls) -> RdfDataset: ...
    defaultGraph: RdfGraph

    def add(self, graphName: str, graph: RdfGraph) -> None: ...

class RdfGraph:
    @classmethod
    def new(cls) -> RdfGraph: ...

    def add(self, triple: RdfTriple) -> None: ...

class RdfTriple:
    @classmethod
    def new(cls) -> RdfTriple: ...
    subject: str
    predicate: str
    object: Union['str', 'RdfLiteral']

class RdfLiteral:
    @classmethod
    def new(cls) -> RdfLiteral: ...
    value: str
    datatype: str
    language: Union['str', 'None']

class JsonLdOptions(TypedDict):
    base: NotRequired[Union['str', 'None']]
    compactArrays: NotRequired[bool]
    compactToRelative: NotRequired[bool]
    documentLoader: NotRequired[Union['LoadDocumentCallback', 'None']]
    expandContext: NotRequired[Union['Union["JsonLdRecord", "None"]', 'str']]
    extractAllScripts: NotRequired[bool]
    frameExpansion: NotRequired[bool]
    ordered: NotRequired[bool]
    processingMode: NotRequired[str]
    produceGeneralizedRdf: NotRequired[bool]
    rdfDirection: NotRequired[Union['str', 'None']]
    useNativeTypes: NotRequired[bool]
    useRdfType: NotRequired[bool]
    embed: NotRequired[Union['JsonLdEmbed', 'bool']]
    explicit: NotRequired[bool]
    omitDefault: NotRequired[bool]
    omitGraph: NotRequired[bool]
    requireAll: NotRequired[bool]
    frameDefault: NotRequired[bool]

class LoadDocumentOptions(TypedDict):
    extractAllScripts: NotRequired[bool]
    profile: NotRequired[str]
    requestProfile: NotRequired[Union['str', 'Sequence[str]']]

class RemoteDocument:
    @classmethod
    def new(cls) -> RemoteDocument: ...
    contentType: str
    contextUrl: str
    document: Any
    documentUrl: str
    profile: str

class JsonLdError(TypedDict):
    code: NotRequired[JsonLdErrorCode]
    message: NotRequired[Union['str', 'None']]

class JsonLdFramingError(TypedDict):
    code: NotRequired[JsonLdFramingErrorCode]
    message: NotRequired[Union['str', 'None']]

class Keyboard(EventTarget):

    def lock(self, keyCodes: Union['Sequence[str]', 'None'] = []) -> Awaitable[None]: ...

    def unlock(self) -> None: ...

    def getLayoutMap(self) -> Awaitable[KeyboardLayoutMap]: ...
    onlayoutchange: EventHandler

class KeyboardLayoutMap: ...

class LargestContentfulPaint(PerformanceEntry):
    renderTime: DOMHighResTimeStamp
    loadTime: DOMHighResTimeStamp
    size: int
    id: str
    url: str
    element: Union['Element', 'None']

    def toJSON(self) -> object: ...

class LayoutShift(PerformanceEntry):
    value: float
    hadRecentInput: bool
    lastInputTime: DOMHighResTimeStamp
    sources: Sequence[LayoutShiftAttribution]

    def toJSON(self) -> object: ...

class LayoutShiftAttribution:
    node: Union['Node', 'None']
    previousRect: DOMRectReadOnly
    currentRect: DOMRectReadOnly

class QueryOptions(TypedDict):
    postscriptNames: NotRequired[Sequence[str]]

class FontData:

    def blob(self) -> Awaitable[Blob]: ...
    postscriptName: str
    fullName: str
    family: str
    style: str

class PerformanceLongTaskTiming(PerformanceEntry):
    attribution: Sequence[TaskAttributionTiming]

    def toJSON(self) -> object: ...

class TaskAttributionTiming(PerformanceEntry):
    containerType: str
    containerSrc: str
    containerId: str
    containerName: str

    def toJSON(self) -> object: ...

class Magnetometer(Sensor):
    @classmethod
    def new(cls, sensorOptions: Union['MagnetometerSensorOptions', 'None'] = {}) -> Magnetometer: ...
    x: Union['float', 'None']
    y: Union['float', 'None']
    z: Union['float', 'None']

class MagnetometerSensorOptions(SensorOptions):
    referenceFrame: NotRequired[MagnetometerLocalCoordinateSystem]

class UncalibratedMagnetometer(Sensor):
    @classmethod
    def new(cls, sensorOptions: Union['MagnetometerSensorOptions', 'None'] = {}) -> UncalibratedMagnetometer: ...
    x: Union['float', 'None']
    y: Union['float', 'None']
    z: Union['float', 'None']
    xBias: Union['float', 'None']
    yBias: Union['float', 'None']
    zBias: Union['float', 'None']

class MagnetometerReadingValues(TypedDict):
    x: Union['float', 'None']
    y: Union['float', 'None']
    z: Union['float', 'None']

class UncalibratedMagnetometerReadingValues(TypedDict):
    x: Union['float', 'None']
    y: Union['float', 'None']
    z: Union['float', 'None']
    xBias: Union['float', 'None']
    yBias: Union['float', 'None']
    zBias: Union['float', 'None']

class BeforeInstallPromptEvent(Event):
    @classmethod
    def new(cls, type: str, eventInitDict: Union['EventInit', 'None'] = {}) -> BeforeInstallPromptEvent: ...

    def prompt(self) -> Awaitable[PromptResponseObject]: ...

class PromptResponseObject(TypedDict):
    userChoice: NotRequired[AppBannerPromptOutcome]

class MediaConfiguration(TypedDict):
    video: NotRequired[VideoConfiguration]
    audio: NotRequired[AudioConfiguration]

class MediaDecodingConfiguration(MediaConfiguration):
    type: MediaDecodingType
    keySystemConfiguration: NotRequired[MediaCapabilitiesKeySystemConfiguration]

class MediaEncodingConfiguration(MediaConfiguration):
    type: MediaEncodingType

class VideoConfiguration(TypedDict):
    contentType: str
    width: int
    height: int
    bitrate: int
    framerate: float
    hasAlphaChannel: NotRequired[bool]
    hdrMetadataType: NotRequired[HdrMetadataType]
    colorGamut: NotRequired[ColorGamut]
    transferFunction: NotRequired[TransferFunction]
    scalabilityMode: NotRequired[str]
    spatialScalability: NotRequired[bool]

class AudioConfiguration(TypedDict):
    contentType: str
    channels: NotRequired[str]
    bitrate: NotRequired[int]
    samplerate: NotRequired[int]
    spatialRendering: NotRequired[bool]

class MediaCapabilitiesKeySystemConfiguration(TypedDict):
    keySystem: str
    initDataType: NotRequired[str]
    distinctiveIdentifier: NotRequired[MediaKeysRequirement]
    persistentState: NotRequired[MediaKeysRequirement]
    sessionTypes: NotRequired[Sequence[str]]
    audio: NotRequired[KeySystemTrackConfiguration]
    video: NotRequired[KeySystemTrackConfiguration]

class KeySystemTrackConfiguration(TypedDict):
    robustness: NotRequired[str]
    encryptionScheme: NotRequired[Union['str', 'None']]

class MediaCapabilitiesInfo(TypedDict):
    supported: bool
    smooth: bool
    powerEfficient: bool

class MediaCapabilitiesDecodingInfo(MediaCapabilitiesInfo):
    keySystemAccess: MediaKeySystemAccess
    configuration: NotRequired[MediaDecodingConfiguration]

class MediaCapabilitiesEncodingInfo(MediaCapabilitiesInfo):
    configuration: NotRequired[MediaEncodingConfiguration]

class MediaCapabilities:

    def decodingInfo(self, configuration: MediaDecodingConfiguration) -> Awaitable[MediaCapabilitiesDecodingInfo]: ...

    def encodingInfo(self, configuration: MediaEncodingConfiguration) -> Awaitable[MediaCapabilitiesEncodingInfo]: ...

class VideoPlaybackQuality:
    creationTime: DOMHighResTimeStamp
    droppedVideoFrames: int
    totalVideoFrames: int
    corruptedVideoFrames: int

class MediaSource(EventTarget):
    @classmethod
    def new(cls) -> MediaSource: ...
    handle: MediaSourceHandle
    sourceBuffers: SourceBufferList
    activeSourceBuffers: SourceBufferList
    readyState: ReadyState
    duration: float
    onsourceopen: EventHandler
    onsourceended: EventHandler
    onsourceclose: EventHandler

    def addSourceBuffer(self, type: str) -> SourceBuffer: ...

    def removeSourceBuffer(self, sourceBuffer: SourceBuffer) -> None: ...

    def endOfStream(self, error: Union['EndOfStreamError', 'None'] = None) -> None: ...

    def setLiveSeekableRange(self, start: float, end: float) -> None: ...

    def clearLiveSeekableRange(self) -> None: ...

class MediaSourceHandle: ...

class SourceBuffer(EventTarget):
    mode: AppendMode
    updating: bool
    buffered: TimeRanges
    timestampOffset: float
    audioTracks: AudioTrackList
    videoTracks: VideoTrackList
    textTracks: TextTrackList
    appendWindowStart: float
    appendWindowEnd: float
    onupdatestart: EventHandler
    onupdate: EventHandler
    onupdateend: EventHandler
    onerror: EventHandler
    onabort: EventHandler

    def appendBuffer(self, data: BufferSource) -> None: ...

    def abort(self) -> None: ...

    def changeType(self, type: str) -> None: ...

    def remove(self, start: float, end: float) -> None: ...

class SourceBufferList(EventTarget):
    length: int
    onaddsourcebuffer: EventHandler
    onremovesourcebuffer: EventHandler

    def __getter__(self, index: int) -> SourceBuffer: ...

class MockCapturePromptResultConfiguration(TypedDict):
    getUserMedia: NotRequired[MockCapturePromptResult]
    getDisplayMedia: NotRequired[MockCapturePromptResult]

class MockCaptureDeviceConfiguration(TypedDict):
    label: NotRequired[str]
    deviceId: NotRequired[str]
    groupId: NotRequired[str]

class MockCameraConfiguration(MockCaptureDeviceConfiguration):
    defaultFrameRate: NotRequired[float]
    facingMode: NotRequired[str]

class MockMicrophoneConfiguration(MockCaptureDeviceConfiguration):
    defaultSampleRate: NotRequired[int]

class CanvasCaptureMediaStreamTrack(MediaStreamTrack):
    canvas: HTMLCanvasElement

    def requestFrame(self) -> None: ...

class CaptureActionEvent(Event):
    @classmethod
    def new(cls, init: Union['CaptureActionEventInit', 'None'] = {}) -> CaptureActionEvent: ...
    action: CaptureAction

class CaptureActionEventInit(EventInit):
    action: NotRequired[str]

class CropTarget: ...

class MediaStream(EventTarget):
    @overload
    @classmethod
    def new(cls) -> MediaStream: ...
    @overload
    @classmethod
    def new(cls, stream: MediaStream) -> MediaStream: ...
    @overload
    @classmethod
    def new(cls, tracks: Sequence[MediaStreamTrack]) -> MediaStream: ...
    id: str

    def getAudioTracks(self) -> Sequence[MediaStreamTrack]: ...

    def getVideoTracks(self) -> Sequence[MediaStreamTrack]: ...

    def getTracks(self) -> Sequence[MediaStreamTrack]: ...

    def getTrackById(self, trackId: str) -> Union['MediaStreamTrack', 'None']: ...

    def addTrack(self, track: MediaStreamTrack) -> None: ...

    def removeTrack(self, track: MediaStreamTrack) -> None: ...

    def clone(self) -> MediaStream: ...
    active: bool
    onaddtrack: EventHandler
    onremovetrack: EventHandler

class MediaTrackConstraints(MediaTrackConstraintSet):
    advanced: NotRequired[Sequence[MediaTrackConstraintSet]]

class MediaStreamTrackEvent(Event):
    @classmethod
    def new(cls, type: str, eventInitDict: MediaStreamTrackEventInit) -> MediaStreamTrackEvent: ...
    track: MediaStreamTrack

class MediaStreamTrackEventInit(EventInit):
    track: MediaStreamTrack

class OverconstrainedError(DOMException):
    @classmethod
    def new(cls, constraint: str, message: Union['str', 'None'] = "") -> OverconstrainedError: ...
    constraint: str

class MediaDeviceInfo:
    deviceId: str
    kind: MediaDeviceKind
    label: str
    groupId: str

    def toJSON(self) -> object: ...

class InputDeviceInfo(MediaDeviceInfo):

    def getCapabilities(self) -> MediaTrackCapabilities: ...

class MediaStreamConstraints(TypedDict):
    video: NotRequired[Union['bool', 'MediaTrackConstraints']]
    audio: NotRequired[Union['bool', 'MediaTrackConstraints']]
    preferCurrentTab: NotRequired[bool]
    peerIdentity: NotRequired[str]

class DoubleRange(TypedDict):
    max: NotRequired[float]
    min: NotRequired[float]

class ConstrainDoubleRange(DoubleRange):
    exact: NotRequired[float]
    ideal: NotRequired[float]

class ULongRange(TypedDict):
    max: NotRequired[int]
    min: NotRequired[int]

class ConstrainULongRange(ULongRange):
    exact: NotRequired[int]
    ideal: NotRequired[int]

class ConstrainBooleanParameters(TypedDict):
    exact: NotRequired[bool]
    ideal: NotRequired[bool]

class ConstrainDOMStringParameters(TypedDict):
    exact: NotRequired[Union['str', 'Sequence[str]']]
    ideal: NotRequired[Union['str', 'Sequence[str]']]

class CameraDevicePermissionDescriptor(PermissionDescriptor):
    panTiltZoom: NotRequired[bool]

class MediaStreamTrackProcessor:
    @classmethod
    def new(cls, init: MediaStreamTrackProcessorInit) -> MediaStreamTrackProcessor: ...
    readable: ReadableStream

class MediaStreamTrackProcessorInit(TypedDict):
    track: MediaStreamTrack
    maxBufferSize: NotRequired[int]

class VideoTrackGenerator:
    @classmethod
    def new(cls) -> VideoTrackGenerator: ...
    writable: WritableStream
    muted: bool
    track: MediaStreamTrack

class ViewportMediaStreamConstraints(TypedDict):
    video: NotRequired[Union['bool', 'MediaTrackConstraints']]
    audio: NotRequired[Union['bool', 'MediaTrackConstraints']]

class MediaSession:
    metadata: Union['MediaMetadata', 'None']
    playbackState: MediaSessionPlaybackState

    def setActionHandler(self, action: MediaSessionAction, handler: Union['MediaSessionActionHandler', 'None']) -> None: ...

    def setPositionState(self, state: Union['MediaPositionState', 'None'] = {}) -> None: ...

    def setMicrophoneActive(self, active: bool) -> None: ...

    def setCameraActive(self, active: bool) -> None: ...

class MediaMetadata:
    @classmethod
    def new(cls, init: Union['MediaMetadataInit', 'None'] = {}) -> MediaMetadata: ...
    title: str
    artist: str
    album: str
    artwork: Sequence[MediaImage]

class MediaMetadataInit(TypedDict):
    title: NotRequired[str]
    artist: NotRequired[str]
    album: NotRequired[str]
    artwork: NotRequired[Sequence[MediaImage]]

class MediaImage(TypedDict):
    src: str
    sizes: NotRequired[str]
    type: NotRequired[str]

class MediaPositionState(TypedDict):
    duration: NotRequired[float]
    playbackRate: NotRequired[float]
    position: NotRequired[float]

class MediaSessionActionDetails(TypedDict):
    action: MediaSessionAction
    seekOffset: NotRequired[float]
    seekTime: NotRequired[float]
    fastSeek: NotRequired[bool]

class MediaRecorder(EventTarget):
    @classmethod
    def new(cls, stream: MediaStream, options: Union['MediaRecorderOptions', 'None'] = {}) -> MediaRecorder: ...
    stream: MediaStream
    mimeType: str
    state: RecordingState
    onstart: EventHandler
    onstop: EventHandler
    ondataavailable: EventHandler
    onpause: EventHandler
    onresume: EventHandler
    onerror: EventHandler
    videoBitsPerSecond: int
    audioBitsPerSecond: int
    audioBitrateMode: BitrateMode

    def start(self, timeslice: Union['int', 'None'] = None) -> None: ...

    def stop(self) -> None: ...

    def pause(self) -> None: ...

    def resume(self) -> None: ...

    def requestData(self) -> None: ...

class MediaRecorderOptions(TypedDict):
    mimeType: NotRequired[str]
    audioBitsPerSecond: NotRequired[int]
    videoBitsPerSecond: NotRequired[int]
    bitsPerSecond: NotRequired[int]
    audioBitrateMode: NotRequired[BitrateMode]
    videoKeyFrameIntervalDuration: NotRequired[DOMHighResTimeStamp]
    videoKeyFrameIntervalCount: NotRequired[int]

class BlobEvent(Event):
    @classmethod
    def new(cls, type: str, eventInitDict: BlobEventInit) -> BlobEvent: ...
    data: Blob
    timecode: DOMHighResTimeStamp

class BlobEventInit(TypedDict):
    data: Blob
    timecode: NotRequired[DOMHighResTimeStamp]

class HTMLModelElement(HTMLElement): ...

class RTCRtpSendParameters(TypedDict, RTCRtpParameters):
    degradationPreference: NotRequired[RTCDegradationPreference]
    transactionId: str
    encodings: Sequence[RTCRtpEncodingParameters]

class PerformanceNavigationTiming(PerformanceResourceTiming):
    unloadEventStart: DOMHighResTimeStamp
    unloadEventEnd: DOMHighResTimeStamp
    domInteractive: DOMHighResTimeStamp
    domContentLoadedEventStart: DOMHighResTimeStamp
    domContentLoadedEventEnd: DOMHighResTimeStamp
    domComplete: DOMHighResTimeStamp
    loadEventStart: DOMHighResTimeStamp
    loadEventEnd: DOMHighResTimeStamp
    type: NavigationTimingType
    redirectCount: int
    criticalCHRestart: DOMHighResTimeStamp

    def toJSON(self) -> object: ...
    activationStart: DOMHighResTimeStamp

class PerformanceTiming:
    navigationStart: int
    unloadEventStart: int
    unloadEventEnd: int
    redirectStart: int
    redirectEnd: int
    fetchStart: int
    domainLookupStart: int
    domainLookupEnd: int
    connectStart: int
    connectEnd: int
    secureConnectionStart: int
    requestStart: int
    responseStart: int
    responseEnd: int
    domLoading: int
    domInteractive: int
    domContentLoadedEventStart: int
    domContentLoadedEventEnd: int
    domComplete: int
    loadEventStart: int
    loadEventEnd: int

    def toJSON(self) -> object: ...

class PerformanceNavigation:
    TYPE_NAVIGATE = 0
    TYPE_RELOAD = 1
    TYPE_BACK_FORWARD = 2
    TYPE_RESERVED = 255
    type: int
    redirectCount: int

    def toJSON(self) -> object: ...

class NavigatorNetworkInformation:
    connection: NetworkInformation

class NetworkInformation(EventTarget, NetworkInformationSaveData):
    type: ConnectionType
    effectiveType: EffectiveConnectionType
    downlinkMax: Megabit
    downlink: Megabit
    rtt: Millisecond
    onchange: EventHandler

class Notification(EventTarget):
    @classmethod
    def new(cls, title: str, options: Union['NotificationOptions', 'None'] = {}) -> Notification: ...
    onclick: EventHandler
    onshow: EventHandler
    onerror: EventHandler
    onclose: EventHandler
    title: str
    dir: NotificationDirection
    lang: str
    body: str
    tag: str
    image: str
    icon: str
    badge: str
    vibrate: Sequence[int]
    timestamp: EpochTimeStamp
    renotify: bool
    silent: Union['bool', 'None']
    requireInteraction: bool
    data: Any
    actions: Sequence[NotificationAction]

    def close(self) -> None: ...

class NotificationOptions(TypedDict):
    dir: NotRequired[NotificationDirection]
    lang: NotRequired[str]
    body: NotRequired[str]
    tag: NotRequired[str]
    image: NotRequired[str]
    icon: NotRequired[str]
    badge: NotRequired[str]
    vibrate: NotRequired[VibratePattern]
    timestamp: NotRequired[EpochTimeStamp]
    renotify: NotRequired[bool]
    silent: NotRequired[Union['bool', 'None']]
    requireInteraction: NotRequired[bool]
    data: NotRequired[Any]
    actions: NotRequired[Sequence[NotificationAction]]

class NotificationAction(TypedDict):
    action: str
    title: str
    icon: NotRequired[str]

class GetNotificationOptions(TypedDict):
    tag: NotRequired[str]

class NotificationEvent(ExtendableEvent):
    @classmethod
    def new(cls, type: str, eventInitDict: NotificationEventInit) -> NotificationEvent: ...
    notification: Notification
    action: str

class NotificationEventInit(ExtendableEventInit):
    notification: Notification
    action: NotRequired[str]

class DeviceOrientationEvent(Event):
    @classmethod
    def new(cls, type: str, eventInitDict: Union['DeviceOrientationEventInit', 'None'] = {}) -> DeviceOrientationEvent: ...
    alpha: Union['float', 'None']
    beta: Union['float', 'None']
    gamma: Union['float', 'None']
    absolute: bool

class DeviceOrientationEventInit(EventInit):
    alpha: NotRequired[Union['float', 'None']]
    beta: NotRequired[Union['float', 'None']]
    gamma: NotRequired[Union['float', 'None']]
    absolute: NotRequired[bool]

class DeviceMotionEventAcceleration:
    x: Union['float', 'None']
    y: Union['float', 'None']
    z: Union['float', 'None']

class DeviceMotionEventRotationRate:
    alpha: Union['float', 'None']
    beta: Union['float', 'None']
    gamma: Union['float', 'None']

class DeviceMotionEvent(Event):
    @classmethod
    def new(cls, type: str, eventInitDict: Union['DeviceMotionEventInit', 'None'] = {}) -> DeviceMotionEvent: ...
    acceleration: Union['DeviceMotionEventAcceleration', 'None']
    accelerationIncludingGravity: Union['DeviceMotionEventAcceleration', 'None']
    rotationRate: Union['DeviceMotionEventRotationRate', 'None']
    interval: float

class DeviceMotionEventAccelerationInit(TypedDict):
    x: NotRequired[Union['float', 'None']]
    y: NotRequired[Union['float', 'None']]
    z: NotRequired[Union['float', 'None']]

class DeviceMotionEventRotationRateInit(TypedDict):
    alpha: NotRequired[Union['float', 'None']]
    beta: NotRequired[Union['float', 'None']]
    gamma: NotRequired[Union['float', 'None']]

class DeviceMotionEventInit(EventInit):
    acceleration: NotRequired[DeviceMotionEventAccelerationInit]
    accelerationIncludingGravity: NotRequired[DeviceMotionEventAccelerationInit]
    rotationRate: NotRequired[DeviceMotionEventRotationRateInit]
    interval: NotRequired[float]

class OrientationSensor(Sensor):
    quaternion: Sequence[float]

    def populateMatrix(self, targetMatrix: RotationMatrixType) -> None: ...

class OrientationSensorOptions(SensorOptions):
    referenceFrame: NotRequired[OrientationSensorLocalCoordinateSystem]

class AbsoluteOrientationSensor(OrientationSensor):
    @classmethod
    def new(cls, sensorOptions: Union['OrientationSensorOptions', 'None'] = {}) -> AbsoluteOrientationSensor: ...

class RelativeOrientationSensor(OrientationSensor):
    @classmethod
    def new(cls, sensorOptions: Union['OrientationSensorOptions', 'None'] = {}) -> RelativeOrientationSensor: ...

class AbsoluteOrientationReadingValues(TypedDict):
    quaternion: Sequence[float]

class RelativeOrientationReadingValues(AbsoluteOrientationReadingValues): ...

class Client:
    lifecycleState: ClientLifecycleState
    url: str
    frameType: FrameType
    id: str
    type: ClientType
    @overload
    def postMessage(self, message: Any, transfer: Sequence[object]) -> None: ...
    @overload
    def postMessage(self, message: Any, options: Union['StructuredSerializeOptions', 'None'] = {}) -> None: ...

class PerformancePaintTiming(PerformanceEntry): ...

class PaymentManager:
    userHint: str

    def enableDelegations(self, delegations: Sequence[PaymentDelegation]) -> Awaitable[None]: ...

class CanMakePaymentEvent(ExtendableEvent):
    @classmethod
    def new(cls, type: str) -> CanMakePaymentEvent: ...

    def respondWith(self, canMakePaymentResponse: Awaitable[bool]) -> None: ...

class PaymentRequestDetailsUpdate(TypedDict):
    error: NotRequired[str]
    total: NotRequired[PaymentCurrencyAmount]
    modifiers: NotRequired[Sequence[PaymentDetailsModifier]]
    shippingOptions: NotRequired[Sequence[PaymentShippingOption]]
    paymentMethodErrors: NotRequired[object]
    shippingAddressErrors: NotRequired[AddressErrors]

class PaymentRequestEvent(ExtendableEvent):
    @classmethod
    def new(cls, type: str, eventInitDict: Union['PaymentRequestEventInit', 'None'] = {}) -> PaymentRequestEvent: ...
    topOrigin: str
    paymentRequestOrigin: str
    paymentRequestId: str
    methodData: Sequence[PaymentMethodData]
    total: object
    modifiers: Sequence[PaymentDetailsModifier]
    paymentOptions: Union['object', 'None']
    shippingOptions: Sequence[PaymentShippingOption]

    def openWindow(self, url: str) -> Awaitable[Union['WindowClient', 'None']]: ...

    def changePaymentMethod(self, methodName: str, methodDetails: Union['object', 'None'] = None) -> Awaitable[Union['PaymentRequestDetailsUpdate', 'None']]: ...

    def changeShippingAddress(self, shippingAddress: Union['AddressInit', 'None'] = {}) -> Awaitable[Union['PaymentRequestDetailsUpdate', 'None']]: ...

    def changeShippingOption(self, shippingOption: str) -> Awaitable[Union['PaymentRequestDetailsUpdate', 'None']]: ...

    def respondWith(self, handlerResponsePromise: Awaitable[PaymentHandlerResponse]) -> None: ...

class PaymentRequestEventInit(ExtendableEventInit):
    topOrigin: NotRequired[str]
    paymentRequestOrigin: NotRequired[str]
    paymentRequestId: NotRequired[str]
    methodData: NotRequired[Sequence[PaymentMethodData]]
    total: NotRequired[PaymentCurrencyAmount]
    modifiers: NotRequired[Sequence[PaymentDetailsModifier]]
    paymentOptions: NotRequired[PaymentOptions]
    shippingOptions: NotRequired[Sequence[PaymentShippingOption]]

class PaymentHandlerResponse(TypedDict):
    methodName: NotRequired[str]
    details: NotRequired[object]
    payerName: NotRequired[Union['str', 'None']]
    payerEmail: NotRequired[Union['str', 'None']]
    payerPhone: NotRequired[Union['str', 'None']]
    shippingAddress: NotRequired[AddressInit]
    shippingOption: NotRequired[Union['str', 'None']]

class AddressInit(TypedDict):
    country: NotRequired[str]
    addressLine: NotRequired[Sequence[str]]
    region: NotRequired[str]
    city: NotRequired[str]
    dependentLocality: NotRequired[str]
    postalCode: NotRequired[str]
    sortingCode: NotRequired[str]
    organization: NotRequired[str]
    recipient: NotRequired[str]
    phone: NotRequired[str]

class PaymentOptions(TypedDict):
    requestPayerName: NotRequired[bool]
    requestBillingAddress: NotRequired[bool]
    requestPayerEmail: NotRequired[bool]
    requestPayerPhone: NotRequired[bool]
    requestShipping: NotRequired[bool]
    shippingType: NotRequired[PaymentShippingType]

class PaymentShippingOption(TypedDict):
    id: str
    label: str
    amount: PaymentCurrencyAmount
    selected: NotRequired[bool]

class AddressErrors(TypedDict):
    addressLine: NotRequired[str]
    city: NotRequired[str]
    country: NotRequired[str]
    dependentLocality: NotRequired[str]
    organization: NotRequired[str]
    phone: NotRequired[str]
    postalCode: NotRequired[str]
    recipient: NotRequired[str]
    region: NotRequired[str]
    sortingCode: NotRequired[str]

class PaymentRequest(EventTarget):
    @classmethod
    def new(cls, methodData: Sequence[PaymentMethodData], details: PaymentDetailsInit) -> PaymentRequest: ...

    def show(self, detailsPromise: Union['Awaitable[PaymentDetailsUpdate]', 'None'] = None) -> Awaitable[PaymentResponse]: ...

    def abort(self) -> Awaitable[None]: ...

    def canMakePayment(self) -> Awaitable[bool]: ...
    id: str
    onpaymentmethodchange: EventHandler

class PaymentMethodData(TypedDict):
    supportedMethods: str
    data: NotRequired[object]

class PaymentCurrencyAmount(TypedDict):
    currency: str
    value: str

class PaymentDetailsBase(TypedDict):
    displayItems: NotRequired[Sequence[PaymentItem]]
    modifiers: NotRequired[Sequence[PaymentDetailsModifier]]

class PaymentDetailsInit(PaymentDetailsBase):
    id: NotRequired[str]
    total: PaymentItem

class PaymentDetailsUpdate(PaymentDetailsBase):
    total: NotRequired[PaymentItem]
    paymentMethodErrors: NotRequired[object]

class PaymentDetailsModifier(TypedDict):
    supportedMethods: str
    total: NotRequired[PaymentItem]
    additionalDisplayItems: NotRequired[Sequence[PaymentItem]]
    data: NotRequired[object]

class PaymentItem(TypedDict):
    label: str
    amount: PaymentCurrencyAmount
    pending: NotRequired[bool]

class PaymentCompleteDetails(TypedDict):
    data: NotRequired[Union['object', 'None']]

class PaymentResponse(EventTarget):

    def toJSON(self) -> object: ...
    requestId: str
    methodName: str
    details: object

    def complete(self, result: Union['PaymentComplete', 'None'] = "unknown", details: Union['PaymentCompleteDetails', 'None'] = {}) -> Awaitable[None]: ...

    def retry(self, errorFields: Union['PaymentValidationErrors', 'None'] = {}) -> Awaitable[None]: ...

class PaymentValidationErrors(TypedDict):
    error: NotRequired[str]
    paymentMethod: NotRequired[object]

class PaymentMethodChangeEvent(PaymentRequestUpdateEvent):
    @classmethod
    def new(cls, type: str, eventInitDict: Union['PaymentMethodChangeEventInit', 'None'] = {}) -> PaymentMethodChangeEvent: ...
    methodName: str
    methodDetails: Union['object', 'None']

class PaymentMethodChangeEventInit(PaymentRequestUpdateEventInit):
    methodName: NotRequired[str]
    methodDetails: NotRequired[Union['object', 'None']]

class PaymentRequestUpdateEvent(Event):
    @classmethod
    def new(cls, type: str, eventInitDict: Union['PaymentRequestUpdateEventInit', 'None'] = {}) -> PaymentRequestUpdateEvent: ...

    def updateWith(self, detailsPromise: Awaitable[PaymentDetailsUpdate]) -> None: ...

class PaymentRequestUpdateEventInit(EventInit): ...

class MemoryMeasurement(TypedDict):
    bytes: NotRequired[int]
    breakdown: NotRequired[Sequence[MemoryBreakdownEntry]]

class MemoryBreakdownEntry(TypedDict):
    bytes: NotRequired[int]
    attribution: NotRequired[Sequence[MemoryAttribution]]
    types: NotRequired[Sequence[str]]

class MemoryAttribution(TypedDict):
    url: NotRequired[str]
    container: NotRequired[MemoryAttributionContainer]
    scope: NotRequired[str]

class MemoryAttributionContainer(TypedDict):
    id: NotRequired[str]
    src: NotRequired[str]

class PerformanceEntry:
    name: str
    entryType: str
    startTime: DOMHighResTimeStamp
    duration: DOMHighResTimeStamp

    def toJSON(self) -> object: ...

class PerformanceObserver:
    @classmethod
    def new(cls, callback: PerformanceObserverCallback) -> PerformanceObserver: ...

    def observe(self, options: Union['PerformanceObserverInit', 'None'] = {}) -> None: ...

    def disconnect(self) -> None: ...

    def takeRecords(self) -> PerformanceEntryList: ...

class PerformanceObserverCallbackOptions(TypedDict):
    droppedEntriesCount: NotRequired[int]

class PerformanceObserverEntryList:

    def getEntries(self) -> PerformanceEntryList: ...

    def getEntriesByType(self, type: str) -> PerformanceEntryList: ...

    def getEntriesByName(self, name: str, type: Union['str', 'None'] = None) -> PerformanceEntryList: ...

class PeriodicSyncManager:

    def register(self, tag: str, options: Union['BackgroundSyncOptions', 'None'] = {}) -> Awaitable[None]: ...

    def getTags(self) -> Awaitable[Sequence[str]]: ...

    def unregister(self, tag: str) -> Awaitable[None]: ...

class BackgroundSyncOptions(TypedDict):
    minInterval: NotRequired[int]

class PeriodicSyncEventInit(ExtendableEventInit):
    tag: str

class PeriodicSyncEvent(ExtendableEvent):
    @classmethod
    def new(cls, type: str, init: PeriodicSyncEventInit) -> PeriodicSyncEvent: ...
    tag: str

class PermissionsPolicy:

    def allowsFeature(self, feature: str, origin: Union['str', 'None'] = None) -> bool: ...

    def features(self) -> Sequence[str]: ...

    def allowedFeatures(self) -> Sequence[str]: ...

    def getAllowlistForFeature(self, feature: str) -> Sequence[str]: ...

class PermissionsPolicyViolationReportBody(ReportBody):
    featureId: str
    sourceFile: Union['str', 'None']
    lineNumber: Union['int', 'None']
    columnNumber: Union['int', 'None']
    disposition: str

class Permissions:

    def request(self, permissionDesc: object) -> Awaitable[PermissionStatus]: ...

    def revoke(self, permissionDesc: object) -> Awaitable[PermissionStatus]: ...

    def query(self, permissionDesc: object) -> Awaitable[PermissionStatus]: ...

class PermissionDescriptor(TypedDict):
    name: str

class PermissionStatus(EventTarget):
    state: PermissionState
    name: str
    onchange: EventHandler

class PermissionSetParameters(TypedDict):
    descriptor: PermissionDescriptor
    state: PermissionState

class PictureInPictureWindow(EventTarget):
    width: int
    height: int
    onresize: EventHandler

class PictureInPictureEvent(Event):
    @classmethod
    def new(cls, type: str, eventInitDict: PictureInPictureEventInit) -> PictureInPictureEvent: ...
    pictureInPictureWindow: PictureInPictureWindow

class PictureInPictureEventInit(EventInit):
    pictureInPictureWindow: PictureInPictureWindow

class PointerEventInit(MouseEventInit):
    pointerId: NotRequired[int]
    width: NotRequired[float]
    height: NotRequired[float]
    pressure: NotRequired[float]
    tangentialPressure: NotRequired[float]
    tiltX: NotRequired[int]
    tiltY: NotRequired[int]
    twist: NotRequired[int]
    altitudeAngle: NotRequired[float]
    azimuthAngle: NotRequired[float]
    pointerType: NotRequired[str]
    isPrimary: NotRequired[bool]
    coalescedEvents: NotRequired[Sequence[PointerEvent]]
    predictedEvents: NotRequired[Sequence[PointerEvent]]

class PointerEvent(MouseEvent):
    @classmethod
    def new(cls, type: str, eventInitDict: Union['PointerEventInit', 'None'] = {}) -> PointerEvent: ...
    pointerId: int
    width: float
    height: float
    pressure: float
    tangentialPressure: float
    tiltX: int
    tiltY: int
    twist: int
    altitudeAngle: float
    azimuthAngle: float
    pointerType: str
    isPrimary: bool

    def getCoalescedEvents(self) -> Sequence[PointerEvent]: ...

    def getPredictedEvents(self) -> Sequence[PointerEvent]: ...

class MouseEventInit(TypedDict, EventModifierInit):
    movementX: NotRequired[float]
    movementY: NotRequired[float]
    screenX: NotRequired[int]
    screenY: NotRequired[int]
    clientX: NotRequired[int]
    clientY: NotRequired[int]
    button: NotRequired[int]
    buttons: NotRequired[int]
    relatedTarget: NotRequired[Union['EventTarget', 'None']]

class HTMLPortalElement(HTMLElement):
    @classmethod
    def new(cls) -> HTMLPortalElement: ...
    src: str
    referrerPolicy: str

    def activate(self, options: Union['PortalActivateOptions', 'None'] = {}) -> Awaitable[None]: ...

    def postMessage(self, message: Any, options: Union['StructuredSerializeOptions', 'None'] = {}) -> None: ...
    onmessage: EventHandler
    onmessageerror: EventHandler

class PortalActivateOptions(StructuredSerializeOptions):
    data: NotRequired[Any]

class PortalHost(EventTarget):

    def postMessage(self, message: Any, options: Union['StructuredSerializeOptions', 'None'] = {}) -> None: ...
    onmessage: EventHandler
    onmessageerror: EventHandler

class PortalActivateEvent(Event):
    @classmethod
    def new(cls, type: str, eventInitDict: Union['PortalActivateEventInit', 'None'] = {}) -> PortalActivateEvent: ...
    data: Any

    def adoptPredecessor(self) -> HTMLPortalElement: ...

class PortalActivateEventInit(EventInit):
    data: NotRequired[Any]

class Presentation:
    defaultRequest: Union['PresentationRequest', 'None']
    receiver: Union['PresentationReceiver', 'None']

class PresentationRequest(EventTarget):
    @overload
    @classmethod
    def new(cls, url: str) -> PresentationRequest: ...
    @overload
    @classmethod
    def new(cls, urls: Sequence[str]) -> PresentationRequest: ...

    def start(self) -> Awaitable[PresentationConnection]: ...

    def reconnect(self, presentationId: str) -> Awaitable[PresentationConnection]: ...

    def getAvailability(self) -> Awaitable[PresentationAvailability]: ...
    onconnectionavailable: EventHandler

class PresentationAvailability(EventTarget):
    value: bool
    onchange: EventHandler

class PresentationConnectionAvailableEvent(Event):
    @classmethod
    def new(cls, type: str, eventInitDict: PresentationConnectionAvailableEventInit) -> PresentationConnectionAvailableEvent: ...
    connection: PresentationConnection

class PresentationConnectionAvailableEventInit(EventInit):
    connection: PresentationConnection

class PresentationConnection(EventTarget):
    id: str
    url: str
    state: PresentationConnectionState

    def close(self) -> None: ...

    def terminate(self) -> None: ...
    onconnect: EventHandler
    onclose: EventHandler
    onterminate: EventHandler
    binaryType: BinaryType
    onmessage: EventHandler
    @overload
    def send(self, message: str) -> None: ...
    @overload
    def send(self, data: Blob) -> None: ...
    @overload
    def send(self, data: ArrayBuffer) -> None: ...
    @overload
    def send(self, data: ArrayBufferView) -> None: ...

class PresentationConnectionCloseEvent(Event):
    @classmethod
    def new(cls, type: str, eventInitDict: PresentationConnectionCloseEventInit) -> PresentationConnectionCloseEvent: ...
    reason: PresentationConnectionCloseReason
    message: str

class PresentationConnectionCloseEventInit(EventInit):
    reason: PresentationConnectionCloseReason
    message: NotRequired[str]

class PresentationReceiver:
    connectionList: Awaitable[PresentationConnectionList]

class PresentationConnectionList(EventTarget):
    connections: Sequence[PresentationConnection]
    onconnectionavailable: EventHandler

class PrivateNetworkAccessPermissionDescriptor(PermissionDescriptor):
    id: NotRequired[str]

class ProximitySensor(Sensor):
    @classmethod
    def new(cls, sensorOptions: Union['SensorOptions', 'None'] = {}) -> ProximitySensor: ...
    distance: Union['float', 'None']
    max: Union['float', 'None']
    near: Union['bool', 'None']

class ProximityReadingValues(TypedDict):
    distance: Union['float', 'None']
    max: Union['float', 'None']
    near: Union['bool', 'None']

class PushPermissionDescriptor(PermissionDescriptor):
    userVisibleOnly: NotRequired[bool]

class PushManager:

    def subscribe(self, options: Union['PushSubscriptionOptionsInit', 'None'] = {}) -> Awaitable[PushSubscription]: ...

    def getSubscription(self) -> Awaitable[Union['PushSubscription', 'None']]: ...

    def permissionState(self, options: Union['PushSubscriptionOptionsInit', 'None'] = {}) -> Awaitable[PermissionState]: ...

class PushSubscriptionOptions:
    userVisibleOnly: bool
    applicationServerKey: ArrayBuffer

class PushSubscriptionOptionsInit(TypedDict):
    userVisibleOnly: NotRequired[bool]
    applicationServerKey: NotRequired[Union['BufferSource', 'str', 'None']]

class PushSubscription:
    endpoint: str
    expirationTime: Union['EpochTimeStamp', 'None']
    options: PushSubscriptionOptions

    def getKey(self, name: PushEncryptionKeyName) -> ArrayBuffer: ...

    def unsubscribe(self) -> Awaitable[bool]: ...

    def toJSON(self) -> PushSubscriptionJSON: ...

class PushSubscriptionJSON(TypedDict):
    endpoint: NotRequired[str]
    expirationTime: NotRequired[Union['EpochTimeStamp', 'None']]
    keys: NotRequired[str]

class PushMessageData:

    def arrayBuffer(self) -> ArrayBuffer: ...

    def blob(self) -> Blob: ...

    def json(self) -> Any: ...

    def text(self) -> str: ...

class PushEvent(ExtendableEvent):
    @classmethod
    def new(cls, type: str, eventInitDict: Union['PushEventInit', 'None'] = {}) -> PushEvent: ...
    data: Union['PushMessageData', 'None']

class PushEventInit(ExtendableEventInit):
    data: NotRequired[PushMessageDataInit]

class PushSubscriptionChangeEvent(ExtendableEvent):
    @classmethod
    def new(cls, type: str, eventInitDict: Union['PushSubscriptionChangeEventInit', 'None'] = {}) -> PushSubscriptionChangeEvent: ...
    newSubscription: Union['PushSubscription', 'None']
    oldSubscription: Union['PushSubscription', 'None']

class PushSubscriptionChangeEventInit(ExtendableEventInit):
    newSubscription: NotRequired[PushSubscription]
    oldSubscription: NotRequired[PushSubscription]

class XRView:
    camera: Union['XRCamera', 'None']
    isFirstPersonObserver: bool
    eye: XREye
    projectionMatrix: Float32Array
    transform: XRRigidTransform
    recommendedViewportScale: Union['float', 'None']

    def requestViewportScale(self, scale: Union['float', 'None']) -> None: ...

class XRCamera:
    width: int
    height: int

class XRWebGLBinding:
    @classmethod
    def new(cls, session: XRSession, context: XRWebGLRenderingContext) -> XRWebGLBinding: ...

    def getCameraImage(self, camera: XRCamera) -> Union['WebGLTexture', 'None']: ...

    def getDepthInformation(self, view: XRView) -> Union['XRWebGLDepthInformation', 'None']: ...

    def getReflectionCubeMap(self, lightProbe: XRLightProbe) -> Union['WebGLTexture', 'None']: ...
    nativeProjectionScaleFactor: float
    usesDepthValues: bool

    def createProjectionLayer(self, init: Union['XRProjectionLayerInit', 'None'] = {}) -> XRProjectionLayer: ...

    def createQuadLayer(self, init: Union['XRQuadLayerInit', 'None'] = {}) -> XRQuadLayer: ...

    def createCylinderLayer(self, init: Union['XRCylinderLayerInit', 'None'] = {}) -> XRCylinderLayer: ...

    def createEquirectLayer(self, init: Union['XREquirectLayerInit', 'None'] = {}) -> XREquirectLayer: ...

    def createCubeLayer(self, init: Union['XRCubeLayerInit', 'None'] = {}) -> XRCubeLayer: ...

    def getSubImage(self, layer: XRCompositionLayer, frame: XRFrame, eye: Union['XREye', 'None'] = "none") -> XRWebGLSubImage: ...

    def getViewSubImage(self, layer: XRProjectionLayer, view: XRView) -> XRWebGLSubImage: ...

class XRMesh:
    meshSpace: XRSpace
    vertices: Sequence[Float32Array]
    indices: Uint32Array
    lastChangedTime: DOMHighResTimeStamp
    semanticLabel: Union['str', 'None']

class XRMeshSet: ...

class RemotePlayback(EventTarget):

    def watchAvailability(self, callback: RemotePlaybackAvailabilityCallback) -> Awaitable[int]: ...

    def cancelWatchAvailability(self, id: Union['int', 'None'] = None) -> Awaitable[None]: ...
    state: RemotePlaybackState
    onconnecting: EventHandler
    onconnect: EventHandler
    ondisconnect: EventHandler

    def prompt(self) -> Awaitable[None]: ...

class ReportBody:

    def toJSON(self) -> object: ...

class Report:

    def toJSON(self) -> object: ...
    type: str
    url: str
    body: Union['ReportBody', 'None']

class ReportingObserver:
    @classmethod
    def new(cls, callback: ReportingObserverCallback, options: Union['ReportingObserverOptions', 'None'] = {}) -> ReportingObserver: ...

    def observe(self) -> None: ...

    def disconnect(self) -> None: ...

    def takeRecords(self) -> ReportList: ...

class ReportingObserverOptions(TypedDict):
    types: NotRequired[Sequence[str]]
    buffered: NotRequired[bool]

class GenerateTestReportParameters(TypedDict):
    message: str
    group: NotRequired[str]

class TopLevelStorageAccessPermissionDescriptor(PermissionDescriptor):
    requestedOrigin: NotRequired[str]

class IdleRequestOptions(TypedDict):
    timeout: NotRequired[int]

class IdleDeadline:

    def timeRemaining(self) -> DOMHighResTimeStamp: ...
    didTimeout: bool

class ResizeObserverOptions(TypedDict):
    box: NotRequired[ResizeObserverBoxOptions]

class ResizeObserver:
    @classmethod
    def new(cls, callback: ResizeObserverCallback) -> ResizeObserver: ...

    def observe(self, target: Element, options: Union['ResizeObserverOptions', 'None'] = {}) -> None: ...

    def unobserve(self, target: Element) -> None: ...

    def disconnect(self) -> None: ...

class ResizeObserverEntry:
    target: Element
    contentRect: DOMRectReadOnly
    borderBoxSize: Sequence[ResizeObserverSize]
    contentBoxSize: Sequence[ResizeObserverSize]
    devicePixelContentBoxSize: Sequence[ResizeObserverSize]

class ResizeObserverSize:
    inlineSize: float
    blockSize: float

class PerformanceResourceTiming(PerformanceEntry):
    initiatorType: str
    deliveryType: str
    nextHopProtocol: ByteString
    workerStart: DOMHighResTimeStamp
    redirectStart: DOMHighResTimeStamp
    redirectEnd: DOMHighResTimeStamp
    fetchStart: DOMHighResTimeStamp
    domainLookupStart: DOMHighResTimeStamp
    domainLookupEnd: DOMHighResTimeStamp
    connectStart: DOMHighResTimeStamp
    connectEnd: DOMHighResTimeStamp
    secureConnectionStart: DOMHighResTimeStamp
    requestStart: DOMHighResTimeStamp
    firstInterimResponseStart: DOMHighResTimeStamp
    responseStart: DOMHighResTimeStamp
    responseEnd: DOMHighResTimeStamp
    transferSize: int
    encodedBodySize: int
    decodedBodySize: int
    responseStatus: int
    renderBlockingStatus: RenderBlockingStatusType
    contentType: str

    def toJSON(self) -> object: ...
    serverTiming: Sequence[PerformanceServerTiming]

class Sanitizer:
    @classmethod
    def new(cls, config: Union['SanitizerConfig', 'None'] = {}) -> Sanitizer: ...

    def sanitize(self, input: Union['Document', 'DocumentFragment']) -> DocumentFragment: ...

    def sanitizeFor(self, element: str, input: str) -> Union['Element', 'None']: ...

    def getConfiguration(self) -> SanitizerConfig: ...

class SetHTMLOptions(TypedDict):
    sanitizer: NotRequired[Sanitizer]

class SanitizerConfig(TypedDict):
    allowElements: NotRequired[Sequence[str]]
    blockElements: NotRequired[Sequence[str]]
    dropElements: NotRequired[Sequence[str]]
    allowAttributes: NotRequired[AttributeMatchList]
    dropAttributes: NotRequired[AttributeMatchList]
    allowCustomElements: NotRequired[bool]
    allowUnknownMarkup: NotRequired[bool]
    allowComments: NotRequired[bool]

class NetworkInformationSaveData:
    saveData: bool

class SchedulerPostTaskOptions(TypedDict):
    signal: NotRequired[AbortSignal]
    priority: NotRequired[TaskPriority]
    delay: NotRequired[int]

class Scheduler:

    def postTask(self, callback: SchedulerPostTaskCallback, options: Union['SchedulerPostTaskOptions', 'None'] = {}) -> Awaitable[Any]: ...

class TaskPriorityChangeEvent(Event):
    @classmethod
    def new(cls, type: str, priorityChangeEventInitDict: TaskPriorityChangeEventInit) -> TaskPriorityChangeEvent: ...
    previousPriority: TaskPriority

class TaskPriorityChangeEventInit(EventInit):
    previousPriority: TaskPriority

class TaskControllerInit(TypedDict):
    priority: NotRequired[TaskPriority]

class TaskController(AbortController):
    @classmethod
    def new(cls, init: Union['TaskControllerInit', 'None'] = {}) -> TaskController: ...

    def setPriority(self, priority: TaskPriority) -> None: ...

class TaskSignalAnyInit(TypedDict):
    priority: NotRequired[Union['TaskPriority', 'TaskSignal']]

class TaskSignal(AbortSignal):
    priority: TaskPriority
    onprioritychange: EventHandler

class DisplayMediaStreamOptions(TypedDict):
    video: NotRequired[Union['bool', 'MediaTrackConstraints']]
    audio: NotRequired[Union['bool', 'MediaTrackConstraints']]
    controller: NotRequired[CaptureController]
    selfBrowserSurface: NotRequired[SelfCapturePreferenceEnum]
    systemAudio: NotRequired[SystemAudioPreferenceEnum]
    surfaceSwitching: NotRequired[SurfaceSwitchingPreferenceEnum]

class ScreenOrientation(EventTarget):

    def lock(self, orientation: OrientationLockType) -> Awaitable[None]: ...

    def unlock(self) -> None: ...
    type: OrientationType
    angle: int
    onchange: EventHandler

class WakeLock:

    def request(self, type: Union['WakeLockType', 'None'] = "screen") -> Awaitable[WakeLockSentinel]: ...

class WakeLockSentinel(EventTarget):
    released: bool
    type: WakeLockType

    def release(self) -> Awaitable[None]: ...
    onrelease: EventHandler

class ScrollTimelineOptions(TypedDict):
    source: NotRequired[Union['Element', 'None']]
    axis: NotRequired[ScrollAxis]

class ScrollTimeline(AnimationTimeline):
    @classmethod
    def new(cls, options: Union['ScrollTimelineOptions', 'None'] = {}) -> ScrollTimeline: ...
    source: Union['Element', 'None']
    axis: ScrollAxis

class ViewTimelineOptions(TypedDict):
    subject: NotRequired[Element]
    axis: NotRequired[ScrollAxis]
    inset: NotRequired[Union['str', 'Sequence[Union["CSSNumericValue", "CSSKeywordValue"]]']]

class ViewTimeline(ScrollTimeline):
    @classmethod
    def new(cls, options: Union['ViewTimelineOptions', 'None'] = {}) -> ViewTimeline: ...
    subject: Element
    startOffset: CSSNumericValue
    endOffset: CSSNumericValue

class FragmentDirective: ...

class SecurePaymentConfirmationRequest(TypedDict):
    challenge: BufferSource
    rpId: str
    credentialIds: Sequence[BufferSource]
    instrument: PaymentCredentialInstrument
    timeout: NotRequired[int]
    payeeName: NotRequired[str]
    payeeOrigin: NotRequired[str]
    extensions: NotRequired[AuthenticationExtensionsClientInputs]
    locale: NotRequired[Sequence[str]]
    showOptOut: NotRequired[bool]

class AuthenticationExtensionsPaymentInputs(TypedDict):
    isPayment: NotRequired[bool]
    rpId: NotRequired[str]
    topOrigin: NotRequired[str]
    payeeName: NotRequired[str]
    payeeOrigin: NotRequired[str]
    total: NotRequired[PaymentCurrencyAmount]
    instrument: NotRequired[PaymentCredentialInstrument]

class CollectedClientPaymentData(CollectedClientData):
    payment: CollectedClientAdditionalPaymentData

class CollectedClientAdditionalPaymentData(TypedDict):
    rpId: str
    topOrigin: str
    payeeName: NotRequired[str]
    payeeOrigin: NotRequired[str]
    total: PaymentCurrencyAmount
    instrument: PaymentCredentialInstrument

class PaymentCredentialInstrument(TypedDict):
    displayName: str
    icon: str
    iconMustBeShown: NotRequired[bool]

class Selection:
    anchorNode: Union['Node', 'None']
    anchorOffset: int
    focusNode: Union['Node', 'None']
    focusOffset: int
    isCollapsed: bool
    rangeCount: int
    type: str
    direction: str

    def getRangeAt(self, index: int) -> Range: ...

    def addRange(self, range: Range) -> None: ...

    def removeRange(self, range: Range) -> None: ...

    def removeAllRanges(self) -> None: ...

    def empty(self) -> None: ...

    def getComposedRanges(self, *shadowRoots: ShadowRoot) -> Sequence[StaticRange]: ...

    def collapse(self, node: Union['Node', 'None'], offset: Union['int', 'None'] = 0) -> None: ...

    def setPosition(self, node: Union['Node', 'None'], offset: Union['int', 'None'] = 0) -> None: ...

    def collapseToStart(self) -> None: ...

    def collapseToEnd(self) -> None: ...

    def extend(self, node: Node, offset: Union['int', 'None'] = 0) -> None: ...

    def setBaseAndExtent(self, anchorNode: Node, anchorOffset: int, focusNode: Node, focusOffset: int) -> None: ...

    def selectAllChildren(self, node: Node) -> None: ...

    def modify(self, alter: Union['str', 'None'] = None, direction: Union['str', 'None'] = None, granularity: Union['str', 'None'] = None) -> None: ...

    def deleteFromDocument(self) -> None: ...

    def containsNode(self, node: Node, allowPartialContainment: Union['bool', 'None'] = False) -> bool: ...

class Serial(EventTarget):
    onconnect: EventHandler
    ondisconnect: EventHandler

    def getPorts(self) -> Awaitable[Sequence[SerialPort]]: ...

    def requestPort(self, options: Union['SerialPortRequestOptions', 'None'] = {}) -> Awaitable[SerialPort]: ...

class SerialPortRequestOptions(TypedDict):
    filters: NotRequired[Sequence[SerialPortFilter]]
    allowedBluetoothServiceClassIds: NotRequired[Sequence[BluetoothServiceUUID]]

class SerialPortFilter(TypedDict):
    usbVendorId: NotRequired[int]
    usbProductId: NotRequired[int]
    bluetoothServiceClassId: NotRequired[BluetoothServiceUUID]

class SerialPort(EventTarget):
    onconnect: EventHandler
    ondisconnect: EventHandler
    readable: ReadableStream
    writable: WritableStream

    def getInfo(self) -> SerialPortInfo: ...

    def open(self, options: SerialOptions) -> Awaitable[None]: ...

    def setSignals(self, signals: Union['SerialOutputSignals', 'None'] = {}) -> Awaitable[None]: ...

    def getSignals(self) -> Awaitable[SerialInputSignals]: ...

    def close(self) -> Awaitable[None]: ...

    def forget(self) -> Awaitable[None]: ...

class SerialPortInfo(TypedDict):
    usbVendorId: NotRequired[int]
    usbProductId: NotRequired[int]
    bluetoothServiceClassId: NotRequired[BluetoothServiceUUID]

class SerialOptions(TypedDict):
    baudRate: int
    dataBits: NotRequired[int]
    stopBits: NotRequired[int]
    parity: NotRequired[ParityType]
    bufferSize: NotRequired[int]
    flowControl: NotRequired[FlowControlType]

class SerialOutputSignals(TypedDict):
    dataTerminalReady: NotRequired[bool]
    requestToSend: NotRequired[bool]

class SerialInputSignals(TypedDict):
    dataCarrierDetect: bool
    clearToSend: bool
    ringIndicator: bool
    dataSetReady: bool

class PerformanceServerTiming:
    name: str
    duration: DOMHighResTimeStamp
    description: str

    def toJSON(self) -> object: ...

class ServiceWorker(EventTarget, AbstractWorker):
    scriptURL: str
    state: ServiceWorkerState
    @overload
    def postMessage(self, message: Any, transfer: Sequence[object]) -> None: ...
    @overload
    def postMessage(self, message: Any, options: Union['StructuredSerializeOptions', 'None'] = {}) -> None: ...
    onstatechange: EventHandler

class ServiceWorkerContainer(EventTarget):
    controller: Union['ServiceWorker', 'None']
    ready: Awaitable[ServiceWorkerRegistration]

    def register(self, scriptURL: str, options: Union['RegistrationOptions', 'None'] = {}) -> Awaitable[ServiceWorkerRegistration]: ...

    def getRegistration(self, clientURL: Union['str', 'None'] = "") -> Awaitable[Union['ServiceWorkerRegistration', 'None']]: ...

    def getRegistrations(self) -> Awaitable[Sequence[ServiceWorkerRegistration]]: ...

    def startMessages(self) -> None: ...
    oncontrollerchange: EventHandler
    onmessage: EventHandler
    onmessageerror: EventHandler

class RegistrationOptions(TypedDict):
    scope: NotRequired[str]
    type: NotRequired[WorkerType]
    updateViaCache: NotRequired[ServiceWorkerUpdateViaCache]

class NavigationPreloadManager:

    def enable(self) -> Awaitable[None]: ...

    def disable(self) -> Awaitable[None]: ...

    def setHeaderValue(self, value: ByteString) -> Awaitable[None]: ...

    def getState(self) -> Awaitable[NavigationPreloadState]: ...

class NavigationPreloadState(TypedDict):
    enabled: NotRequired[bool]
    headerValue: NotRequired[ByteString]

class WindowClient(Client):
    visibilityState: DocumentVisibilityState
    focused: bool
    ancestorOrigins: Sequence[str]

    def focus(self) -> Awaitable[WindowClient]: ...

    def navigate(self, url: str) -> Awaitable[Union['WindowClient', 'None']]: ...

class Clients:

    def get(self, id: str) -> Awaitable[Union['Client', 'None']]: ...

    def matchAll(self, options: Union['ClientQueryOptions', 'None'] = {}) -> Awaitable[Sequence[Client]]: ...

    def openWindow(self, url: str) -> Awaitable[Union['WindowClient', 'None']]: ...

    def claim(self) -> Awaitable[None]: ...

class ClientQueryOptions(TypedDict):
    includeUncontrolled: NotRequired[bool]
    type: NotRequired[ClientType]

class ExtendableEvent(Event):
    @classmethod
    def new(cls, type: str, eventInitDict: Union['ExtendableEventInit', 'None'] = {}) -> ExtendableEvent: ...

    def waitUntil(self, f: Awaitable[Any]) -> None: ...

class ExtendableEventInit(EventInit): ...

class FetchEvent(ExtendableEvent):
    @classmethod
    def new(cls, type: str, eventInitDict: FetchEventInit) -> FetchEvent: ...
    request: Request
    preloadResponse: Awaitable[Any]
    clientId: str
    resultingClientId: str
    replacesClientId: str
    handled: Awaitable[None]

    def respondWith(self, r: Awaitable[Response]) -> None: ...

class FetchEventInit(ExtendableEventInit):
    request: Request
    preloadResponse: NotRequired[Awaitable[Any]]
    clientId: NotRequired[str]
    resultingClientId: NotRequired[str]
    replacesClientId: NotRequired[str]
    handled: NotRequired[Awaitable[None]]

class ExtendableMessageEvent(ExtendableEvent):
    @classmethod
    def new(cls, type: str, eventInitDict: Union['ExtendableMessageEventInit', 'None'] = {}) -> ExtendableMessageEvent: ...
    data: Any
    origin: str
    lastEventId: str
    source: Union['Client', 'ServiceWorker', 'MessagePort', 'None']
    ports: Sequence[MessagePort]

class ExtendableMessageEventInit(ExtendableEventInit):
    data: NotRequired[Any]
    origin: NotRequired[str]
    lastEventId: NotRequired[str]
    source: NotRequired[Union['Client', 'ServiceWorker', 'MessagePort', 'None']]
    ports: NotRequired[Sequence[MessagePort]]

class Cache:

    def match(self, request: RequestInfo, options: Union['CacheQueryOptions', 'None'] = {}) -> Awaitable[Union['Response', 'None']]: ...

    def matchAll(self, request: Union['RequestInfo', 'None'] = None, options: Union['CacheQueryOptions', 'None'] = {}) -> Awaitable[Sequence[Response]]: ...

    def add(self, request: RequestInfo) -> Awaitable[None]: ...

    def addAll(self, requests: Sequence[RequestInfo]) -> Awaitable[None]: ...

    def put(self, request: RequestInfo, response: Response) -> Awaitable[None]: ...

    def delete(self, request: RequestInfo, options: Union['CacheQueryOptions', 'None'] = {}) -> Awaitable[bool]: ...

    def keys(self, request: Union['RequestInfo', 'None'] = None, options: Union['CacheQueryOptions', 'None'] = {}) -> Awaitable[Sequence[Request]]: ...

class CacheQueryOptions(TypedDict):
    ignoreSearch: NotRequired[bool]
    ignoreMethod: NotRequired[bool]
    ignoreVary: NotRequired[bool]

class CacheStorage:

    def match(self, request: RequestInfo, options: Union['MultiCacheQueryOptions', 'None'] = {}) -> Awaitable[Union['Response', 'None']]: ...

    def has(self, cacheName: str) -> Awaitable[bool]: ...

    def open(self, cacheName: str) -> Awaitable[Cache]: ...

    def delete(self, cacheName: str) -> Awaitable[bool]: ...

    def keys(self) -> Awaitable[Sequence[str]]: ...

class MultiCacheQueryOptions(CacheQueryOptions):
    cacheName: NotRequired[str]

class FaceDetector:
    @classmethod
    def new(cls, faceDetectorOptions: Union['FaceDetectorOptions', 'None'] = {}) -> FaceDetector: ...

    def detect(self, image: ImageBitmapSource) -> Awaitable[Sequence[DetectedFace]]: ...

class FaceDetectorOptions(TypedDict):
    maxDetectedFaces: NotRequired[int]
    fastMode: NotRequired[bool]

class DetectedFace(TypedDict):
    boundingBox: DOMRectReadOnly
    landmarks: Sequence[Landmark]

class Landmark(TypedDict):
    locations: Sequence[Point2D]
    type: NotRequired[LandmarkType]

class BarcodeDetector:
    @classmethod
    def new(cls, barcodeDetectorOptions: Union['BarcodeDetectorOptions', 'None'] = {}) -> BarcodeDetector: ...

    def detect(self, image: ImageBitmapSource) -> Awaitable[Sequence[DetectedBarcode]]: ...

class BarcodeDetectorOptions(TypedDict):
    formats: NotRequired[Sequence[BarcodeFormat]]

class DetectedBarcode(TypedDict):
    boundingBox: DOMRectReadOnly
    rawValue: str
    format: BarcodeFormat
    cornerPoints: Sequence[Point2D]

class SharedStorageWorklet(Worklet): ...

class SharedStorageWorkletGlobalScope(WorkletGlobalScope):

    def register(self, name: str, operationCtor: SharedStorageOperationConstructor) -> None: ...
    sharedStorage: WorkletSharedStorage

class SharedStorageOperation: ...

class SharedStorageRunOperationMethodOptions(TypedDict):
    data: NotRequired[object]
    resolveToConfig: NotRequired[bool]
    keepAlive: NotRequired[bool]

class SharedStorageRunOperation(SharedStorageOperation):

    def run(self, data: object) -> Awaitable[None]: ...

class SharedStorageSelectURLOperation(SharedStorageOperation):

    def run(self, data: object, urls: Sequence[SharedStorageUrlWithMetadata]) -> Awaitable[int]: ...

class SharedStorage:

    def set(self, key: str, value: str, options: Union['SharedStorageSetMethodOptions', 'None'] = {}) -> Awaitable[Any]: ...

    def append(self, key: str, value: str) -> Awaitable[Any]: ...

    def delete(self, key: str) -> Awaitable[Any]: ...

    def clear(self) -> Awaitable[Any]: ...

class SharedStorageSetMethodOptions(TypedDict):
    ignoreIfPresent: NotRequired[bool]

class WindowSharedStorage(SharedStorage):

    def run(self, name: str, options: Union['SharedStorageRunOperationMethodOptions', 'None'] = {}) -> Awaitable[Any]: ...

    def selectURL(self, name: str, urls: Sequence[SharedStorageUrlWithMetadata], options: Union['SharedStorageRunOperationMethodOptions', 'None'] = {}) -> Awaitable[SharedStorageResponse]: ...
    worklet: SharedStorageWorklet

class SharedStorageUrlWithMetadata(TypedDict):
    url: str
    reportingMetadata: NotRequired[object]

class WorkletSharedStorage(SharedStorage):

    def get(self, key: str) -> Awaitable[str]: ...

    def length(self) -> Awaitable[int]: ...

    def remainingBudget(self) -> Awaitable[float]: ...

class SpeechRecognition(EventTarget):
    @classmethod
    def new(cls) -> SpeechRecognition: ...
    grammars: SpeechGrammarList
    lang: str
    continuous: bool
    interimResults: bool
    maxAlternatives: int

    def start(self) -> None: ...

    def stop(self) -> None: ...

    def abort(self) -> None: ...
    onaudiostart: EventHandler
    onsoundstart: EventHandler
    onspeechstart: EventHandler
    onspeechend: EventHandler
    onsoundend: EventHandler
    onaudioend: EventHandler
    onresult: EventHandler
    onnomatch: EventHandler
    onerror: EventHandler
    onstart: EventHandler
    onend: EventHandler

class SpeechRecognitionErrorEvent(Event):
    @classmethod
    def new(cls, type: str, eventInitDict: SpeechRecognitionErrorEventInit) -> SpeechRecognitionErrorEvent: ...
    error: SpeechRecognitionErrorCode
    message: str

class SpeechRecognitionErrorEventInit(EventInit):
    error: SpeechRecognitionErrorCode
    message: NotRequired[str]

class SpeechRecognitionAlternative:
    transcript: str
    confidence: float

class SpeechRecognitionResult:
    length: int

    def item(self, index: int) -> SpeechRecognitionAlternative: ...
    isFinal: bool

class SpeechRecognitionResultList:
    length: int

    def item(self, index: int) -> SpeechRecognitionResult: ...

class SpeechRecognitionEvent(Event):
    @classmethod
    def new(cls, type: str, eventInitDict: SpeechRecognitionEventInit) -> SpeechRecognitionEvent: ...
    resultIndex: int
    results: SpeechRecognitionResultList

class SpeechRecognitionEventInit(EventInit):
    resultIndex: NotRequired[int]
    results: SpeechRecognitionResultList

class SpeechGrammar:
    src: str
    weight: float

class SpeechGrammarList:
    @classmethod
    def new(cls) -> SpeechGrammarList: ...
    length: int

    def item(self, index: int) -> SpeechGrammar: ...

    def addFromURI(self, src: str, weight: Union['float', 'None'] = 1.0) -> None: ...

    def addFromString(self, string: str, weight: Union['float', 'None'] = 1.0) -> None: ...

class SpeechSynthesis(EventTarget):
    pending: bool
    speaking: bool
    paused: bool
    onvoiceschanged: EventHandler

    def speak(self, utterance: SpeechSynthesisUtterance) -> None: ...

    def cancel(self) -> None: ...

    def pause(self) -> None: ...

    def resume(self) -> None: ...

    def getVoices(self) -> Sequence[SpeechSynthesisVoice]: ...

class SpeechSynthesisUtterance(EventTarget):
    @classmethod
    def new(cls, text: Union['str', 'None'] = None) -> SpeechSynthesisUtterance: ...
    text: str
    lang: str
    voice: Union['SpeechSynthesisVoice', 'None']
    volume: float
    rate: float
    pitch: float
    onstart: EventHandler
    onend: EventHandler
    onerror: EventHandler
    onpause: EventHandler
    onresume: EventHandler
    onmark: EventHandler
    onboundary: EventHandler

class SpeechSynthesisEvent(Event):
    @classmethod
    def new(cls, type: str, eventInitDict: SpeechSynthesisEventInit) -> SpeechSynthesisEvent: ...
    utterance: SpeechSynthesisUtterance
    charIndex: int
    charLength: int
    elapsedTime: float
    name: str

class SpeechSynthesisEventInit(EventInit):
    utterance: SpeechSynthesisUtterance
    charIndex: NotRequired[int]
    charLength: NotRequired[int]
    elapsedTime: NotRequired[float]
    name: NotRequired[str]

class SpeechSynthesisErrorEvent(SpeechSynthesisEvent):
    @classmethod
    def new(cls, type: str, eventInitDict: SpeechSynthesisErrorEventInit) -> SpeechSynthesisErrorEvent: ...
    error: SpeechSynthesisErrorCode

class SpeechSynthesisErrorEventInit(SpeechSynthesisEventInit):
    error: SpeechSynthesisErrorCode

class SpeechSynthesisVoice:
    voiceURI: str
    name: str
    lang: str
    localService: bool
    default: bool

class NavigatorStorageBuckets:
    storageBuckets: StorageBucketManager

class StorageBucketManager:

    def open(self, name: str, options: Union['StorageBucketOptions', 'None'] = {}) -> Awaitable[StorageBucket]: ...

    def keys(self) -> Awaitable[Sequence[str]]: ...

    def delete(self, name: str) -> Awaitable[None]: ...

class StorageBucketOptions(TypedDict):
    persisted: NotRequired[Union['bool', 'None']]
    durability: NotRequired[Union['StorageBucketDurability', 'None']]
    quota: NotRequired[Union['int', 'None']]
    expires: NotRequired[Union['DOMHighResTimeStamp', 'None']]

class StorageBucket:
    name: str

    def persist(self) -> Awaitable[bool]: ...

    def persisted(self) -> Awaitable[bool]: ...

    def estimate(self) -> Awaitable[StorageEstimate]: ...

    def durability(self) -> Awaitable[StorageBucketDurability]: ...

    def setExpires(self, expires: DOMHighResTimeStamp) -> Awaitable[None]: ...

    def expires(self) -> Awaitable[Union['DOMHighResTimeStamp', 'None']]: ...
    indexedDB: IDBFactory
    caches: CacheStorage

    def getDirectory(self) -> Awaitable[FileSystemDirectoryHandle]: ...

class NavigatorStorage:
    storage: StorageManager

class StorageEstimate(TypedDict):
    usage: NotRequired[int]
    quota: NotRequired[int]

class ReadableStream:
    @classmethod
    def new(cls, underlyingSource: Union['object', 'None'] = None, strategy: Union['QueuingStrategy', 'None'] = {}) -> ReadableStream: ...
    locked: bool

    def cancel(self, reason: Union['Any', 'None'] = None) -> Awaitable[None]: ...

    def getReader(self, options: Union['ReadableStreamGetReaderOptions', 'None'] = {}) -> ReadableStreamReader: ...

    def pipeThrough(self, transform: ReadableWritablePair, options: Union['StreamPipeOptions', 'None'] = {}) -> ReadableStream: ...

    def pipeTo(self, destination: WritableStream, options: Union['StreamPipeOptions', 'None'] = {}) -> Awaitable[None]: ...

    def tee(self) -> Sequence[ReadableStream]: ...

class ReadableStreamGetReaderOptions(TypedDict):
    mode: NotRequired[ReadableStreamReaderMode]

class ReadableStreamIteratorOptions(TypedDict):
    preventCancel: NotRequired[bool]

class ReadableWritablePair(TypedDict):
    readable: ReadableStream
    writable: WritableStream

class StreamPipeOptions(TypedDict):
    preventClose: NotRequired[bool]
    preventAbort: NotRequired[bool]
    preventCancel: NotRequired[bool]
    signal: NotRequired[AbortSignal]

class UnderlyingSource(TypedDict):
    start: NotRequired[UnderlyingSourceStartCallback]
    pull: NotRequired[UnderlyingSourcePullCallback]
    cancel: NotRequired[UnderlyingSourceCancelCallback]
    type: NotRequired[ReadableStreamType]
    autoAllocateChunkSize: NotRequired[int]

class ReadableStreamGenericReader:
    closed: Awaitable[None]

    def cancel(self, reason: Union['Any', 'None'] = None) -> Awaitable[None]: ...

class ReadableStreamDefaultReader(ReadableStreamGenericReader):
    @classmethod
    def new(cls, stream: ReadableStream) -> ReadableStreamDefaultReader: ...

    def read(self) -> Awaitable[ReadableStreamReadResult]: ...

    def releaseLock(self) -> None: ...

class ReadableStreamReadResult(TypedDict):
    value: NotRequired[Any]
    done: NotRequired[bool]

class ReadableStreamBYOBReader(ReadableStreamGenericReader):
    @classmethod
    def new(cls, stream: ReadableStream) -> ReadableStreamBYOBReader: ...

    def read(self, view: ArrayBufferView) -> Awaitable[ReadableStreamReadResult]: ...

    def releaseLock(self) -> None: ...

class ReadableStreamDefaultController:
    desiredSize: Union['float', 'None']

    def close(self) -> None: ...

    def enqueue(self, chunk: Union['Any', 'None'] = None) -> None: ...

    def error(self, e: Union['Any', 'None'] = None) -> None: ...

class ReadableByteStreamController:
    byobRequest: Union['ReadableStreamBYOBRequest', 'None']
    desiredSize: Union['float', 'None']

    def close(self) -> None: ...

    def enqueue(self, chunk: ArrayBufferView) -> None: ...

    def error(self, e: Union['Any', 'None'] = None) -> None: ...

class ReadableStreamBYOBRequest:
    view: Union['ArrayBufferView', 'None']

    def respond(self, bytesWritten: int) -> None: ...

    def respondWithNewView(self, view: ArrayBufferView) -> None: ...

class WritableStream:
    @classmethod
    def new(cls, underlyingSink: Union['object', 'None'] = None, strategy: Union['QueuingStrategy', 'None'] = {}) -> WritableStream: ...
    locked: bool

    def abort(self, reason: Union['Any', 'None'] = None) -> Awaitable[None]: ...

    def close(self) -> Awaitable[None]: ...

    def getWriter(self) -> WritableStreamDefaultWriter: ...

class UnderlyingSink(TypedDict):
    start: NotRequired[UnderlyingSinkStartCallback]
    write: NotRequired[UnderlyingSinkWriteCallback]
    close: NotRequired[UnderlyingSinkCloseCallback]
    abort: NotRequired[UnderlyingSinkAbortCallback]
    type: NotRequired[Any]

class WritableStreamDefaultWriter:
    @classmethod
    def new(cls, stream: WritableStream) -> WritableStreamDefaultWriter: ...
    closed: Awaitable[None]
    desiredSize: Union['float', 'None']
    ready: Awaitable[None]

    def abort(self, reason: Union['Any', 'None'] = None) -> Awaitable[None]: ...

    def close(self) -> Awaitable[None]: ...

    def releaseLock(self) -> None: ...

    def write(self, chunk: Union['Any', 'None'] = None) -> Awaitable[None]: ...

class WritableStreamDefaultController:
    signal: AbortSignal

    def error(self, e: Union['Any', 'None'] = None) -> None: ...

class TransformStream:
    @classmethod
    def new(cls, transformer: Union['object', 'None'] = None, writableStrategy: Union['QueuingStrategy', 'None'] = {}, readableStrategy: Union['QueuingStrategy', 'None'] = {}) -> TransformStream: ...
    readable: ReadableStream
    writable: WritableStream

class Transformer(TypedDict):
    start: NotRequired[TransformerStartCallback]
    transform: NotRequired[TransformerTransformCallback]
    flush: NotRequired[TransformerFlushCallback]
    readableType: NotRequired[Any]
    writableType: NotRequired[Any]

class TransformStreamDefaultController:
    desiredSize: Union['float', 'None']

    def enqueue(self, chunk: Union['Any', 'None'] = None) -> None: ...

    def error(self, reason: Union['Any', 'None'] = None) -> None: ...

    def terminate(self) -> None: ...

class QueuingStrategy(TypedDict):
    highWaterMark: NotRequired[float]
    size: NotRequired[QueuingStrategySize]

class QueuingStrategyInit(TypedDict):
    highWaterMark: float

class ByteLengthQueuingStrategy:
    @classmethod
    def new(cls, init: QueuingStrategyInit) -> ByteLengthQueuingStrategy: ...
    highWaterMark: float
    size: Function

class CountQueuingStrategy:
    @classmethod
    def new(cls, init: QueuingStrategyInit) -> CountQueuingStrategy: ...
    highWaterMark: float
    size: Function

class GenericTransformStream:
    readable: ReadableStream
    writable: WritableStream

class TimeEvent(Event):
    view: Union['WindowProxy', 'None']
    detail: int

    def initTimeEvent(self, typeArg: str, viewArg: Union['Window', 'None'], detailArg: int) -> None: ...

class SVGAnimationElement(SVGElement, SVGTests):
    targetElement: Union['SVGElement', 'None']
    onbegin: EventHandler
    onend: EventHandler
    onrepeat: EventHandler

    def getStartTime(self) -> float: ...

    def getCurrentTime(self) -> float: ...

    def getSimpleDuration(self) -> float: ...

    def beginElement(self) -> None: ...

    def beginElementAt(self, offset: float) -> None: ...

    def endElement(self) -> None: ...

    def endElementAt(self, offset: float) -> None: ...

class SVGAnimateElement(SVGAnimationElement): ...

class SVGSetElement(SVGAnimationElement): ...

class SVGAnimateMotionElement(SVGAnimationElement): ...

class SVGMPathElement(SVGElement, SVGURIReference): ...

class SVGAnimateTransformElement(SVGAnimationElement): ...

class SVGDiscardElement(SVGAnimationElement): ...

class TestutilsNamespace:

    def gc(self) -> Awaitable[None]: ...

class TextDetector:
    @classmethod
    def new(cls) -> TextDetector: ...

    def detect(self, image: ImageBitmapSource) -> Awaitable[Sequence[DetectedText]]: ...

class DetectedText(TypedDict):
    boundingBox: DOMRectReadOnly
    rawValue: str
    cornerPoints: Sequence[Point2D]

class BrowsingTopic(TypedDict):
    topic: NotRequired[int]
    version: NotRequired[str]
    configVersion: NotRequired[str]
    modelVersion: NotRequired[str]
    taxonomyVersion: NotRequired[str]

class BrowsingTopicsOptions(TypedDict):
    skipObservation: NotRequired[bool]

class TouchInit(TypedDict):
    identifier: int
    target: EventTarget
    clientX: NotRequired[float]
    clientY: NotRequired[float]
    screenX: NotRequired[float]
    screenY: NotRequired[float]
    pageX: NotRequired[float]
    pageY: NotRequired[float]
    radiusX: NotRequired[float]
    radiusY: NotRequired[float]
    rotationAngle: NotRequired[float]
    force: NotRequired[float]
    altitudeAngle: NotRequired[float]
    azimuthAngle: NotRequired[float]
    touchType: NotRequired[TouchType]

class Touch:
    @classmethod
    def new(cls, touchInitDict: TouchInit) -> Touch: ...
    identifier: int
    target: EventTarget
    screenX: float
    screenY: float
    clientX: float
    clientY: float
    pageX: float
    pageY: float
    radiusX: float
    radiusY: float
    rotationAngle: float
    force: float
    altitudeAngle: float
    azimuthAngle: float
    touchType: TouchType

class TouchList:
    length: int

    def item(self, index: int) -> Union['Touch', 'None']: ...

class TouchEventInit(EventModifierInit):
    touches: NotRequired[Sequence[Touch]]
    targetTouches: NotRequired[Sequence[Touch]]
    changedTouches: NotRequired[Sequence[Touch]]

class TouchEvent(UIEvent):
    @classmethod
    def new(cls, type: str, eventInitDict: Union['TouchEventInit', 'None'] = {}) -> TouchEvent: ...
    touches: TouchList
    targetTouches: TouchList
    changedTouches: TouchList
    altKey: bool
    metaKey: bool
    ctrlKey: bool
    shiftKey: bool

    def getModifierState(self, keyArg: str) -> bool: ...

class PrivateToken(TypedDict):
    version: TokenVersion
    operation: OperationType
    refreshPolicy: NotRequired[RefreshPolicy]
    issuers: NotRequired[Sequence[str]]

class TrustedHTML:

    def toJSON(self) -> str: ...

class TrustedScript:

    def toJSON(self) -> str: ...

class TrustedScriptURL:

    def toJSON(self) -> str: ...

class TrustedTypePolicyFactory:

    def createPolicy(self, policyName: str, policyOptions: Union['TrustedTypePolicyOptions', 'None'] = {}) -> TrustedTypePolicy: ...

    def isHTML(self, value: Any) -> bool: ...

    def isScript(self, value: Any) -> bool: ...

    def isScriptURL(self, value: Any) -> bool: ...
    emptyHTML: TrustedHTML
    emptyScript: TrustedScript

    def getAttributeType(self, tagName: str, attribute: str, elementNs: Union['str', 'None'] = "", attrNs: Union['str', 'None'] = "") -> Union['str', 'None']: ...

    def getPropertyType(self, tagName: str, property: str, elementNs: Union['str', 'None'] = "") -> Union['str', 'None']: ...
    defaultPolicy: Union['TrustedTypePolicy', 'None']

class TrustedTypePolicy:
    name: str

    def createHTML(self, input: str, *arguments: Any) -> TrustedHTML: ...

    def createScript(self, input: str, *arguments: Any) -> TrustedScript: ...

    def createScriptURL(self, input: str, *arguments: Any) -> TrustedScriptURL: ...

class TrustedTypePolicyOptions(TypedDict):
    createHTML: NotRequired[Union['CreateHTMLCallback', 'None']]
    createScript: NotRequired[Union['CreateScriptCallback', 'None']]
    createScriptURL: NotRequired[Union['CreateScriptURLCallback', 'None']]

class AuctionAd(TypedDict):
    renderURL: str
    metadata: NotRequired[Any]
    buyerReportingId: NotRequired[str]
    buyerAndSellerReportingId: NotRequired[str]

class GenerateBidInterestGroup(TypedDict):
    owner: str
    name: str
    lifetimeMs: float
    enableBiddingSignalsPrioritization: NotRequired[bool]
    priorityVector: NotRequired[float]
    executionMode: NotRequired[str]
    biddingLogicURL: NotRequired[str]
    biddingWasmHelperURL: NotRequired[str]
    updateURL: NotRequired[str]
    trustedBiddingSignalsURL: NotRequired[str]
    trustedBiddingSignalsKeys: NotRequired[Sequence[str]]
    userBiddingSignals: NotRequired[Any]
    ads: NotRequired[Sequence[AuctionAd]]
    adComponents: NotRequired[Sequence[AuctionAd]]

class AuctionAdInterestGroup(GenerateBidInterestGroup):
    priority: NotRequired[float]
    prioritySignalsOverrides: NotRequired[float]

class AuctionAdInterestGroupKey(TypedDict):
    owner: str
    name: str

class AuctionAdConfig(TypedDict):
    seller: str
    decisionLogicURL: str
    trustedScoringSignalsURL: NotRequired[str]
    interestGroupBuyers: NotRequired[Sequence[str]]
    auctionSignals: NotRequired[Awaitable[Any]]
    sellerSignals: NotRequired[Awaitable[Any]]
    directFromSellerSignals: NotRequired[Awaitable[str]]
    sellerTimeout: NotRequired[int]
    sellerExperimentGroupId: NotRequired[int]
    sellerCurrency: NotRequired[str]
    perBuyerSignals: NotRequired[Awaitable[Any]]
    perBuyerTimeouts: NotRequired[Awaitable[int]]
    perBuyerGroupLimits: NotRequired[int]
    perBuyerExperimentGroupIds: NotRequired[int]
    perBuyerPrioritySignals: NotRequired[float]
    perBuyerCurrencies: NotRequired[Awaitable[str]]
    componentAuctions: NotRequired[Sequence[AuctionAdConfig]]
    signal: NotRequired[Union['AbortSignal', 'None']]
    resolveToConfig: NotRequired[Awaitable[bool]]

class InterestGroupScriptRunnerGlobalScope: ...

class InterestGroupBiddingScriptRunnerGlobalScope(InterestGroupScriptRunnerGlobalScope):

    def setBid(self, generateBidOutput: Union['GenerateBidOutput', 'None'] = {}) -> bool: ...

    def setPriority(self, priority: float) -> None: ...

    def setPrioritySignalsOverride(self, key: str, priority: Union['float', 'None'] = None) -> None: ...

class AdRender(TypedDict):
    url: str
    width: NotRequired[str]
    height: NotRequired[str]

class GenerateBidOutput(TypedDict):
    bid: NotRequired[float]
    bidCurrency: NotRequired[str]
    render: NotRequired[Union['str', 'AdRender']]
    ad: NotRequired[Any]
    adComponents: NotRequired[Sequence[Union['str', 'AdRender']]]
    adCost: NotRequired[float]
    modelingSignals: NotRequired[float]
    allowComponentAuction: NotRequired[bool]

class InterestGroupScoringScriptRunnerGlobalScope(InterestGroupScriptRunnerGlobalScope): ...

class InterestGroupReportingScriptRunnerGlobalScope(InterestGroupScriptRunnerGlobalScope):

    def sendReportTo(self, url: str) -> None: ...

    def registerAdBeacon(self, map: str) -> None: ...

class PreviousWin(TypedDict):
    timeDelta: int
    adJSON: str

class BiddingBrowserSignals(TypedDict):
    topWindowHostname: str
    seller: str
    joinCount: int
    bidCount: int
    recency: int
    topLevelSeller: NotRequired[str]
    prevWinsMs: NotRequired[Sequence[PreviousWin]]
    wasmHelper: NotRequired[object]
    dataVersion: NotRequired[int]

class ScoringBrowserSignals(TypedDict):
    topWindowHostname: str
    interestGroupOwner: str
    renderURL: str
    biddingDurationMsec: int
    bidCurrency: str
    dataVersion: NotRequired[int]
    adComponents: NotRequired[Sequence[str]]

class ReportingBrowserSignals(TypedDict):
    topWindowHostname: str
    interestGroupOwner: str
    renderURL: str
    bid: float
    highestScoringOtherBid: float
    bidCurrency: NotRequired[str]
    highestScoringOtherBidCurrency: NotRequired[str]
    topLevelSeller: NotRequired[str]
    componentSeller: NotRequired[str]
    buyerAndSellerReportingId: NotRequired[str]

class ReportResultBrowserSignals(ReportingBrowserSignals):
    desirability: float
    topLevelSellerSignals: NotRequired[str]
    modifiedBid: NotRequired[float]
    dataVersion: NotRequired[int]

class ReportWinBrowserSignals(ReportingBrowserSignals):
    adCost: NotRequired[float]
    seller: NotRequired[str]
    madeHighestScoringOtherBid: NotRequired[bool]
    interestGroupName: NotRequired[str]
    buyerReportingId: NotRequired[str]
    modelingSignals: NotRequired[int]
    dataVersion: NotRequired[int]

class ScoreAdOutput(TypedDict):
    desirability: float
    bid: NotRequired[float]
    bidCurrency: NotRequired[str]
    incomingBidInSellerCurrency: NotRequired[float]
    allowComponentAuction: NotRequired[bool]

class NavigatorUABrandVersion(TypedDict):
    brand: NotRequired[str]
    version: NotRequired[str]

class UADataValues(TypedDict):
    architecture: NotRequired[str]
    bitness: NotRequired[str]
    brands: NotRequired[Sequence[NavigatorUABrandVersion]]
    formFactor: NotRequired[str]
    fullVersionList: NotRequired[Sequence[NavigatorUABrandVersion]]
    model: NotRequired[str]
    mobile: NotRequired[bool]
    platform: NotRequired[str]
    platformVersion: NotRequired[str]
    uaFullVersion: NotRequired[str]
    wow64: NotRequired[bool]

class UALowEntropyJSON(TypedDict):
    brands: NotRequired[Sequence[NavigatorUABrandVersion]]
    mobile: NotRequired[bool]
    platform: NotRequired[str]

class NavigatorUAData:
    brands: Sequence[NavigatorUABrandVersion]
    mobile: bool
    platform: str

    def getHighEntropyValues(self, hints: Sequence[str]) -> Awaitable[UADataValues]: ...

    def toJSON(self) -> UALowEntropyJSON: ...

class NavigatorUA:
    userAgentData: NavigatorUAData

class FocusEvent(UIEvent):
    @classmethod
    def new(cls, type: str, eventInitDict: Union['FocusEventInit', 'None'] = {}) -> FocusEvent: ...
    relatedTarget: Union['EventTarget', 'None']

class FocusEventInit(UIEventInit):
    relatedTarget: NotRequired[Union['EventTarget', 'None']]

class EventModifierInit(UIEventInit):
    ctrlKey: NotRequired[bool]
    shiftKey: NotRequired[bool]
    altKey: NotRequired[bool]
    metaKey: NotRequired[bool]
    modifierAltGraph: NotRequired[bool]
    modifierCapsLock: NotRequired[bool]
    modifierFn: NotRequired[bool]
    modifierFnLock: NotRequired[bool]
    modifierHyper: NotRequired[bool]
    modifierNumLock: NotRequired[bool]
    modifierScrollLock: NotRequired[bool]
    modifierSuper: NotRequired[bool]
    modifierSymbol: NotRequired[bool]
    modifierSymbolLock: NotRequired[bool]

class WheelEvent(MouseEvent):
    @classmethod
    def new(cls, type: str, eventInitDict: Union['WheelEventInit', 'None'] = {}) -> WheelEvent: ...
    DOM_DELTA_PIXEL = 0x00
    DOM_DELTA_LINE = 0x01
    DOM_DELTA_PAGE = 0x02
    deltaX: float
    deltaY: float
    deltaZ: float
    deltaMode: int

class WheelEventInit(MouseEventInit):
    deltaX: NotRequired[float]
    deltaY: NotRequired[float]
    deltaZ: NotRequired[float]
    deltaMode: NotRequired[int]

class KeyboardEvent(UIEvent):
    @classmethod
    def new(cls, type: str, eventInitDict: Union['KeyboardEventInit', 'None'] = {}) -> KeyboardEvent: ...
    DOM_KEY_LOCATION_STANDARD = 0x00
    DOM_KEY_LOCATION_LEFT = 0x01
    DOM_KEY_LOCATION_RIGHT = 0x02
    DOM_KEY_LOCATION_NUMPAD = 0x03
    key: str
    code: str
    location: int
    ctrlKey: bool
    shiftKey: bool
    altKey: bool
    metaKey: bool
    repeat: bool
    isComposing: bool

    def getModifierState(self, keyArg: str) -> bool: ...

    def initKeyboardEvent(self, typeArg: str, bubblesArg: Union['bool', 'None'] = False, cancelableArg: Union['bool', 'None'] = False, viewArg: Union['Window', 'None'] = None, keyArg: Union['str', 'None'] = "", locationArg: Union['int', 'None'] = 0, ctrlKey: Union['bool', 'None'] = False, altKey: Union['bool', 'None'] = False, shiftKey: Union['bool', 'None'] = False, metaKey: Union['bool', 'None'] = False) -> None: ...
    charCode: int
    keyCode: int

class KeyboardEventInit(EventModifierInit, TypedDict):
    key: NotRequired[str]
    code: NotRequired[str]
    location: NotRequired[int]
    repeat: NotRequired[bool]
    isComposing: NotRequired[bool]
    charCode: NotRequired[int]
    keyCode: NotRequired[int]

class CompositionEvent(UIEvent):
    @classmethod
    def new(cls, type: str, eventInitDict: Union['CompositionEventInit', 'None'] = {}) -> CompositionEvent: ...
    data: str

    def initCompositionEvent(self, typeArg: str, bubblesArg: Union['bool', 'None'] = False, cancelableArg: Union['bool', 'None'] = False, viewArg: Union['WindowProxy', 'None'] = None, dataArg: Union['str', 'None'] = "") -> None: ...

class CompositionEventInit(UIEventInit):
    data: NotRequired[str]

class MutationEvent(Event):
    MODIFICATION = 1
    ADDITION = 2
    REMOVAL = 3
    relatedNode: Union['Node', 'None']
    prevValue: str
    newValue: str
    attrName: str
    attrChange: int

    def initMutationEvent(self, typeArg: str, bubblesArg: Union['bool', 'None'] = False, cancelableArg: Union['bool', 'None'] = False, relatedNodeArg: Union['Node', 'None'] = None, prevValueArg: Union['str', 'None'] = "", newValueArg: Union['str', 'None'] = "", attrNameArg: Union['str', 'None'] = "", attrChangeArg: Union['int', 'None'] = 0) -> None: ...

class URLSearchParams:
    @classmethod
    def new(cls, init: Union['Sequence[Sequence[str]]', 'str', 'str', 'None'] = "") -> URLSearchParams: ...
    size: int

    def append(self, name: str, value: str) -> None: ...

    def delete(self, name: str, value: Union['str', 'None'] = None) -> None: ...

    def get(self, name: str) -> Union['str', 'None']: ...

    def getAll(self, name: str) -> Sequence[str]: ...

    def has(self, name: str, value: Union['str', 'None'] = None) -> bool: ...

    def set(self, name: str, value: str) -> None: ...

    def sort(self) -> None: ...

class URLPattern:
    @overload
    @classmethod
    def new(cls, input: URLPatternInput, baseURL: str, options: Union['URLPatternOptions', 'None'] = {}) -> URLPattern: ...
    @overload
    @classmethod
    def new(cls, input: Union['URLPatternInput', 'None'] = {}, options: Union['URLPatternOptions', 'None'] = {}) -> URLPattern: ...

    def test(self, input: Union['URLPatternInput', 'None'] = {}, baseURL: Union['str', 'None'] = None) -> bool: ...

    def exec(self, input: Union['URLPatternInput', 'None'] = {}, baseURL: Union['str', 'None'] = None) -> Union['URLPatternResult', 'None']: ...
    protocol: str
    username: str
    password: str
    hostname: str
    port: str
    pathname: str
    search: str
    hash: str

class URLPatternInit(TypedDict):
    protocol: NotRequired[str]
    username: NotRequired[str]
    password: NotRequired[str]
    hostname: NotRequired[str]
    port: NotRequired[str]
    pathname: NotRequired[str]
    search: NotRequired[str]
    hash: NotRequired[str]
    baseURL: NotRequired[str]

class URLPatternOptions(TypedDict):
    ignoreCase: NotRequired[bool]

class URLPatternResult(TypedDict):
    inputs: NotRequired[Sequence[URLPatternInput]]
    protocol: NotRequired[URLPatternComponentResult]
    username: NotRequired[URLPatternComponentResult]
    password: NotRequired[URLPatternComponentResult]
    hostname: NotRequired[URLPatternComponentResult]
    port: NotRequired[URLPatternComponentResult]
    pathname: NotRequired[URLPatternComponentResult]
    search: NotRequired[URLPatternComponentResult]
    hash: NotRequired[URLPatternComponentResult]

class URLPatternComponentResult(TypedDict):
    input: NotRequired[str]
    groups: NotRequired[Union['str', 'None']]

class PerformanceMarkOptions(TypedDict):
    detail: NotRequired[Any]
    startTime: NotRequired[DOMHighResTimeStamp]

class PerformanceMeasureOptions(TypedDict):
    detail: NotRequired[Any]
    start: NotRequired[Union['str', 'DOMHighResTimeStamp']]
    duration: NotRequired[DOMHighResTimeStamp]
    end: NotRequired[Union['str', 'DOMHighResTimeStamp']]

class PerformanceMark(PerformanceEntry):
    @classmethod
    def new(cls, markName: str, markOptions: Union['PerformanceMarkOptions', 'None'] = {}) -> PerformanceMark: ...
    detail: Any

class PerformanceMeasure(PerformanceEntry):
    detail: Any

class VideoFrameCallbackMetadata(TypedDict):
    presentationTime: DOMHighResTimeStamp
    expectedDisplayTime: DOMHighResTimeStamp
    width: int
    height: int
    mediaTime: float
    presentedFrames: int
    processingDuration: NotRequired[float]
    captureTime: NotRequired[DOMHighResTimeStamp]
    receiveTime: NotRequired[DOMHighResTimeStamp]
    rtpTimestamp: NotRequired[int]

class VirtualKeyboard(EventTarget):

    def show(self) -> None: ...

    def hide(self) -> None: ...
    boundingRect: DOMRect
    overlaysContent: bool
    ongeometrychange: EventHandler

class ARIAMixin:
    role: Union['str', 'None']
    ariaActiveDescendantElement: Union['Element', 'None']
    ariaAtomic: Union['str', 'None']
    ariaAutoComplete: Union['str', 'None']
    ariaBusy: Union['str', 'None']
    ariaChecked: Union['str', 'None']
    ariaColCount: Union['str', 'None']
    ariaColIndex: Union['str', 'None']
    ariaColIndexText: Union['str', 'None']
    ariaColSpan: Union['str', 'None']
    ariaControlsElements: Sequence[Element]
    ariaCurrent: Union['str', 'None']
    ariaDescribedByElements: Sequence[Element]
    ariaDescription: Union['str', 'None']
    ariaDetailsElements: Sequence[Element]
    ariaDisabled: Union['str', 'None']
    ariaErrorMessageElements: Sequence[Element]
    ariaExpanded: Union['str', 'None']
    ariaFlowToElements: Sequence[Element]
    ariaHasPopup: Union['str', 'None']
    ariaHidden: Union['str', 'None']
    ariaInvalid: Union['str', 'None']
    ariaKeyShortcuts: Union['str', 'None']
    ariaLabel: Union['str', 'None']
    ariaLabelledByElements: Sequence[Element]
    ariaLevel: Union['str', 'None']
    ariaLive: Union['str', 'None']
    ariaModal: Union['str', 'None']
    ariaMultiLine: Union['str', 'None']
    ariaMultiSelectable: Union['str', 'None']
    ariaOrientation: Union['str', 'None']
    ariaOwnsElements: Sequence[Element]
    ariaPlaceholder: Union['str', 'None']
    ariaPosInSet: Union['str', 'None']
    ariaPressed: Union['str', 'None']
    ariaReadOnly: Union['str', 'None']
    ariaRequired: Union['str', 'None']
    ariaRoleDescription: Union['str', 'None']
    ariaRowCount: Union['str', 'None']
    ariaRowIndex: Union['str', 'None']
    ariaRowIndexText: Union['str', 'None']
    ariaRowSpan: Union['str', 'None']
    ariaSelected: Union['str', 'None']
    ariaSetSize: Union['str', 'None']
    ariaSort: Union['str', 'None']
    ariaValueMax: Union['str', 'None']
    ariaValueMin: Union['str', 'None']
    ariaValueNow: Union['str', 'None']
    ariaValueText: Union['str', 'None']

class WebAssemblyInstantiatedSource(TypedDict):
    module: Module
    instance: Instance

class WebassemblyNamespace:

    def validate(self, bytes: BufferSource) -> bool: ...

    def compile(self, bytes: BufferSource) -> Awaitable[Module]: ...
    @overload
    def instantiate(self, bytes: BufferSource, importObject: Union['object', 'None'] = None) -> Awaitable[WebAssemblyInstantiatedSource]: ...
    @overload
    def instantiate(self, moduleObject: Module, importObject: Union['object', 'None'] = None) -> Awaitable[Instance]: ...

    def compileStreaming(self, source: Awaitable[Response]) -> Awaitable[Module]: ...

    def instantiateStreaming(self, source: Awaitable[Response], importObject: Union['object', 'None'] = None) -> Awaitable[WebAssemblyInstantiatedSource]: ...

class ModuleExportDescriptor(TypedDict):
    name: str
    kind: ImportExportKind

class ModuleImportDescriptor(TypedDict):
    module: str
    name: str
    kind: ImportExportKind

class Module:
    @classmethod
    def new(cls, bytes: BufferSource) -> Module: ...

class Instance:
    @classmethod
    def new(cls, module: Module, importObject: Union['object', 'None'] = None) -> Instance: ...
    exports: object

class MemoryDescriptor(TypedDict):
    initial: int
    maximum: NotRequired[int]

class Memory:
    @classmethod
    def new(cls, descriptor: MemoryDescriptor) -> Memory: ...

    def grow(self, delta: int) -> int: ...
    buffer: ArrayBuffer

class TableDescriptor(TypedDict):
    element: TableKind
    initial: int
    maximum: NotRequired[int]

class Table:
    @classmethod
    def new(cls, descriptor: TableDescriptor, value: Union['Any', 'None'] = None) -> Table: ...

    def grow(self, delta: int, value: Union['Any', 'None'] = None) -> int: ...

    def get(self, index: int) -> Any: ...

    def set(self, index: int, value: Union['Any', 'None'] = None) -> None: ...
    length: int

class GlobalDescriptor(TypedDict):
    value: ValueType
    mutable: NotRequired[bool]

class Global:
    @classmethod
    def new(cls, descriptor: GlobalDescriptor, v: Union['Any', 'None'] = None) -> Global: ...

    def valueOf(self) -> Any: ...
    value: Any

class AnimationTimeline:
    currentTime: Union['CSSNumberish', 'None']
    duration: Union['CSSNumberish', 'None']

    def play(self, effect: Union['AnimationEffect', 'None'] = None) -> Animation: ...

class Animation(EventTarget):
    @classmethod
    def new(cls, effect: Union['AnimationEffect', 'None'] = None, timeline: Union['AnimationTimeline', 'None'] = None) -> Animation: ...
    startTime: Union['CSSNumberish', 'None']
    currentTime: Union['CSSNumberish', 'None']
    id: str
    effect: Union['AnimationEffect', 'None']
    timeline: Union['AnimationTimeline', 'None']
    playbackRate: float
    playState: AnimationPlayState
    replaceState: AnimationReplaceState
    pending: bool
    ready: Awaitable[Animation]
    finished: Awaitable[Animation]
    onfinish: EventHandler
    oncancel: EventHandler
    onremove: EventHandler

    def cancel(self) -> None: ...

    def finish(self) -> None: ...

    def play(self) -> None: ...

    def pause(self) -> None: ...

    def updatePlaybackRate(self, playbackRate: float) -> None: ...

    def reverse(self) -> None: ...

    def persist(self) -> None: ...

    def commitStyles(self) -> None: ...

class AnimationEffect:
    parent: Union['GroupEffect', 'None']
    previousSibling: Union['AnimationEffect', 'None']
    nextSibling: Union['AnimationEffect', 'None']

    def before(self, *effects: AnimationEffect) -> None: ...

    def after(self, *effects: AnimationEffect) -> None: ...

    def replace(self, *effects: AnimationEffect) -> None: ...

    def remove(self) -> None: ...

    def getTiming(self) -> EffectTiming: ...

    def getComputedTiming(self) -> ComputedEffectTiming: ...

    def updateTiming(self, timing: Union['OptionalEffectTiming', 'None'] = {}) -> None: ...

class EffectTiming(TypedDict):
    delay: NotRequired[float]
    endDelay: NotRequired[float]
    playbackRate: NotRequired[float]
    duration: NotRequired[Union['float', 'CSSNumericValue', 'str']]
    fill: NotRequired[FillMode]
    iterationStart: NotRequired[float]
    iterations: NotRequired[float]
    direction: NotRequired[PlaybackDirection]
    easing: NotRequired[str]

class OptionalEffectTiming(TypedDict):
    playbackRate: NotRequired[float]
    delay: NotRequired[float]
    endDelay: NotRequired[float]
    fill: NotRequired[FillMode]
    iterationStart: NotRequired[float]
    iterations: NotRequired[float]
    duration: NotRequired[Union['float', 'str']]
    direction: NotRequired[PlaybackDirection]
    easing: NotRequired[str]

class ComputedEffectTiming(TypedDict, EffectTiming):
    startTime: NotRequired[CSSNumberish]
    endTime: NotRequired[CSSNumberish]
    activeDuration: NotRequired[CSSNumberish]
    localTime: NotRequired[Union['CSSNumberish', 'None']]
    progress: NotRequired[Union['float', 'None']]
    currentIteration: NotRequired[Union['float', 'None']]

class GroupEffect:
    @classmethod
    def new(cls, children: Sequence[AnimationEffect], timing: Union['float', 'EffectTiming', 'None'] = {}) -> GroupEffect: ...
    children: AnimationNodeList
    firstChild: Union['AnimationEffect', 'None']
    lastChild: Union['AnimationEffect', 'None']

    def clone(self) -> GroupEffect: ...

    def prepend(self, *effects: AnimationEffect) -> None: ...

    def append(self, *effects: AnimationEffect) -> None: ...

class AnimationNodeList:
    length: int

    def item(self, index: int) -> Union['AnimationEffect', 'None']: ...

class SequenceEffect(GroupEffect):
    @classmethod
    def new(cls, children: Sequence[AnimationEffect], timing: Union['float', 'EffectTiming', 'None'] = {}) -> SequenceEffect: ...

    def clone(self) -> SequenceEffect: ...

class KeyframeEffect(AnimationEffect):
    @overload
    @classmethod
    def new(cls, target: Union['Element', 'None'], keyframes: Union['object', 'None'], options: Union['float', 'KeyframeEffectOptions', 'None'] = {}) -> KeyframeEffect: ...
    @overload
    @classmethod
    def new(cls, source: KeyframeEffect) -> KeyframeEffect: ...
    iterationComposite: IterationCompositeOperation
    target: Union['Element', 'None']
    pseudoElement: Union['str', 'None']
    composite: CompositeOperation

    def getKeyframes(self) -> Sequence[object]: ...

    def setKeyframes(self, keyframes: Union['object', 'None']) -> None: ...

class KeyframeEffectOptions(TypedDict, EffectTiming):
    iterationComposite: NotRequired[IterationCompositeOperation]
    composite: NotRequired[CompositeOperation]
    pseudoElement: NotRequired[Union['str', 'None']]

class TimelineRangeOffset(TypedDict):
    rangeName: NotRequired[Union['str', 'None']]
    offset: NotRequired[CSSNumericValue]

class KeyframeAnimationOptions(TypedDict, KeyframeEffectOptions):
    rangeStart: NotRequired[Union['TimelineRangeOffset', 'CSSNumericValue', 'CSSKeywordValue', 'str']]
    rangeEnd: NotRequired[Union['TimelineRangeOffset', 'CSSNumericValue', 'CSSKeywordValue', 'str']]
    id: NotRequired[str]
    timeline: NotRequired[Union['AnimationTimeline', 'None']]

class AnimationPlaybackEvent(Event):
    @classmethod
    def new(cls, type: str, eventInitDict: Union['AnimationPlaybackEventInit', 'None'] = {}) -> AnimationPlaybackEvent: ...
    currentTime: Union['CSSNumberish', 'None']
    timelineTime: Union['CSSNumberish', 'None']

class AnimationPlaybackEventInit(EventInit):
    currentTime: NotRequired[Union['CSSNumberish', 'None']]
    timelineTime: NotRequired[Union['CSSNumberish', 'None']]

class DocumentTimelineOptions(TypedDict):
    originTime: NotRequired[DOMHighResTimeStamp]

class DocumentTimeline(AnimationTimeline):
    @classmethod
    def new(cls, options: Union['DocumentTimelineOptions', 'None'] = {}) -> DocumentTimeline: ...

class BaseComputedKeyframe(TypedDict):
    offset: NotRequired[Union['float', 'None']]
    computedOffset: NotRequired[float]
    easing: NotRequired[str]
    composite: NotRequired[CompositeOperationOrAuto]

class BasePropertyIndexedKeyframe(TypedDict):
    offset: NotRequired[Union['Union["float", "None"]', 'Sequence[Union["float", "None"]]']]
    easing: NotRequired[Union['str', 'Sequence[str]']]
    composite: NotRequired[Union['CompositeOperationOrAuto', 'Sequence[CompositeOperationOrAuto]']]

class BaseKeyframe(TypedDict):
    offset: NotRequired[Union['float', 'None']]
    easing: NotRequired[str]
    composite: NotRequired[CompositeOperationOrAuto]

class Animatable:

    def animate(self, keyframes: Union['object', 'None'], options: Union['float', 'KeyframeAnimationOptions', 'None'] = {}) -> Animation: ...

    def getAnimations(self, options: Union['GetAnimationsOptions', 'None'] = {}) -> Sequence[Animation]: ...

class GetAnimationsOptions(TypedDict):
    subtree: NotRequired[bool]

class LaunchParams:
    targetURL: Union['str', 'None']
    files: Sequence[FileSystemHandle]

class LaunchQueue:

    def setConsumer(self, consumer: LaunchConsumer) -> None: ...

class BluetoothDataFilterInit(TypedDict):
    dataPrefix: NotRequired[BufferSource]
    mask: NotRequired[BufferSource]

class BluetoothManufacturerDataFilterInit(BluetoothDataFilterInit):
    companyIdentifier: int

class BluetoothServiceDataFilterInit(BluetoothDataFilterInit):
    service: BluetoothServiceUUID

class BluetoothLEScanFilterInit(TypedDict):
    services: NotRequired[Sequence[BluetoothServiceUUID]]
    name: NotRequired[str]
    namePrefix: NotRequired[str]
    manufacturerData: NotRequired[Sequence[BluetoothManufacturerDataFilterInit]]
    serviceData: NotRequired[Sequence[BluetoothServiceDataFilterInit]]

class RequestDeviceOptions(TypedDict):
    filters: NotRequired[Sequence[BluetoothLEScanFilterInit]]
    exclusionFilters: NotRequired[Sequence[BluetoothLEScanFilterInit]]
    optionalServices: NotRequired[Sequence[BluetoothServiceUUID]]
    optionalManufacturerData: NotRequired[Sequence[int]]
    acceptAllDevices: NotRequired[bool]

class Bluetooth(EventTarget, BluetoothDeviceEventHandlers, CharacteristicEventHandlers, ServiceEventHandlers):

    def getAvailability(self) -> Awaitable[bool]: ...
    onavailabilitychanged: EventHandler
    referringDevice: Union['BluetoothDevice', 'None']

    def getDevices(self) -> Awaitable[Sequence[BluetoothDevice]]: ...

    def requestDevice(self, options: Union['RequestDeviceOptions', 'None'] = {}) -> Awaitable[BluetoothDevice]: ...

class BluetoothPermissionDescriptor(PermissionDescriptor):
    deviceId: NotRequired[str]
    filters: NotRequired[Sequence[BluetoothLEScanFilterInit]]
    optionalServices: NotRequired[Sequence[BluetoothServiceUUID]]
    optionalManufacturerData: NotRequired[Sequence[int]]
    acceptAllDevices: NotRequired[bool]

class AllowedBluetoothDevice(TypedDict):
    deviceId: str
    mayUseGATT: bool
    allowedServices: Union['str', 'Sequence[UUID]']
    allowedManufacturerData: Sequence[int]

class BluetoothPermissionStorage(TypedDict):
    allowedDevices: Sequence[AllowedBluetoothDevice]

class BluetoothPermissionResult(PermissionStatus):
    devices: Sequence[BluetoothDevice]

class ValueEvent(Event):
    @classmethod
    def new(cls, type: str, initDict: Union['ValueEventInit', 'None'] = {}) -> ValueEvent: ...
    value: Any

class ValueEventInit(EventInit):
    value: NotRequired[Any]

class BluetoothDevice(EventTarget, BluetoothDeviceEventHandlers, CharacteristicEventHandlers, ServiceEventHandlers):
    id: str
    name: Union['str', 'None']
    gatt: Union['BluetoothRemoteGATTServer', 'None']

    def forget(self) -> Awaitable[None]: ...

    def watchAdvertisements(self, options: Union['WatchAdvertisementsOptions', 'None'] = {}) -> Awaitable[None]: ...
    watchingAdvertisements: bool

class WatchAdvertisementsOptions(TypedDict):
    signal: NotRequired[AbortSignal]

class BluetoothManufacturerDataMap: ...

class BluetoothServiceDataMap: ...

class BluetoothAdvertisingEvent(Event):
    @classmethod
    def new(cls, type: str, init: BluetoothAdvertisingEventInit) -> BluetoothAdvertisingEvent: ...
    device: BluetoothDevice
    uuids: Sequence[UUID]
    name: Union['str', 'None']
    appearance: Union['int', 'None']
    txPower: Union['int', 'None']
    rssi: Union['int', 'None']
    manufacturerData: BluetoothManufacturerDataMap
    serviceData: BluetoothServiceDataMap

class BluetoothAdvertisingEventInit(EventInit):
    device: BluetoothDevice
    uuids: NotRequired[Sequence[Union['str', 'int']]]
    name: NotRequired[str]
    appearance: NotRequired[int]
    txPower: NotRequired[int]
    rssi: NotRequired[int]
    manufacturerData: NotRequired[BluetoothManufacturerDataMap]
    serviceData: NotRequired[BluetoothServiceDataMap]

class BluetoothRemoteGATTServer:
    device: BluetoothDevice
    connected: bool

    def connect(self) -> Awaitable[BluetoothRemoteGATTServer]: ...

    def disconnect(self) -> None: ...

    def getPrimaryService(self, service: BluetoothServiceUUID) -> Awaitable[BluetoothRemoteGATTService]: ...

    def getPrimaryServices(self, service: Union['BluetoothServiceUUID', 'None'] = None) -> Awaitable[Sequence[BluetoothRemoteGATTService]]: ...

class BluetoothRemoteGATTService(EventTarget, CharacteristicEventHandlers, ServiceEventHandlers):
    device: BluetoothDevice
    uuid: UUID
    isPrimary: bool

    def getCharacteristic(self, characteristic: BluetoothCharacteristicUUID) -> Awaitable[BluetoothRemoteGATTCharacteristic]: ...

    def getCharacteristics(self, characteristic: Union['BluetoothCharacteristicUUID', 'None'] = None) -> Awaitable[Sequence[BluetoothRemoteGATTCharacteristic]]: ...

    def getIncludedService(self, service: BluetoothServiceUUID) -> Awaitable[BluetoothRemoteGATTService]: ...

    def getIncludedServices(self, service: Union['BluetoothServiceUUID', 'None'] = None) -> Awaitable[Sequence[BluetoothRemoteGATTService]]: ...

class BluetoothRemoteGATTCharacteristic(EventTarget, CharacteristicEventHandlers):
    service: BluetoothRemoteGATTService
    uuid: UUID
    properties: BluetoothCharacteristicProperties
    value: DataView

    def getDescriptor(self, descriptor: BluetoothDescriptorUUID) -> Awaitable[BluetoothRemoteGATTDescriptor]: ...

    def getDescriptors(self, descriptor: Union['BluetoothDescriptorUUID', 'None'] = None) -> Awaitable[Sequence[BluetoothRemoteGATTDescriptor]]: ...

    def readValue(self) -> Awaitable[DataView]: ...

    def writeValue(self, value: BufferSource) -> Awaitable[None]: ...

    def writeValueWithResponse(self, value: BufferSource) -> Awaitable[None]: ...

    def writeValueWithoutResponse(self, value: BufferSource) -> Awaitable[None]: ...

    def startNotifications(self) -> Awaitable[BluetoothRemoteGATTCharacteristic]: ...

    def stopNotifications(self) -> Awaitable[BluetoothRemoteGATTCharacteristic]: ...

class BluetoothCharacteristicProperties:
    broadcast: bool
    read: bool
    writeWithoutResponse: bool
    write: bool
    notify: bool
    indicate: bool
    authenticatedSignedWrites: bool
    reliableWrite: bool
    writableAuxiliaries: bool

class BluetoothRemoteGATTDescriptor:
    characteristic: BluetoothRemoteGATTCharacteristic
    uuid: UUID
    value: DataView

    def readValue(self) -> Awaitable[DataView]: ...

    def writeValue(self, value: BufferSource) -> Awaitable[None]: ...

class CharacteristicEventHandlers:
    oncharacteristicvaluechanged: EventHandler

class BluetoothDeviceEventHandlers:
    onadvertisementreceived: EventHandler
    ongattserverdisconnected: EventHandler

class ServiceEventHandlers:
    onserviceadded: EventHandler
    onservicechanged: EventHandler
    onserviceremoved: EventHandler

class BluetoothUUID: ...

class NavigatorLocks:
    locks: LockManager

class LockManager:
    @overload
    def request(self, name: str, callback: LockGrantedCallback) -> Awaitable[Any]: ...
    @overload
    def request(self, name: str, options: LockOptions, callback: LockGrantedCallback) -> Awaitable[Any]: ...

    def query(self) -> Awaitable[LockManagerSnapshot]: ...

class LockOptions(TypedDict):
    mode: NotRequired[LockMode]
    ifAvailable: NotRequired[bool]
    steal: NotRequired[bool]
    signal: NotRequired[AbortSignal]

class LockManagerSnapshot(TypedDict):
    held: NotRequired[Sequence[LockInfo]]
    pending: NotRequired[Sequence[LockInfo]]

class LockInfo(TypedDict):
    name: NotRequired[str]
    mode: NotRequired[LockMode]
    clientId: NotRequired[str]

class Lock:
    name: str
    mode: LockMode

class NDEFMessage:
    @classmethod
    def new(cls, messageInit: NDEFMessageInit) -> NDEFMessage: ...
    records: Sequence[NDEFRecord]

class NDEFMessageInit(TypedDict):
    records: Sequence[NDEFRecordInit]

class NDEFRecord:
    @classmethod
    def new(cls, recordInit: NDEFRecordInit) -> NDEFRecord: ...
    recordType: str
    mediaType: Union['str', 'None']
    id: Union['str', 'None']
    data: DataView
    encoding: Union['str', 'None']
    lang: Union['str', 'None']

    def toRecords(self) -> Sequence[NDEFRecord]: ...

class NDEFRecordInit(TypedDict):
    recordType: str
    mediaType: NotRequired[str]
    id: NotRequired[str]
    encoding: NotRequired[str]
    lang: NotRequired[str]
    data: NotRequired[Any]

class NDEFReader(EventTarget):
    @classmethod
    def new(cls) -> NDEFReader: ...
    onreading: EventHandler
    onreadingerror: EventHandler

    def scan(self, options: Union['NDEFScanOptions', 'None'] = {}) -> Awaitable[None]: ...

    def write(self, message: NDEFMessageSource, options: Union['NDEFWriteOptions', 'None'] = {}) -> Awaitable[None]: ...

    def makeReadOnly(self, options: Union['NDEFMakeReadOnlyOptions', 'None'] = {}) -> Awaitable[None]: ...

class NDEFReadingEvent(Event):
    @classmethod
    def new(cls, type: str, readingEventInitDict: NDEFReadingEventInit) -> NDEFReadingEvent: ...
    serialNumber: str
    message: NDEFMessage

class NDEFReadingEventInit(EventInit):
    serialNumber: NotRequired[Union['str', 'None']]
    message: NDEFMessageInit

class NDEFWriteOptions(TypedDict):
    overwrite: NotRequired[bool]
    signal: NotRequired[Union['AbortSignal', 'None']]

class NDEFMakeReadOnlyOptions(TypedDict):
    signal: NotRequired[Union['AbortSignal', 'None']]

class NDEFScanOptions(TypedDict):
    signal: NotRequired[AbortSignal]

class OTPCredential(Credential):
    code: str

class OTPCredentialRequestOptions(TypedDict):
    transport: NotRequired[Sequence[OTPCredentialTransportType]]

class ShareData(TypedDict):
    files: NotRequired[Sequence[File]]
    title: NotRequired[str]
    text: NotRequired[str]
    url: NotRequired[str]

class BaseAudioContext(EventTarget):
    destination: AudioDestinationNode
    sampleRate: float
    currentTime: float
    listener: AudioListener
    state: AudioContextState
    audioWorklet: AudioWorklet
    onstatechange: EventHandler

    def createAnalyser(self) -> AnalyserNode: ...

    def createBiquadFilter(self) -> BiquadFilterNode: ...

    def createBuffer(self, numberOfChannels: int, length: int, sampleRate: float) -> AudioBuffer: ...

    def createBufferSource(self) -> AudioBufferSourceNode: ...

    def createChannelMerger(self, numberOfInputs: Union['int', 'None'] = 6) -> ChannelMergerNode: ...

    def createChannelSplitter(self, numberOfOutputs: Union['int', 'None'] = 6) -> ChannelSplitterNode: ...

    def createConstantSource(self) -> ConstantSourceNode: ...

    def createConvolver(self) -> ConvolverNode: ...

    def createDelay(self, maxDelayTime: Union['float', 'None'] = 1.0) -> DelayNode: ...

    def createDynamicsCompressor(self) -> DynamicsCompressorNode: ...

    def createGain(self) -> GainNode: ...

    def createIIRFilter(self, feedforward: Sequence[float], feedback: Sequence[float]) -> IIRFilterNode: ...

    def createOscillator(self) -> OscillatorNode: ...

    def createPanner(self) -> PannerNode: ...

    def createPeriodicWave(self, real: Sequence[float], imag: Sequence[float], constraints: Union['PeriodicWaveConstraints', 'None'] = {}) -> PeriodicWave: ...

    def createScriptProcessor(self, bufferSize: Union['int', 'None'] = 0, numberOfInputChannels: Union['int', 'None'] = 2, numberOfOutputChannels: Union['int', 'None'] = 2) -> ScriptProcessorNode: ...

    def createStereoPanner(self) -> StereoPannerNode: ...

    def createWaveShaper(self) -> WaveShaperNode: ...

    def decodeAudioData(self, audioData: ArrayBuffer, successCallback: Union['DecodeSuccessCallback', 'None'] = None, errorCallback: Union['DecodeErrorCallback', 'None'] = None) -> Awaitable[AudioBuffer]: ...

class AudioContext(BaseAudioContext):
    @classmethod
    def new(cls, contextOptions: Union['AudioContextOptions', 'None'] = {}) -> AudioContext: ...
    baseLatency: float
    outputLatency: float
    sinkId: Union['str', 'AudioSinkInfo']
    renderCapacity: AudioRenderCapacity
    onsinkchange: EventHandler

    def getOutputTimestamp(self) -> AudioTimestamp: ...

    def resume(self) -> Awaitable[None]: ...

    def suspend(self) -> Awaitable[None]: ...

    def close(self) -> Awaitable[None]: ...

    def setSinkId(self, sinkId: Union['str', 'AudioSinkOptions']) -> Awaitable[None]: ...

    def createMediaElementSource(self, mediaElement: HTMLMediaElement) -> MediaElementAudioSourceNode: ...

    def createMediaStreamSource(self, mediaStream: MediaStream) -> MediaStreamAudioSourceNode: ...

    def createMediaStreamTrackSource(self, mediaStreamTrack: MediaStreamTrack) -> MediaStreamTrackAudioSourceNode: ...

    def createMediaStreamDestination(self) -> MediaStreamAudioDestinationNode: ...

class AudioContextOptions(TypedDict):
    latencyHint: NotRequired[Union['AudioContextLatencyCategory', 'float']]
    sampleRate: NotRequired[float]
    sinkId: NotRequired[Union['str', 'AudioSinkOptions']]

class AudioSinkOptions(TypedDict):
    type: AudioSinkType

class AudioSinkInfo:
    type: AudioSinkType

class AudioTimestamp(TypedDict):
    contextTime: NotRequired[float]
    performanceTime: NotRequired[DOMHighResTimeStamp]

class AudioRenderCapacity(EventTarget):

    def start(self, options: Union['AudioRenderCapacityOptions', 'None'] = {}) -> None: ...

    def stop(self) -> None: ...
    onupdate: EventHandler

class AudioRenderCapacityOptions(TypedDict):
    updateInterval: NotRequired[float]

class AudioRenderCapacityEvent(Event):
    @classmethod
    def new(cls, type: str, eventInitDict: Union['AudioRenderCapacityEventInit', 'None'] = {}) -> AudioRenderCapacityEvent: ...
    timestamp: float
    averageLoad: float
    peakLoad: float
    underrunRatio: float

class AudioRenderCapacityEventInit(EventInit):
    timestamp: NotRequired[float]
    averageLoad: NotRequired[float]
    peakLoad: NotRequired[float]
    underrunRatio: NotRequired[float]

class OfflineAudioContext(BaseAudioContext):
    @overload
    @classmethod
    def new(cls, contextOptions: OfflineAudioContextOptions) -> OfflineAudioContext: ...
    @overload
    @classmethod
    def new(cls, numberOfChannels: int, length: int, sampleRate: float) -> OfflineAudioContext: ...

    def startRendering(self) -> Awaitable[AudioBuffer]: ...

    def resume(self) -> Awaitable[None]: ...

    def suspend(self, suspendTime: float) -> Awaitable[None]: ...
    length: int
    oncomplete: EventHandler

class OfflineAudioContextOptions(TypedDict):
    numberOfChannels: NotRequired[int]
    length: int
    sampleRate: float

class OfflineAudioCompletionEvent(Event):
    @classmethod
    def new(cls, type: str, eventInitDict: OfflineAudioCompletionEventInit) -> OfflineAudioCompletionEvent: ...
    renderedBuffer: AudioBuffer

class OfflineAudioCompletionEventInit(EventInit):
    renderedBuffer: AudioBuffer

class AudioBuffer:
    @classmethod
    def new(cls, options: AudioBufferOptions) -> AudioBuffer: ...
    sampleRate: float
    length: int
    duration: float
    numberOfChannels: int

    def getChannelData(self, channel: int) -> Float32Array: ...

    def copyFromChannel(self, destination: Float32Array, channelNumber: int, bufferOffset: Union['int', 'None'] = 0) -> None: ...

    def copyToChannel(self, source: Float32Array, channelNumber: int, bufferOffset: Union['int', 'None'] = 0) -> None: ...

class AudioBufferOptions(TypedDict):
    numberOfChannels: NotRequired[int]
    length: int
    sampleRate: float

class AudioNode(EventTarget):
    @overload
    def connect(self, destinationNode: AudioNode, output: Union['int', 'None'] = 0, input: Union['int', 'None'] = 0) -> AudioNode: ...
    @overload
    def connect(self, destinationParam: AudioParam, output: Union['int', 'None'] = 0) -> None: ...
    @overload
    def disconnect(self) -> None: ...
    @overload
    def disconnect(self, output: int) -> None: ...
    @overload
    def disconnect(self, destinationNode: AudioNode) -> None: ...
    @overload
    def disconnect(self, destinationNode: AudioNode, output: int) -> None: ...
    @overload
    def disconnect(self, destinationNode: AudioNode, output: int, input: int) -> None: ...
    @overload
    def disconnect(self, destinationParam: AudioParam) -> None: ...
    @overload
    def disconnect(self, destinationParam: AudioParam, output: int) -> None: ...
    context: BaseAudioContext
    numberOfInputs: int
    numberOfOutputs: int
    channelCount: int
    channelCountMode: ChannelCountMode
    channelInterpretation: ChannelInterpretation

class AudioNodeOptions(TypedDict):
    channelCount: NotRequired[int]
    channelCountMode: NotRequired[ChannelCountMode]
    channelInterpretation: NotRequired[ChannelInterpretation]

class AudioParam:
    value: float
    automationRate: AutomationRate
    defaultValue: float
    minValue: float
    maxValue: float

    def setValueAtTime(self, value: float, startTime: float) -> AudioParam: ...

    def linearRampToValueAtTime(self, value: float, endTime: float) -> AudioParam: ...

    def exponentialRampToValueAtTime(self, value: float, endTime: float) -> AudioParam: ...

    def setTargetAtTime(self, target: float, startTime: float, timeConstant: float) -> AudioParam: ...

    def setValueCurveAtTime(self, values: Sequence[float], startTime: float, duration: float) -> AudioParam: ...

    def cancelScheduledValues(self, cancelTime: float) -> AudioParam: ...

    def cancelAndHoldAtTime(self, cancelTime: float) -> AudioParam: ...

class AudioScheduledSourceNode(AudioNode):
    onended: EventHandler

    def start(self, when: Union['float', 'None'] = 0) -> None: ...

    def stop(self, when: Union['float', 'None'] = 0) -> None: ...

class AnalyserNode(AudioNode):
    @classmethod
    def new(cls, context: BaseAudioContext, options: Union['AnalyserOptions', 'None'] = {}) -> AnalyserNode: ...

    def getFloatFrequencyData(self, array: Float32Array) -> None: ...

    def getByteFrequencyData(self, array: Uint8Array) -> None: ...

    def getFloatTimeDomainData(self, array: Float32Array) -> None: ...

    def getByteTimeDomainData(self, array: Uint8Array) -> None: ...
    fftSize: int
    frequencyBinCount: int
    minDecibels: float
    maxDecibels: float
    smoothingTimeConstant: float

class AnalyserOptions(AudioNodeOptions):
    fftSize: NotRequired[int]
    maxDecibels: NotRequired[float]
    minDecibels: NotRequired[float]
    smoothingTimeConstant: NotRequired[float]

class AudioBufferSourceNode(AudioScheduledSourceNode):
    @classmethod
    def new(cls, context: BaseAudioContext, options: Union['AudioBufferSourceOptions', 'None'] = {}) -> AudioBufferSourceNode: ...
    buffer: Union['AudioBuffer', 'None']
    playbackRate: AudioParam
    detune: AudioParam
    loop: bool
    loopStart: float
    loopEnd: float

    def start(self, when: Union['float', 'None'] = 0, offset: Union['float', 'None'] = None, duration: Union['float', 'None'] = None) -> None: ...

class AudioBufferSourceOptions(TypedDict):
    buffer: NotRequired[Union['AudioBuffer', 'None']]
    detune: NotRequired[float]
    loop: NotRequired[bool]
    loopEnd: NotRequired[float]
    loopStart: NotRequired[float]
    playbackRate: NotRequired[float]

class AudioDestinationNode(AudioNode):
    maxChannelCount: int

class AudioListener:
    positionX: AudioParam
    positionY: AudioParam
    positionZ: AudioParam
    forwardX: AudioParam
    forwardY: AudioParam
    forwardZ: AudioParam
    upX: AudioParam
    upY: AudioParam
    upZ: AudioParam

    def setPosition(self, x: float, y: float, z: float) -> None: ...

    def setOrientation(self, x: float, y: float, z: float, xUp: float, yUp: float, zUp: float) -> None: ...

class AudioProcessingEvent(Event):
    @classmethod
    def new(cls, type: str, eventInitDict: AudioProcessingEventInit) -> AudioProcessingEvent: ...
    playbackTime: float
    inputBuffer: AudioBuffer
    outputBuffer: AudioBuffer

class AudioProcessingEventInit(EventInit):
    playbackTime: float
    inputBuffer: AudioBuffer
    outputBuffer: AudioBuffer

class BiquadFilterNode(AudioNode):
    @classmethod
    def new(cls, context: BaseAudioContext, options: Union['BiquadFilterOptions', 'None'] = {}) -> BiquadFilterNode: ...
    type: BiquadFilterType
    frequency: AudioParam
    detune: AudioParam
    Q: AudioParam
    gain: AudioParam

    def getFrequencyResponse(self, frequencyHz: Float32Array, magResponse: Float32Array, phaseResponse: Float32Array) -> None: ...

class BiquadFilterOptions(AudioNodeOptions):
    type: NotRequired[BiquadFilterType]
    Q: NotRequired[float]
    detune: NotRequired[float]
    frequency: NotRequired[float]
    gain: NotRequired[float]

class ChannelMergerNode(AudioNode):
    @classmethod
    def new(cls, context: BaseAudioContext, options: Union['ChannelMergerOptions', 'None'] = {}) -> ChannelMergerNode: ...

class ChannelMergerOptions(AudioNodeOptions):
    numberOfInputs: NotRequired[int]

class ChannelSplitterNode(AudioNode):
    @classmethod
    def new(cls, context: BaseAudioContext, options: Union['ChannelSplitterOptions', 'None'] = {}) -> ChannelSplitterNode: ...

class ChannelSplitterOptions(AudioNodeOptions):
    numberOfOutputs: NotRequired[int]

class ConstantSourceNode(AudioScheduledSourceNode):
    @classmethod
    def new(cls, context: BaseAudioContext, options: Union['ConstantSourceOptions', 'None'] = {}) -> ConstantSourceNode: ...
    offset: AudioParam

class ConstantSourceOptions(TypedDict):
    offset: NotRequired[float]

class ConvolverNode(AudioNode):
    @classmethod
    def new(cls, context: BaseAudioContext, options: Union['ConvolverOptions', 'None'] = {}) -> ConvolverNode: ...
    buffer: Union['AudioBuffer', 'None']
    normalize: bool

class ConvolverOptions(AudioNodeOptions):
    buffer: NotRequired[Union['AudioBuffer', 'None']]
    disableNormalization: NotRequired[bool]

class DelayNode(AudioNode):
    @classmethod
    def new(cls, context: BaseAudioContext, options: Union['DelayOptions', 'None'] = {}) -> DelayNode: ...
    delayTime: AudioParam

class DelayOptions(AudioNodeOptions):
    maxDelayTime: NotRequired[float]
    delayTime: NotRequired[float]

class DynamicsCompressorNode(AudioNode):
    @classmethod
    def new(cls, context: BaseAudioContext, options: Union['DynamicsCompressorOptions', 'None'] = {}) -> DynamicsCompressorNode: ...
    threshold: AudioParam
    knee: AudioParam
    ratio: AudioParam
    reduction: float
    attack: AudioParam
    release: AudioParam

class DynamicsCompressorOptions(AudioNodeOptions):
    attack: NotRequired[float]
    knee: NotRequired[float]
    ratio: NotRequired[float]
    release: NotRequired[float]
    threshold: NotRequired[float]

class GainNode(AudioNode):
    @classmethod
    def new(cls, context: BaseAudioContext, options: Union['GainOptions', 'None'] = {}) -> GainNode: ...
    gain: AudioParam

class GainOptions(AudioNodeOptions):
    gain: NotRequired[float]

class IIRFilterNode(AudioNode):
    @classmethod
    def new(cls, context: BaseAudioContext, options: IIRFilterOptions) -> IIRFilterNode: ...

    def getFrequencyResponse(self, frequencyHz: Float32Array, magResponse: Float32Array, phaseResponse: Float32Array) -> None: ...

class IIRFilterOptions(AudioNodeOptions):
    feedforward: Sequence[float]
    feedback: Sequence[float]

class MediaElementAudioSourceNode(AudioNode):
    @classmethod
    def new(cls, context: AudioContext, options: MediaElementAudioSourceOptions) -> MediaElementAudioSourceNode: ...
    mediaElement: HTMLMediaElement

class MediaElementAudioSourceOptions(TypedDict):
    mediaElement: HTMLMediaElement

class MediaStreamAudioDestinationNode(AudioNode):
    @classmethod
    def new(cls, context: AudioContext, options: Union['AudioNodeOptions', 'None'] = {}) -> MediaStreamAudioDestinationNode: ...
    stream: MediaStream

class MediaStreamAudioSourceNode(AudioNode):
    @classmethod
    def new(cls, context: AudioContext, options: MediaStreamAudioSourceOptions) -> MediaStreamAudioSourceNode: ...
    mediaStream: MediaStream

class MediaStreamAudioSourceOptions(TypedDict):
    mediaStream: MediaStream

class MediaStreamTrackAudioSourceNode(AudioNode):
    @classmethod
    def new(cls, context: AudioContext, options: MediaStreamTrackAudioSourceOptions) -> MediaStreamTrackAudioSourceNode: ...

class MediaStreamTrackAudioSourceOptions(TypedDict):
    mediaStreamTrack: MediaStreamTrack

class OscillatorNode(AudioScheduledSourceNode):
    @classmethod
    def new(cls, context: BaseAudioContext, options: Union['OscillatorOptions', 'None'] = {}) -> OscillatorNode: ...
    type: OscillatorType
    frequency: AudioParam
    detune: AudioParam

    def setPeriodicWave(self, periodicWave: PeriodicWave) -> None: ...

class OscillatorOptions(AudioNodeOptions):
    type: NotRequired[OscillatorType]
    frequency: NotRequired[float]
    detune: NotRequired[float]
    periodicWave: NotRequired[PeriodicWave]

class PannerNode(AudioNode):
    @classmethod
    def new(cls, context: BaseAudioContext, options: Union['PannerOptions', 'None'] = {}) -> PannerNode: ...
    panningModel: PanningModelType
    positionX: AudioParam
    positionY: AudioParam
    positionZ: AudioParam
    orientationX: AudioParam
    orientationY: AudioParam
    orientationZ: AudioParam
    distanceModel: DistanceModelType
    refDistance: float
    maxDistance: float
    rolloffFactor: float
    coneInnerAngle: float
    coneOuterAngle: float
    coneOuterGain: float

    def setPosition(self, x: float, y: float, z: float) -> None: ...

    def setOrientation(self, x: float, y: float, z: float) -> None: ...

class PannerOptions(AudioNodeOptions):
    panningModel: NotRequired[PanningModelType]
    distanceModel: NotRequired[DistanceModelType]
    positionX: NotRequired[float]
    positionY: NotRequired[float]
    positionZ: NotRequired[float]
    orientationX: NotRequired[float]
    orientationY: NotRequired[float]
    orientationZ: NotRequired[float]
    refDistance: NotRequired[float]
    maxDistance: NotRequired[float]
    rolloffFactor: NotRequired[float]
    coneInnerAngle: NotRequired[float]
    coneOuterAngle: NotRequired[float]
    coneOuterGain: NotRequired[float]

class PeriodicWave:
    @classmethod
    def new(cls, context: BaseAudioContext, options: Union['PeriodicWaveOptions', 'None'] = {}) -> PeriodicWave: ...

class PeriodicWaveConstraints(TypedDict):
    disableNormalization: NotRequired[bool]

class PeriodicWaveOptions(PeriodicWaveConstraints):
    real: NotRequired[Sequence[float]]
    imag: NotRequired[Sequence[float]]

class ScriptProcessorNode(AudioNode):
    onaudioprocess: EventHandler
    bufferSize: int

class StereoPannerNode(AudioNode):
    @classmethod
    def new(cls, context: BaseAudioContext, options: Union['StereoPannerOptions', 'None'] = {}) -> StereoPannerNode: ...
    pan: AudioParam

class StereoPannerOptions(AudioNodeOptions):
    pan: NotRequired[float]

class WaveShaperNode(AudioNode):
    @classmethod
    def new(cls, context: BaseAudioContext, options: Union['WaveShaperOptions', 'None'] = {}) -> WaveShaperNode: ...
    curve: Float32Array
    oversample: OverSampleType

class WaveShaperOptions(AudioNodeOptions):
    curve: NotRequired[Sequence[float]]
    oversample: NotRequired[OverSampleType]

class AudioWorklet(Worklet):
    port: MessagePort

class AudioWorkletGlobalScope(WorkletGlobalScope):

    def registerProcessor(self, name: str, processorCtor: AudioWorkletProcessorConstructor) -> None: ...
    currentFrame: int
    currentTime: float
    sampleRate: float
    port: MessagePort

class AudioParamMap: ...

class AudioWorkletNode(AudioNode):
    @classmethod
    def new(cls, context: BaseAudioContext, name: str, options: Union['AudioWorkletNodeOptions', 'None'] = {}) -> AudioWorkletNode: ...
    parameters: AudioParamMap
    port: MessagePort
    onprocessorerror: EventHandler

class AudioWorkletNodeOptions(AudioNodeOptions):
    numberOfInputs: NotRequired[int]
    numberOfOutputs: NotRequired[int]
    outputChannelCount: NotRequired[Sequence[int]]
    parameterData: NotRequired[float]
    processorOptions: NotRequired[object]

class AudioWorkletProcessor:
    @classmethod
    def new(cls) -> AudioWorkletProcessor: ...
    port: MessagePort

class AudioParamDescriptor(TypedDict):
    name: str
    defaultValue: NotRequired[float]
    minValue: NotRequired[float]
    maxValue: NotRequired[float]
    automationRate: NotRequired[AutomationRate]

class PublicKeyCredential(Credential):
    rawId: ArrayBuffer
    response: AuthenticatorResponse
    authenticatorAttachment: Union['str', 'None']

    def getClientExtensionResults(self) -> AuthenticationExtensionsClientOutputs: ...

    def toJSON(self) -> PublicKeyCredentialJSON: ...

class RegistrationResponseJSON(TypedDict):
    id: Base64URLString
    rawId: Base64URLString
    response: AuthenticatorAttestationResponseJSON
    authenticatorAttachment: NotRequired[str]
    clientExtensionResults: AuthenticationExtensionsClientOutputsJSON
    type: str

class AuthenticatorAttestationResponseJSON(TypedDict):
    clientDataJSON: Base64URLString
    authenticatorData: Base64URLString
    transports: Sequence[str]
    publicKey: NotRequired[Base64URLString]
    publicKeyAlgorithm: int
    attestationObject: Base64URLString

class AuthenticationResponseJSON(TypedDict):
    id: Base64URLString
    rawId: Base64URLString
    response: AuthenticatorAssertionResponseJSON
    authenticatorAttachment: NotRequired[str]
    clientExtensionResults: AuthenticationExtensionsClientOutputsJSON
    type: str

class AuthenticatorAssertionResponseJSON(TypedDict):
    clientDataJSON: Base64URLString
    authenticatorData: Base64URLString
    signature: Base64URLString
    userHandle: NotRequired[Base64URLString]
    attestationObject: NotRequired[Base64URLString]

class AuthenticationExtensionsClientOutputsJSON(TypedDict): ...

class PublicKeyCredentialCreationOptionsJSON(TypedDict):
    rp: PublicKeyCredentialRpEntity
    user: PublicKeyCredentialUserEntityJSON
    challenge: Base64URLString
    pubKeyCredParams: Sequence[PublicKeyCredentialParameters]
    timeout: NotRequired[int]
    excludeCredentials: NotRequired[Sequence[PublicKeyCredentialDescriptorJSON]]
    authenticatorSelection: NotRequired[AuthenticatorSelectionCriteria]
    hints: NotRequired[Sequence[str]]
    attestation: NotRequired[str]
    attestationFormats: NotRequired[Sequence[str]]
    extensions: NotRequired[AuthenticationExtensionsClientInputsJSON]

class PublicKeyCredentialUserEntityJSON(TypedDict):
    id: Base64URLString
    name: str
    displayName: str

class PublicKeyCredentialDescriptorJSON(TypedDict):
    id: Base64URLString
    type: str
    transports: NotRequired[Sequence[str]]

class AuthenticationExtensionsClientInputsJSON(TypedDict): ...

class PublicKeyCredentialRequestOptionsJSON(TypedDict):
    challenge: Base64URLString
    timeout: NotRequired[int]
    rpId: NotRequired[str]
    allowCredentials: NotRequired[Sequence[PublicKeyCredentialDescriptorJSON]]
    userVerification: NotRequired[str]
    hints: NotRequired[Sequence[str]]
    attestation: NotRequired[str]
    attestationFormats: NotRequired[Sequence[str]]
    extensions: NotRequired[AuthenticationExtensionsClientInputsJSON]

class AuthenticatorResponse:
    clientDataJSON: ArrayBuffer

class AuthenticatorAttestationResponse(AuthenticatorResponse):
    attestationObject: ArrayBuffer

    def getTransports(self) -> Sequence[str]: ...

    def getAuthenticatorData(self) -> ArrayBuffer: ...

    def getPublicKey(self) -> ArrayBuffer: ...

    def getPublicKeyAlgorithm(self) -> COSEAlgorithmIdentifier: ...

class AuthenticatorAssertionResponse(AuthenticatorResponse):
    authenticatorData: ArrayBuffer
    signature: ArrayBuffer
    userHandle: ArrayBuffer
    attestationObject: ArrayBuffer

class PublicKeyCredentialParameters(TypedDict):
    type: str
    alg: COSEAlgorithmIdentifier

class PublicKeyCredentialCreationOptions(TypedDict):
    rp: PublicKeyCredentialRpEntity
    user: PublicKeyCredentialUserEntity
    challenge: BufferSource
    pubKeyCredParams: Sequence[PublicKeyCredentialParameters]
    timeout: NotRequired[int]
    excludeCredentials: NotRequired[Sequence[PublicKeyCredentialDescriptor]]
    authenticatorSelection: NotRequired[AuthenticatorSelectionCriteria]
    hints: NotRequired[Sequence[str]]
    attestation: NotRequired[str]
    attestationFormats: NotRequired[Sequence[str]]
    extensions: NotRequired[AuthenticationExtensionsClientInputs]

class PublicKeyCredentialEntity(TypedDict):
    name: str

class PublicKeyCredentialRpEntity(PublicKeyCredentialEntity):
    id: NotRequired[str]

class PublicKeyCredentialUserEntity(PublicKeyCredentialEntity):
    id: BufferSource
    displayName: str

class AuthenticatorSelectionCriteria(TypedDict):
    authenticatorAttachment: NotRequired[str]
    residentKey: NotRequired[str]
    requireResidentKey: NotRequired[bool]
    userVerification: NotRequired[str]

class PublicKeyCredentialRequestOptions(TypedDict):
    challenge: BufferSource
    timeout: NotRequired[int]
    rpId: NotRequired[str]
    allowCredentials: NotRequired[Sequence[PublicKeyCredentialDescriptor]]
    userVerification: NotRequired[str]
    hints: NotRequired[Sequence[str]]
    attestation: NotRequired[str]
    attestationFormats: NotRequired[Sequence[str]]
    extensions: NotRequired[AuthenticationExtensionsClientInputs]

class CollectedClientData(TypedDict):
    type: str
    challenge: str
    origin: str
    topOrigin: NotRequired[str]
    crossOrigin: NotRequired[bool]

class TokenBinding(TypedDict):
    status: str
    id: NotRequired[str]

class PublicKeyCredentialDescriptor(TypedDict):
    type: str
    id: BufferSource
    transports: NotRequired[Sequence[str]]

class CredentialPropertiesOutput(TypedDict):
    rk: NotRequired[bool]

class AuthenticationExtensionsPRFValues(TypedDict):
    first: BufferSource
    second: NotRequired[BufferSource]

class AuthenticationExtensionsPRFInputs(TypedDict):
    eval: NotRequired[AuthenticationExtensionsPRFValues]
    evalByCredential: NotRequired[AuthenticationExtensionsPRFValues]

class AuthenticationExtensionsPRFOutputs(TypedDict):
    enabled: NotRequired[bool]
    results: NotRequired[AuthenticationExtensionsPRFValues]

class AuthenticationExtensionsLargeBlobInputs(TypedDict):
    support: NotRequired[str]
    read: NotRequired[bool]
    write: NotRequired[BufferSource]

class AuthenticationExtensionsLargeBlobOutputs(TypedDict):
    supported: NotRequired[bool]
    blob: NotRequired[ArrayBuffer]
    written: NotRequired[bool]

class AuthenticationExtensionsDevicePublicKeyInputs(TypedDict):
    attestation: NotRequired[str]
    attestationFormats: NotRequired[Sequence[str]]

class AuthenticationExtensionsDevicePublicKeyOutputs(TypedDict):
    signature: NotRequired[ArrayBuffer]

class AudioEncoderConfig(TypedDict):
    aac: NotRequired[AacEncoderConfig]
    flac: NotRequired[FlacEncoderConfig]
    opus: NotRequired[OpusEncoderConfig]
    codec: str
    sampleRate: NotRequired[int]
    numberOfChannels: NotRequired[int]
    bitrate: NotRequired[int]
    bitrateMode: NotRequired[BitrateMode]

class AacEncoderConfig(TypedDict):
    format: NotRequired[AacBitstreamFormat]

class VideoEncoderConfig(TypedDict):
    av1: NotRequired[AV1EncoderConfig]
    avc: NotRequired[AvcEncoderConfig]
    hevc: NotRequired[HevcEncoderConfig]
    codec: str
    width: int
    height: int
    displayWidth: NotRequired[int]
    displayHeight: NotRequired[int]
    bitrate: NotRequired[int]
    framerate: NotRequired[float]
    hardwareAcceleration: NotRequired[HardwareAcceleration]
    alpha: NotRequired[AlphaOption]
    scalabilityMode: NotRequired[str]
    bitrateMode: NotRequired[VideoEncoderBitrateMode]
    latencyMode: NotRequired[LatencyMode]

class AV1EncoderConfig(TypedDict):
    forceScreenContentTools: NotRequired[bool]

class VideoEncoderEncodeOptions(TypedDict):
    av1: NotRequired[VideoEncoderEncodeOptionsForAv1]
    avc: NotRequired[VideoEncoderEncodeOptionsForAvc]
    hevc: NotRequired[VideoEncoderEncodeOptionsForHevc]
    vp9: NotRequired[VideoEncoderEncodeOptionsForVp9]
    keyFrame: NotRequired[bool]

class VideoEncoderEncodeOptionsForAv1(TypedDict):
    quantizer: NotRequired[Union['int', 'None']]

class AvcEncoderConfig(TypedDict):
    format: NotRequired[AvcBitstreamFormat]

class VideoEncoderEncodeOptionsForAvc(TypedDict):
    quantizer: NotRequired[Union['int', 'None']]

class FlacEncoderConfig(TypedDict):
    blockSize: NotRequired[int]
    compressLevel: NotRequired[int]

class HevcEncoderConfig(TypedDict):
    format: NotRequired[HevcBitstreamFormat]

class VideoEncoderEncodeOptionsForHevc(TypedDict):
    quantizer: NotRequired[Union['int', 'None']]

class OpusEncoderConfig(TypedDict):
    format: NotRequired[OpusBitstreamFormat]
    frameDuration: NotRequired[int]
    complexity: NotRequired[int]
    packetlossperc: NotRequired[int]
    useinbandfec: NotRequired[bool]
    usedtx: NotRequired[bool]

class VideoEncoderEncodeOptionsForVp9(TypedDict):
    quantizer: NotRequired[Union['int', 'None']]

class AudioDecoder(EventTarget):
    @classmethod
    def new(cls, init: AudioDecoderInit) -> AudioDecoder: ...
    state: CodecState
    decodeQueueSize: int
    ondequeue: EventHandler

    def configure(self, config: AudioDecoderConfig) -> None: ...

    def decode(self, chunk: EncodedAudioChunk) -> None: ...

    def flush(self) -> Awaitable[None]: ...

    def reset(self) -> None: ...

    def close(self) -> None: ...

class AudioDecoderInit(TypedDict):
    output: AudioDataOutputCallback
    error: WebCodecsErrorCallback

class VideoDecoder(EventTarget):
    @classmethod
    def new(cls, init: VideoDecoderInit) -> VideoDecoder: ...
    state: CodecState
    decodeQueueSize: int
    ondequeue: EventHandler

    def configure(self, config: VideoDecoderConfig) -> None: ...

    def decode(self, chunk: EncodedVideoChunk) -> None: ...

    def flush(self) -> Awaitable[None]: ...

    def reset(self) -> None: ...

    def close(self) -> None: ...

class VideoDecoderInit(TypedDict):
    output: VideoFrameOutputCallback
    error: WebCodecsErrorCallback

class AudioEncoder(EventTarget):
    @classmethod
    def new(cls, init: AudioEncoderInit) -> AudioEncoder: ...
    state: CodecState
    encodeQueueSize: int
    ondequeue: EventHandler

    def configure(self, config: AudioEncoderConfig) -> None: ...

    def encode(self, data: AudioData) -> None: ...

    def flush(self) -> Awaitable[None]: ...

    def reset(self) -> None: ...

    def close(self) -> None: ...

class AudioEncoderInit(TypedDict):
    output: EncodedAudioChunkOutputCallback
    error: WebCodecsErrorCallback

class EncodedAudioChunkMetadata(TypedDict):
    decoderConfig: NotRequired[AudioDecoderConfig]

class VideoEncoder(EventTarget):
    @classmethod
    def new(cls, init: VideoEncoderInit) -> VideoEncoder: ...
    state: CodecState
    encodeQueueSize: int
    ondequeue: EventHandler

    def configure(self, config: VideoEncoderConfig) -> None: ...

    def encode(self, frame: VideoFrame, options: Union['VideoEncoderEncodeOptions', 'None'] = {}) -> None: ...

    def flush(self) -> Awaitable[None]: ...

    def reset(self) -> None: ...

    def close(self) -> None: ...

class VideoEncoderInit(TypedDict):
    output: EncodedVideoChunkOutputCallback
    error: WebCodecsErrorCallback

class EncodedVideoChunkMetadata(TypedDict):
    decoderConfig: NotRequired[VideoDecoderConfig]
    svc: NotRequired[SvcOutputMetadata]
    alphaSideData: NotRequired[BufferSource]

class SvcOutputMetadata(TypedDict):
    temporalLayerId: NotRequired[int]

class AudioDecoderSupport(TypedDict):
    supported: NotRequired[bool]
    config: NotRequired[AudioDecoderConfig]

class VideoDecoderSupport(TypedDict):
    supported: NotRequired[bool]
    config: NotRequired[VideoDecoderConfig]

class AudioEncoderSupport(TypedDict):
    supported: NotRequired[bool]
    config: NotRequired[AudioEncoderConfig]

class VideoEncoderSupport(TypedDict):
    supported: NotRequired[bool]
    config: NotRequired[VideoEncoderConfig]

class AudioDecoderConfig(TypedDict):
    codec: str
    sampleRate: int
    numberOfChannels: int
    description: NotRequired[BufferSource]

class VideoDecoderConfig(TypedDict):
    codec: str
    description: NotRequired[AllowSharedBufferSource]
    codedWidth: NotRequired[int]
    codedHeight: NotRequired[int]
    displayAspectWidth: NotRequired[int]
    displayAspectHeight: NotRequired[int]
    colorSpace: NotRequired[VideoColorSpaceInit]
    hardwareAcceleration: NotRequired[HardwareAcceleration]
    optimizeForLatency: NotRequired[bool]

class EncodedAudioChunk:
    @classmethod
    def new(cls, init: EncodedAudioChunkInit) -> EncodedAudioChunk: ...
    type: EncodedAudioChunkType
    timestamp: int
    duration: Union['int', 'None']
    byteLength: int

    def copyTo(self, destination: AllowSharedBufferSource) -> None: ...

class EncodedAudioChunkInit(TypedDict):
    type: EncodedAudioChunkType
    timestamp: int
    duration: NotRequired[int]
    data: BufferSource

class EncodedVideoChunk:
    @classmethod
    def new(cls, init: EncodedVideoChunkInit) -> EncodedVideoChunk: ...
    type: EncodedVideoChunkType
    timestamp: int
    duration: Union['int', 'None']
    byteLength: int

    def copyTo(self, destination: AllowSharedBufferSource) -> None: ...

class EncodedVideoChunkInit(TypedDict):
    type: EncodedVideoChunkType
    timestamp: int
    duration: NotRequired[int]
    data: AllowSharedBufferSource

class AudioData:
    @classmethod
    def new(cls, init: AudioDataInit) -> AudioData: ...
    format: Union['AudioSampleFormat', 'None']
    sampleRate: float
    numberOfFrames: int
    numberOfChannels: int
    duration: int
    timestamp: int

    def allocationSize(self, options: AudioDataCopyToOptions) -> int: ...

    def copyTo(self, destination: AllowSharedBufferSource, options: AudioDataCopyToOptions) -> None: ...

    def clone(self) -> AudioData: ...

    def close(self) -> None: ...

class AudioDataInit(TypedDict):
    format: AudioSampleFormat
    sampleRate: float
    numberOfFrames: int
    numberOfChannels: int
    timestamp: int
    data: BufferSource
    transfer: NotRequired[Sequence[ArrayBuffer]]

class AudioDataCopyToOptions(TypedDict):
    planeIndex: int
    frameOffset: NotRequired[int]
    frameCount: NotRequired[int]
    format: NotRequired[AudioSampleFormat]

class VideoFrame:
    @overload
    @classmethod
    def new(cls, image: CanvasImageSource, init: Union['VideoFrameInit', 'None'] = {}) -> VideoFrame: ...
    @overload
    @classmethod
    def new(cls, data: AllowSharedBufferSource, init: VideoFrameBufferInit) -> VideoFrame: ...
    format: Union['VideoPixelFormat', 'None']
    codedWidth: int
    codedHeight: int
    codedRect: Union['DOMRectReadOnly', 'None']
    visibleRect: Union['DOMRectReadOnly', 'None']
    displayWidth: int
    displayHeight: int
    duration: Union['int', 'None']
    timestamp: int
    colorSpace: VideoColorSpace

    def metadata(self) -> VideoFrameMetadata: ...

    def allocationSize(self, options: Union['VideoFrameCopyToOptions', 'None'] = {}) -> int: ...

    def copyTo(self, destination: AllowSharedBufferSource, options: Union['VideoFrameCopyToOptions', 'None'] = {}) -> Awaitable[Sequence[PlaneLayout]]: ...

    def clone(self) -> VideoFrame: ...

    def close(self) -> None: ...

class VideoFrameInit(TypedDict):
    duration: NotRequired[int]
    timestamp: NotRequired[int]
    alpha: NotRequired[AlphaOption]
    visibleRect: NotRequired[DOMRectInit]
    displayWidth: NotRequired[int]
    displayHeight: NotRequired[int]
    metadata: NotRequired[VideoFrameMetadata]

class VideoFrameBufferInit(TypedDict):
    format: VideoPixelFormat
    codedWidth: int
    codedHeight: int
    timestamp: int
    duration: NotRequired[int]
    layout: NotRequired[Sequence[PlaneLayout]]
    visibleRect: NotRequired[DOMRectInit]
    displayWidth: NotRequired[int]
    displayHeight: NotRequired[int]
    colorSpace: NotRequired[VideoColorSpaceInit]
    transfer: NotRequired[Sequence[ArrayBuffer]]

class VideoFrameMetadata(TypedDict): ...

class VideoFrameCopyToOptions(TypedDict):
    rect: NotRequired[DOMRectInit]
    layout: NotRequired[Sequence[PlaneLayout]]

class PlaneLayout(TypedDict):
    offset: int
    stride: int

class VideoColorSpace:
    @classmethod
    def new(cls, init: Union['VideoColorSpaceInit', 'None'] = {}) -> VideoColorSpace: ...
    primaries: Union['VideoColorPrimaries', 'None']
    transfer: Union['VideoTransferCharacteristics', 'None']
    matrix: Union['VideoMatrixCoefficients', 'None']
    fullRange: Union['bool', 'None']

    def toJSON(self) -> VideoColorSpaceInit: ...

class VideoColorSpaceInit(TypedDict):
    primaries: NotRequired[Union['VideoColorPrimaries', 'None']]
    transfer: NotRequired[Union['VideoTransferCharacteristics', 'None']]
    matrix: NotRequired[Union['VideoMatrixCoefficients', 'None']]
    fullRange: NotRequired[Union['bool', 'None']]

class ImageDecoder:
    @classmethod
    def new(cls, init: ImageDecoderInit) -> ImageDecoder: ...
    type: str
    complete: bool
    completed: Awaitable[None]
    tracks: ImageTrackList

    def decode(self, options: Union['ImageDecodeOptions', 'None'] = {}) -> Awaitable[ImageDecodeResult]: ...

    def reset(self) -> None: ...

    def close(self) -> None: ...

class ImageDecoderInit(TypedDict):
    type: str
    data: ImageBufferSource
    colorSpaceConversion: NotRequired[ColorSpaceConversion]
    desiredWidth: NotRequired[int]
    desiredHeight: NotRequired[int]
    preferAnimation: NotRequired[bool]
    transfer: NotRequired[Sequence[ArrayBuffer]]

class ImageDecodeOptions(TypedDict):
    frameIndex: NotRequired[int]
    completeFramesOnly: NotRequired[bool]

class ImageDecodeResult(TypedDict):
    image: VideoFrame
    complete: bool

class ImageTrackList:

    def __getter__(self, index: int) -> ImageTrack: ...
    ready: Awaitable[None]
    length: int
    selectedIndex: int
    selectedTrack: Union['ImageTrack', 'None']

class ImageTrack:
    animated: bool
    frameCount: int
    repetitionCount: float
    selected: bool

class Ed448Params(Algorithm):
    context: NotRequired[BufferSource]

class NavigatorAutomationInformation:
    webdriver: bool

class WebGLContextAttributes(TypedDict):
    alpha: NotRequired[bool]
    depth: NotRequired[bool]
    stencil: NotRequired[bool]
    antialias: NotRequired[bool]
    premultipliedAlpha: NotRequired[bool]
    preserveDrawingBuffer: NotRequired[bool]
    powerPreference: NotRequired[WebGLPowerPreference]
    failIfMajorPerformanceCaveat: NotRequired[bool]
    desynchronized: NotRequired[bool]
    xrCompatible: NotRequired[bool]

class WebGLObject: ...

class WebGLBuffer(WebGLObject): ...

class WebGLFramebuffer(WebGLObject): ...

class WebGLProgram(WebGLObject): ...

class WebGLRenderbuffer(WebGLObject): ...

class WebGLShader(WebGLObject): ...

class WebGLTexture(WebGLObject): ...

class WebGLUniformLocation: ...

class WebGLActiveInfo:
    size: GLint
    type: GLenum
    name: str

class WebGLShaderPrecisionFormat:
    rangeMin: GLint
    rangeMax: GLint
    precision: GLint

class WebGLRenderingContextBase:
    DEPTH_BUFFER_BIT = 0x00000100
    STENCIL_BUFFER_BIT = 0x00000400
    COLOR_BUFFER_BIT = 0x00004000
    POINTS = 0x0000
    LINES = 0x0001
    LINE_LOOP = 0x0002
    LINE_STRIP = 0x0003
    TRIANGLES = 0x0004
    TRIANGLE_STRIP = 0x0005
    TRIANGLE_FAN = 0x0006
    ZERO = 0
    ONE = 1
    SRC_COLOR = 0x0300
    ONE_MINUS_SRC_COLOR = 0x0301
    SRC_ALPHA = 0x0302
    ONE_MINUS_SRC_ALPHA = 0x0303
    DST_ALPHA = 0x0304
    ONE_MINUS_DST_ALPHA = 0x0305
    DST_COLOR = 0x0306
    ONE_MINUS_DST_COLOR = 0x0307
    SRC_ALPHA_SATURATE = 0x0308
    FUNC_ADD = 0x8006
    BLEND_EQUATION = 0x8009
    BLEND_EQUATION_RGB = 0x8009
    BLEND_EQUATION_ALPHA = 0x883D
    FUNC_SUBTRACT = 0x800A
    FUNC_REVERSE_SUBTRACT = 0x800B
    BLEND_DST_RGB = 0x80C8
    BLEND_SRC_RGB = 0x80C9
    BLEND_DST_ALPHA = 0x80CA
    BLEND_SRC_ALPHA = 0x80CB
    CONSTANT_COLOR = 0x8001
    ONE_MINUS_CONSTANT_COLOR = 0x8002
    CONSTANT_ALPHA = 0x8003
    ONE_MINUS_CONSTANT_ALPHA = 0x8004
    BLEND_COLOR = 0x8005
    ARRAY_BUFFER = 0x8892
    ELEMENT_ARRAY_BUFFER = 0x8893
    ARRAY_BUFFER_BINDING = 0x8894
    ELEMENT_ARRAY_BUFFER_BINDING = 0x8895
    STREAM_DRAW = 0x88E0
    STATIC_DRAW = 0x88E4
    DYNAMIC_DRAW = 0x88E8
    BUFFER_SIZE = 0x8764
    BUFFER_USAGE = 0x8765
    CURRENT_VERTEX_ATTRIB = 0x8626
    FRONT = 0x0404
    BACK = 0x0405
    FRONT_AND_BACK = 0x0408
    CULL_FACE = 0x0B44
    BLEND = 0x0BE2
    DITHER = 0x0BD0
    STENCIL_TEST = 0x0B90
    DEPTH_TEST = 0x0B71
    SCISSOR_TEST = 0x0C11
    POLYGON_OFFSET_FILL = 0x8037
    SAMPLE_ALPHA_TO_COVERAGE = 0x809E
    SAMPLE_COVERAGE = 0x80A0
    NO_ERROR = 0
    INVALID_ENUM = 0x0500
    INVALID_VALUE = 0x0501
    INVALID_OPERATION = 0x0502
    OUT_OF_MEMORY = 0x0505
    CW = 0x0900
    CCW = 0x0901
    LINE_WIDTH = 0x0B21
    ALIASED_POINT_SIZE_RANGE = 0x846D
    ALIASED_LINE_WIDTH_RANGE = 0x846E
    CULL_FACE_MODE = 0x0B45
    FRONT_FACE = 0x0B46
    DEPTH_RANGE = 0x0B70
    DEPTH_WRITEMASK = 0x0B72
    DEPTH_CLEAR_VALUE = 0x0B73
    DEPTH_FUNC = 0x0B74
    STENCIL_CLEAR_VALUE = 0x0B91
    STENCIL_FUNC = 0x0B92
    STENCIL_FAIL = 0x0B94
    STENCIL_PASS_DEPTH_FAIL = 0x0B95
    STENCIL_PASS_DEPTH_PASS = 0x0B96
    STENCIL_REF = 0x0B97
    STENCIL_VALUE_MASK = 0x0B93
    STENCIL_WRITEMASK = 0x0B98
    STENCIL_BACK_FUNC = 0x8800
    STENCIL_BACK_FAIL = 0x8801
    STENCIL_BACK_PASS_DEPTH_FAIL = 0x8802
    STENCIL_BACK_PASS_DEPTH_PASS = 0x8803
    STENCIL_BACK_REF = 0x8CA3
    STENCIL_BACK_VALUE_MASK = 0x8CA4
    STENCIL_BACK_WRITEMASK = 0x8CA5
    VIEWPORT = 0x0BA2
    SCISSOR_BOX = 0x0C10
    COLOR_CLEAR_VALUE = 0x0C22
    COLOR_WRITEMASK = 0x0C23
    UNPACK_ALIGNMENT = 0x0CF5
    PACK_ALIGNMENT = 0x0D05
    MAX_TEXTURE_SIZE = 0x0D33
    MAX_VIEWPORT_DIMS = 0x0D3A
    SUBPIXEL_BITS = 0x0D50
    RED_BITS = 0x0D52
    GREEN_BITS = 0x0D53
    BLUE_BITS = 0x0D54
    ALPHA_BITS = 0x0D55
    DEPTH_BITS = 0x0D56
    STENCIL_BITS = 0x0D57
    POLYGON_OFFSET_UNITS = 0x2A00
    POLYGON_OFFSET_FACTOR = 0x8038
    TEXTURE_BINDING_2D = 0x8069
    SAMPLE_BUFFERS = 0x80A8
    SAMPLES = 0x80A9
    SAMPLE_COVERAGE_VALUE = 0x80AA
    SAMPLE_COVERAGE_INVERT = 0x80AB
    COMPRESSED_TEXTURE_FORMATS = 0x86A3
    DONT_CARE = 0x1100
    FASTEST = 0x1101
    NICEST = 0x1102
    GENERATE_MIPMAP_HINT = 0x8192
    BYTE = 0x1400
    UNSIGNED_BYTE = 0x1401
    SHORT = 0x1402
    UNSIGNED_SHORT = 0x1403
    INT = 0x1404
    UNSIGNED_INT = 0x1405
    FLOAT = 0x1406
    DEPTH_COMPONENT = 0x1902
    ALPHA = 0x1906
    RGB = 0x1907
    RGBA = 0x1908
    LUMINANCE = 0x1909
    LUMINANCE_ALPHA = 0x190A
    UNSIGNED_SHORT_4_4_4_4 = 0x8033
    UNSIGNED_SHORT_5_5_5_1 = 0x8034
    UNSIGNED_SHORT_5_6_5 = 0x8363
    FRAGMENT_SHADER = 0x8B30
    VERTEX_SHADER = 0x8B31
    MAX_VERTEX_ATTRIBS = 0x8869
    MAX_VERTEX_UNIFORM_VECTORS = 0x8DFB
    MAX_VARYING_VECTORS = 0x8DFC
    MAX_COMBINED_TEXTURE_IMAGE_UNITS = 0x8B4D
    MAX_VERTEX_TEXTURE_IMAGE_UNITS = 0x8B4C
    MAX_TEXTURE_IMAGE_UNITS = 0x8872
    MAX_FRAGMENT_UNIFORM_VECTORS = 0x8DFD
    SHADER_TYPE = 0x8B4F
    DELETE_STATUS = 0x8B80
    LINK_STATUS = 0x8B82
    VALIDATE_STATUS = 0x8B83
    ATTACHED_SHADERS = 0x8B85
    ACTIVE_UNIFORMS = 0x8B86
    ACTIVE_ATTRIBUTES = 0x8B89
    SHADING_LANGUAGE_VERSION = 0x8B8C
    CURRENT_PROGRAM = 0x8B8D
    NEVER = 0x0200
    LESS = 0x0201
    EQUAL = 0x0202
    LEQUAL = 0x0203
    GREATER = 0x0204
    NOTEQUAL = 0x0205
    GEQUAL = 0x0206
    ALWAYS = 0x0207
    KEEP = 0x1E00
    REPLACE = 0x1E01
    INCR = 0x1E02
    DECR = 0x1E03
    INVERT = 0x150A
    INCR_WRAP = 0x8507
    DECR_WRAP = 0x8508
    VENDOR = 0x1F00
    RENDERER = 0x1F01
    VERSION = 0x1F02
    NEAREST = 0x2600
    LINEAR = 0x2601
    NEAREST_MIPMAP_NEAREST = 0x2700
    LINEAR_MIPMAP_NEAREST = 0x2701
    NEAREST_MIPMAP_LINEAR = 0x2702
    LINEAR_MIPMAP_LINEAR = 0x2703
    TEXTURE_MAG_FILTER = 0x2800
    TEXTURE_MIN_FILTER = 0x2801
    TEXTURE_WRAP_S = 0x2802
    TEXTURE_WRAP_T = 0x2803
    TEXTURE_2D = 0x0DE1
    TEXTURE = 0x1702
    TEXTURE_CUBE_MAP = 0x8513
    TEXTURE_BINDING_CUBE_MAP = 0x8514
    TEXTURE_CUBE_MAP_POSITIVE_X = 0x8515
    TEXTURE_CUBE_MAP_NEGATIVE_X = 0x8516
    TEXTURE_CUBE_MAP_POSITIVE_Y = 0x8517
    TEXTURE_CUBE_MAP_NEGATIVE_Y = 0x8518
    TEXTURE_CUBE_MAP_POSITIVE_Z = 0x8519
    TEXTURE_CUBE_MAP_NEGATIVE_Z = 0x851A
    MAX_CUBE_MAP_TEXTURE_SIZE = 0x851C
    TEXTURE0 = 0x84C0
    TEXTURE1 = 0x84C1
    TEXTURE2 = 0x84C2
    TEXTURE3 = 0x84C3
    TEXTURE4 = 0x84C4
    TEXTURE5 = 0x84C5
    TEXTURE6 = 0x84C6
    TEXTURE7 = 0x84C7
    TEXTURE8 = 0x84C8
    TEXTURE9 = 0x84C9
    TEXTURE10 = 0x84CA
    TEXTURE11 = 0x84CB
    TEXTURE12 = 0x84CC
    TEXTURE13 = 0x84CD
    TEXTURE14 = 0x84CE
    TEXTURE15 = 0x84CF
    TEXTURE16 = 0x84D0
    TEXTURE17 = 0x84D1
    TEXTURE18 = 0x84D2
    TEXTURE19 = 0x84D3
    TEXTURE20 = 0x84D4
    TEXTURE21 = 0x84D5
    TEXTURE22 = 0x84D6
    TEXTURE23 = 0x84D7
    TEXTURE24 = 0x84D8
    TEXTURE25 = 0x84D9
    TEXTURE26 = 0x84DA
    TEXTURE27 = 0x84DB
    TEXTURE28 = 0x84DC
    TEXTURE29 = 0x84DD
    TEXTURE30 = 0x84DE
    TEXTURE31 = 0x84DF
    ACTIVE_TEXTURE = 0x84E0
    REPEAT = 0x2901
    CLAMP_TO_EDGE = 0x812F
    MIRRORED_REPEAT = 0x8370
    FLOAT_VEC2 = 0x8B50
    FLOAT_VEC3 = 0x8B51
    FLOAT_VEC4 = 0x8B52
    INT_VEC2 = 0x8B53
    INT_VEC3 = 0x8B54
    INT_VEC4 = 0x8B55
    BOOL = 0x8B56
    BOOL_VEC2 = 0x8B57
    BOOL_VEC3 = 0x8B58
    BOOL_VEC4 = 0x8B59
    FLOAT_MAT2 = 0x8B5A
    FLOAT_MAT3 = 0x8B5B
    FLOAT_MAT4 = 0x8B5C
    SAMPLER_2D = 0x8B5E
    SAMPLER_CUBE = 0x8B60
    VERTEX_ATTRIB_ARRAY_ENABLED = 0x8622
    VERTEX_ATTRIB_ARRAY_SIZE = 0x8623
    VERTEX_ATTRIB_ARRAY_STRIDE = 0x8624
    VERTEX_ATTRIB_ARRAY_TYPE = 0x8625
    VERTEX_ATTRIB_ARRAY_NORMALIZED = 0x886A
    VERTEX_ATTRIB_ARRAY_POINTER = 0x8645
    VERTEX_ATTRIB_ARRAY_BUFFER_BINDING = 0x889F
    IMPLEMENTATION_COLOR_READ_TYPE = 0x8B9A
    IMPLEMENTATION_COLOR_READ_FORMAT = 0x8B9B
    COMPILE_STATUS = 0x8B81
    LOW_FLOAT = 0x8DF0
    MEDIUM_FLOAT = 0x8DF1
    HIGH_FLOAT = 0x8DF2
    LOW_INT = 0x8DF3
    MEDIUM_INT = 0x8DF4
    HIGH_INT = 0x8DF5
    FRAMEBUFFER = 0x8D40
    RENDERBUFFER = 0x8D41
    RGBA4 = 0x8056
    RGB5_A1 = 0x8057
    RGB565 = 0x8D62
    DEPTH_COMPONENT16 = 0x81A5
    STENCIL_INDEX8 = 0x8D48
    DEPTH_STENCIL = 0x84F9
    RENDERBUFFER_WIDTH = 0x8D42
    RENDERBUFFER_HEIGHT = 0x8D43
    RENDERBUFFER_INTERNAL_FORMAT = 0x8D44
    RENDERBUFFER_RED_SIZE = 0x8D50
    RENDERBUFFER_GREEN_SIZE = 0x8D51
    RENDERBUFFER_BLUE_SIZE = 0x8D52
    RENDERBUFFER_ALPHA_SIZE = 0x8D53
    RENDERBUFFER_DEPTH_SIZE = 0x8D54
    RENDERBUFFER_STENCIL_SIZE = 0x8D55
    FRAMEBUFFER_ATTACHMENT_OBJECT_TYPE = 0x8CD0
    FRAMEBUFFER_ATTACHMENT_OBJECT_NAME = 0x8CD1
    FRAMEBUFFER_ATTACHMENT_TEXTURE_LEVEL = 0x8CD2
    FRAMEBUFFER_ATTACHMENT_TEXTURE_CUBE_MAP_FACE = 0x8CD3
    COLOR_ATTACHMENT0 = 0x8CE0
    DEPTH_ATTACHMENT = 0x8D00
    STENCIL_ATTACHMENT = 0x8D20
    DEPTH_STENCIL_ATTACHMENT = 0x821A
    NONE = 0
    FRAMEBUFFER_COMPLETE = 0x8CD5
    FRAMEBUFFER_INCOMPLETE_ATTACHMENT = 0x8CD6
    FRAMEBUFFER_INCOMPLETE_MISSING_ATTACHMENT = 0x8CD7
    FRAMEBUFFER_INCOMPLETE_DIMENSIONS = 0x8CD9
    FRAMEBUFFER_UNSUPPORTED = 0x8CDD
    FRAMEBUFFER_BINDING = 0x8CA6
    RENDERBUFFER_BINDING = 0x8CA7
    MAX_RENDERBUFFER_SIZE = 0x84E8
    INVALID_FRAMEBUFFER_OPERATION = 0x0506
    UNPACK_FLIP_Y_WEBGL = 0x9240
    UNPACK_PREMULTIPLY_ALPHA_WEBGL = 0x9241
    CONTEXT_LOST_WEBGL = 0x9242
    UNPACK_COLORSPACE_CONVERSION_WEBGL = 0x9243
    BROWSER_DEFAULT_WEBGL = 0x9244
    canvas: Union['HTMLCanvasElement', 'OffscreenCanvas']
    drawingBufferWidth: GLsizei
    drawingBufferHeight: GLsizei
    drawingBufferColorSpace: PredefinedColorSpace
    unpackColorSpace: PredefinedColorSpace

    def getContextAttributes(self) -> Union['WebGLContextAttributes', 'None']: ...

    def isContextLost(self) -> bool: ...

    def getSupportedExtensions(self) -> Sequence[str]: ...

    def getExtension(self, name: str) -> Union['object', 'None']: ...

    def activeTexture(self, texture: GLenum) -> None: ...

    def attachShader(self, program: WebGLProgram, shader: WebGLShader) -> None: ...

    def bindAttribLocation(self, program: WebGLProgram, index: GLuint, name: str) -> None: ...

    def bindBuffer(self, target: GLenum, buffer: Union['WebGLBuffer', 'None']) -> None: ...

    def bindFramebuffer(self, target: GLenum, framebuffer: Union['WebGLFramebuffer', 'None']) -> None: ...

    def bindRenderbuffer(self, target: GLenum, renderbuffer: Union['WebGLRenderbuffer', 'None']) -> None: ...

    def bindTexture(self, target: GLenum, texture: Union['WebGLTexture', 'None']) -> None: ...

    def blendColor(self, red: GLclampf, green: GLclampf, blue: GLclampf, alpha: GLclampf) -> None: ...

    def blendEquation(self, mode: GLenum) -> None: ...

    def blendEquationSeparate(self, modeRGB: GLenum, modeAlpha: GLenum) -> None: ...

    def blendFunc(self, sfactor: GLenum, dfactor: GLenum) -> None: ...

    def blendFuncSeparate(self, srcRGB: GLenum, dstRGB: GLenum, srcAlpha: GLenum, dstAlpha: GLenum) -> None: ...

    def checkFramebufferStatus(self, target: GLenum) -> GLenum: ...

    def clear(self, mask: GLbitfield) -> None: ...

    def clearColor(self, red: GLclampf, green: GLclampf, blue: GLclampf, alpha: GLclampf) -> None: ...

    def clearDepth(self, depth: GLclampf) -> None: ...

    def clearStencil(self, s: GLint) -> None: ...

    def colorMask(self, red: GLboolean, green: GLboolean, blue: GLboolean, alpha: GLboolean) -> None: ...

    def compileShader(self, shader: WebGLShader) -> None: ...

    def copyTexImage2D(self, target: GLenum, level: GLint, internalformat: GLenum, x: GLint, y: GLint, width: GLsizei, height: GLsizei, border: GLint) -> None: ...

    def copyTexSubImage2D(self, target: GLenum, level: GLint, xoffset: GLint, yoffset: GLint, x: GLint, y: GLint, width: GLsizei, height: GLsizei) -> None: ...

    def createBuffer(self) -> Union['WebGLBuffer', 'None']: ...

    def createFramebuffer(self) -> Union['WebGLFramebuffer', 'None']: ...

    def createProgram(self) -> Union['WebGLProgram', 'None']: ...

    def createRenderbuffer(self) -> Union['WebGLRenderbuffer', 'None']: ...

    def createShader(self, type: GLenum) -> Union['WebGLShader', 'None']: ...

    def createTexture(self) -> Union['WebGLTexture', 'None']: ...

    def cullFace(self, mode: GLenum) -> None: ...

    def deleteBuffer(self, buffer: Union['WebGLBuffer', 'None']) -> None: ...

    def deleteFramebuffer(self, framebuffer: Union['WebGLFramebuffer', 'None']) -> None: ...

    def deleteProgram(self, program: Union['WebGLProgram', 'None']) -> None: ...

    def deleteRenderbuffer(self, renderbuffer: Union['WebGLRenderbuffer', 'None']) -> None: ...

    def deleteShader(self, shader: Union['WebGLShader', 'None']) -> None: ...

    def deleteTexture(self, texture: Union['WebGLTexture', 'None']) -> None: ...

    def depthFunc(self, func: GLenum) -> None: ...

    def depthMask(self, flag: GLboolean) -> None: ...

    def depthRange(self, zNear: GLclampf, zFar: GLclampf) -> None: ...

    def detachShader(self, program: WebGLProgram, shader: WebGLShader) -> None: ...

    def disable(self, cap: GLenum) -> None: ...

    def disableVertexAttribArray(self, index: GLuint) -> None: ...

    def drawArrays(self, mode: GLenum, first: GLint, count: GLsizei) -> None: ...

    def drawElements(self, mode: GLenum, count: GLsizei, type: GLenum, offset: GLintptr) -> None: ...

    def enable(self, cap: GLenum) -> None: ...

    def enableVertexAttribArray(self, index: GLuint) -> None: ...

    def finish(self) -> None: ...

    def flush(self) -> None: ...

    def framebufferRenderbuffer(self, target: GLenum, attachment: GLenum, renderbuffertarget: GLenum, renderbuffer: Union['WebGLRenderbuffer', 'None']) -> None: ...

    def framebufferTexture2D(self, target: GLenum, attachment: GLenum, textarget: GLenum, texture: Union['WebGLTexture', 'None'], level: GLint) -> None: ...

    def frontFace(self, mode: GLenum) -> None: ...

    def generateMipmap(self, target: GLenum) -> None: ...

    def getActiveAttrib(self, program: WebGLProgram, index: GLuint) -> Union['WebGLActiveInfo', 'None']: ...

    def getActiveUniform(self, program: WebGLProgram, index: GLuint) -> Union['WebGLActiveInfo', 'None']: ...

    def getAttachedShaders(self, program: WebGLProgram) -> Sequence[WebGLShader]: ...

    def getAttribLocation(self, program: WebGLProgram, name: str) -> GLint: ...

    def getBufferParameter(self, target: GLenum, pname: GLenum) -> Any: ...

    def getParameter(self, pname: GLenum) -> Any: ...

    def getError(self) -> GLenum: ...

    def getFramebufferAttachmentParameter(self, target: GLenum, attachment: GLenum, pname: GLenum) -> Any: ...

    def getProgramParameter(self, program: WebGLProgram, pname: GLenum) -> Any: ...

    def getProgramInfoLog(self, program: WebGLProgram) -> Union['str', 'None']: ...

    def getRenderbufferParameter(self, target: GLenum, pname: GLenum) -> Any: ...

    def getShaderParameter(self, shader: WebGLShader, pname: GLenum) -> Any: ...

    def getShaderPrecisionFormat(self, shadertype: GLenum, precisiontype: GLenum) -> Union['WebGLShaderPrecisionFormat', 'None']: ...

    def getShaderInfoLog(self, shader: WebGLShader) -> Union['str', 'None']: ...

    def getShaderSource(self, shader: WebGLShader) -> Union['str', 'None']: ...

    def getTexParameter(self, target: GLenum, pname: GLenum) -> Any: ...

    def getUniform(self, program: WebGLProgram, location: WebGLUniformLocation) -> Any: ...

    def getUniformLocation(self, program: WebGLProgram, name: str) -> Union['WebGLUniformLocation', 'None']: ...

    def getVertexAttrib(self, index: GLuint, pname: GLenum) -> Any: ...

    def getVertexAttribOffset(self, index: GLuint, pname: GLenum) -> GLintptr: ...

    def hint(self, target: GLenum, mode: GLenum) -> None: ...

    def isBuffer(self, buffer: Union['WebGLBuffer', 'None']) -> GLboolean: ...

    def isEnabled(self, cap: GLenum) -> GLboolean: ...

    def isFramebuffer(self, framebuffer: Union['WebGLFramebuffer', 'None']) -> GLboolean: ...

    def isProgram(self, program: Union['WebGLProgram', 'None']) -> GLboolean: ...

    def isRenderbuffer(self, renderbuffer: Union['WebGLRenderbuffer', 'None']) -> GLboolean: ...

    def isShader(self, shader: Union['WebGLShader', 'None']) -> GLboolean: ...

    def isTexture(self, texture: Union['WebGLTexture', 'None']) -> GLboolean: ...

    def lineWidth(self, width: GLfloat) -> None: ...

    def linkProgram(self, program: WebGLProgram) -> None: ...

    def pixelStorei(self, pname: GLenum, param: GLint) -> None: ...

    def polygonOffset(self, factor: GLfloat, units: GLfloat) -> None: ...

    def renderbufferStorage(self, target: GLenum, internalformat: GLenum, width: GLsizei, height: GLsizei) -> None: ...

    def sampleCoverage(self, value: GLclampf, invert: GLboolean) -> None: ...

    def scissor(self, x: GLint, y: GLint, width: GLsizei, height: GLsizei) -> None: ...

    def shaderSource(self, shader: WebGLShader, source: str) -> None: ...

    def stencilFunc(self, func: GLenum, ref: GLint, mask: GLuint) -> None: ...

    def stencilFuncSeparate(self, face: GLenum, func: GLenum, ref: GLint, mask: GLuint) -> None: ...

    def stencilMask(self, mask: GLuint) -> None: ...

    def stencilMaskSeparate(self, face: GLenum, mask: GLuint) -> None: ...

    def stencilOp(self, fail: GLenum, zfail: GLenum, zpass: GLenum) -> None: ...

    def stencilOpSeparate(self, face: GLenum, fail: GLenum, zfail: GLenum, zpass: GLenum) -> None: ...

    def texParameterf(self, target: GLenum, pname: GLenum, param: GLfloat) -> None: ...

    def texParameteri(self, target: GLenum, pname: GLenum, param: GLint) -> None: ...

    def uniform1f(self, location: Union['WebGLUniformLocation', 'None'], x: GLfloat) -> None: ...

    def uniform2f(self, location: Union['WebGLUniformLocation', 'None'], x: GLfloat, y: GLfloat) -> None: ...

    def uniform3f(self, location: Union['WebGLUniformLocation', 'None'], x: GLfloat, y: GLfloat, z: GLfloat) -> None: ...

    def uniform4f(self, location: Union['WebGLUniformLocation', 'None'], x: GLfloat, y: GLfloat, z: GLfloat, w: GLfloat) -> None: ...

    def uniform1i(self, location: Union['WebGLUniformLocation', 'None'], x: GLint) -> None: ...

    def uniform2i(self, location: Union['WebGLUniformLocation', 'None'], x: GLint, y: GLint) -> None: ...

    def uniform3i(self, location: Union['WebGLUniformLocation', 'None'], x: GLint, y: GLint, z: GLint) -> None: ...

    def uniform4i(self, location: Union['WebGLUniformLocation', 'None'], x: GLint, y: GLint, z: GLint, w: GLint) -> None: ...

    def useProgram(self, program: Union['WebGLProgram', 'None']) -> None: ...

    def validateProgram(self, program: WebGLProgram) -> None: ...

    def vertexAttrib1f(self, index: GLuint, x: GLfloat) -> None: ...

    def vertexAttrib2f(self, index: GLuint, x: GLfloat, y: GLfloat) -> None: ...

    def vertexAttrib3f(self, index: GLuint, x: GLfloat, y: GLfloat, z: GLfloat) -> None: ...

    def vertexAttrib4f(self, index: GLuint, x: GLfloat, y: GLfloat, z: GLfloat, w: GLfloat) -> None: ...

    def vertexAttrib1fv(self, index: GLuint, values: Float32List) -> None: ...

    def vertexAttrib2fv(self, index: GLuint, values: Float32List) -> None: ...

    def vertexAttrib3fv(self, index: GLuint, values: Float32List) -> None: ...

    def vertexAttrib4fv(self, index: GLuint, values: Float32List) -> None: ...

    def vertexAttribPointer(self, index: GLuint, size: GLint, type: GLenum, normalized: GLboolean, stride: GLsizei, offset: GLintptr) -> None: ...

    def viewport(self, x: GLint, y: GLint, width: GLsizei, height: GLsizei) -> None: ...

    def makeXRCompatible(self) -> Awaitable[None]: ...

class WebGLRenderingContextOverloads:
    @overload
    def bufferData(self, target: GLenum, size: GLsizeiptr, usage: GLenum) -> None: ...
    @overload
    def bufferData(self, target: GLenum, data: Union['AllowSharedBufferSource', 'None'], usage: GLenum) -> None: ...

    def bufferSubData(self, target: GLenum, offset: GLintptr, data: AllowSharedBufferSource) -> None: ...

    def compressedTexImage2D(self, target: GLenum, level: GLint, internalformat: GLenum, width: GLsizei, height: GLsizei, border: GLint, data: ArrayBufferView) -> None: ...

    def compressedTexSubImage2D(self, target: GLenum, level: GLint, xoffset: GLint, yoffset: GLint, width: GLsizei, height: GLsizei, format: GLenum, data: ArrayBufferView) -> None: ...

    def readPixels(self, x: GLint, y: GLint, width: GLsizei, height: GLsizei, format: GLenum, type: GLenum, pixels: Union['ArrayBufferView', 'None']) -> None: ...
    @overload
    def texImage2D(self, target: GLenum, level: GLint, internalformat: GLint, width: GLsizei, height: GLsizei, border: GLint, format: GLenum, type: GLenum, pixels: Union['ArrayBufferView', 'None']) -> None: ...
    @overload
    def texImage2D(self, target: GLenum, level: GLint, internalformat: GLint, format: GLenum, type: GLenum, source: TexImageSource) -> None: ...
    @overload
    def texSubImage2D(self, target: GLenum, level: GLint, xoffset: GLint, yoffset: GLint, width: GLsizei, height: GLsizei, format: GLenum, type: GLenum, pixels: Union['ArrayBufferView', 'None']) -> None: ...
    @overload
    def texSubImage2D(self, target: GLenum, level: GLint, xoffset: GLint, yoffset: GLint, format: GLenum, type: GLenum, source: TexImageSource) -> None: ...

    def uniform1fv(self, location: Union['WebGLUniformLocation', 'None'], v: Float32List) -> None: ...

    def uniform2fv(self, location: Union['WebGLUniformLocation', 'None'], v: Float32List) -> None: ...

    def uniform3fv(self, location: Union['WebGLUniformLocation', 'None'], v: Float32List) -> None: ...

    def uniform4fv(self, location: Union['WebGLUniformLocation', 'None'], v: Float32List) -> None: ...

    def uniform1iv(self, location: Union['WebGLUniformLocation', 'None'], v: Int32List) -> None: ...

    def uniform2iv(self, location: Union['WebGLUniformLocation', 'None'], v: Int32List) -> None: ...

    def uniform3iv(self, location: Union['WebGLUniformLocation', 'None'], v: Int32List) -> None: ...

    def uniform4iv(self, location: Union['WebGLUniformLocation', 'None'], v: Int32List) -> None: ...

    def uniformMatrix2fv(self, location: Union['WebGLUniformLocation', 'None'], transpose: GLboolean, value: Float32List) -> None: ...

    def uniformMatrix3fv(self, location: Union['WebGLUniformLocation', 'None'], transpose: GLboolean, value: Float32List) -> None: ...

    def uniformMatrix4fv(self, location: Union['WebGLUniformLocation', 'None'], transpose: GLboolean, value: Float32List) -> None: ...

class WebGLRenderingContext(WebGLRenderingContextBase, WebGLRenderingContextOverloads): ...

class WebGLContextEvent(Event):
    @classmethod
    def new(cls, type: str, eventInit: Union['WebGLContextEventInit', 'None'] = {}) -> WebGLContextEvent: ...
    statusMessage: str

class WebGLContextEventInit(EventInit):
    statusMessage: NotRequired[str]

class WebGLQuery(WebGLObject): ...

class WebGLSampler(WebGLObject): ...

class WebGLSync(WebGLObject): ...

class WebGLTransformFeedback(WebGLObject): ...

class WebGLVertexArrayObject(WebGLObject): ...

class WebGL2RenderingContextBase:
    READ_BUFFER = 0x0C02
    UNPACK_ROW_LENGTH = 0x0CF2
    UNPACK_SKIP_ROWS = 0x0CF3
    UNPACK_SKIP_PIXELS = 0x0CF4
    PACK_ROW_LENGTH = 0x0D02
    PACK_SKIP_ROWS = 0x0D03
    PACK_SKIP_PIXELS = 0x0D04
    COLOR = 0x1800
    DEPTH = 0x1801
    STENCIL = 0x1802
    RED = 0x1903
    RGB8 = 0x8051
    RGBA8 = 0x8058
    RGB10_A2 = 0x8059
    TEXTURE_BINDING_3D = 0x806A
    UNPACK_SKIP_IMAGES = 0x806D
    UNPACK_IMAGE_HEIGHT = 0x806E
    TEXTURE_3D = 0x806F
    TEXTURE_WRAP_R = 0x8072
    MAX_3D_TEXTURE_SIZE = 0x8073
    UNSIGNED_INT_2_10_10_10_REV = 0x8368
    MAX_ELEMENTS_VERTICES = 0x80E8
    MAX_ELEMENTS_INDICES = 0x80E9
    TEXTURE_MIN_LOD = 0x813A
    TEXTURE_MAX_LOD = 0x813B
    TEXTURE_BASE_LEVEL = 0x813C
    TEXTURE_MAX_LEVEL = 0x813D
    MIN = 0x8007
    MAX = 0x8008
    DEPTH_COMPONENT24 = 0x81A6
    MAX_TEXTURE_LOD_BIAS = 0x84FD
    TEXTURE_COMPARE_MODE = 0x884C
    TEXTURE_COMPARE_FUNC = 0x884D
    CURRENT_QUERY = 0x8865
    QUERY_RESULT = 0x8866
    QUERY_RESULT_AVAILABLE = 0x8867
    STREAM_READ = 0x88E1
    STREAM_COPY = 0x88E2
    STATIC_READ = 0x88E5
    STATIC_COPY = 0x88E6
    DYNAMIC_READ = 0x88E9
    DYNAMIC_COPY = 0x88EA
    MAX_DRAW_BUFFERS = 0x8824
    DRAW_BUFFER0 = 0x8825
    DRAW_BUFFER1 = 0x8826
    DRAW_BUFFER2 = 0x8827
    DRAW_BUFFER3 = 0x8828
    DRAW_BUFFER4 = 0x8829
    DRAW_BUFFER5 = 0x882A
    DRAW_BUFFER6 = 0x882B
    DRAW_BUFFER7 = 0x882C
    DRAW_BUFFER8 = 0x882D
    DRAW_BUFFER9 = 0x882E
    DRAW_BUFFER10 = 0x882F
    DRAW_BUFFER11 = 0x8830
    DRAW_BUFFER12 = 0x8831
    DRAW_BUFFER13 = 0x8832
    DRAW_BUFFER14 = 0x8833
    DRAW_BUFFER15 = 0x8834
    MAX_FRAGMENT_UNIFORM_COMPONENTS = 0x8B49
    MAX_VERTEX_UNIFORM_COMPONENTS = 0x8B4A
    SAMPLER_3D = 0x8B5F
    SAMPLER_2D_SHADOW = 0x8B62
    FRAGMENT_SHADER_DERIVATIVE_HINT = 0x8B8B
    PIXEL_PACK_BUFFER = 0x88EB
    PIXEL_UNPACK_BUFFER = 0x88EC
    PIXEL_PACK_BUFFER_BINDING = 0x88ED
    PIXEL_UNPACK_BUFFER_BINDING = 0x88EF
    FLOAT_MAT2x3 = 0x8B65
    FLOAT_MAT2x4 = 0x8B66
    FLOAT_MAT3x2 = 0x8B67
    FLOAT_MAT3x4 = 0x8B68
    FLOAT_MAT4x2 = 0x8B69
    FLOAT_MAT4x3 = 0x8B6A
    SRGB = 0x8C40
    SRGB8 = 0x8C41
    SRGB8_ALPHA8 = 0x8C43
    COMPARE_REF_TO_TEXTURE = 0x884E
    RGBA32F = 0x8814
    RGB32F = 0x8815
    RGBA16F = 0x881A
    RGB16F = 0x881B
    VERTEX_ATTRIB_ARRAY_INTEGER = 0x88FD
    MAX_ARRAY_TEXTURE_LAYERS = 0x88FF
    MIN_PROGRAM_TEXEL_OFFSET = 0x8904
    MAX_PROGRAM_TEXEL_OFFSET = 0x8905
    MAX_VARYING_COMPONENTS = 0x8B4B
    TEXTURE_2D_ARRAY = 0x8C1A
    TEXTURE_BINDING_2D_ARRAY = 0x8C1D
    R11F_G11F_B10F = 0x8C3A
    UNSIGNED_INT_10F_11F_11F_REV = 0x8C3B
    RGB9_E5 = 0x8C3D
    UNSIGNED_INT_5_9_9_9_REV = 0x8C3E
    TRANSFORM_FEEDBACK_BUFFER_MODE = 0x8C7F
    MAX_TRANSFORM_FEEDBACK_SEPARATE_COMPONENTS = 0x8C80
    TRANSFORM_FEEDBACK_VARYINGS = 0x8C83
    TRANSFORM_FEEDBACK_BUFFER_START = 0x8C84
    TRANSFORM_FEEDBACK_BUFFER_SIZE = 0x8C85
    TRANSFORM_FEEDBACK_PRIMITIVES_WRITTEN = 0x8C88
    RASTERIZER_DISCARD = 0x8C89
    MAX_TRANSFORM_FEEDBACK_INTERLEAVED_COMPONENTS = 0x8C8A
    MAX_TRANSFORM_FEEDBACK_SEPARATE_ATTRIBS = 0x8C8B
    INTERLEAVED_ATTRIBS = 0x8C8C
    SEPARATE_ATTRIBS = 0x8C8D
    TRANSFORM_FEEDBACK_BUFFER = 0x8C8E
    TRANSFORM_FEEDBACK_BUFFER_BINDING = 0x8C8F
    RGBA32UI = 0x8D70
    RGB32UI = 0x8D71
    RGBA16UI = 0x8D76
    RGB16UI = 0x8D77
    RGBA8UI = 0x8D7C
    RGB8UI = 0x8D7D
    RGBA32I = 0x8D82
    RGB32I = 0x8D83
    RGBA16I = 0x8D88
    RGB16I = 0x8D89
    RGBA8I = 0x8D8E
    RGB8I = 0x8D8F
    RED_INTEGER = 0x8D94
    RGB_INTEGER = 0x8D98
    RGBA_INTEGER = 0x8D99
    SAMPLER_2D_ARRAY = 0x8DC1
    SAMPLER_2D_ARRAY_SHADOW = 0x8DC4
    SAMPLER_CUBE_SHADOW = 0x8DC5
    UNSIGNED_INT_VEC2 = 0x8DC6
    UNSIGNED_INT_VEC3 = 0x8DC7
    UNSIGNED_INT_VEC4 = 0x8DC8
    INT_SAMPLER_2D = 0x8DCA
    INT_SAMPLER_3D = 0x8DCB
    INT_SAMPLER_CUBE = 0x8DCC
    INT_SAMPLER_2D_ARRAY = 0x8DCF
    UNSIGNED_INT_SAMPLER_2D = 0x8DD2
    UNSIGNED_INT_SAMPLER_3D = 0x8DD3
    UNSIGNED_INT_SAMPLER_CUBE = 0x8DD4
    UNSIGNED_INT_SAMPLER_2D_ARRAY = 0x8DD7
    DEPTH_COMPONENT32F = 0x8CAC
    DEPTH32F_STENCIL8 = 0x8CAD
    FLOAT_32_UNSIGNED_INT_24_8_REV = 0x8DAD
    FRAMEBUFFER_ATTACHMENT_COLOR_ENCODING = 0x8210
    FRAMEBUFFER_ATTACHMENT_COMPONENT_TYPE = 0x8211
    FRAMEBUFFER_ATTACHMENT_RED_SIZE = 0x8212
    FRAMEBUFFER_ATTACHMENT_GREEN_SIZE = 0x8213
    FRAMEBUFFER_ATTACHMENT_BLUE_SIZE = 0x8214
    FRAMEBUFFER_ATTACHMENT_ALPHA_SIZE = 0x8215
    FRAMEBUFFER_ATTACHMENT_DEPTH_SIZE = 0x8216
    FRAMEBUFFER_ATTACHMENT_STENCIL_SIZE = 0x8217
    FRAMEBUFFER_DEFAULT = 0x8218
    UNSIGNED_INT_24_8 = 0x84FA
    DEPTH24_STENCIL8 = 0x88F0
    UNSIGNED_NORMALIZED = 0x8C17
    DRAW_FRAMEBUFFER_BINDING = 0x8CA6
    READ_FRAMEBUFFER = 0x8CA8
    DRAW_FRAMEBUFFER = 0x8CA9
    READ_FRAMEBUFFER_BINDING = 0x8CAA
    RENDERBUFFER_SAMPLES = 0x8CAB
    FRAMEBUFFER_ATTACHMENT_TEXTURE_LAYER = 0x8CD4
    MAX_COLOR_ATTACHMENTS = 0x8CDF
    COLOR_ATTACHMENT1 = 0x8CE1
    COLOR_ATTACHMENT2 = 0x8CE2
    COLOR_ATTACHMENT3 = 0x8CE3
    COLOR_ATTACHMENT4 = 0x8CE4
    COLOR_ATTACHMENT5 = 0x8CE5
    COLOR_ATTACHMENT6 = 0x8CE6
    COLOR_ATTACHMENT7 = 0x8CE7
    COLOR_ATTACHMENT8 = 0x8CE8
    COLOR_ATTACHMENT9 = 0x8CE9
    COLOR_ATTACHMENT10 = 0x8CEA
    COLOR_ATTACHMENT11 = 0x8CEB
    COLOR_ATTACHMENT12 = 0x8CEC
    COLOR_ATTACHMENT13 = 0x8CED
    COLOR_ATTACHMENT14 = 0x8CEE
    COLOR_ATTACHMENT15 = 0x8CEF
    FRAMEBUFFER_INCOMPLETE_MULTISAMPLE = 0x8D56
    MAX_SAMPLES = 0x8D57
    HALF_FLOAT = 0x140B
    RG = 0x8227
    RG_INTEGER = 0x8228
    R8 = 0x8229
    RG8 = 0x822B
    R16F = 0x822D
    R32F = 0x822E
    RG16F = 0x822F
    RG32F = 0x8230
    R8I = 0x8231
    R8UI = 0x8232
    R16I = 0x8233
    R16UI = 0x8234
    R32I = 0x8235
    R32UI = 0x8236
    RG8I = 0x8237
    RG8UI = 0x8238
    RG16I = 0x8239
    RG16UI = 0x823A
    RG32I = 0x823B
    RG32UI = 0x823C
    VERTEX_ARRAY_BINDING = 0x85B5
    R8_SNORM = 0x8F94
    RG8_SNORM = 0x8F95
    RGB8_SNORM = 0x8F96
    RGBA8_SNORM = 0x8F97
    SIGNED_NORMALIZED = 0x8F9C
    COPY_READ_BUFFER = 0x8F36
    COPY_WRITE_BUFFER = 0x8F37
    COPY_READ_BUFFER_BINDING = 0x8F36
    COPY_WRITE_BUFFER_BINDING = 0x8F37
    UNIFORM_BUFFER = 0x8A11
    UNIFORM_BUFFER_BINDING = 0x8A28
    UNIFORM_BUFFER_START = 0x8A29
    UNIFORM_BUFFER_SIZE = 0x8A2A
    MAX_VERTEX_UNIFORM_BLOCKS = 0x8A2B
    MAX_FRAGMENT_UNIFORM_BLOCKS = 0x8A2D
    MAX_COMBINED_UNIFORM_BLOCKS = 0x8A2E
    MAX_UNIFORM_BUFFER_BINDINGS = 0x8A2F
    MAX_UNIFORM_BLOCK_SIZE = 0x8A30
    MAX_COMBINED_VERTEX_UNIFORM_COMPONENTS = 0x8A31
    MAX_COMBINED_FRAGMENT_UNIFORM_COMPONENTS = 0x8A33
    UNIFORM_BUFFER_OFFSET_ALIGNMENT = 0x8A34
    ACTIVE_UNIFORM_BLOCKS = 0x8A36
    UNIFORM_TYPE = 0x8A37
    UNIFORM_SIZE = 0x8A38
    UNIFORM_BLOCK_INDEX = 0x8A3A
    UNIFORM_OFFSET = 0x8A3B
    UNIFORM_ARRAY_STRIDE = 0x8A3C
    UNIFORM_MATRIX_STRIDE = 0x8A3D
    UNIFORM_IS_ROW_MAJOR = 0x8A3E
    UNIFORM_BLOCK_BINDING = 0x8A3F
    UNIFORM_BLOCK_DATA_SIZE = 0x8A40
    UNIFORM_BLOCK_ACTIVE_UNIFORMS = 0x8A42
    UNIFORM_BLOCK_ACTIVE_UNIFORM_INDICES = 0x8A43
    UNIFORM_BLOCK_REFERENCED_BY_VERTEX_SHADER = 0x8A44
    UNIFORM_BLOCK_REFERENCED_BY_FRAGMENT_SHADER = 0x8A46
    INVALID_INDEX = 0xFFFFFFFF
    MAX_VERTEX_OUTPUT_COMPONENTS = 0x9122
    MAX_FRAGMENT_INPUT_COMPONENTS = 0x9125
    MAX_SERVER_WAIT_TIMEOUT = 0x9111
    OBJECT_TYPE = 0x9112
    SYNC_CONDITION = 0x9113
    SYNC_STATUS = 0x9114
    SYNC_FLAGS = 0x9115
    SYNC_FENCE = 0x9116
    SYNC_GPU_COMMANDS_COMPLETE = 0x9117
    UNSIGNALED = 0x9118
    SIGNALED = 0x9119
    ALREADY_SIGNALED = 0x911A
    TIMEOUT_EXPIRED = 0x911B
    CONDITION_SATISFIED = 0x911C
    WAIT_FAILED = 0x911D
    SYNC_FLUSH_COMMANDS_BIT = 0x00000001
    VERTEX_ATTRIB_ARRAY_DIVISOR = 0x88FE
    ANY_SAMPLES_PASSED = 0x8C2F
    ANY_SAMPLES_PASSED_CONSERVATIVE = 0x8D6A
    SAMPLER_BINDING = 0x8919
    RGB10_A2UI = 0x906F
    INT_2_10_10_10_REV = 0x8D9F
    TRANSFORM_FEEDBACK = 0x8E22
    TRANSFORM_FEEDBACK_PAUSED = 0x8E23
    TRANSFORM_FEEDBACK_ACTIVE = 0x8E24
    TRANSFORM_FEEDBACK_BINDING = 0x8E25
    TEXTURE_IMMUTABLE_FORMAT = 0x912F
    MAX_ELEMENT_INDEX = 0x8D6B
    TEXTURE_IMMUTABLE_LEVELS = 0x82DF
    TIMEOUT_IGNORED = -1
    MAX_CLIENT_WAIT_TIMEOUT_WEBGL = 0x9247

    def copyBufferSubData(self, readTarget: GLenum, writeTarget: GLenum, readOffset: GLintptr, writeOffset: GLintptr, size: GLsizeiptr) -> None: ...

    def getBufferSubData(self, target: GLenum, srcByteOffset: GLintptr, dstBuffer: ArrayBufferView, dstOffset: Union['GLuint', 'None'] = 0, length: Union['GLuint', 'None'] = 0) -> None: ...

    def blitFramebuffer(self, srcX0: GLint, srcY0: GLint, srcX1: GLint, srcY1: GLint, dstX0: GLint, dstY0: GLint, dstX1: GLint, dstY1: GLint, mask: GLbitfield, filter: GLenum) -> None: ...

    def framebufferTextureLayer(self, target: GLenum, attachment: GLenum, texture: Union['WebGLTexture', 'None'], level: GLint, layer: GLint) -> None: ...

    def invalidateFramebuffer(self, target: GLenum, attachments: Sequence[GLenum]) -> None: ...

    def invalidateSubFramebuffer(self, target: GLenum, attachments: Sequence[GLenum], x: GLint, y: GLint, width: GLsizei, height: GLsizei) -> None: ...

    def readBuffer(self, src: GLenum) -> None: ...

    def getInternalformatParameter(self, target: GLenum, internalformat: GLenum, pname: GLenum) -> Any: ...

    def renderbufferStorageMultisample(self, target: GLenum, samples: GLsizei, internalformat: GLenum, width: GLsizei, height: GLsizei) -> None: ...

    def texStorage2D(self, target: GLenum, levels: GLsizei, internalformat: GLenum, width: GLsizei, height: GLsizei) -> None: ...

    def texStorage3D(self, target: GLenum, levels: GLsizei, internalformat: GLenum, width: GLsizei, height: GLsizei, depth: GLsizei) -> None: ...
    @overload
    def texImage3D(self, target: GLenum, level: GLint, internalformat: GLint, width: GLsizei, height: GLsizei, depth: GLsizei, border: GLint, format: GLenum, type: GLenum, pboOffset: GLintptr) -> None: ...
    @overload
    def texImage3D(self, target: GLenum, level: GLint, internalformat: GLint, width: GLsizei, height: GLsizei, depth: GLsizei, border: GLint, format: GLenum, type: GLenum, source: TexImageSource) -> None: ...
    @overload
    def texImage3D(self, target: GLenum, level: GLint, internalformat: GLint, width: GLsizei, height: GLsizei, depth: GLsizei, border: GLint, format: GLenum, type: GLenum, srcData: Union['ArrayBufferView', 'None']) -> None: ...
    @overload
    def texImage3D(self, target: GLenum, level: GLint, internalformat: GLint, width: GLsizei, height: GLsizei, depth: GLsizei, border: GLint, format: GLenum, type: GLenum, srcData: ArrayBufferView, srcOffset: GLuint) -> None: ...
    @overload
    def texSubImage3D(self, target: GLenum, level: GLint, xoffset: GLint, yoffset: GLint, zoffset: GLint, width: GLsizei, height: GLsizei, depth: GLsizei, format: GLenum, type: GLenum, pboOffset: GLintptr) -> None: ...
    @overload
    def texSubImage3D(self, target: GLenum, level: GLint, xoffset: GLint, yoffset: GLint, zoffset: GLint, width: GLsizei, height: GLsizei, depth: GLsizei, format: GLenum, type: GLenum, source: TexImageSource) -> None: ...
    @overload
    def texSubImage3D(self, target: GLenum, level: GLint, xoffset: GLint, yoffset: GLint, zoffset: GLint, width: GLsizei, height: GLsizei, depth: GLsizei, format: GLenum, type: GLenum, srcData: Union['ArrayBufferView', 'None'], srcOffset: Union['GLuint', 'None'] = 0) -> None: ...

    def copyTexSubImage3D(self, target: GLenum, level: GLint, xoffset: GLint, yoffset: GLint, zoffset: GLint, x: GLint, y: GLint, width: GLsizei, height: GLsizei) -> None: ...
    @overload
    def compressedTexImage3D(self, target: GLenum, level: GLint, internalformat: GLenum, width: GLsizei, height: GLsizei, depth: GLsizei, border: GLint, imageSize: GLsizei, offset: GLintptr) -> None: ...
    @overload
    def compressedTexImage3D(self, target: GLenum, level: GLint, internalformat: GLenum, width: GLsizei, height: GLsizei, depth: GLsizei, border: GLint, srcData: ArrayBufferView, srcOffset: Union['GLuint', 'None'] = 0, srcLengthOverride: Union['GLuint', 'None'] = 0) -> None: ...
    @overload
    def compressedTexSubImage3D(self, target: GLenum, level: GLint, xoffset: GLint, yoffset: GLint, zoffset: GLint, width: GLsizei, height: GLsizei, depth: GLsizei, format: GLenum, imageSize: GLsizei, offset: GLintptr) -> None: ...
    @overload
    def compressedTexSubImage3D(self, target: GLenum, level: GLint, xoffset: GLint, yoffset: GLint, zoffset: GLint, width: GLsizei, height: GLsizei, depth: GLsizei, format: GLenum, srcData: ArrayBufferView, srcOffset: Union['GLuint', 'None'] = 0, srcLengthOverride: Union['GLuint', 'None'] = 0) -> None: ...

    def getFragDataLocation(self, program: WebGLProgram, name: str) -> GLint: ...

    def uniform1ui(self, location: Union['WebGLUniformLocation', 'None'], v0: GLuint) -> None: ...

    def uniform2ui(self, location: Union['WebGLUniformLocation', 'None'], v0: GLuint, v1: GLuint) -> None: ...

    def uniform3ui(self, location: Union['WebGLUniformLocation', 'None'], v0: GLuint, v1: GLuint, v2: GLuint) -> None: ...

    def uniform4ui(self, location: Union['WebGLUniformLocation', 'None'], v0: GLuint, v1: GLuint, v2: GLuint, v3: GLuint) -> None: ...

    def uniform1uiv(self, location: Union['WebGLUniformLocation', 'None'], data: Uint32List, srcOffset: Union['GLuint', 'None'] = 0, srcLength: Union['GLuint', 'None'] = 0) -> None: ...

    def uniform2uiv(self, location: Union['WebGLUniformLocation', 'None'], data: Uint32List, srcOffset: Union['GLuint', 'None'] = 0, srcLength: Union['GLuint', 'None'] = 0) -> None: ...

    def uniform3uiv(self, location: Union['WebGLUniformLocation', 'None'], data: Uint32List, srcOffset: Union['GLuint', 'None'] = 0, srcLength: Union['GLuint', 'None'] = 0) -> None: ...

    def uniform4uiv(self, location: Union['WebGLUniformLocation', 'None'], data: Uint32List, srcOffset: Union['GLuint', 'None'] = 0, srcLength: Union['GLuint', 'None'] = 0) -> None: ...

    def uniformMatrix3x2fv(self, location: Union['WebGLUniformLocation', 'None'], transpose: GLboolean, data: Float32List, srcOffset: Union['GLuint', 'None'] = 0, srcLength: Union['GLuint', 'None'] = 0) -> None: ...

    def uniformMatrix4x2fv(self, location: Union['WebGLUniformLocation', 'None'], transpose: GLboolean, data: Float32List, srcOffset: Union['GLuint', 'None'] = 0, srcLength: Union['GLuint', 'None'] = 0) -> None: ...

    def uniformMatrix2x3fv(self, location: Union['WebGLUniformLocation', 'None'], transpose: GLboolean, data: Float32List, srcOffset: Union['GLuint', 'None'] = 0, srcLength: Union['GLuint', 'None'] = 0) -> None: ...

    def uniformMatrix4x3fv(self, location: Union['WebGLUniformLocation', 'None'], transpose: GLboolean, data: Float32List, srcOffset: Union['GLuint', 'None'] = 0, srcLength: Union['GLuint', 'None'] = 0) -> None: ...

    def uniformMatrix2x4fv(self, location: Union['WebGLUniformLocation', 'None'], transpose: GLboolean, data: Float32List, srcOffset: Union['GLuint', 'None'] = 0, srcLength: Union['GLuint', 'None'] = 0) -> None: ...

    def uniformMatrix3x4fv(self, location: Union['WebGLUniformLocation', 'None'], transpose: GLboolean, data: Float32List, srcOffset: Union['GLuint', 'None'] = 0, srcLength: Union['GLuint', 'None'] = 0) -> None: ...

    def vertexAttribI4i(self, index: GLuint, x: GLint, y: GLint, z: GLint, w: GLint) -> None: ...

    def vertexAttribI4iv(self, index: GLuint, values: Int32List) -> None: ...

    def vertexAttribI4ui(self, index: GLuint, x: GLuint, y: GLuint, z: GLuint, w: GLuint) -> None: ...

    def vertexAttribI4uiv(self, index: GLuint, values: Uint32List) -> None: ...

    def vertexAttribIPointer(self, index: GLuint, size: GLint, type: GLenum, stride: GLsizei, offset: GLintptr) -> None: ...

    def vertexAttribDivisor(self, index: GLuint, divisor: GLuint) -> None: ...

    def drawArraysInstanced(self, mode: GLenum, first: GLint, count: GLsizei, instanceCount: GLsizei) -> None: ...

    def drawElementsInstanced(self, mode: GLenum, count: GLsizei, type: GLenum, offset: GLintptr, instanceCount: GLsizei) -> None: ...

    def drawRangeElements(self, mode: GLenum, start: GLuint, end: GLuint, count: GLsizei, type: GLenum, offset: GLintptr) -> None: ...

    def drawBuffers(self, buffers: Sequence[GLenum]) -> None: ...

    def clearBufferfv(self, buffer: GLenum, drawbuffer: GLint, values: Float32List, srcOffset: Union['GLuint', 'None'] = 0) -> None: ...

    def clearBufferiv(self, buffer: GLenum, drawbuffer: GLint, values: Int32List, srcOffset: Union['GLuint', 'None'] = 0) -> None: ...

    def clearBufferuiv(self, buffer: GLenum, drawbuffer: GLint, values: Uint32List, srcOffset: Union['GLuint', 'None'] = 0) -> None: ...

    def clearBufferfi(self, buffer: GLenum, drawbuffer: GLint, depth: GLfloat, stencil: GLint) -> None: ...

    def createQuery(self) -> Union['WebGLQuery', 'None']: ...

    def deleteQuery(self, query: Union['WebGLQuery', 'None']) -> None: ...

    def isQuery(self, query: Union['WebGLQuery', 'None']) -> GLboolean: ...

    def beginQuery(self, target: GLenum, query: WebGLQuery) -> None: ...

    def endQuery(self, target: GLenum) -> None: ...

    def getQuery(self, target: GLenum, pname: GLenum) -> Union['WebGLQuery', 'None']: ...

    def getQueryParameter(self, query: WebGLQuery, pname: GLenum) -> Any: ...

    def createSampler(self) -> Union['WebGLSampler', 'None']: ...

    def deleteSampler(self, sampler: Union['WebGLSampler', 'None']) -> None: ...

    def isSampler(self, sampler: Union['WebGLSampler', 'None']) -> GLboolean: ...

    def bindSampler(self, unit: GLuint, sampler: Union['WebGLSampler', 'None']) -> None: ...

    def samplerParameteri(self, sampler: WebGLSampler, pname: GLenum, param: GLint) -> None: ...

    def samplerParameterf(self, sampler: WebGLSampler, pname: GLenum, param: GLfloat) -> None: ...

    def getSamplerParameter(self, sampler: WebGLSampler, pname: GLenum) -> Any: ...

    def fenceSync(self, condition: GLenum, flags: GLbitfield) -> Union['WebGLSync', 'None']: ...

    def isSync(self, sync: Union['WebGLSync', 'None']) -> GLboolean: ...

    def deleteSync(self, sync: Union['WebGLSync', 'None']) -> None: ...

    def clientWaitSync(self, sync: WebGLSync, flags: GLbitfield, timeout: GLuint64) -> GLenum: ...

    def waitSync(self, sync: WebGLSync, flags: GLbitfield, timeout: GLint64) -> None: ...

    def getSyncParameter(self, sync: WebGLSync, pname: GLenum) -> Any: ...

    def createTransformFeedback(self) -> Union['WebGLTransformFeedback', 'None']: ...

    def deleteTransformFeedback(self, tf: Union['WebGLTransformFeedback', 'None']) -> None: ...

    def isTransformFeedback(self, tf: Union['WebGLTransformFeedback', 'None']) -> GLboolean: ...

    def bindTransformFeedback(self, target: GLenum, tf: Union['WebGLTransformFeedback', 'None']) -> None: ...

    def beginTransformFeedback(self, primitiveMode: GLenum) -> None: ...

    def endTransformFeedback(self) -> None: ...

    def transformFeedbackVaryings(self, program: WebGLProgram, varyings: Sequence[str], bufferMode: GLenum) -> None: ...

    def getTransformFeedbackVarying(self, program: WebGLProgram, index: GLuint) -> Union['WebGLActiveInfo', 'None']: ...

    def pauseTransformFeedback(self) -> None: ...

    def resumeTransformFeedback(self) -> None: ...

    def bindBufferBase(self, target: GLenum, index: GLuint, buffer: Union['WebGLBuffer', 'None']) -> None: ...

    def bindBufferRange(self, target: GLenum, index: GLuint, buffer: Union['WebGLBuffer', 'None'], offset: GLintptr, size: GLsizeiptr) -> None: ...

    def getIndexedParameter(self, target: GLenum, index: GLuint) -> Any: ...

    def getUniformIndices(self, program: WebGLProgram, uniformNames: Sequence[str]) -> Sequence[GLuint]: ...

    def getActiveUniforms(self, program: WebGLProgram, uniformIndices: Sequence[GLuint], pname: GLenum) -> Any: ...

    def getUniformBlockIndex(self, program: WebGLProgram, uniformBlockName: str) -> GLuint: ...

    def getActiveUniformBlockParameter(self, program: WebGLProgram, uniformBlockIndex: GLuint, pname: GLenum) -> Any: ...

    def getActiveUniformBlockName(self, program: WebGLProgram, uniformBlockIndex: GLuint) -> Union['str', 'None']: ...

    def uniformBlockBinding(self, program: WebGLProgram, uniformBlockIndex: GLuint, uniformBlockBinding: GLuint) -> None: ...

    def createVertexArray(self) -> Union['WebGLVertexArrayObject', 'None']: ...

    def deleteVertexArray(self, vertexArray: Union['WebGLVertexArrayObject', 'None']) -> None: ...

    def isVertexArray(self, vertexArray: Union['WebGLVertexArrayObject', 'None']) -> GLboolean: ...

    def bindVertexArray(self, array: Union['WebGLVertexArrayObject', 'None']) -> None: ...

class WebGL2RenderingContextOverloads:
    @overload
    def bufferData(self, target: GLenum, size: GLsizeiptr, usage: GLenum) -> None: ...
    @overload
    def bufferData(self, target: GLenum, srcData: Union['AllowSharedBufferSource', 'None'], usage: GLenum) -> None: ...
    @overload
    def bufferData(self, target: GLenum, srcData: ArrayBufferView, usage: GLenum, srcOffset: GLuint, length: Union['GLuint', 'None'] = 0) -> None: ...
    @overload
    def bufferSubData(self, target: GLenum, dstByteOffset: GLintptr, srcData: AllowSharedBufferSource) -> None: ...
    @overload
    def bufferSubData(self, target: GLenum, dstByteOffset: GLintptr, srcData: ArrayBufferView, srcOffset: GLuint, length: Union['GLuint', 'None'] = 0) -> None: ...
    @overload
    def texImage2D(self, target: GLenum, level: GLint, internalformat: GLint, width: GLsizei, height: GLsizei, border: GLint, format: GLenum, type: GLenum, pixels: Union['ArrayBufferView', 'None']) -> None: ...
    @overload
    def texImage2D(self, target: GLenum, level: GLint, internalformat: GLint, format: GLenum, type: GLenum, source: TexImageSource) -> None: ...
    @overload
    def texImage2D(self, target: GLenum, level: GLint, internalformat: GLint, width: GLsizei, height: GLsizei, border: GLint, format: GLenum, type: GLenum, pboOffset: GLintptr) -> None: ...
    @overload
    def texImage2D(self, target: GLenum, level: GLint, internalformat: GLint, width: GLsizei, height: GLsizei, border: GLint, format: GLenum, type: GLenum, source: TexImageSource) -> None: ...
    @overload
    def texImage2D(self, target: GLenum, level: GLint, internalformat: GLint, width: GLsizei, height: GLsizei, border: GLint, format: GLenum, type: GLenum, srcData: ArrayBufferView, srcOffset: GLuint) -> None: ...
    @overload
    def texSubImage2D(self, target: GLenum, level: GLint, xoffset: GLint, yoffset: GLint, width: GLsizei, height: GLsizei, format: GLenum, type: GLenum, pixels: Union['ArrayBufferView', 'None']) -> None: ...
    @overload
    def texSubImage2D(self, target: GLenum, level: GLint, xoffset: GLint, yoffset: GLint, format: GLenum, type: GLenum, source: TexImageSource) -> None: ...
    @overload
    def texSubImage2D(self, target: GLenum, level: GLint, xoffset: GLint, yoffset: GLint, width: GLsizei, height: GLsizei, format: GLenum, type: GLenum, pboOffset: GLintptr) -> None: ...
    @overload
    def texSubImage2D(self, target: GLenum, level: GLint, xoffset: GLint, yoffset: GLint, width: GLsizei, height: GLsizei, format: GLenum, type: GLenum, source: TexImageSource) -> None: ...
    @overload
    def texSubImage2D(self, target: GLenum, level: GLint, xoffset: GLint, yoffset: GLint, width: GLsizei, height: GLsizei, format: GLenum, type: GLenum, srcData: ArrayBufferView, srcOffset: GLuint) -> None: ...
    @overload
    def compressedTexImage2D(self, target: GLenum, level: GLint, internalformat: GLenum, width: GLsizei, height: GLsizei, border: GLint, imageSize: GLsizei, offset: GLintptr) -> None: ...
    @overload
    def compressedTexImage2D(self, target: GLenum, level: GLint, internalformat: GLenum, width: GLsizei, height: GLsizei, border: GLint, srcData: ArrayBufferView, srcOffset: Union['GLuint', 'None'] = 0, srcLengthOverride: Union['GLuint', 'None'] = 0) -> None: ...
    @overload
    def compressedTexSubImage2D(self, target: GLenum, level: GLint, xoffset: GLint, yoffset: GLint, width: GLsizei, height: GLsizei, format: GLenum, imageSize: GLsizei, offset: GLintptr) -> None: ...
    @overload
    def compressedTexSubImage2D(self, target: GLenum, level: GLint, xoffset: GLint, yoffset: GLint, width: GLsizei, height: GLsizei, format: GLenum, srcData: ArrayBufferView, srcOffset: Union['GLuint', 'None'] = 0, srcLengthOverride: Union['GLuint', 'None'] = 0) -> None: ...

    def uniform1fv(self, location: Union['WebGLUniformLocation', 'None'], data: Float32List, srcOffset: Union['GLuint', 'None'] = 0, srcLength: Union['GLuint', 'None'] = 0) -> None: ...

    def uniform2fv(self, location: Union['WebGLUniformLocation', 'None'], data: Float32List, srcOffset: Union['GLuint', 'None'] = 0, srcLength: Union['GLuint', 'None'] = 0) -> None: ...

    def uniform3fv(self, location: Union['WebGLUniformLocation', 'None'], data: Float32List, srcOffset: Union['GLuint', 'None'] = 0, srcLength: Union['GLuint', 'None'] = 0) -> None: ...

    def uniform4fv(self, location: Union['WebGLUniformLocation', 'None'], data: Float32List, srcOffset: Union['GLuint', 'None'] = 0, srcLength: Union['GLuint', 'None'] = 0) -> None: ...

    def uniform1iv(self, location: Union['WebGLUniformLocation', 'None'], data: Int32List, srcOffset: Union['GLuint', 'None'] = 0, srcLength: Union['GLuint', 'None'] = 0) -> None: ...

    def uniform2iv(self, location: Union['WebGLUniformLocation', 'None'], data: Int32List, srcOffset: Union['GLuint', 'None'] = 0, srcLength: Union['GLuint', 'None'] = 0) -> None: ...

    def uniform3iv(self, location: Union['WebGLUniformLocation', 'None'], data: Int32List, srcOffset: Union['GLuint', 'None'] = 0, srcLength: Union['GLuint', 'None'] = 0) -> None: ...

    def uniform4iv(self, location: Union['WebGLUniformLocation', 'None'], data: Int32List, srcOffset: Union['GLuint', 'None'] = 0, srcLength: Union['GLuint', 'None'] = 0) -> None: ...

    def uniformMatrix2fv(self, location: Union['WebGLUniformLocation', 'None'], transpose: GLboolean, data: Float32List, srcOffset: Union['GLuint', 'None'] = 0, srcLength: Union['GLuint', 'None'] = 0) -> None: ...

    def uniformMatrix3fv(self, location: Union['WebGLUniformLocation', 'None'], transpose: GLboolean, data: Float32List, srcOffset: Union['GLuint', 'None'] = 0, srcLength: Union['GLuint', 'None'] = 0) -> None: ...

    def uniformMatrix4fv(self, location: Union['WebGLUniformLocation', 'None'], transpose: GLboolean, data: Float32List, srcOffset: Union['GLuint', 'None'] = 0, srcLength: Union['GLuint', 'None'] = 0) -> None: ...
    @overload
    def readPixels(self, x: GLint, y: GLint, width: GLsizei, height: GLsizei, format: GLenum, type: GLenum, dstData: Union['ArrayBufferView', 'None']) -> None: ...
    @overload
    def readPixels(self, x: GLint, y: GLint, width: GLsizei, height: GLsizei, format: GLenum, type: GLenum, offset: GLintptr) -> None: ...
    @overload
    def readPixels(self, x: GLint, y: GLint, width: GLsizei, height: GLsizei, format: GLenum, type: GLenum, dstData: ArrayBufferView, dstOffset: GLuint) -> None: ...

class WebGL2RenderingContext(WebGLRenderingContextBase, WebGL2RenderingContextBase, WebGL2RenderingContextOverloads): ...

class GPUObjectBase:
    label: str

class GPUObjectDescriptorBase(TypedDict):
    label: NotRequired[str]

class GPUSupportedLimits:
    maxTextureDimension1D: int
    maxTextureDimension2D: int
    maxTextureDimension3D: int
    maxTextureArrayLayers: int
    maxBindGroups: int
    maxBindGroupsPlusVertexBuffers: int
    maxBindingsPerBindGroup: int
    maxDynamicUniformBuffersPerPipelineLayout: int
    maxDynamicStorageBuffersPerPipelineLayout: int
    maxSampledTexturesPerShaderStage: int
    maxSamplersPerShaderStage: int
    maxStorageBuffersPerShaderStage: int
    maxStorageTexturesPerShaderStage: int
    maxUniformBuffersPerShaderStage: int
    maxUniformBufferBindingSize: int
    maxStorageBufferBindingSize: int
    minUniformBufferOffsetAlignment: int
    minStorageBufferOffsetAlignment: int
    maxVertexBuffers: int
    maxBufferSize: int
    maxVertexAttributes: int
    maxVertexBufferArrayStride: int
    maxInterStageShaderComponents: int
    maxInterStageShaderVariables: int
    maxColorAttachments: int
    maxColorAttachmentBytesPerSample: int
    maxComputeWorkgroupStorageSize: int
    maxComputeInvocationsPerWorkgroup: int
    maxComputeWorkgroupSizeX: int
    maxComputeWorkgroupSizeY: int
    maxComputeWorkgroupSizeZ: int
    maxComputeWorkgroupsPerDimension: int

class GPUSupportedFeatures: ...

class WGSLLanguageFeatures: ...

class GPUAdapterInfo:
    vendor: str
    architecture: str
    device: str
    description: str

class NavigatorGPU:
    gpu: GPU

class GPU:

    def requestAdapter(self, options: Union['GPURequestAdapterOptions', 'None'] = {}) -> Awaitable[Union['GPUAdapter', 'None']]: ...

    def getPreferredCanvasFormat(self) -> GPUTextureFormat: ...
    wgslLanguageFeatures: WGSLLanguageFeatures

class GPURequestAdapterOptions(TypedDict):
    powerPreference: NotRequired[GPUPowerPreference]
    forceFallbackAdapter: NotRequired[bool]

class GPUAdapter:
    features: GPUSupportedFeatures
    limits: GPUSupportedLimits
    isFallbackAdapter: bool

    def requestDevice(self, descriptor: Union['GPUDeviceDescriptor', 'None'] = {}) -> Awaitable[GPUDevice]: ...

    def requestAdapterInfo(self, unmaskHints: Union['Sequence[str]', 'None'] = []) -> Awaitable[GPUAdapterInfo]: ...

class GPUDeviceDescriptor(GPUObjectDescriptorBase):
    requiredFeatures: NotRequired[Sequence[GPUFeatureName]]
    requiredLimits: NotRequired[GPUSize64]
    defaultQueue: NotRequired[GPUQueueDescriptor]

class GPUDevice(EventTarget, GPUObjectBase):
    features: GPUSupportedFeatures
    limits: GPUSupportedLimits
    queue: GPUQueue

    def destroy(self) -> None: ...

    def createBuffer(self, descriptor: GPUBufferDescriptor) -> GPUBuffer: ...

    def createTexture(self, descriptor: GPUTextureDescriptor) -> GPUTexture: ...

    def createSampler(self, descriptor: Union['GPUSamplerDescriptor', 'None'] = {}) -> GPUSampler: ...

    def importExternalTexture(self, descriptor: GPUExternalTextureDescriptor) -> GPUExternalTexture: ...

    def createBindGroupLayout(self, descriptor: GPUBindGroupLayoutDescriptor) -> GPUBindGroupLayout: ...

    def createPipelineLayout(self, descriptor: GPUPipelineLayoutDescriptor) -> GPUPipelineLayout: ...

    def createBindGroup(self, descriptor: GPUBindGroupDescriptor) -> GPUBindGroup: ...

    def createShaderModule(self, descriptor: GPUShaderModuleDescriptor) -> GPUShaderModule: ...

    def createComputePipeline(self, descriptor: GPUComputePipelineDescriptor) -> GPUComputePipeline: ...

    def createRenderPipeline(self, descriptor: GPURenderPipelineDescriptor) -> GPURenderPipeline: ...

    def createComputePipelineAsync(self, descriptor: GPUComputePipelineDescriptor) -> Awaitable[GPUComputePipeline]: ...

    def createRenderPipelineAsync(self, descriptor: GPURenderPipelineDescriptor) -> Awaitable[GPURenderPipeline]: ...

    def createCommandEncoder(self, descriptor: Union['GPUCommandEncoderDescriptor', 'None'] = {}) -> GPUCommandEncoder: ...

    def createRenderBundleEncoder(self, descriptor: GPURenderBundleEncoderDescriptor) -> GPURenderBundleEncoder: ...

    def createQuerySet(self, descriptor: GPUQuerySetDescriptor) -> GPUQuerySet: ...
    lost: Awaitable[GPUDeviceLostInfo]

    def pushErrorScope(self, filter: GPUErrorFilter) -> None: ...

    def popErrorScope(self) -> Awaitable[Union['GPUError', 'None']]: ...
    onuncapturederror: EventHandler

class GPUBuffer(GPUObjectBase):
    size: GPUSize64Out
    usage: GPUFlagsConstant
    mapState: GPUBufferMapState

    def mapAsync(self, mode: GPUMapModeFlags, offset: Union['GPUSize64', 'None'] = 0, size: Union['GPUSize64', 'None'] = None) -> Awaitable[None]: ...

    def getMappedRange(self, offset: Union['GPUSize64', 'None'] = 0, size: Union['GPUSize64', 'None'] = None) -> ArrayBuffer: ...

    def unmap(self) -> None: ...

    def destroy(self) -> None: ...

class GPUBufferDescriptor(GPUObjectDescriptorBase):
    size: GPUSize64
    usage: GPUBufferUsageFlags
    mappedAtCreation: NotRequired[bool]

class GPUTexture(GPUObjectBase):

    def createView(self, descriptor: Union['GPUTextureViewDescriptor', 'None'] = {}) -> GPUTextureView: ...

    def destroy(self) -> None: ...
    width: GPUIntegerCoordinateOut
    height: GPUIntegerCoordinateOut
    depthOrArrayLayers: GPUIntegerCoordinateOut
    mipLevelCount: GPUIntegerCoordinateOut
    sampleCount: GPUSize32Out
    dimension: GPUTextureDimension
    format: GPUTextureFormat
    usage: GPUFlagsConstant

class GPUTextureDescriptor(GPUObjectDescriptorBase):
    size: GPUExtent3D
    mipLevelCount: NotRequired[GPUIntegerCoordinate]
    sampleCount: NotRequired[GPUSize32]
    dimension: NotRequired[GPUTextureDimension]
    format: GPUTextureFormat
    usage: GPUTextureUsageFlags
    viewFormats: NotRequired[Sequence[GPUTextureFormat]]

class GPUTextureView(GPUObjectBase): ...

class GPUTextureViewDescriptor(GPUObjectDescriptorBase):
    format: NotRequired[GPUTextureFormat]
    dimension: NotRequired[GPUTextureViewDimension]
    aspect: NotRequired[GPUTextureAspect]
    baseMipLevel: NotRequired[GPUIntegerCoordinate]
    mipLevelCount: NotRequired[GPUIntegerCoordinate]
    baseArrayLayer: NotRequired[GPUIntegerCoordinate]
    arrayLayerCount: NotRequired[GPUIntegerCoordinate]

class GPUExternalTexture(GPUObjectBase): ...

class GPUExternalTextureDescriptor(GPUObjectDescriptorBase):
    source: Union['HTMLVideoElement', 'VideoFrame']
    colorSpace: NotRequired[PredefinedColorSpace]

class GPUSampler(GPUObjectBase): ...

class GPUSamplerDescriptor(GPUObjectDescriptorBase):
    addressModeU: NotRequired[GPUAddressMode]
    addressModeV: NotRequired[GPUAddressMode]
    addressModeW: NotRequired[GPUAddressMode]
    magFilter: NotRequired[GPUFilterMode]
    minFilter: NotRequired[GPUFilterMode]
    mipmapFilter: NotRequired[GPUMipmapFilterMode]
    lodMinClamp: NotRequired[float]
    lodMaxClamp: NotRequired[float]
    compare: NotRequired[GPUCompareFunction]
    maxAnisotropy: NotRequired[int]

class GPUBindGroupLayout(GPUObjectBase): ...

class GPUBindGroupLayoutDescriptor(GPUObjectDescriptorBase):
    entries: Sequence[GPUBindGroupLayoutEntry]

class GPUBindGroupLayoutEntry(TypedDict):
    binding: GPUIndex32
    visibility: GPUShaderStageFlags
    buffer: NotRequired[GPUBufferBindingLayout]
    sampler: NotRequired[GPUSamplerBindingLayout]
    texture: NotRequired[GPUTextureBindingLayout]
    storageTexture: NotRequired[GPUStorageTextureBindingLayout]
    externalTexture: NotRequired[GPUExternalTextureBindingLayout]

class GPUBufferBindingLayout(TypedDict):
    type: NotRequired[GPUBufferBindingType]
    hasDynamicOffset: NotRequired[bool]
    minBindingSize: NotRequired[GPUSize64]

class GPUSamplerBindingLayout(TypedDict):
    type: NotRequired[GPUSamplerBindingType]

class GPUTextureBindingLayout(TypedDict):
    sampleType: NotRequired[GPUTextureSampleType]
    viewDimension: NotRequired[GPUTextureViewDimension]
    multisampled: NotRequired[bool]

class GPUStorageTextureBindingLayout(TypedDict):
    access: NotRequired[GPUStorageTextureAccess]
    format: GPUTextureFormat
    viewDimension: NotRequired[GPUTextureViewDimension]

class GPUExternalTextureBindingLayout(TypedDict): ...

class GPUBindGroup(GPUObjectBase): ...

class GPUBindGroupDescriptor(GPUObjectDescriptorBase):
    layout: GPUBindGroupLayout
    entries: Sequence[GPUBindGroupEntry]

class GPUBindGroupEntry(TypedDict):
    binding: GPUIndex32
    resource: GPUBindingResource

class GPUBufferBinding(TypedDict):
    buffer: GPUBuffer
    offset: NotRequired[GPUSize64]
    size: NotRequired[GPUSize64]

class GPUPipelineLayout(GPUObjectBase): ...

class GPUPipelineLayoutDescriptor(GPUObjectDescriptorBase):
    bindGroupLayouts: Sequence[GPUBindGroupLayout]

class GPUShaderModule(GPUObjectBase):

    def getCompilationInfo(self) -> Awaitable[GPUCompilationInfo]: ...

class GPUShaderModuleDescriptor(GPUObjectDescriptorBase):
    code: str
    sourceMap: NotRequired[object]
    hints: NotRequired[GPUShaderModuleCompilationHint]

class GPUShaderModuleCompilationHint(TypedDict):
    layout: NotRequired[Union['GPUPipelineLayout', 'GPUAutoLayoutMode']]

class GPUCompilationMessage:
    message: str
    type: GPUCompilationMessageType
    lineNum: int
    linePos: int
    offset: int
    length: int

class GPUCompilationInfo:
    messages: Sequence[GPUCompilationMessage]

class GPUPipelineError(DOMException):
    @classmethod
    def new(cls, message: Union['str', 'None'] = "", options: GPUPipelineErrorInit) -> GPUPipelineError: ...
    reason: GPUPipelineErrorReason

class GPUPipelineErrorInit(TypedDict):
    reason: GPUPipelineErrorReason

class GPUPipelineDescriptorBase(GPUObjectDescriptorBase):
    layout: Union['GPUPipelineLayout', 'GPUAutoLayoutMode']

class GPUPipelineBase:

    def getBindGroupLayout(self, index: int) -> GPUBindGroupLayout: ...

class GPUProgrammableStage(TypedDict):
    module: GPUShaderModule
    entryPoint: str
    constants: NotRequired[GPUPipelineConstantValue]

class GPUComputePipeline(GPUObjectBase, GPUPipelineBase): ...

class GPUComputePipelineDescriptor(GPUPipelineDescriptorBase):
    compute: GPUProgrammableStage

class GPURenderPipeline(GPUObjectBase, GPUPipelineBase): ...

class GPURenderPipelineDescriptor(GPUPipelineDescriptorBase):
    vertex: GPUVertexState
    primitive: NotRequired[GPUPrimitiveState]
    depthStencil: NotRequired[GPUDepthStencilState]
    multisample: NotRequired[GPUMultisampleState]
    fragment: NotRequired[GPUFragmentState]

class GPUPrimitiveState(TypedDict):
    topology: NotRequired[GPUPrimitiveTopology]
    stripIndexFormat: NotRequired[GPUIndexFormat]
    frontFace: NotRequired[GPUFrontFace]
    cullMode: NotRequired[GPUCullMode]
    unclippedDepth: NotRequired[bool]

class GPUMultisampleState(TypedDict):
    count: NotRequired[GPUSize32]
    mask: NotRequired[GPUSampleMask]
    alphaToCoverageEnabled: NotRequired[bool]

class GPUFragmentState(GPUProgrammableStage):
    targets: Sequence[Union['GPUColorTargetState', 'None']]

class GPUColorTargetState(TypedDict):
    format: GPUTextureFormat
    blend: NotRequired[GPUBlendState]
    writeMask: NotRequired[GPUColorWriteFlags]

class GPUBlendState(TypedDict):
    color: GPUBlendComponent
    alpha: GPUBlendComponent

class GPUBlendComponent(TypedDict):
    operation: NotRequired[GPUBlendOperation]
    srcFactor: NotRequired[GPUBlendFactor]
    dstFactor: NotRequired[GPUBlendFactor]

class GPUDepthStencilState(TypedDict):
    format: GPUTextureFormat
    depthWriteEnabled: bool
    depthCompare: GPUCompareFunction
    stencilFront: NotRequired[GPUStencilFaceState]
    stencilBack: NotRequired[GPUStencilFaceState]
    stencilReadMask: NotRequired[GPUStencilValue]
    stencilWriteMask: NotRequired[GPUStencilValue]
    depthBias: NotRequired[GPUDepthBias]
    depthBiasSlopeScale: NotRequired[float]
    depthBiasClamp: NotRequired[float]

class GPUStencilFaceState(TypedDict):
    compare: NotRequired[GPUCompareFunction]
    failOp: NotRequired[GPUStencilOperation]
    depthFailOp: NotRequired[GPUStencilOperation]
    passOp: NotRequired[GPUStencilOperation]

class GPUVertexState(GPUProgrammableStage):
    buffers: NotRequired[Sequence[Union['GPUVertexBufferLayout', 'None']]]

class GPUVertexBufferLayout(TypedDict):
    arrayStride: GPUSize64
    stepMode: NotRequired[GPUVertexStepMode]
    attributes: Sequence[GPUVertexAttribute]

class GPUVertexAttribute(TypedDict):
    format: GPUVertexFormat
    offset: GPUSize64
    shaderLocation: GPUIndex32

class GPUImageDataLayout(TypedDict):
    offset: NotRequired[GPUSize64]
    bytesPerRow: NotRequired[GPUSize32]
    rowsPerImage: NotRequired[GPUSize32]

class GPUImageCopyBuffer(GPUImageDataLayout):
    buffer: GPUBuffer

class GPUImageCopyTexture(TypedDict):
    texture: GPUTexture
    mipLevel: NotRequired[GPUIntegerCoordinate]
    origin: NotRequired[GPUOrigin3D]
    aspect: NotRequired[GPUTextureAspect]

class GPUImageCopyTextureTagged(GPUImageCopyTexture):
    colorSpace: NotRequired[PredefinedColorSpace]
    premultipliedAlpha: NotRequired[bool]

class GPUImageCopyExternalImage(TypedDict):
    source: GPUImageCopyExternalImageSource
    origin: NotRequired[GPUOrigin2D]
    flipY: NotRequired[bool]

class GPUCommandBuffer(GPUObjectBase): ...

class GPUCommandBufferDescriptor(GPUObjectDescriptorBase): ...

class GPUCommandsMixin: ...

class GPUCommandEncoder(GPUObjectBase, GPUCommandsMixin, GPUDebugCommandsMixin):

    def beginRenderPass(self, descriptor: GPURenderPassDescriptor) -> GPURenderPassEncoder: ...

    def beginComputePass(self, descriptor: Union['GPUComputePassDescriptor', 'None'] = {}) -> GPUComputePassEncoder: ...

    def copyBufferToBuffer(self, source: GPUBuffer, sourceOffset: GPUSize64, destination: GPUBuffer, destinationOffset: GPUSize64, size: GPUSize64) -> None: ...

    def copyBufferToTexture(self, source: GPUImageCopyBuffer, destination: GPUImageCopyTexture, copySize: GPUExtent3D) -> None: ...

    def copyTextureToBuffer(self, source: GPUImageCopyTexture, destination: GPUImageCopyBuffer, copySize: GPUExtent3D) -> None: ...

    def copyTextureToTexture(self, source: GPUImageCopyTexture, destination: GPUImageCopyTexture, copySize: GPUExtent3D) -> None: ...

    def clearBuffer(self, buffer: GPUBuffer, offset: Union['GPUSize64', 'None'] = 0, size: Union['GPUSize64', 'None'] = None) -> None: ...

    def writeTimestamp(self, querySet: GPUQuerySet, queryIndex: GPUSize32) -> None: ...

    def resolveQuerySet(self, querySet: GPUQuerySet, firstQuery: GPUSize32, queryCount: GPUSize32, destination: GPUBuffer, destinationOffset: GPUSize64) -> None: ...

    def finish(self, descriptor: Union['GPUCommandBufferDescriptor', 'None'] = {}) -> GPUCommandBuffer: ...

class GPUCommandEncoderDescriptor(GPUObjectDescriptorBase): ...

class GPUBindingCommandsMixin:
    @overload
    def setBindGroup(self, index: GPUIndex32, bindGroup: Union['GPUBindGroup', 'None'], dynamicOffsets: Union['Sequence[GPUBufferDynamicOffset]', 'None'] = []) -> None: ...
    @overload
    def setBindGroup(self, index: GPUIndex32, bindGroup: Union['GPUBindGroup', 'None'], dynamicOffsetsData: Uint32Array, dynamicOffsetsDataStart: GPUSize64, dynamicOffsetsDataLength: GPUSize32) -> None: ...

class GPUDebugCommandsMixin:

    def pushDebugGroup(self, groupLabel: str) -> None: ...

    def popDebugGroup(self) -> None: ...

    def insertDebugMarker(self, markerLabel: str) -> None: ...

class GPUComputePassEncoder(GPUObjectBase, GPUCommandsMixin, GPUDebugCommandsMixin, GPUBindingCommandsMixin):

    def setPipeline(self, pipeline: GPUComputePipeline) -> None: ...

    def dispatchWorkgroups(self, workgroupCountX: GPUSize32, workgroupCountY: Union['GPUSize32', 'None'] = 1, workgroupCountZ: Union['GPUSize32', 'None'] = 1) -> None: ...

    def dispatchWorkgroupsIndirect(self, indirectBuffer: GPUBuffer, indirectOffset: GPUSize64) -> None: ...

    def end(self) -> None: ...

class GPUComputePassTimestampWrites(TypedDict):
    querySet: GPUQuerySet
    beginningOfPassWriteIndex: NotRequired[GPUSize32]
    endOfPassWriteIndex: NotRequired[GPUSize32]

class GPUComputePassDescriptor(GPUObjectDescriptorBase):
    timestampWrites: NotRequired[GPUComputePassTimestampWrites]

class GPURenderPassEncoder(GPUObjectBase, GPUCommandsMixin, GPUDebugCommandsMixin, GPUBindingCommandsMixin, GPURenderCommandsMixin):

    def setViewport(self, x: float, y: float, width: float, height: float, minDepth: float, maxDepth: float) -> None: ...

    def setScissorRect(self, x: GPUIntegerCoordinate, y: GPUIntegerCoordinate, width: GPUIntegerCoordinate, height: GPUIntegerCoordinate) -> None: ...

    def setBlendConstant(self, color: GPUColor) -> None: ...

    def setStencilReference(self, reference: GPUStencilValue) -> None: ...

    def beginOcclusionQuery(self, queryIndex: GPUSize32) -> None: ...

    def endOcclusionQuery(self) -> None: ...

    def executeBundles(self, bundles: Sequence[GPURenderBundle]) -> None: ...

    def end(self) -> None: ...

class GPURenderPassTimestampWrites(TypedDict):
    querySet: GPUQuerySet
    beginningOfPassWriteIndex: NotRequired[GPUSize32]
    endOfPassWriteIndex: NotRequired[GPUSize32]

class GPURenderPassDescriptor(GPUObjectDescriptorBase):
    colorAttachments: Sequence[Union['GPURenderPassColorAttachment', 'None']]
    depthStencilAttachment: NotRequired[GPURenderPassDepthStencilAttachment]
    occlusionQuerySet: NotRequired[GPUQuerySet]
    timestampWrites: NotRequired[GPURenderPassTimestampWrites]
    maxDrawCount: NotRequired[GPUSize64]

class GPURenderPassColorAttachment(TypedDict):
    view: GPUTextureView
    resolveTarget: NotRequired[GPUTextureView]
    clearValue: NotRequired[GPUColor]
    loadOp: GPULoadOp
    storeOp: GPUStoreOp

class GPURenderPassDepthStencilAttachment(TypedDict):
    view: GPUTextureView
    depthClearValue: NotRequired[float]
    depthLoadOp: NotRequired[GPULoadOp]
    depthStoreOp: NotRequired[GPUStoreOp]
    depthReadOnly: NotRequired[bool]
    stencilClearValue: NotRequired[GPUStencilValue]
    stencilLoadOp: NotRequired[GPULoadOp]
    stencilStoreOp: NotRequired[GPUStoreOp]
    stencilReadOnly: NotRequired[bool]

class GPURenderPassLayout(GPUObjectDescriptorBase):
    colorFormats: Sequence[Union['GPUTextureFormat', 'None']]
    depthStencilFormat: NotRequired[GPUTextureFormat]
    sampleCount: NotRequired[GPUSize32]

class GPURenderCommandsMixin:

    def setPipeline(self, pipeline: GPURenderPipeline) -> None: ...

    def setIndexBuffer(self, buffer: GPUBuffer, indexFormat: GPUIndexFormat, offset: Union['GPUSize64', 'None'] = 0, size: Union['GPUSize64', 'None'] = None) -> None: ...

    def setVertexBuffer(self, slot: GPUIndex32, buffer: Union['GPUBuffer', 'None'], offset: Union['GPUSize64', 'None'] = 0, size: Union['GPUSize64', 'None'] = None) -> None: ...

    def draw(self, vertexCount: GPUSize32, instanceCount: Union['GPUSize32', 'None'] = 1, firstVertex: Union['GPUSize32', 'None'] = 0, firstInstance: Union['GPUSize32', 'None'] = 0) -> None: ...

    def drawIndexed(self, indexCount: GPUSize32, instanceCount: Union['GPUSize32', 'None'] = 1, firstIndex: Union['GPUSize32', 'None'] = 0, baseVertex: Union['GPUSignedOffset32', 'None'] = 0, firstInstance: Union['GPUSize32', 'None'] = 0) -> None: ...

    def drawIndirect(self, indirectBuffer: GPUBuffer, indirectOffset: GPUSize64) -> None: ...

    def drawIndexedIndirect(self, indirectBuffer: GPUBuffer, indirectOffset: GPUSize64) -> None: ...

class GPURenderBundle(GPUObjectBase): ...

class GPURenderBundleDescriptor(GPUObjectDescriptorBase): ...

class GPURenderBundleEncoder(GPUObjectBase, GPUCommandsMixin, GPUDebugCommandsMixin, GPUBindingCommandsMixin, GPURenderCommandsMixin):

    def finish(self, descriptor: Union['GPURenderBundleDescriptor', 'None'] = {}) -> GPURenderBundle: ...

class GPURenderBundleEncoderDescriptor(GPURenderPassLayout):
    depthReadOnly: NotRequired[bool]
    stencilReadOnly: NotRequired[bool]

class GPUQueueDescriptor(GPUObjectDescriptorBase): ...

class GPUQueue(GPUObjectBase):

    def submit(self, commandBuffers: Sequence[GPUCommandBuffer]) -> None: ...

    def onSubmittedWorkDone(self) -> Awaitable[None]: ...

    def writeBuffer(self, buffer: GPUBuffer, bufferOffset: GPUSize64, data: AllowSharedBufferSource, dataOffset: Union['GPUSize64', 'None'] = 0, size: Union['GPUSize64', 'None'] = None) -> None: ...

    def writeTexture(self, destination: GPUImageCopyTexture, data: AllowSharedBufferSource, dataLayout: GPUImageDataLayout, size: GPUExtent3D) -> None: ...

    def copyExternalImageToTexture(self, source: GPUImageCopyExternalImage, destination: GPUImageCopyTextureTagged, copySize: GPUExtent3D) -> None: ...

class GPUQuerySet(GPUObjectBase):

    def destroy(self) -> None: ...
    type: GPUQueryType
    count: GPUSize32Out

class GPUQuerySetDescriptor(GPUObjectDescriptorBase):
    type: GPUQueryType
    count: GPUSize32

class GPUCanvasContext:
    canvas: Union['HTMLCanvasElement', 'OffscreenCanvas']

    def configure(self, configuration: GPUCanvasConfiguration) -> None: ...

    def unconfigure(self) -> None: ...

    def getCurrentTexture(self) -> GPUTexture: ...

class GPUCanvasConfiguration(TypedDict):
    device: GPUDevice
    format: GPUTextureFormat
    usage: NotRequired[GPUTextureUsageFlags]
    viewFormats: NotRequired[Sequence[GPUTextureFormat]]
    colorSpace: NotRequired[PredefinedColorSpace]
    alphaMode: NotRequired[GPUCanvasAlphaMode]

class GPUDeviceLostInfo:
    reason: GPUDeviceLostReason
    message: str

class GPUError:
    message: str

class GPUValidationError(GPUError):
    @classmethod
    def new(cls, message: str) -> GPUValidationError: ...

class GPUOutOfMemoryError(GPUError):
    @classmethod
    def new(cls, message: str) -> GPUOutOfMemoryError: ...

class GPUInternalError(GPUError):
    @classmethod
    def new(cls, message: str) -> GPUInternalError: ...

class GPUUncapturedErrorEvent(Event):
    @classmethod
    def new(cls, type: str, gpuUncapturedErrorEventInitDict: GPUUncapturedErrorEventInit) -> GPUUncapturedErrorEvent: ...
    error: GPUError

class GPUUncapturedErrorEventInit(EventInit):
    error: GPUError

class GPUColorDict(TypedDict):
    r: float
    g: float
    b: float
    a: float

class GPUOrigin2DDict(TypedDict):
    x: NotRequired[GPUIntegerCoordinate]
    y: NotRequired[GPUIntegerCoordinate]

class GPUOrigin3DDict(TypedDict):
    x: NotRequired[GPUIntegerCoordinate]
    y: NotRequired[GPUIntegerCoordinate]
    z: NotRequired[GPUIntegerCoordinate]

class GPUExtent3DDict(TypedDict):
    width: GPUIntegerCoordinate
    height: NotRequired[GPUIntegerCoordinate]
    depthOrArrayLayers: NotRequired[GPUIntegerCoordinate]

class HID(EventTarget):
    onconnect: EventHandler
    ondisconnect: EventHandler

    def getDevices(self) -> Awaitable[Sequence[HIDDevice]]: ...

    def requestDevice(self, options: HIDDeviceRequestOptions) -> Awaitable[Sequence[HIDDevice]]: ...

class HIDDeviceRequestOptions(TypedDict):
    filters: Sequence[HIDDeviceFilter]
    exclusionFilters: NotRequired[Sequence[HIDDeviceFilter]]

class HIDDeviceFilter(TypedDict):
    vendorId: NotRequired[int]
    productId: NotRequired[int]
    usagePage: NotRequired[int]
    usage: NotRequired[int]

class HIDDevice(EventTarget):
    oninputreport: EventHandler
    opened: bool
    vendorId: int
    productId: int
    productName: str
    collections: Sequence[HIDCollectionInfo]

    def open(self) -> Awaitable[None]: ...

    def close(self) -> Awaitable[None]: ...

    def forget(self) -> Awaitable[None]: ...

    def sendReport(self, reportId: int, data: BufferSource) -> Awaitable[None]: ...

    def sendFeatureReport(self, reportId: int, data: BufferSource) -> Awaitable[None]: ...

    def receiveFeatureReport(self, reportId: int) -> Awaitable[DataView]: ...

class HIDConnectionEvent(Event):
    @classmethod
    def new(cls, type: str, eventInitDict: HIDConnectionEventInit) -> HIDConnectionEvent: ...
    device: HIDDevice

class HIDConnectionEventInit(EventInit):
    device: HIDDevice

class HIDInputReportEvent(Event):
    @classmethod
    def new(cls, type: str, eventInitDict: HIDInputReportEventInit) -> HIDInputReportEvent: ...
    device: HIDDevice
    reportId: int
    data: DataView

class HIDInputReportEventInit(EventInit):
    device: HIDDevice
    reportId: int
    data: DataView

class HIDCollectionInfo(TypedDict):
    usagePage: NotRequired[int]
    usage: NotRequired[int]
    type: NotRequired[int]
    children: NotRequired[Sequence[HIDCollectionInfo]]
    inputReports: NotRequired[Sequence[HIDReportInfo]]
    outputReports: NotRequired[Sequence[HIDReportInfo]]
    featureReports: NotRequired[Sequence[HIDReportInfo]]

class HIDReportInfo(TypedDict):
    reportId: NotRequired[int]
    items: NotRequired[Sequence[HIDReportItem]]

class HIDReportItem(TypedDict):
    isAbsolute: NotRequired[bool]
    isArray: NotRequired[bool]
    isBufferedBytes: NotRequired[bool]
    isConstant: NotRequired[bool]
    isLinear: NotRequired[bool]
    isRange: NotRequired[bool]
    isVolatile: NotRequired[bool]
    hasNull: NotRequired[bool]
    hasPreferredState: NotRequired[bool]
    wrap: NotRequired[bool]
    usages: NotRequired[Sequence[int]]
    usageMinimum: NotRequired[int]
    usageMaximum: NotRequired[int]
    reportSize: NotRequired[int]
    reportCount: NotRequired[int]
    unitExponent: NotRequired[int]
    unitSystem: NotRequired[HIDUnitSystem]
    unitFactorLengthExponent: NotRequired[int]
    unitFactorMassExponent: NotRequired[int]
    unitFactorTimeExponent: NotRequired[int]
    unitFactorTemperatureExponent: NotRequired[int]
    unitFactorCurrentExponent: NotRequired[int]
    unitFactorLuminousIntensityExponent: NotRequired[int]
    logicalMinimum: NotRequired[int]
    logicalMaximum: NotRequired[int]
    physicalMinimum: NotRequired[int]
    physicalMaximum: NotRequired[int]
    strings: NotRequired[Sequence[str]]

class DOMException:
    @classmethod
    def new(cls, message: Union['str', 'None'] = "", name: Union['str', 'None'] = "Error") -> DOMException: ...
    name: str
    message: str
    code: int
    INDEX_SIZE_ERR = 1
    DOMSTRING_SIZE_ERR = 2
    HIERARCHY_REQUEST_ERR = 3
    WRONG_DOCUMENT_ERR = 4
    INVALID_CHARACTER_ERR = 5
    NO_DATA_ALLOWED_ERR = 6
    NO_MODIFICATION_ALLOWED_ERR = 7
    NOT_FOUND_ERR = 8
    NOT_SUPPORTED_ERR = 9
    INUSE_ATTRIBUTE_ERR = 10
    INVALID_STATE_ERR = 11
    SYNTAX_ERR = 12
    INVALID_MODIFICATION_ERR = 13
    NAMESPACE_ERR = 14
    INVALID_ACCESS_ERR = 15
    VALIDATION_ERR = 16
    TYPE_MISMATCH_ERR = 17
    SECURITY_ERR = 18
    NETWORK_ERR = 19
    ABORT_ERR = 20
    URL_MISMATCH_ERR = 21
    QUOTA_EXCEEDED_ERR = 22
    TIMEOUT_ERR = 23
    INVALID_NODE_TYPE_ERR = 24
    DATA_CLONE_ERR = 25

class MidiPermissionDescriptor(PermissionDescriptor):
    sysex: NotRequired[bool]

class MIDIOptions(TypedDict):
    sysex: NotRequired[bool]
    software: NotRequired[bool]

class MIDIInputMap: ...

class MIDIOutputMap: ...

class MIDIAccess(EventTarget):
    inputs: MIDIInputMap
    outputs: MIDIOutputMap
    onstatechange: EventHandler
    sysexEnabled: bool

class MIDIPort(EventTarget):
    id: str
    manufacturer: Union['str', 'None']
    name: Union['str', 'None']
    type: MIDIPortType
    version: Union['str', 'None']
    state: MIDIPortDeviceState
    connection: MIDIPortConnectionState
    onstatechange: EventHandler

    def open(self) -> Awaitable[MIDIPort]: ...

    def close(self) -> Awaitable[MIDIPort]: ...

class MIDIInput(MIDIPort):
    onmidimessage: EventHandler

class MIDIOutput(MIDIPort):

    def send(self, data: Sequence[int], timestamp: Union['DOMHighResTimeStamp', 'None'] = 0) -> None: ...

    def clear(self) -> None: ...

class MIDIMessageEvent(Event):
    @classmethod
    def new(cls, type: str, eventInitDict: Union['MIDIMessageEventInit', 'None'] = {}) -> MIDIMessageEvent: ...
    data: Uint8Array

class MIDIMessageEventInit(EventInit):
    data: NotRequired[Uint8Array]

class MIDIConnectionEvent(Event):
    @classmethod
    def new(cls, type: str, eventInitDict: Union['MIDIConnectionEventInit', 'None'] = {}) -> MIDIConnectionEvent: ...
    port: MIDIPort

class MIDIConnectionEventInit(EventInit):
    port: NotRequired[MIDIPort]

class NavigatorML:
    ml: ML

class MLContextOptions(TypedDict):
    deviceType: NotRequired[MLDeviceType]
    powerPreference: NotRequired[MLPowerPreference]

class ML:
    @overload
    def createContext(self, options: Union['MLContextOptions', 'None'] = {}) -> Awaitable[MLContext]: ...
    @overload
    def createContext(self, gpuDevice: GPUDevice) -> Awaitable[MLContext]: ...
    @overload
    def createContextSync(self, options: Union['MLContextOptions', 'None'] = {}) -> MLContext: ...
    @overload
    def createContextSync(self, gpuDevice: GPUDevice) -> MLContext: ...

class MLGraph: ...

class MLOperandDescriptor(TypedDict):
    type: MLOperandType
    dimensions: NotRequired[Sequence[int]]

class MLOperand: ...

class MLActivation: ...

class MLContext:

    def computeSync(self, graph: MLGraph, inputs: MLNamedArrayBufferViews, outputs: MLNamedArrayBufferViews) -> None: ...

    def compute(self, graph: MLGraph, inputs: MLNamedArrayBufferViews, outputs: MLNamedArrayBufferViews) -> Awaitable[MLComputeResult]: ...

    def createCommandEncoder(self) -> MLCommandEncoder: ...

class MLComputeResult(TypedDict):
    inputs: NotRequired[MLNamedArrayBufferViews]
    outputs: NotRequired[MLNamedArrayBufferViews]

class MLCommandEncoder:

    def initializeGraph(self, graph: MLGraph) -> None: ...

    def dispatch(self, graph: MLGraph, inputs: MLNamedGPUResources, outputs: MLNamedGPUResources) -> None: ...

    def finish(self, descriptor: Union['GPUCommandBufferDescriptor', 'None'] = {}) -> GPUCommandBuffer: ...

class MLBufferResourceView(TypedDict):
    resource: GPUBuffer
    offset: NotRequired[int]
    size: NotRequired[int]

class MLGraphBuilder:
    @classmethod
    def new(cls, context: MLContext) -> MLGraphBuilder: ...

    def input(self, name: str, descriptor: MLOperandDescriptor) -> MLOperand: ...
    @overload
    def constant(self, descriptor: MLOperandDescriptor, bufferView: MLBufferView) -> MLOperand: ...
    @overload
    def constant(self, value: float, type: Union['MLOperandType', 'None'] = "float32") -> MLOperand: ...

    def build(self, outputs: MLNamedOperands) -> Awaitable[MLGraph]: ...

    def buildSync(self, outputs: MLNamedOperands) -> MLGraph: ...

    def batchNormalization(self, input: MLOperand, mean: MLOperand, variance: MLOperand, options: Union['MLBatchNormalizationOptions', 'None'] = {}) -> MLOperand: ...
    @overload
    def clamp(self, x: MLOperand, options: Union['MLClampOptions', 'None'] = {}) -> MLOperand: ...
    @overload
    def clamp(self, options: Union['MLClampOptions', 'None'] = {}) -> MLActivation: ...

    def concat(self, inputs: Sequence[MLOperand], axis: int) -> MLOperand: ...

    def conv2d(self, input: MLOperand, filter: MLOperand, options: Union['MLConv2dOptions', 'None'] = {}) -> MLOperand: ...

    def convTranspose2d(self, input: MLOperand, filter: MLOperand, options: Union['MLConvTranspose2dOptions', 'None'] = {}) -> MLOperand: ...

    def add(self, a: MLOperand, b: MLOperand) -> MLOperand: ...

    def sub(self, a: MLOperand, b: MLOperand) -> MLOperand: ...

    def mul(self, a: MLOperand, b: MLOperand) -> MLOperand: ...

    def div(self, a: MLOperand, b: MLOperand) -> MLOperand: ...

    def max(self, a: MLOperand, b: MLOperand) -> MLOperand: ...

    def min(self, a: MLOperand, b: MLOperand) -> MLOperand: ...

    def pow(self, a: MLOperand, b: MLOperand) -> MLOperand: ...

    def abs(self, x: MLOperand) -> MLOperand: ...

    def ceil(self, x: MLOperand) -> MLOperand: ...

    def cos(self, x: MLOperand) -> MLOperand: ...

    def exp(self, x: MLOperand) -> MLOperand: ...

    def floor(self, x: MLOperand) -> MLOperand: ...

    def log(self, x: MLOperand) -> MLOperand: ...

    def neg(self, x: MLOperand) -> MLOperand: ...

    def sin(self, x: MLOperand) -> MLOperand: ...

    def tan(self, x: MLOperand) -> MLOperand: ...
    @overload
    def elu(self, x: MLOperand, options: Union['MLEluOptions', 'None'] = {}) -> MLOperand: ...
    @overload
    def elu(self, options: Union['MLEluOptions', 'None'] = {}) -> MLActivation: ...

    def gemm(self, a: MLOperand, b: MLOperand, options: Union['MLGemmOptions', 'None'] = {}) -> MLOperand: ...

    def gru(self, input: MLOperand, weight: MLOperand, recurrentWeight: MLOperand, steps: int, hiddenSize: int, options: Union['MLGruOptions', 'None'] = {}) -> Sequence[MLOperand]: ...

    def gruCell(self, input: MLOperand, weight: MLOperand, recurrentWeight: MLOperand, hiddenState: MLOperand, hiddenSize: int, options: Union['MLGruCellOptions', 'None'] = {}) -> MLOperand: ...
    @overload
    def hardSigmoid(self, x: MLOperand, options: Union['MLHardSigmoidOptions', 'None'] = {}) -> MLOperand: ...
    @overload
    def hardSigmoid(self, options: Union['MLHardSigmoidOptions', 'None'] = {}) -> MLActivation: ...
    @overload
    def hardSwish(self, x: MLOperand) -> MLOperand: ...
    @overload
    def hardSwish(self) -> MLActivation: ...

    def instanceNormalization(self, input: MLOperand, options: Union['MLInstanceNormalizationOptions', 'None'] = {}) -> MLOperand: ...
    @overload
    def leakyRelu(self, x: MLOperand, options: Union['MLLeakyReluOptions', 'None'] = {}) -> MLOperand: ...
    @overload
    def leakyRelu(self, options: Union['MLLeakyReluOptions', 'None'] = {}) -> MLActivation: ...
    @overload
    def linear(self, x: MLOperand, options: Union['MLLinearOptions', 'None'] = {}) -> MLOperand: ...
    @overload
    def linear(self, options: Union['MLLinearOptions', 'None'] = {}) -> MLActivation: ...

    def lstm(self, input: MLOperand, weight: MLOperand, recurrentWeight: MLOperand, steps: int, hiddenSize: int, options: Union['MLLstmOptions', 'None'] = {}) -> Sequence[MLOperand]: ...

    def lstmCell(self, input: MLOperand, weight: MLOperand, recurrentWeight: MLOperand, hiddenState: MLOperand, cellState: MLOperand, hiddenSize: int, options: Union['MLLstmCellOptions', 'None'] = {}) -> Sequence[MLOperand]: ...

    def matmul(self, a: MLOperand, b: MLOperand) -> MLOperand: ...

    def pad(self, input: MLOperand, beginningPadding: Sequence[int], endingPadding: Sequence[int], options: Union['MLPadOptions', 'None'] = {}) -> MLOperand: ...

    def averagePool2d(self, input: MLOperand, options: Union['MLPool2dOptions', 'None'] = {}) -> MLOperand: ...

    def l2Pool2d(self, input: MLOperand, options: Union['MLPool2dOptions', 'None'] = {}) -> MLOperand: ...

    def maxPool2d(self, input: MLOperand, options: Union['MLPool2dOptions', 'None'] = {}) -> MLOperand: ...

    def prelu(self, x: MLOperand, slope: MLOperand) -> MLOperand: ...

    def reduceL1(self, input: MLOperand, options: Union['MLReduceOptions', 'None'] = {}) -> MLOperand: ...

    def reduceL2(self, input: MLOperand, options: Union['MLReduceOptions', 'None'] = {}) -> MLOperand: ...

    def reduceLogSum(self, input: MLOperand, options: Union['MLReduceOptions', 'None'] = {}) -> MLOperand: ...

    def reduceLogSumExp(self, input: MLOperand, options: Union['MLReduceOptions', 'None'] = {}) -> MLOperand: ...

    def reduceMax(self, input: MLOperand, options: Union['MLReduceOptions', 'None'] = {}) -> MLOperand: ...

    def reduceMean(self, input: MLOperand, options: Union['MLReduceOptions', 'None'] = {}) -> MLOperand: ...

    def reduceMin(self, input: MLOperand, options: Union['MLReduceOptions', 'None'] = {}) -> MLOperand: ...

    def reduceProduct(self, input: MLOperand, options: Union['MLReduceOptions', 'None'] = {}) -> MLOperand: ...

    def reduceSum(self, input: MLOperand, options: Union['MLReduceOptions', 'None'] = {}) -> MLOperand: ...

    def reduceSumSquare(self, input: MLOperand, options: Union['MLReduceOptions', 'None'] = {}) -> MLOperand: ...
    @overload
    def relu(self, x: MLOperand) -> MLOperand: ...
    @overload
    def relu(self) -> MLActivation: ...

    def resample2d(self, input: MLOperand, options: Union['MLResample2dOptions', 'None'] = {}) -> MLOperand: ...

    def reshape(self, input: MLOperand, newShape: Sequence[Union['int', 'None']]) -> MLOperand: ...
    @overload
    def sigmoid(self, x: MLOperand) -> MLOperand: ...
    @overload
    def sigmoid(self) -> MLActivation: ...

    def slice(self, input: MLOperand, starts: Sequence[int], sizes: Sequence[int]) -> MLOperand: ...
    @overload
    def softmax(self, x: MLOperand) -> MLOperand: ...
    @overload
    def softmax(self) -> MLActivation: ...
    @overload
    def softplus(self, x: MLOperand, options: Union['MLSoftplusOptions', 'None'] = {}) -> MLOperand: ...
    @overload
    def softplus(self, options: Union['MLSoftplusOptions', 'None'] = {}) -> MLActivation: ...
    @overload
    def softsign(self, x: MLOperand) -> MLOperand: ...
    @overload
    def softsign(self) -> MLActivation: ...

    def split(self, input: MLOperand, splits: Union['int', 'Sequence[int]'], options: Union['MLSplitOptions', 'None'] = {}) -> Sequence[MLOperand]: ...

    def squeeze(self, input: MLOperand, options: Union['MLSqueezeOptions', 'None'] = {}) -> MLOperand: ...
    @overload
    def tanh(self, x: MLOperand) -> MLOperand: ...
    @overload
    def tanh(self) -> MLActivation: ...

    def transpose(self, input: MLOperand, options: Union['MLTransposeOptions', 'None'] = {}) -> MLOperand: ...

class MLBatchNormalizationOptions(TypedDict):
    scale: NotRequired[MLOperand]
    bias: NotRequired[MLOperand]
    axis: NotRequired[int]
    epsilon: NotRequired[float]
    activation: NotRequired[MLActivation]

class MLClampOptions(TypedDict):
    minValue: NotRequired[float]
    maxValue: NotRequired[float]

class MLConv2dOptions(TypedDict):
    padding: NotRequired[Sequence[int]]
    strides: NotRequired[Sequence[int]]
    dilations: NotRequired[Sequence[int]]
    autoPad: NotRequired[MLAutoPad]
    groups: NotRequired[int]
    inputLayout: NotRequired[MLInputOperandLayout]
    filterLayout: NotRequired[MLConv2dFilterOperandLayout]
    bias: NotRequired[MLOperand]
    activation: NotRequired[MLActivation]

class MLConvTranspose2dOptions(TypedDict):
    padding: NotRequired[Sequence[int]]
    strides: NotRequired[Sequence[int]]
    dilations: NotRequired[Sequence[int]]
    outputPadding: NotRequired[Sequence[int]]
    outputSizes: NotRequired[Sequence[int]]
    autoPad: NotRequired[MLAutoPad]
    groups: NotRequired[int]
    inputLayout: NotRequired[MLInputOperandLayout]
    filterLayout: NotRequired[MLConvTranspose2dFilterOperandLayout]
    bias: NotRequired[MLOperand]
    activation: NotRequired[MLActivation]

class MLEluOptions(TypedDict):
    alpha: NotRequired[float]

class MLGemmOptions(TypedDict):
    c: NotRequired[MLOperand]
    alpha: NotRequired[float]
    beta: NotRequired[float]
    aTranspose: NotRequired[bool]
    bTranspose: NotRequired[bool]

class MLGruOptions(TypedDict):
    bias: NotRequired[MLOperand]
    recurrentBias: NotRequired[MLOperand]
    initialHiddenState: NotRequired[MLOperand]
    resetAfter: NotRequired[bool]
    returnSequence: NotRequired[bool]
    direction: NotRequired[MLRecurrentNetworkDirection]
    layout: NotRequired[MLGruWeightLayout]
    activations: NotRequired[Sequence[MLActivation]]

class MLGruCellOptions(TypedDict):
    bias: NotRequired[MLOperand]
    recurrentBias: NotRequired[MLOperand]
    resetAfter: NotRequired[bool]
    layout: NotRequired[MLGruWeightLayout]
    activations: NotRequired[Sequence[MLActivation]]

class MLHardSigmoidOptions(TypedDict):
    alpha: NotRequired[float]
    beta: NotRequired[float]

class MLInstanceNormalizationOptions(TypedDict):
    scale: NotRequired[MLOperand]
    bias: NotRequired[MLOperand]
    epsilon: NotRequired[float]
    layout: NotRequired[MLInputOperandLayout]

class MLLeakyReluOptions(TypedDict):
    alpha: NotRequired[float]

class MLLinearOptions(TypedDict):
    alpha: NotRequired[float]
    beta: NotRequired[float]

class MLLstmOptions(TypedDict):
    bias: NotRequired[MLOperand]
    recurrentBias: NotRequired[MLOperand]
    peepholeWeight: NotRequired[MLOperand]
    initialHiddenState: NotRequired[MLOperand]
    initialCellState: NotRequired[MLOperand]
    returnSequence: NotRequired[bool]
    direction: NotRequired[MLRecurrentNetworkDirection]
    layout: NotRequired[MLLstmWeightLayout]
    activations: NotRequired[Sequence[MLActivation]]

class MLLstmCellOptions(TypedDict):
    bias: NotRequired[MLOperand]
    recurrentBias: NotRequired[MLOperand]
    peepholeWeight: NotRequired[MLOperand]
    layout: NotRequired[MLLstmWeightLayout]
    activations: NotRequired[Sequence[MLActivation]]

class MLPadOptions(TypedDict):
    mode: NotRequired[MLPaddingMode]
    value: NotRequired[float]

class MLPool2dOptions(TypedDict):
    windowDimensions: NotRequired[Sequence[int]]
    padding: NotRequired[Sequence[int]]
    strides: NotRequired[Sequence[int]]
    dilations: NotRequired[Sequence[int]]
    autoPad: NotRequired[MLAutoPad]
    layout: NotRequired[MLInputOperandLayout]
    roundingType: NotRequired[MLRoundingType]
    outputSizes: NotRequired[Sequence[int]]

class MLReduceOptions(TypedDict):
    axes: NotRequired[Sequence[int]]
    keepDimensions: NotRequired[bool]

class MLResample2dOptions(TypedDict):
    mode: NotRequired[MLInterpolationMode]
    scales: NotRequired[Sequence[float]]
    sizes: NotRequired[Sequence[int]]
    axes: NotRequired[Sequence[int]]

class MLSoftplusOptions(TypedDict):
    steepness: NotRequired[float]

class MLSplitOptions(TypedDict):
    axis: NotRequired[int]

class MLSqueezeOptions(TypedDict):
    axes: NotRequired[Sequence[int]]

class MLTransposeOptions(TypedDict):
    permutation: NotRequired[Sequence[int]]

class RTCRtpSender:
    transform: Union['RTCRtpTransform', 'None']

    def generateKeyFrame(self, rids: Union['Sequence[str]', 'None'] = None) -> Awaitable[None]: ...
    track: Union['MediaStreamTrack', 'None']
    transport: Union['RTCDtlsTransport', 'None']

    def setParameters(self, parameters: RTCRtpSendParameters, setParameterOptions: Union['RTCSetParameterOptions', 'None'] = {}) -> Awaitable[None]: ...

    def getParameters(self) -> RTCRtpSendParameters: ...

    def replaceTrack(self, withTrack: Union['MediaStreamTrack', 'None']) -> Awaitable[None]: ...

    def setStreams(self, *streams: MediaStream) -> None: ...

    def getStats(self) -> Awaitable[RTCStatsReport]: ...
    dtmf: Union['RTCDTMFSender', 'None']

class RTCRtpReceiver:
    transform: Union['RTCRtpTransform', 'None']
    track: MediaStreamTrack
    transport: Union['RTCDtlsTransport', 'None']

    def getParameters(self) -> RTCRtpReceiveParameters: ...

    def getContributingSources(self) -> Sequence[RTCRtpContributingSource]: ...

    def getSynchronizationSources(self) -> Sequence[RTCRtpSynchronizationSource]: ...

    def getStats(self) -> Awaitable[RTCStatsReport]: ...

class SFrameTransformOptions(TypedDict):
    role: NotRequired[SFrameTransformRole]

class SFrameTransform(EventTarget, GenericTransformStream):
    @classmethod
    def new(cls, options: Union['SFrameTransformOptions', 'None'] = {}) -> SFrameTransform: ...

    def setEncryptionKey(self, key: CryptoKey, keyID: Union['CryptoKeyID', 'None'] = None) -> Awaitable[None]: ...
    onerror: EventHandler

class SFrameTransformErrorEvent(Event):
    @classmethod
    def new(cls, type: str, eventInitDict: SFrameTransformErrorEventInit) -> SFrameTransformErrorEvent: ...
    errorType: SFrameTransformErrorEventType
    keyID: Union['CryptoKeyID', 'None']
    frame: Any

class SFrameTransformErrorEventInit(EventInit):
    errorType: SFrameTransformErrorEventType
    frame: Any
    keyID: NotRequired[Union['CryptoKeyID', 'None']]

class RTCEncodedVideoFrameMetadata(TypedDict):
    frameId: NotRequired[int]
    dependencies: NotRequired[Sequence[int]]
    width: NotRequired[int]
    height: NotRequired[int]
    spatialIndex: NotRequired[int]
    temporalIndex: NotRequired[int]
    synchronizationSource: NotRequired[int]
    payloadType: NotRequired[int]
    contributingSources: NotRequired[Sequence[int]]
    timestamp: NotRequired[int]

class RTCEncodedVideoFrame:
    type: RTCEncodedVideoFrameType
    timestamp: int
    data: ArrayBuffer

    def getMetadata(self) -> RTCEncodedVideoFrameMetadata: ...

class RTCEncodedAudioFrameMetadata(TypedDict):
    synchronizationSource: NotRequired[int]
    payloadType: NotRequired[int]
    contributingSources: NotRequired[Sequence[int]]
    sequenceNumber: NotRequired[int]

class RTCEncodedAudioFrame:
    timestamp: int
    data: ArrayBuffer

    def getMetadata(self) -> RTCEncodedAudioFrameMetadata: ...

class RTCTransformEvent(Event):
    transformer: RTCRtpScriptTransformer

class RTCRtpScriptTransformer:
    readable: ReadableStream
    writable: WritableStream
    options: Any

    def generateKeyFrame(self, rid: Union['str', 'None'] = None) -> Awaitable[int]: ...

    def sendKeyFrameRequest(self) -> Awaitable[None]: ...

class RTCRtpScriptTransform:
    @classmethod
    def new(cls, worker: Worker, options: Union['Any', 'None'] = None, transfer: Union['Sequence[object]', 'None'] = None) -> RTCRtpScriptTransform: ...

class RTCIceParameters(TypedDict):
    iceLite: NotRequired[bool]
    usernameFragment: NotRequired[str]
    password: NotRequired[str]

class RTCIceGatherOptions(TypedDict):
    gatherPolicy: NotRequired[RTCIceTransportPolicy]
    iceServers: NotRequired[Sequence[RTCIceServer]]

class RTCIceTransport(EventTarget):
    @classmethod
    def new(cls) -> RTCIceTransport: ...

    def gather(self, options: Union['RTCIceGatherOptions', 'None'] = {}) -> None: ...

    def start(self, remoteParameters: Union['RTCIceParameters', 'None'] = {}, role: Union['RTCIceRole', 'None'] = "controlled") -> None: ...

    def stop(self) -> None: ...

    def addRemoteCandidate(self, remoteCandidate: Union['RTCIceCandidateInit', 'None'] = {}) -> None: ...
    onerror: EventHandler
    onicecandidate: EventHandler
    role: RTCIceRole
    component: RTCIceComponent
    state: RTCIceTransportState
    gatheringState: RTCIceGathererState

    def getLocalCandidates(self) -> Sequence[RTCIceCandidate]: ...

    def getRemoteCandidates(self) -> Sequence[RTCIceCandidate]: ...

    def getSelectedCandidatePair(self) -> Union['RTCIceCandidatePair', 'None']: ...

    def getLocalParameters(self) -> Union['RTCIceParameters', 'None']: ...

    def getRemoteParameters(self) -> Union['RTCIceParameters', 'None']: ...
    onstatechange: EventHandler
    ongatheringstatechange: EventHandler
    onselectedcandidatepairchange: EventHandler

class RTCIdentityProviderGlobalScope(WorkerGlobalScope):
    rtcIdentityProvider: RTCIdentityProviderRegistrar

class RTCIdentityProviderRegistrar:

    def register(self, idp: RTCIdentityProvider) -> None: ...

class RTCIdentityProvider(TypedDict):
    generateAssertion: GenerateAssertionCallback
    validateAssertion: ValidateAssertionCallback

class RTCIdentityAssertionResult(TypedDict):
    idp: RTCIdentityProviderDetails
    assertion: str

class RTCIdentityProviderDetails(TypedDict):
    domain: str
    protocol: NotRequired[str]

class RTCIdentityValidationResult(TypedDict):
    identity: str
    contents: str

class RTCPeerConnection(EventTarget):
    @classmethod
    def new(cls, configuration: Union['RTCConfiguration', 'None'] = {}) -> RTCPeerConnection: ...

    def setIdentityProvider(self, provider: str, options: Union['RTCIdentityProviderOptions', 'None'] = {}) -> None: ...

    def getIdentityAssertion(self) -> Awaitable[str]: ...
    peerIdentity: Awaitable[RTCIdentityAssertion]
    idpLoginUrl: Union['str', 'None']
    idpErrorInfo: Union['str', 'None']
    @overload
    def createOffer(self, options: Union['RTCOfferOptions', 'None'] = {}) -> Awaitable[RTCSessionDescriptionInit]: ...
    @overload
    def createOffer(self, successCallback: RTCSessionDescriptionCallback, failureCallback: RTCPeerConnectionErrorCallback, options: Union['RTCOfferOptions', 'None'] = {}) -> Awaitable[None]: ...
    @overload
    def createAnswer(self, options: Union['RTCAnswerOptions', 'None'] = {}) -> Awaitable[RTCSessionDescriptionInit]: ...
    @overload
    def createAnswer(self, successCallback: RTCSessionDescriptionCallback, failureCallback: RTCPeerConnectionErrorCallback) -> Awaitable[None]: ...
    @overload
    def setLocalDescription(self, description: Union['RTCLocalSessionDescriptionInit', 'None'] = {}) -> Awaitable[None]: ...
    @overload
    def setLocalDescription(self, description: RTCLocalSessionDescriptionInit, successCallback: VoidFunction, failureCallback: RTCPeerConnectionErrorCallback) -> Awaitable[None]: ...
    localDescription: Union['RTCSessionDescription', 'None']
    currentLocalDescription: Union['RTCSessionDescription', 'None']
    pendingLocalDescription: Union['RTCSessionDescription', 'None']
    @overload
    def setRemoteDescription(self, description: RTCSessionDescriptionInit) -> Awaitable[None]: ...
    @overload
    def setRemoteDescription(self, description: RTCSessionDescriptionInit, successCallback: VoidFunction, failureCallback: RTCPeerConnectionErrorCallback) -> Awaitable[None]: ...
    remoteDescription: Union['RTCSessionDescription', 'None']
    currentRemoteDescription: Union['RTCSessionDescription', 'None']
    pendingRemoteDescription: Union['RTCSessionDescription', 'None']
    @overload
    def addIceCandidate(self, candidate: Union['RTCIceCandidateInit', 'None'] = {}) -> Awaitable[None]: ...
    @overload
    def addIceCandidate(self, candidate: RTCIceCandidateInit, successCallback: VoidFunction, failureCallback: RTCPeerConnectionErrorCallback) -> Awaitable[None]: ...
    signalingState: RTCSignalingState
    iceGatheringState: RTCIceGatheringState
    iceConnectionState: RTCIceConnectionState
    connectionState: RTCPeerConnectionState
    canTrickleIceCandidates: Union['bool', 'None']

    def restartIce(self) -> None: ...

    def getConfiguration(self) -> RTCConfiguration: ...

    def setConfiguration(self, configuration: Union['RTCConfiguration', 'None'] = {}) -> None: ...

    def close(self) -> None: ...
    onnegotiationneeded: EventHandler
    onicecandidate: EventHandler
    onicecandidateerror: EventHandler
    onsignalingstatechange: EventHandler
    oniceconnectionstatechange: EventHandler
    onicegatheringstatechange: EventHandler
    onconnectionstatechange: EventHandler

    def getSenders(self) -> Sequence[RTCRtpSender]: ...

    def getReceivers(self) -> Sequence[RTCRtpReceiver]: ...

    def getTransceivers(self) -> Sequence[RTCRtpTransceiver]: ...

    def addTrack(self, track: MediaStreamTrack, *streams: MediaStream) -> RTCRtpSender: ...

    def removeTrack(self, sender: RTCRtpSender) -> None: ...

    def addTransceiver(self, trackOrKind: Union['MediaStreamTrack', 'str'], init: Union['RTCRtpTransceiverInit', 'None'] = {}) -> RTCRtpTransceiver: ...
    ontrack: EventHandler
    sctp: Union['RTCSctpTransport', 'None']

    def createDataChannel(self, label: str, dataChannelDict: Union['RTCDataChannelInit', 'None'] = {}) -> RTCDataChannel: ...
    ondatachannel: EventHandler

    def getStats(self, selector: Union['MediaStreamTrack', 'None'] = None) -> Awaitable[RTCStatsReport]: ...

class RTCConfiguration(TypedDict):
    peerIdentity: NotRequired[str]
    iceServers: NotRequired[Sequence[RTCIceServer]]
    iceTransportPolicy: NotRequired[RTCIceTransportPolicy]
    bundlePolicy: NotRequired[RTCBundlePolicy]
    rtcpMuxPolicy: NotRequired[RTCRtcpMuxPolicy]
    certificates: NotRequired[Sequence[RTCCertificate]]
    iceCandidatePoolSize: NotRequired[int]

class RTCIdentityProviderOptions(TypedDict):
    protocol: NotRequired[str]
    usernameHint: NotRequired[str]
    peerIdentity: NotRequired[str]

class RTCIdentityAssertion:
    @classmethod
    def new(cls, idp: str, name: str) -> RTCIdentityAssertion: ...
    idp: str
    name: str

class RTCError(DOMException):
    @classmethod
    def new(cls, init: RTCErrorInit, message: Union['str', 'None'] = "") -> RTCError: ...
    httpRequestStatusCode: Union['int', 'None']
    errorDetail: RTCErrorDetailType
    sdpLineNumber: Union['int', 'None']
    sctpCauseCode: Union['int', 'None']
    receivedAlert: Union['int', 'None']
    sentAlert: Union['int', 'None']

class RTCErrorInit(TypedDict):
    httpRequestStatusCode: NotRequired[int]
    errorDetail: RTCErrorDetailType
    sdpLineNumber: NotRequired[int]
    sctpCauseCode: NotRequired[int]
    receivedAlert: NotRequired[int]
    sentAlert: NotRequired[int]

class RTCRtpEncodingParameters(TypedDict, RTCRtpCodingParameters):
    priority: NotRequired[RTCPriorityType]
    networkPriority: NotRequired[RTCPriorityType]
    scalabilityMode: NotRequired[str]
    active: NotRequired[bool]
    maxBitrate: NotRequired[int]
    maxFramerate: NotRequired[float]
    scaleResolutionDownBy: NotRequired[float]

class RTCDataChannel(EventTarget):
    priority: RTCPriorityType
    label: str
    ordered: bool
    maxPacketLifeTime: Union['int', 'None']
    maxRetransmits: Union['int', 'None']
    protocol: str
    negotiated: bool
    id: Union['int', 'None']
    readyState: RTCDataChannelState
    bufferedAmount: int
    bufferedAmountLowThreshold: int
    onopen: EventHandler
    onbufferedamountlow: EventHandler
    onerror: EventHandler
    onclosing: EventHandler
    onclose: EventHandler

    def close(self) -> None: ...
    onmessage: EventHandler
    binaryType: BinaryType
    @overload
    def send(self, data: str) -> None: ...
    @overload
    def send(self, data: Blob) -> None: ...
    @overload
    def send(self, data: ArrayBuffer) -> None: ...
    @overload
    def send(self, data: ArrayBufferView) -> None: ...

class RTCDataChannelInit(TypedDict):
    priority: NotRequired[RTCPriorityType]
    ordered: NotRequired[bool]
    maxPacketLifeTime: NotRequired[int]
    maxRetransmits: NotRequired[int]
    protocol: NotRequired[str]
    negotiated: NotRequired[bool]
    id: NotRequired[int]

class RTCRtpStreamStats(RTCStats):
    ssrc: int
    kind: str
    transportId: NotRequired[str]
    codecId: NotRequired[str]

class RTCCodecStats(RTCStats):
    payloadType: int
    transportId: str
    mimeType: str
    clockRate: NotRequired[int]
    channels: NotRequired[int]
    sdpFmtpLine: NotRequired[str]

class RTCReceivedRtpStreamStats(RTCRtpStreamStats):
    packetsReceived: NotRequired[int]
    packetsLost: NotRequired[int]
    jitter: NotRequired[float]

class RTCInboundRtpStreamStats(RTCReceivedRtpStreamStats):
    trackIdentifier: str
    mid: NotRequired[str]
    remoteId: NotRequired[str]
    framesDecoded: NotRequired[int]
    keyFramesDecoded: NotRequired[int]
    framesRendered: NotRequired[int]
    framesDropped: NotRequired[int]
    frameWidth: NotRequired[int]
    frameHeight: NotRequired[int]
    framesPerSecond: NotRequired[float]
    qpSum: NotRequired[int]
    totalDecodeTime: NotRequired[float]
    totalInterFrameDelay: NotRequired[float]
    totalSquaredInterFrameDelay: NotRequired[float]
    pauseCount: NotRequired[int]
    totalPausesDuration: NotRequired[float]
    freezeCount: NotRequired[int]
    totalFreezesDuration: NotRequired[float]
    lastPacketReceivedTimestamp: NotRequired[DOMHighResTimeStamp]
    headerBytesReceived: NotRequired[int]
    packetsDiscarded: NotRequired[int]
    fecBytesReceived: NotRequired[int]
    fecPacketsReceived: NotRequired[int]
    fecPacketsDiscarded: NotRequired[int]
    bytesReceived: NotRequired[int]
    nackCount: NotRequired[int]
    firCount: NotRequired[int]
    pliCount: NotRequired[int]
    totalProcessingDelay: NotRequired[float]
    estimatedPlayoutTimestamp: NotRequired[DOMHighResTimeStamp]
    jitterBufferDelay: NotRequired[float]
    jitterBufferTargetDelay: NotRequired[float]
    jitterBufferEmittedCount: NotRequired[int]
    jitterBufferMinimumDelay: NotRequired[float]
    totalSamplesReceived: NotRequired[int]
    concealedSamples: NotRequired[int]
    silentConcealedSamples: NotRequired[int]
    concealmentEvents: NotRequired[int]
    insertedSamplesForDeceleration: NotRequired[int]
    removedSamplesForAcceleration: NotRequired[int]
    audioLevel: NotRequired[float]
    totalAudioEnergy: NotRequired[float]
    totalSamplesDuration: NotRequired[float]
    framesReceived: NotRequired[int]
    decoderImplementation: NotRequired[str]
    playoutId: NotRequired[str]
    powerEfficientDecoder: NotRequired[bool]
    framesAssembledFromMultiplePackets: NotRequired[int]
    totalAssemblyTime: NotRequired[float]
    retransmittedPacketsReceived: NotRequired[int]
    retransmittedBytesReceived: NotRequired[int]
    rtxSsrc: NotRequired[int]
    fecSsrc: NotRequired[int]

class RTCRemoteInboundRtpStreamStats(RTCReceivedRtpStreamStats):
    localId: NotRequired[str]
    roundTripTime: NotRequired[float]
    totalRoundTripTime: NotRequired[float]
    fractionLost: NotRequired[float]
    roundTripTimeMeasurements: NotRequired[int]

class RTCSentRtpStreamStats(RTCRtpStreamStats):
    packetsSent: NotRequired[int]
    bytesSent: NotRequired[int]

class RTCOutboundRtpStreamStats(RTCSentRtpStreamStats):
    mid: NotRequired[str]
    mediaSourceId: NotRequired[str]
    remoteId: NotRequired[str]
    rid: NotRequired[str]
    headerBytesSent: NotRequired[int]
    retransmittedPacketsSent: NotRequired[int]
    retransmittedBytesSent: NotRequired[int]
    rtxSsrc: NotRequired[int]
    targetBitrate: NotRequired[float]
    totalEncodedBytesTarget: NotRequired[int]
    frameWidth: NotRequired[int]
    frameHeight: NotRequired[int]
    framesPerSecond: NotRequired[float]
    framesSent: NotRequired[int]
    hugeFramesSent: NotRequired[int]
    framesEncoded: NotRequired[int]
    keyFramesEncoded: NotRequired[int]
    qpSum: NotRequired[int]
    totalEncodeTime: NotRequired[float]
    totalPacketSendDelay: NotRequired[float]
    qualityLimitationReason: NotRequired[RTCQualityLimitationReason]
    qualityLimitationDurations: NotRequired[float]
    qualityLimitationResolutionChanges: NotRequired[int]
    nackCount: NotRequired[int]
    firCount: NotRequired[int]
    pliCount: NotRequired[int]
    encoderImplementation: NotRequired[str]
    powerEfficientEncoder: NotRequired[bool]
    active: NotRequired[bool]
    scalabilityMode: NotRequired[str]

class RTCRemoteOutboundRtpStreamStats(RTCSentRtpStreamStats):
    localId: NotRequired[str]
    remoteTimestamp: NotRequired[DOMHighResTimeStamp]
    reportsSent: NotRequired[int]
    roundTripTime: NotRequired[float]
    totalRoundTripTime: NotRequired[float]
    roundTripTimeMeasurements: NotRequired[int]

class RTCMediaSourceStats(RTCStats):
    trackIdentifier: str
    kind: str

class RTCAudioSourceStats(RTCMediaSourceStats):
    audioLevel: NotRequired[float]
    totalAudioEnergy: NotRequired[float]
    totalSamplesDuration: NotRequired[float]
    echoReturnLoss: NotRequired[float]
    echoReturnLossEnhancement: NotRequired[float]
    droppedSamplesDuration: NotRequired[float]
    droppedSamplesEvents: NotRequired[int]
    totalCaptureDelay: NotRequired[float]
    totalSamplesCaptured: NotRequired[int]

class RTCVideoSourceStats(RTCMediaSourceStats):
    width: NotRequired[int]
    height: NotRequired[int]
    frames: NotRequired[int]
    framesPerSecond: NotRequired[float]

class RTCAudioPlayoutStats(RTCStats):
    kind: str
    synthesizedSamplesDuration: NotRequired[float]
    synthesizedSamplesEvents: NotRequired[int]
    totalSamplesDuration: NotRequired[float]
    totalPlayoutDelay: NotRequired[float]
    totalSamplesCount: NotRequired[int]

class RTCPeerConnectionStats(RTCStats):
    dataChannelsOpened: NotRequired[int]
    dataChannelsClosed: NotRequired[int]

class RTCDataChannelStats(RTCStats):
    label: NotRequired[str]
    protocol: NotRequired[str]
    dataChannelIdentifier: NotRequired[int]
    state: RTCDataChannelState
    messagesSent: NotRequired[int]
    bytesSent: NotRequired[int]
    messagesReceived: NotRequired[int]
    bytesReceived: NotRequired[int]

class RTCTransportStats(RTCStats):
    packetsSent: NotRequired[int]
    packetsReceived: NotRequired[int]
    bytesSent: NotRequired[int]
    bytesReceived: NotRequired[int]
    iceRole: NotRequired[RTCIceRole]
    iceLocalUsernameFragment: NotRequired[str]
    dtlsState: RTCDtlsTransportState
    iceState: NotRequired[RTCIceTransportState]
    selectedCandidatePairId: NotRequired[str]
    localCertificateId: NotRequired[str]
    remoteCertificateId: NotRequired[str]
    tlsVersion: NotRequired[str]
    dtlsCipher: NotRequired[str]
    dtlsRole: NotRequired[RTCDtlsRole]
    srtpCipher: NotRequired[str]
    selectedCandidatePairChanges: NotRequired[int]

class RTCIceCandidateStats(RTCStats):
    transportId: str
    address: NotRequired[Union['str', 'None']]
    port: NotRequired[int]
    protocol: NotRequired[str]
    candidateType: RTCIceCandidateType
    priority: NotRequired[int]
    url: NotRequired[str]
    relayProtocol: NotRequired[RTCIceServerTransportProtocol]
    foundation: NotRequired[str]
    relatedAddress: NotRequired[str]
    relatedPort: NotRequired[int]
    usernameFragment: NotRequired[str]
    tcpType: NotRequired[RTCIceTcpCandidateType]

class RTCIceCandidatePairStats(RTCStats):
    transportId: str
    localCandidateId: str
    remoteCandidateId: str
    state: RTCStatsIceCandidatePairState
    nominated: NotRequired[bool]
    packetsSent: NotRequired[int]
    packetsReceived: NotRequired[int]
    bytesSent: NotRequired[int]
    bytesReceived: NotRequired[int]
    lastPacketSentTimestamp: NotRequired[DOMHighResTimeStamp]
    lastPacketReceivedTimestamp: NotRequired[DOMHighResTimeStamp]
    totalRoundTripTime: NotRequired[float]
    currentRoundTripTime: NotRequired[float]
    availableOutgoingBitrate: NotRequired[float]
    availableIncomingBitrate: NotRequired[float]
    requestsReceived: NotRequired[int]
    requestsSent: NotRequired[int]
    responsesReceived: NotRequired[int]
    responsesSent: NotRequired[int]
    consentRequestsSent: NotRequired[int]
    packetsDiscardedOnSend: NotRequired[int]
    bytesDiscardedOnSend: NotRequired[int]

class RTCCertificateStats(RTCStats):
    fingerprint: str
    fingerprintAlgorithm: str
    base64Certificate: str
    issuerCertificateId: NotRequired[str]

class RTCIceServer(TypedDict):
    urls: Union['str', 'Sequence[str]']
    username: NotRequired[str]
    credential: NotRequired[str]

class RTCOfferAnswerOptions(TypedDict): ...

class RTCOfferOptions(RTCOfferAnswerOptions, TypedDict):
    iceRestart: NotRequired[bool]
    offerToReceiveAudio: NotRequired[bool]
    offerToReceiveVideo: NotRequired[bool]

class RTCAnswerOptions(RTCOfferAnswerOptions): ...

class RTCSessionDescription:
    @classmethod
    def new(cls, descriptionInitDict: RTCSessionDescriptionInit) -> RTCSessionDescription: ...
    type: RTCSdpType
    sdp: str

    def toJSON(self) -> object: ...

class RTCSessionDescriptionInit(TypedDict):
    type: RTCSdpType
    sdp: NotRequired[str]

class RTCLocalSessionDescriptionInit(TypedDict):
    type: NotRequired[RTCSdpType]
    sdp: NotRequired[str]

class RTCIceCandidate:
    @classmethod
    def new(cls, candidateInitDict: Union['RTCIceCandidateInit', 'None'] = {}) -> RTCIceCandidate: ...
    candidate: str
    sdpMid: Union['str', 'None']
    sdpMLineIndex: Union['int', 'None']
    foundation: Union['str', 'None']
    component: Union['RTCIceComponent', 'None']
    priority: Union['int', 'None']
    address: Union['str', 'None']
    protocol: Union['RTCIceProtocol', 'None']
    port: Union['int', 'None']
    type: Union['RTCIceCandidateType', 'None']
    tcpType: Union['RTCIceTcpCandidateType', 'None']
    relatedAddress: Union['str', 'None']
    relatedPort: Union['int', 'None']
    usernameFragment: Union['str', 'None']
    relayProtocol: Union['RTCIceServerTransportProtocol', 'None']
    url: Union['str', 'None']

    def toJSON(self) -> RTCIceCandidateInit: ...

class RTCIceCandidateInit(TypedDict):
    candidate: NotRequired[str]
    sdpMid: NotRequired[Union['str', 'None']]
    sdpMLineIndex: NotRequired[Union['int', 'None']]
    usernameFragment: NotRequired[Union['str', 'None']]

class RTCPeerConnectionIceEvent(Event):
    @classmethod
    def new(cls, type: str, eventInitDict: Union['RTCPeerConnectionIceEventInit', 'None'] = {}) -> RTCPeerConnectionIceEvent: ...
    candidate: Union['RTCIceCandidate', 'None']
    url: Union['str', 'None']

class RTCPeerConnectionIceEventInit(EventInit):
    candidate: NotRequired[Union['RTCIceCandidate', 'None']]
    url: NotRequired[Union['str', 'None']]

class RTCPeerConnectionIceErrorEvent(Event):
    @classmethod
    def new(cls, type: str, eventInitDict: RTCPeerConnectionIceErrorEventInit) -> RTCPeerConnectionIceErrorEvent: ...
    address: Union['str', 'None']
    port: Union['int', 'None']
    url: str
    errorCode: int
    errorText: str

class RTCPeerConnectionIceErrorEventInit(EventInit):
    address: NotRequired[Union['str', 'None']]
    port: NotRequired[Union['int', 'None']]
    url: NotRequired[str]
    errorCode: int
    errorText: NotRequired[str]

class RTCCertificateExpiration(TypedDict):
    expires: NotRequired[int]

class RTCCertificate:
    expires: EpochTimeStamp

    def getFingerprints(self) -> Sequence[RTCDtlsFingerprint]: ...

class RTCRtpTransceiverInit(TypedDict):
    direction: NotRequired[RTCRtpTransceiverDirection]
    streams: NotRequired[Sequence[MediaStream]]
    sendEncodings: NotRequired[Sequence[RTCRtpEncodingParameters]]

class RTCRtpParameters(TypedDict):
    headerExtensions: Sequence[RTCRtpHeaderExtensionParameters]
    rtcp: RTCRtcpParameters
    codecs: Sequence[RTCRtpCodecParameters]

class RTCRtpReceiveParameters(RTCRtpParameters): ...

class RTCRtpCodingParameters(TypedDict):
    rid: NotRequired[str]

class RTCRtcpParameters(TypedDict):
    cname: NotRequired[str]
    reducedSize: NotRequired[bool]

class RTCRtpHeaderExtensionParameters(TypedDict):
    uri: str
    id: int
    encrypted: NotRequired[bool]

class RTCRtpCodec(TypedDict):
    mimeType: str
    clockRate: int
    channels: NotRequired[int]
    sdpFmtpLine: NotRequired[str]

class RTCRtpCodecParameters(RTCRtpCodec):
    payloadType: int

class RTCRtpCapabilities(TypedDict):
    codecs: Sequence[RTCRtpCodecCapability]
    headerExtensions: Sequence[RTCRtpHeaderExtensionCapability]

class RTCRtpCodecCapability(RTCRtpCodec): ...

class RTCRtpHeaderExtensionCapability(TypedDict):
    uri: str

class RTCSetParameterOptions(TypedDict): ...

class RTCRtpContributingSource(TypedDict):
    timestamp: DOMHighResTimeStamp
    source: int
    audioLevel: NotRequired[float]
    rtpTimestamp: int

class RTCRtpSynchronizationSource(RTCRtpContributingSource): ...

class RTCRtpTransceiver:
    mid: Union['str', 'None']
    sender: RTCRtpSender
    receiver: RTCRtpReceiver
    direction: RTCRtpTransceiverDirection
    currentDirection: Union['RTCRtpTransceiverDirection', 'None']

    def stop(self) -> None: ...

    def setCodecPreferences(self, codecs: Sequence[RTCRtpCodecCapability]) -> None: ...

class RTCDtlsTransport(EventTarget):
    iceTransport: RTCIceTransport
    state: RTCDtlsTransportState

    def getRemoteCertificates(self) -> Sequence[ArrayBuffer]: ...
    onstatechange: EventHandler
    onerror: EventHandler

class RTCDtlsFingerprint(TypedDict):
    algorithm: NotRequired[str]
    value: NotRequired[str]

class RTCIceCandidatePair(TypedDict):
    local: NotRequired[RTCIceCandidate]
    remote: NotRequired[RTCIceCandidate]

class RTCTrackEvent(Event):
    @classmethod
    def new(cls, type: str, eventInitDict: RTCTrackEventInit) -> RTCTrackEvent: ...
    receiver: RTCRtpReceiver
    track: MediaStreamTrack
    streams: Sequence[MediaStream]
    transceiver: RTCRtpTransceiver

class RTCTrackEventInit(EventInit):
    receiver: RTCRtpReceiver
    track: MediaStreamTrack
    streams: NotRequired[Sequence[MediaStream]]
    transceiver: RTCRtpTransceiver

class RTCSctpTransport(EventTarget):
    transport: RTCDtlsTransport
    state: RTCSctpTransportState
    maxMessageSize: float
    maxChannels: Union['int', 'None']
    onstatechange: EventHandler

class RTCDataChannelEvent(Event):
    @classmethod
    def new(cls, type: str, eventInitDict: RTCDataChannelEventInit) -> RTCDataChannelEvent: ...
    channel: RTCDataChannel

class RTCDataChannelEventInit(EventInit):
    channel: RTCDataChannel

class RTCDTMFSender(EventTarget):

    def insertDTMF(self, tones: str, duration: Union['int', 'None'] = 100, interToneGap: Union['int', 'None'] = 70) -> None: ...
    ontonechange: EventHandler
    canInsertDTMF: bool
    toneBuffer: str

class RTCDTMFToneChangeEvent(Event):
    @classmethod
    def new(cls, type: str, eventInitDict: Union['RTCDTMFToneChangeEventInit', 'None'] = {}) -> RTCDTMFToneChangeEvent: ...
    tone: str

class RTCDTMFToneChangeEventInit(EventInit):
    tone: NotRequired[str]

class RTCStatsReport: ...

class RTCStats(TypedDict):
    timestamp: DOMHighResTimeStamp
    type: RTCStatsType
    id: str

class RTCErrorEvent(Event):
    @classmethod
    def new(cls, type: str, eventInitDict: RTCErrorEventInit) -> RTCErrorEvent: ...
    error: RTCError

class RTCErrorEventInit(EventInit):
    error: RTCError

class WebSocket(EventTarget):
    @classmethod
    def new(cls, url: str, protocols: Union['str', 'Sequence[str]', 'None'] = []) -> WebSocket: ...
    url: str
    CONNECTING = 0
    OPEN = 1
    CLOSING = 2
    CLOSED = 3
    readyState: int
    bufferedAmount: int
    onopen: EventHandler
    onerror: EventHandler
    onclose: EventHandler
    extensions: str
    protocol: str

    def close(self, code: Union['int', 'None'] = None, reason: Union['str', 'None'] = None) -> None: ...
    onmessage: EventHandler
    binaryType: BinaryType

    def send(self, data: Union['BufferSource', 'Blob', 'str']) -> None: ...

class CloseEvent(Event):
    @classmethod
    def new(cls, type: str, eventInitDict: Union['CloseEventInit', 'None'] = {}) -> CloseEvent: ...
    wasClean: bool
    code: int
    reason: str

class CloseEventInit(EventInit):
    wasClean: NotRequired[bool]
    code: NotRequired[int]
    reason: NotRequired[str]

class WebTransportDatagramDuplexStream:
    readable: ReadableStream
    writable: WritableStream
    maxDatagramSize: int
    incomingMaxAge: float
    outgoingMaxAge: float
    incomingHighWaterMark: float
    outgoingHighWaterMark: float

class WebTransport:
    @classmethod
    def new(cls, url: str, options: Union['WebTransportOptions', 'None'] = {}) -> WebTransport: ...

    def getStats(self) -> Awaitable[WebTransportStats]: ...
    ready: Awaitable[None]
    reliability: WebTransportReliabilityMode
    congestionControl: WebTransportCongestionControl
    closed: Awaitable[WebTransportCloseInfo]
    draining: Awaitable[None]

    def close(self, closeInfo: Union['WebTransportCloseInfo', 'None'] = {}) -> None: ...
    datagrams: WebTransportDatagramDuplexStream

    def createBidirectionalStream(self, options: Union['WebTransportSendStreamOptions', 'None'] = {}) -> Awaitable[WebTransportBidirectionalStream]: ...
    incomingBidirectionalStreams: ReadableStream

    def createUnidirectionalStream(self, options: Union['WebTransportSendStreamOptions', 'None'] = {}) -> Awaitable[WebTransportSendStream]: ...
    incomingUnidirectionalStreams: ReadableStream

class WebTransportHash(TypedDict):
    algorithm: NotRequired[str]
    value: NotRequired[BufferSource]

class WebTransportOptions(TypedDict):
    allowPooling: NotRequired[bool]
    requireUnreliable: NotRequired[bool]
    serverCertificateHashes: NotRequired[Sequence[WebTransportHash]]
    congestionControl: NotRequired[WebTransportCongestionControl]

class WebTransportCloseInfo(TypedDict):
    closeCode: NotRequired[int]
    reason: NotRequired[str]

class WebTransportSendStreamOptions(TypedDict):
    sendOrder: NotRequired[Union['int', 'None']]

class WebTransportStats(TypedDict):
    timestamp: NotRequired[DOMHighResTimeStamp]
    bytesSent: NotRequired[int]
    packetsSent: NotRequired[int]
    packetsLost: NotRequired[int]
    numOutgoingStreamsCreated: NotRequired[int]
    numIncomingStreamsCreated: NotRequired[int]
    bytesReceived: NotRequired[int]
    packetsReceived: NotRequired[int]
    smoothedRtt: NotRequired[DOMHighResTimeStamp]
    rttVariation: NotRequired[DOMHighResTimeStamp]
    minRtt: NotRequired[DOMHighResTimeStamp]
    datagrams: NotRequired[WebTransportDatagramStats]
    estimatedSendRate: NotRequired[Union['int', 'None']]

class WebTransportDatagramStats(TypedDict):
    timestamp: NotRequired[DOMHighResTimeStamp]
    expiredOutgoing: NotRequired[int]
    droppedIncoming: NotRequired[int]
    lostOutgoing: NotRequired[int]

class WebTransportSendStream(WritableStream):
    sendOrder: Union['int', 'None']

    def getStats(self) -> Awaitable[WebTransportSendStreamStats]: ...

class WebTransportSendStreamStats(TypedDict):
    timestamp: NotRequired[DOMHighResTimeStamp]
    bytesWritten: NotRequired[int]
    bytesSent: NotRequired[int]
    bytesAcknowledged: NotRequired[int]

class WebTransportReceiveStream(ReadableStream):

    def getStats(self) -> Awaitable[WebTransportReceiveStreamStats]: ...

class WebTransportReceiveStreamStats(TypedDict):
    timestamp: NotRequired[DOMHighResTimeStamp]
    bytesReceived: NotRequired[int]
    bytesRead: NotRequired[int]

class WebTransportBidirectionalStream:
    readable: WebTransportReceiveStream
    writable: WebTransportSendStream

class WebTransportError(DOMException):
    @classmethod
    def new(cls, message: Union['str', 'None'] = "", options: Union['WebTransportErrorOptions', 'None'] = {}) -> WebTransportError: ...
    source: WebTransportErrorSource
    streamErrorCode: Union['int', 'None']

class WebTransportErrorOptions(TypedDict):
    source: NotRequired[WebTransportErrorSource]
    streamErrorCode: NotRequired[Union['int', 'None']]

class USBDeviceFilter(TypedDict):
    vendorId: NotRequired[int]
    productId: NotRequired[int]
    classCode: NotRequired[int]
    subclassCode: NotRequired[int]
    protocolCode: NotRequired[int]
    serialNumber: NotRequired[str]

class USBDeviceRequestOptions(TypedDict):
    filters: Sequence[USBDeviceFilter]
    exclusionFilters: NotRequired[Sequence[USBDeviceFilter]]

class USB(EventTarget):
    onconnect: EventHandler
    ondisconnect: EventHandler

    def getDevices(self) -> Awaitable[Sequence[USBDevice]]: ...

    def requestDevice(self, options: USBDeviceRequestOptions) -> Awaitable[USBDevice]: ...

class USBConnectionEventInit(EventInit):
    device: USBDevice

class USBConnectionEvent(Event):
    @classmethod
    def new(cls, type: str, eventInitDict: USBConnectionEventInit) -> USBConnectionEvent: ...
    device: USBDevice

class USBInTransferResult:
    @classmethod
    def new(cls, status: USBTransferStatus, data: Union['DataView', 'None'] = None) -> USBInTransferResult: ...
    data: DataView
    status: USBTransferStatus

class USBOutTransferResult:
    @classmethod
    def new(cls, status: USBTransferStatus, bytesWritten: Union['int', 'None'] = 0) -> USBOutTransferResult: ...
    bytesWritten: int
    status: USBTransferStatus

class USBIsochronousInTransferPacket:
    @classmethod
    def new(cls, status: USBTransferStatus, data: Union['DataView', 'None'] = None) -> USBIsochronousInTransferPacket: ...
    data: DataView
    status: USBTransferStatus

class USBIsochronousInTransferResult:
    @classmethod
    def new(cls, packets: Sequence[USBIsochronousInTransferPacket], data: Union['DataView', 'None'] = None) -> USBIsochronousInTransferResult: ...
    data: DataView
    packets: Sequence[USBIsochronousInTransferPacket]

class USBIsochronousOutTransferPacket:
    @classmethod
    def new(cls, status: USBTransferStatus, bytesWritten: Union['int', 'None'] = 0) -> USBIsochronousOutTransferPacket: ...
    bytesWritten: int
    status: USBTransferStatus

class USBIsochronousOutTransferResult:
    @classmethod
    def new(cls, packets: Sequence[USBIsochronousOutTransferPacket]) -> USBIsochronousOutTransferResult: ...
    packets: Sequence[USBIsochronousOutTransferPacket]

class USBDevice:
    usbVersionMajor: int
    usbVersionMinor: int
    usbVersionSubminor: int
    deviceClass: int
    deviceSubclass: int
    deviceProtocol: int
    vendorId: int
    productId: int
    deviceVersionMajor: int
    deviceVersionMinor: int
    deviceVersionSubminor: int
    manufacturerName: Union['str', 'None']
    productName: Union['str', 'None']
    serialNumber: Union['str', 'None']
    configuration: Union['USBConfiguration', 'None']
    configurations: Sequence[USBConfiguration]
    opened: bool

    def open(self) -> Awaitable[None]: ...

    def close(self) -> Awaitable[None]: ...

    def forget(self) -> Awaitable[None]: ...

    def selectConfiguration(self, configurationValue: int) -> Awaitable[None]: ...

    def claimInterface(self, interfaceNumber: int) -> Awaitable[None]: ...

    def releaseInterface(self, interfaceNumber: int) -> Awaitable[None]: ...

    def selectAlternateInterface(self, interfaceNumber: int, alternateSetting: int) -> Awaitable[None]: ...

    def controlTransferIn(self, setup: USBControlTransferParameters, length: int) -> Awaitable[USBInTransferResult]: ...

    def controlTransferOut(self, setup: USBControlTransferParameters, data: Union['BufferSource', 'None'] = None) -> Awaitable[USBOutTransferResult]: ...

    def clearHalt(self, direction: USBDirection, endpointNumber: int) -> Awaitable[None]: ...

    def transferIn(self, endpointNumber: int, length: int) -> Awaitable[USBInTransferResult]: ...

    def transferOut(self, endpointNumber: int, data: BufferSource) -> Awaitable[USBOutTransferResult]: ...

    def isochronousTransferIn(self, endpointNumber: int, packetLengths: Sequence[int]) -> Awaitable[USBIsochronousInTransferResult]: ...

    def isochronousTransferOut(self, endpointNumber: int, data: BufferSource, packetLengths: Sequence[int]) -> Awaitable[USBIsochronousOutTransferResult]: ...

    def reset(self) -> Awaitable[None]: ...

class USBControlTransferParameters(TypedDict):
    requestType: USBRequestType
    recipient: USBRecipient
    request: int
    value: int
    index: int

class USBConfiguration:
    @classmethod
    def new(cls, device: USBDevice, configurationValue: int) -> USBConfiguration: ...
    configurationValue: int
    configurationName: Union['str', 'None']
    interfaces: Sequence[USBInterface]

class USBInterface:
    @classmethod
    def new(cls, configuration: USBConfiguration, interfaceNumber: int) -> USBInterface: ...
    interfaceNumber: int
    alternate: USBAlternateInterface
    alternates: Sequence[USBAlternateInterface]
    claimed: bool

class USBAlternateInterface:
    @classmethod
    def new(cls, deviceInterface: USBInterface, alternateSetting: int) -> USBAlternateInterface: ...
    alternateSetting: int
    interfaceClass: int
    interfaceSubclass: int
    interfaceProtocol: int
    interfaceName: Union['str', 'None']
    endpoints: Sequence[USBEndpoint]

class USBEndpoint:
    @classmethod
    def new(cls, alternate: USBAlternateInterface, endpointNumber: int, direction: USBDirection) -> USBEndpoint: ...
    endpointNumber: int
    direction: USBDirection
    type: USBEndpointType
    packetSize: int

class USBPermissionDescriptor(PermissionDescriptor):
    filters: NotRequired[Sequence[USBDeviceFilter]]
    exclusionFilters: NotRequired[Sequence[USBDeviceFilter]]

class AllowedUSBDevice(TypedDict):
    vendorId: int
    productId: int
    serialNumber: NotRequired[str]

class USBPermissionStorage(TypedDict):
    allowedDevices: NotRequired[Sequence[AllowedUSBDevice]]

class USBPermissionResult(PermissionStatus):
    devices: Sequence[USBDevice]

class VTTCue(TextTrackCue):
    @classmethod
    def new(cls, startTime: float, endTime: float, text: str) -> VTTCue: ...
    region: Union['VTTRegion', 'None']
    vertical: DirectionSetting
    snapToLines: bool
    line: LineAndPositionSetting
    lineAlign: LineAlignSetting
    position: LineAndPositionSetting
    positionAlign: PositionAlignSetting
    size: float
    align: AlignSetting
    text: str

    def getCueAsHTML(self) -> DocumentFragment: ...

class VTTRegion:
    @classmethod
    def new(cls) -> VTTRegion: ...
    id: str
    width: float
    lines: int
    regionAnchorX: float
    regionAnchorY: float
    viewportAnchorX: float
    viewportAnchorY: float
    scroll: ScrollSetting

class XRDepthStateInit(TypedDict):
    usagePreference: Sequence[XRDepthUsage]
    dataFormatPreference: Sequence[XRDepthDataFormat]

class XRSessionInit(TypedDict):
    depthSensing: NotRequired[XRDepthStateInit]
    domOverlay: NotRequired[Union['XRDOMOverlayInit', 'None']]
    requiredFeatures: NotRequired[Sequence[str]]
    optionalFeatures: NotRequired[Sequence[str]]

class XRDepthInformation:
    width: int
    height: int
    normDepthBufferFromNormView: XRRigidTransform
    rawValueToMeters: float

class XRCPUDepthInformation(XRDepthInformation):
    data: ArrayBuffer

    def getDepthInMeters(self, x: float, y: float) -> float: ...

class XRWebGLDepthInformation(XRDepthInformation):
    texture: WebGLTexture

class XRDOMOverlayInit(TypedDict):
    root: Element

class XRDOMOverlayState(TypedDict):
    type: NotRequired[XRDOMOverlayType]

class XRInputSource:
    gamepad: Union['Gamepad', 'None']
    hand: Union['XRHand', 'None']
    handedness: XRHandedness
    targetRayMode: XRTargetRayMode
    targetRaySpace: XRSpace
    gripSpace: Union['XRSpace', 'None']
    profiles: Sequence[str]

class XRHand:
    size: int

    def get(self, key: XRHandJoint) -> XRJointSpace: ...

class XRJointSpace(XRSpace):
    jointName: XRHandJoint

class XRJointPose(XRPose):
    radius: float

class XRHitTestOptionsInit(TypedDict):
    space: XRSpace
    entityTypes: NotRequired[Sequence[XRHitTestTrackableType]]
    offsetRay: NotRequired[XRRay]

class XRTransientInputHitTestOptionsInit(TypedDict):
    profile: str
    entityTypes: NotRequired[Sequence[XRHitTestTrackableType]]
    offsetRay: NotRequired[XRRay]

class XRHitTestSource:

    def cancel(self) -> None: ...

class XRTransientInputHitTestSource:

    def cancel(self) -> None: ...

class XRTransientInputHitTestResult:
    inputSource: XRInputSource
    results: Sequence[XRHitTestResult]

class XRRayDirectionInit(TypedDict):
    x: NotRequired[float]
    y: NotRequired[float]
    z: NotRequired[float]
    w: NotRequired[float]

class XRRay:
    @overload
    @classmethod
    def new(cls, origin: Union['DOMPointInit', 'None'] = {}, direction: Union['XRRayDirectionInit', 'None'] = {}) -> XRRay: ...
    @overload
    @classmethod
    def new(cls, transform: XRRigidTransform) -> XRRay: ...
    origin: DOMPointReadOnly
    direction: DOMPointReadOnly
    matrix: Float32Array

class XRLightProbe(EventTarget):
    probeSpace: XRSpace
    onreflectionchange: EventHandler

class XRLightEstimate:
    sphericalHarmonicsCoefficients: Float32Array
    primaryLightDirection: DOMPointReadOnly
    primaryLightIntensity: DOMPointReadOnly

class XRLightProbeInit(TypedDict):
    reflectionFormat: NotRequired[XRReflectionFormat]

class XRSystem(EventTarget):

    def isSessionSupported(self, mode: XRSessionMode) -> Awaitable[bool]: ...

    def requestSession(self, mode: XRSessionMode, options: Union['XRSessionInit', 'None'] = {}) -> Awaitable[XRSession]: ...
    ondevicechange: EventHandler

class XRRenderStateInit(TypedDict):
    depthNear: NotRequired[float]
    depthFar: NotRequired[float]
    inlineVerticalFieldOfView: NotRequired[float]
    baseLayer: NotRequired[Union['XRWebGLLayer', 'None']]
    layers: NotRequired[Sequence[XRLayer]]

class XRRenderState:
    depthNear: float
    depthFar: float
    inlineVerticalFieldOfView: Union['float', 'None']
    baseLayer: Union['XRWebGLLayer', 'None']
    layers: Sequence[XRLayer]

class XRSpace(EventTarget): ...

class XRReferenceSpace(XRSpace):

    def getOffsetReferenceSpace(self, originOffset: XRRigidTransform) -> XRReferenceSpace: ...
    onreset: EventHandler

class XRBoundedReferenceSpace(XRReferenceSpace):
    boundsGeometry: Sequence[DOMPointReadOnly]

class XRViewport:
    x: int
    y: int
    width: int
    height: int

class XRRigidTransform:
    @classmethod
    def new(cls, position: Union['DOMPointInit', 'None'] = {}, orientation: Union['DOMPointInit', 'None'] = {}) -> XRRigidTransform: ...
    position: DOMPointReadOnly
    orientation: DOMPointReadOnly
    matrix: Float32Array
    inverse: XRRigidTransform

class XRPose:
    transform: XRRigidTransform
    linearVelocity: Union['DOMPointReadOnly', 'None']
    angularVelocity: Union['DOMPointReadOnly', 'None']
    emulatedPosition: bool

class XRViewerPose(XRPose):
    views: Sequence[XRView]

class XRInputSourceArray:
    length: int

    def __getter__(self, index: int) -> XRInputSource: ...

class XRLayer(EventTarget): ...

class XRWebGLLayerInit(TypedDict):
    antialias: NotRequired[bool]
    depth: NotRequired[bool]
    stencil: NotRequired[bool]
    alpha: NotRequired[bool]
    ignoreDepthValues: NotRequired[bool]
    framebufferScaleFactor: NotRequired[float]

class XRWebGLLayer(XRLayer):
    @classmethod
    def new(cls, session: XRSession, context: XRWebGLRenderingContext, layerInit: Union['XRWebGLLayerInit', 'None'] = {}) -> XRWebGLLayer: ...
    antialias: bool
    ignoreDepthValues: bool
    fixedFoveation: Union['float', 'None']
    framebuffer: Union['WebGLFramebuffer', 'None']
    framebufferWidth: int
    framebufferHeight: int

    def getViewport(self, view: XRView) -> Union['XRViewport', 'None']: ...

class XRSessionEvent(Event):
    @classmethod
    def new(cls, type: str, eventInitDict: XRSessionEventInit) -> XRSessionEvent: ...
    session: XRSession

class XRSessionEventInit(EventInit):
    session: XRSession

class XRInputSourceEvent(Event):
    @classmethod
    def new(cls, type: str, eventInitDict: XRInputSourceEventInit) -> XRInputSourceEvent: ...
    frame: XRFrame
    inputSource: XRInputSource

class XRInputSourceEventInit(EventInit):
    frame: XRFrame
    inputSource: XRInputSource

class XRInputSourcesChangeEvent(Event):
    @classmethod
    def new(cls, type: str, eventInitDict: XRInputSourcesChangeEventInit) -> XRInputSourcesChangeEvent: ...
    session: XRSession
    added: Sequence[XRInputSource]
    removed: Sequence[XRInputSource]

class XRInputSourcesChangeEventInit(EventInit):
    session: XRSession
    added: Sequence[XRInputSource]
    removed: Sequence[XRInputSource]

class XRReferenceSpaceEvent(Event):
    @classmethod
    def new(cls, type: str, eventInitDict: XRReferenceSpaceEventInit) -> XRReferenceSpaceEvent: ...
    referenceSpace: XRReferenceSpace
    transform: Union['XRRigidTransform', 'None']

class XRReferenceSpaceEventInit(EventInit):
    referenceSpace: XRReferenceSpace
    transform: NotRequired[Union['XRRigidTransform', 'None']]

class XRSessionSupportedPermissionDescriptor(PermissionDescriptor):
    mode: NotRequired[XRSessionMode]

class XRPermissionDescriptor(PermissionDescriptor):
    mode: NotRequired[XRSessionMode]
    requiredFeatures: NotRequired[Sequence[str]]
    optionalFeatures: NotRequired[Sequence[str]]

class XRPermissionStatus(PermissionStatus):
    granted: Sequence[str]

class XRCompositionLayer(XRLayer):
    layout: XRLayerLayout
    blendTextureSourceAlpha: bool
    forceMonoPresentation: bool
    opacity: float
    mipLevels: int
    quality: XRLayerQuality
    needsRedraw: bool

    def destroy(self) -> None: ...

class XRProjectionLayer(XRCompositionLayer):
    textureWidth: int
    textureHeight: int
    textureArrayLength: int
    ignoreDepthValues: bool
    fixedFoveation: Union['float', 'None']
    deltaPose: Union['XRRigidTransform', 'None']

class XRQuadLayer(XRCompositionLayer):
    space: XRSpace
    transform: XRRigidTransform
    width: float
    height: float
    onredraw: EventHandler

class XRCylinderLayer(XRCompositionLayer):
    space: XRSpace
    transform: XRRigidTransform
    radius: float
    centralAngle: float
    aspectRatio: float
    onredraw: EventHandler

class XREquirectLayer(XRCompositionLayer):
    space: XRSpace
    transform: XRRigidTransform
    radius: float
    centralHorizontalAngle: float
    upperVerticalAngle: float
    lowerVerticalAngle: float
    onredraw: EventHandler

class XRCubeLayer(XRCompositionLayer):
    space: XRSpace
    orientation: DOMPointReadOnly
    onredraw: EventHandler

class XRSubImage:
    viewport: XRViewport

class XRWebGLSubImage(XRSubImage):
    colorTexture: WebGLTexture
    depthStencilTexture: Union['WebGLTexture', 'None']
    motionVectorTexture: Union['WebGLTexture', 'None']
    imageIndex: Union['int', 'None']
    colorTextureWidth: int
    colorTextureHeight: int
    depthStencilTextureWidth: Union['int', 'None']
    depthStencilTextureHeight: Union['int', 'None']
    motionVectorTextureWidth: Union['int', 'None']
    motionVectorTextureHeight: Union['int', 'None']

class XRProjectionLayerInit(TypedDict):
    textureType: NotRequired[XRTextureType]
    colorFormat: NotRequired[GLenum]
    depthFormat: NotRequired[GLenum]
    scaleFactor: NotRequired[float]
    clearOnAccess: NotRequired[bool]

class XRLayerInit(TypedDict):
    space: XRSpace
    colorFormat: NotRequired[GLenum]
    depthFormat: NotRequired[Union['GLenum', 'None']]
    mipLevels: NotRequired[int]
    viewPixelWidth: int
    viewPixelHeight: int
    layout: NotRequired[XRLayerLayout]
    isStatic: NotRequired[bool]
    clearOnAccess: NotRequired[bool]

class XRQuadLayerInit(XRLayerInit):
    textureType: NotRequired[XRTextureType]
    transform: NotRequired[Union['XRRigidTransform', 'None']]
    width: NotRequired[float]
    height: NotRequired[float]

class XRCylinderLayerInit(XRLayerInit):
    textureType: NotRequired[XRTextureType]
    transform: NotRequired[Union['XRRigidTransform', 'None']]
    radius: NotRequired[float]
    centralAngle: NotRequired[float]
    aspectRatio: NotRequired[float]

class XREquirectLayerInit(XRLayerInit):
    textureType: NotRequired[XRTextureType]
    transform: NotRequired[Union['XRRigidTransform', 'None']]
    radius: NotRequired[float]
    centralHorizontalAngle: NotRequired[float]
    upperVerticalAngle: NotRequired[float]
    lowerVerticalAngle: NotRequired[float]

class XRCubeLayerInit(XRLayerInit):
    orientation: NotRequired[Union['DOMPointReadOnly', 'None']]

class XRMediaLayerInit(TypedDict):
    space: XRSpace
    layout: NotRequired[XRLayerLayout]
    invertStereo: NotRequired[bool]

class XRMediaQuadLayerInit(XRMediaLayerInit):
    transform: NotRequired[Union['XRRigidTransform', 'None']]
    width: NotRequired[Union['float', 'None']]
    height: NotRequired[Union['float', 'None']]

class XRMediaCylinderLayerInit(XRMediaLayerInit):
    transform: NotRequired[Union['XRRigidTransform', 'None']]
    radius: NotRequired[float]
    centralAngle: NotRequired[float]
    aspectRatio: NotRequired[Union['float', 'None']]

class XRMediaEquirectLayerInit(XRMediaLayerInit):
    transform: NotRequired[Union['XRRigidTransform', 'None']]
    radius: NotRequired[float]
    centralHorizontalAngle: NotRequired[float]
    upperVerticalAngle: NotRequired[float]
    lowerVerticalAngle: NotRequired[float]

class XRMediaBinding:
    @classmethod
    def new(cls, session: XRSession) -> XRMediaBinding: ...

    def createQuadLayer(self, video: HTMLVideoElement, init: Union['XRMediaQuadLayerInit', 'None'] = {}) -> XRQuadLayer: ...

    def createCylinderLayer(self, video: HTMLVideoElement, init: Union['XRMediaCylinderLayerInit', 'None'] = {}) -> XRCylinderLayer: ...

    def createEquirectLayer(self, video: HTMLVideoElement, init: Union['XRMediaEquirectLayerInit', 'None'] = {}) -> XREquirectLayer: ...

class XRLayerEvent(Event):
    @classmethod
    def new(cls, type: str, eventInitDict: XRLayerEventInit) -> XRLayerEvent: ...
    layer: XRLayer

class XRLayerEventInit(EventInit):
    layer: XRLayer

class WindowControlsOverlay(EventTarget):
    visible: bool

    def getTitlebarAreaRect(self) -> DOMRect: ...
    ongeometrychange: EventHandler

class WindowControlsOverlayGeometryChangeEvent(Event):
    @classmethod
    def new(cls, type: str, eventInitDict: WindowControlsOverlayGeometryChangeEventInit) -> WindowControlsOverlayGeometryChangeEvent: ...
    titlebarAreaRect: DOMRect
    visible: bool

class WindowControlsOverlayGeometryChangeEventInit(EventInit):
    titlebarAreaRect: DOMRect
    visible: NotRequired[bool]

class ScreenDetails(EventTarget):
    screens: Sequence[ScreenDetailed]
    currentScreen: ScreenDetailed
    onscreenschange: EventHandler
    oncurrentscreenchange: EventHandler

class ScreenDetailed(Screen):
    availLeft: int
    availTop: int
    left: int
    top: int
    isPrimary: bool
    isInternal: bool
    devicePixelRatio: float
    label: str

class XMLHttpRequestEventTarget(EventTarget):
    onloadstart: EventHandler
    onprogress: EventHandler
    onabort: EventHandler
    onerror: EventHandler
    onload: EventHandler
    ontimeout: EventHandler
    onloadend: EventHandler

class XMLHttpRequestUpload(XMLHttpRequestEventTarget): ...

class FormData:
    @classmethod
    def new(cls, form: Union['HTMLFormElement', 'None'] = None, submitter: Union['HTMLElement', 'None'] = None) -> FormData: ...
    @overload
    def append(self, name: str, value: str) -> None: ...
    @overload
    def append(self, name: str, blobValue: Blob, filename: Union['str', 'None'] = None) -> None: ...

    def delete(self, name: str) -> None: ...

    def get(self, name: str) -> Union['FormDataEntryValue', 'None']: ...

    def getAll(self, name: str) -> Sequence[FormDataEntryValue]: ...

    def has(self, name: str) -> bool: ...
    @overload
    def set(self, name: str, value: str) -> None: ...
    @overload
    def set(self, name: str, blobValue: Blob, filename: Union['str', 'None'] = None) -> None: ...

class ProgressEvent(Event):
    @classmethod
    def new(cls, type: str, eventInitDict: Union['ProgressEventInit', 'None'] = {}) -> ProgressEvent: ...
    lengthComputable: bool
    loaded: int
    total: int

class ProgressEventInit(EventInit):
    lengthComputable: NotRequired[bool]
    loaded: NotRequired[int]
    total: NotRequired[int]



document: Document
window: Window
navigator: Navigator
console: ConsoleNamespace
WindowProxy: TypeAlias = Window
