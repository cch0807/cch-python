# 1. typing.Callable[..., ReturnType]
# 함수를 인자로 받는 경우에 Callable 타입을 활용.

from typing import Callable


def on_some_event_happened(callback: Callable[[int, str, str]], int) -> None:
    pass


def do_this(a: int, b: str, c: str) -> int:
    pass


# 콜백 함수의 인자를 신경 쓰지 않고, 리턴 타입만을 명시해주고 싶은 경우가 있다.
# 그럴 때는 해당 타입의 인자 자리에 ... (Ellipsis) 를 넣어주면 된다.


def calculate(fn: Callable[..., float], *args: float) -> float:
    return fn(args)


def multiply(*args: float) -> float:
    v = 1
    for arg in args:
        v *= arg
    return v


def sum(*args: float) -> float:
    v = 0
    for arg in args:
        v += arg
    return v


# 2. typing.TypeVar
# 여러 타입을 일반화한 것을 제네릭 타입이라고 한다.
# typing.TypeVar 을 사용하면 제네릭 타입을 나타낼 수 있다.

from typing import Sequence, TypeVar, Iterable

T = TypeVar("T")  # T 대신 다른 문자/단어를 써도 되지만 일반적으로 T를 사용한다.


def batch_iter(data: Sequence[T], size: int) -> Iterable[Sequence[T]]:
    # Sequence 타입의 data를 주어진 data를 size 만큼 잘라서 iterate 하는 함수.
    # 제네릭 타입을 사용하기 때문에, Sequence[int]. Sequence[str], Sequence[Person] 등 T 자리에 어떤 타입도 올 수 있다.
    for i in range(0, len(data), size):
        yield data[i : i + size]


# TypeVar 를 선언할 때 bound를 명시하면 타입을 제한할 수도 있다.
from typing import Union

T = TypeVar("T", bound=Union[int, str, bytes])


def batch_iter(data: Sequence[T], size: int) -> Iterable[Sequence[T]]:
    # 이 함수의 경우에는 T로 대체될 수 있는 타입이 int, str, bytes 또는 해당 타입을 상속한 타입으로 제한된다.
    for i in range(0, len(data, size)):
        yield data[i : i + size]


# 3. typing.Generic
# TypeVar를 사용하면 함수 내에서 제네릭 타입의 의존관계를 나타낼 수 있다.
# 하지만 클래스를 선언할 때 타입이 결정되는 제네릭 클래스를 표현하기에는 부족하다.
# 이 경우에는 typing.Generic 와 typing.TypeVar를 함께 이용하면 된다.

from typing import Generic
from logging import Logger

T = TypeVar("T")


class LoggedVar(Generic[T]):
    def __init__(self, value: T, name: str, logger: Logger) -> None:
        self.name = name
        self.logger = logger
        self.value = value

    def set(self, new: T) -> None:
        self.log("Set" + repr(self.value))
        self.value = new

    def get(self) -> T:
        self.log("Get", repr(self.value))
        return self.value
