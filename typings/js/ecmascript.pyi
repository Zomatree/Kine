from typing import Callable, ClassVar, Generic, Iterator, TypeVar, TypedDict, NotRequired, overload, Any, Self

T = TypeVar("T")

globalThis: Any
Infinity: float
NaN: float
undefined: None

def eval(script: str) -> Any: ...
def isFinite(testValue: Any) -> bool: ...

class Object:
    def __init__(self, value: Any) -> None: ...

    prototype: type[Self]
    def hasOwnProperty(self, prop: str) -> bool: ...
    def isPrototypeOf(self, object: Any) -> bool: ...
    def propertyIsEnumerable(self, object: str) -> bool: ...
    def toLocaleString(self) -> str: ...
    def toString(self) -> str: ...
    def valueOf(self) -> Any: ...

class Function(Object):
    @overload
    def __init__(self, functionBody: str) -> None: ...
    @overload
    def __init__(self, arg0: str, functionBody: str) -> None: ...
    @overload
    def __init__(self, arg0: str, arg1: str, functionBody: str) -> None: ...
    @overload
    def __init__(self, arg0: str, arg1: str, arg2: str, functionBody: str) -> None: ...
    @overload
    def __init__(self, arg0: str, arg1: str, arg2: str, arg3: str, functionBody: str) -> None: ...
    @overload
    def __init__(self, arg0: str, arg1: str, arg2: str, arg3: str, arg4: str, functionBody: str) -> None: ...
    @overload
    def __init__(self, arg0: str, arg1: str, arg2: str, arg3: str, arg4: str, arg5: str, functionBody: str) -> None: ...
    @overload
    def __init__(self, arg0: str, arg1: str, arg2: str, arg3: str, arg4: str, arg5: str, arg6: str, functionBody: str) -> None: ...
    @overload
    def __init__(self, arg0: str, arg1: str, arg2: str, arg3: str, arg4: str, arg5: str, arg6: str, arg7: str, functionBody: str) -> None: ...

    constructor: ClassVar[Function]
    length: ClassVar[int]
    name: ClassVar[str]

    @overload
    def apply(self, thisArg: Any) -> Any: ...
    @overload
    def apply(self, argsArray: list[Any]) -> Any: ...

    def bind(self, thisArg: Any, *args: Any) -> Function: ...
    def call(self, thisArg: Any, *args: Any) -> Any: ...

    def __call__(self, *args: Any) -> Any:
        ...

class Boolean(Function):
    def __init__(self, value: Any) -> None: ...

class Symbol(Function):
    @overload
    def __init__(self) -> None: ...
    @overload
    def __init__(self, description: str) -> None: ...

    description: str | None

class ArrayBufferOptions(TypedDict):
    maxByteLength: NotRequired[int]


class Error(Function):
    cause: str
    message: str

class ArrayBuffer(Function):
    @overload
    def __init__(self, length: int) -> None: ...
    @overload
    def __init__(self, length: int, options: ArrayBufferOptions) -> None: ...

    byteLength: int
    maxByteLength: int
    resizable: bool

    @classmethod
    def isView(cls, value: Any) -> bool: ...
    def resize(self, newLength: int) -> None: ...
    @overload
    def slice(self, begin: int) -> Self: ...
    @overload
    def slice(self, begin: int, end: int) -> Self: ...

class AsyncValue(Object):
    done: bool
    value: Any

class AsyncGenerator(Function):
    @overload
    def next(self) -> Promise[AsyncValue]: ...
    @overload
    def next(self, value: Any) -> Promise[AsyncValue]: ...

    def _return(self, value: Any) -> Promise[AsyncValue]: ...
    def throw(self, exception: Any) -> Promise[AsyncValue]: ...

class Promise(Function, Generic[T]):
    @staticmethod
    def all(iterable: Iterator[Promise[T]]) -> Promise[T]: ...
    @staticmethod
    def allSettled(iterable: Iterator[Promise[T]]) -> Promise[T]: ...
    @staticmethod
    def any(iterable: Iterator[Promise[T]]) -> Promise[T]: ...
    @staticmethod
    def race(iterable: Iterator[Promise[T]]) -> Promise[T]: ...
    @staticmethod
    def reject(reason: Any) -> Promise[T]: ...
    @staticmethod
    def resolve(reason: Any) -> Promise[T]: ...

    def catch(self, onRejected: Callable[[Any], None]) -> Self: ...
    def _finally(self, onFinally: Callable[[], None]) -> Self: ...
    @overload
    def then(self, onFulfilled: Callable[[T], Any]) -> Self: ...
    @overload
    def then(self, onFulfilled: Callable[[T], Any], onRejected: Callable[[T], Any]) -> Self: ...

class TypedArray:
    BYTES_PER_ELEMENT: ClassVar[int]

    length: int

    def at(self, index: int) -> int | None: ...
    @overload
    def copyWithin(self, target: int, start: int) -> Self: ...
    @overload
    def copyWithin(self, target: int, start: int, end: int) -> Self: ...
    def entries(self) -> Iterator[int]: ...
    @overload
    def every(self, callbackFn: Callable[[int], bool] | Callable[[int, int], bool] | Callable[[int, int, Self], bool]) -> bool: ...
    @overload
    def every(self, callbackFn: Callable[[int], bool] | Callable[[int, int], bool] | Callable[[int, int, Self], bool], thisArg: Any) -> bool: ...
    @overload
    def fill(self, value: int) -> Self: ...
    @overload
    def fill(self, value: int, start: int) -> Self: ...
    @overload
    def fill(self, value: int, start: int, end: int) -> Self: ...
    @overload
    def filter(self, callbackFn: Callable[[int], bool] | Callable[[int, int], bool] | Callable[[int, int, Self], bool]) -> bool: ...
    @overload
    def filter(self, callbackFn: Callable[[int], bool] | Callable[[int, int], bool] | Callable[[int, int, Self], bool], thisArg: Any) -> bool: ...
    @overload
    def find(self, callbackFn: Callable[[int], bool] | Callable[[int, int], bool] | Callable[[int, int, Self], bool]) -> int | None: ...
    @overload
    def find(self, callbackFn: Callable[[int], bool] | Callable[[int, int], bool] | Callable[[int, int, Self], bool], thisArg: Any) -> int | None: ...
    @overload
    def findIndex(self, callbackFn: Callable[[int], bool] | Callable[[int, int], bool] | Callable[[int, int, Self], bool]) -> int: ...
    @overload
    def findIndex(self, callbackFn: Callable[[int], bool] | Callable[[int, int], bool] | Callable[[int, int, Self], bool], thisArg: Any) -> int: ...
    @overload
    def findLast(self, callbackFn: Callable[[int], bool] | Callable[[int, int], bool] | Callable[[int, int, Self], bool]) -> int | None: ...
    @overload
    def findLast(self, callbackFn: Callable[[int], bool] | Callable[[int, int], bool] | Callable[[int, int, Self], bool], thisArg: Any) -> int | None: ...
    @overload
    def findLastIndex(self, callbackFn: Callable[[int], bool] | Callable[[int, int], bool] | Callable[[int, int, Self], bool]) -> int: ...
    @overload
    def findLastIndex(self, callbackFn: Callable[[int], bool] | Callable[[int, int], bool] | Callable[[int, int, Self], bool], thisArg: Any) -> int: ...
    @overload
    def forEach(self, callbackFn: Callable[[int], bool] | Callable[[int, int], bool] | Callable[[int, int, Self], bool]) -> None: ...
    @overload
    def forEach(self, callbackFn: Callable[[int], bool] | Callable[[int, int], bool] | Callable[[int, int, Self], bool], thisArg: Any) -> None: ...
    @classmethod
    def _from(cls, arrayLike: Iterator[T], mapFn: Callable[[T], Any] | Callable[[T, int], Any]) -> Self: ...
    @overload
    def includes(self, searchElement: int) -> bool: ...
    @overload
    def includes(self, searchElement: int, fromIndex: int) -> bool: ...
    @overload
    def indexOf(self, searchElement: int) -> int: ...
    @overload
    def indexOf(self, searchElement: int, fromIndex: int) -> int: ...
    @overload
    def join(self) -> str: ...
    @overload
    def join(self, seperator: str) -> str: ...
    def keys(self) -> Iterator[int]: ...
    @overload
    def lastIndexOf(self, searchElement: int) -> int: ...
    @overload
    def lastIndexOf(self, searchElement: int, fromIndex: int) -> int: ...
    @overload
    def map(self, callbackFn: Callable[[int], bool] | Callable[[int, int], int] | Callable[[int, int, Self], int]) -> Self: ...
    @overload
    def map(self, callbackFn: Callable[[int], bool] | Callable[[int, int], bool] | Callable[[int, int, Self], bool], thisArg: Any) -> Self: ...
    @classmethod
    def _of(cls, *elements: Any) -> Self: ...
    @overload
    def reduce(self, callbackFn: Callable[[Any], Any] | Callable[[Any, int], Any] | Callable[[Any, int, int], Any] | Callable[[Any, int, int, Self], Any]) -> int: ...
    @overload
    def reduce(self, callbackFn: Callable[[Any], Any] | Callable[[Any, int], Any] | Callable[[Any, int, int], Any] | Callable[[Any, int, int, Self], Any], initialValue: Any) -> int: ...
    @overload
    def reduceRight(self, callbackFn: Callable[[Any], Any] | Callable[[Any, int], Any] | Callable[[Any, int, int], Any] | Callable[[Any, int, int, Self], Any]) -> int: ...
    @overload
    def reduceRight(self, callbackFn: Callable[[Any], Any] | Callable[[Any, int], Any] | Callable[[Any, int, int], Any] | Callable[[Any, int, int, Self], Any], initialValue: Any) -> int: ...
    def reverse(self) -> None: ...
    @overload
    def set(self, array: list[int] | Self) -> None: ...
    @overload
    def set(self, array: list[int] | Self, targetOffset: int) -> None: ...
    @overload
    def slice(self) -> Self: ...
    @overload
    def slice(self, start: int) -> Self: ...
    @overload
    def slice(self, start: int, end: int) -> Self: ...
    @overload
    def some(self, callbackFn: Callable[[int], bool] | Callable[[int, int], bool] | Callable[[int, int, Self], bool]) -> bool: ...
    @overload
    def some(self, callbackFn: Callable[[int], bool] | Callable[[int, int], bool] | Callable[[int, int, Self], bool], thisArg: Any) -> bool: ...
    @overload
    def sort(self) -> Self: ...
    @overload
    def sort(self, compareFn: Callable[[int, int], int]) -> Self: ...
    @overload
    def subarray(self) -> Self: ...
    @overload
    def subarray(self, begin: int) -> Self: ...
    @overload
    def subarray(self, begin: int, end: int) -> Self: ...
    def toReversed(self) -> Self: ...
    @overload
    def toSorted(self) -> Self: ...
    @overload
    def toSorted(self, compareFn: Callable[[int, int], int]) -> Self: ...
    def values(self) -> Iterator[int]: ...
    def _with(self, index: int, value: int) -> Self: ...

class Int8Array(TypedArray):
    pass

class Uint8Array(TypedArray):
    pass

class Uint8ClampedArray(TypedArray):
    pass

class Int16Array(TypedArray):
    pass

class Uint16Array(TypedArray):
    pass

class Int32Array(TypedArray):
    pass

class Uint32Array(TypedArray):
    pass

class Float32Array(TypedArray):
    pass

class Float64Array(TypedArray):
    pass

class BigInt64Array(TypedArray):
    pass

class BigUint64Array(TypedArray):
    pass

class Atomics(Object):
    @staticmethod
    def add(typedArray: TypedArray, index: int, value: int) -> int: ...
    @staticmethod
    def _and(typedArray: TypedArray, index: int, value: int) -> int: ...
    @staticmethod
    def compareExchange(typedArray: TypedArray, index: int, expectedValue: int, replacementValue: int) -> int: ...
    @staticmethod
    def exchange(typedArray: TypedArray, index: int, value: int) -> int: ...