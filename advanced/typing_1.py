# Typing 기초
# python 3.5 버전 이후부터는 아래와 같이 변수나 함수의 인자, 리턴 값에 타입을 명시할 수 있다.
# 변수나 인자의 경우 변수: <타입> 으로 명시할 수 있고
# 함수의 응답 값은 : 전에 -> <타입> 을 붙여주면 된다.

# a는 int 타입을 가지고 있다.
a: int = 3

# process_message 함수는 str 타입의 msg를 인자로 받아서 str타입을 리턴한다.
def process_message(msg: str) -> str:
    return msg.strip()


# 기초 타입 8가지

# 1. typing.Union
# 하나의 함수의 인자에 여러 타입이 사용될 수 있을 때 typing.Union을 사용.

from typing import Union


def process_message(msg: Union[str, bytes, None]) -> str:
    # str 또는 bytes 타입 혹은 None 값을 인자로 받는다.
    pass


# 2. typing.Optional
# Union[<타입>, None]은 Optional 로 대체할 수 있디.

from typing import Optional


def eat_food(food: Optional[str]) -> None:
    # food의 인자로 str타입 또는 None 값을 받는다.
    pass


# 3. typing.List, typing,Tuple, typing.Dcit
# 리스트(배열) -> typing.List[<type>]
# 튜플의 > typing.Tuple[<type>, <type>]
# 딕셔너리 -> typing.Dict[<key type>, <value type>]

from typing import List, Tuple, Dict

names: List[str]
location: Tuple[int, int, int]
count_map: Dict[str, int]

# 4. typing.TypedDict
# 딕셔너리의 경우 벨류의 타입이 하나로 고정되지 않는다.
# 이럴 때는 TypedDict를 활용할 수 있다.
# TypedDict 를 상속받은 클래스를 만든 다음 키와 벨류의 타입을 매칭시키면 된다.

from typing import TypedDict


class Person(TypedDict):
    name: str
    age: int
    gender: str


def calc_cost(person: Person) -> float:
    pass


# 아래와 같이 사용할 수도 있다.

from typing import TypedDict

Person = TypedDict("Person", name=str, age=int, gender=str)
Person = TypedDict("Person", {"name": str, "age": int, "gender": str})

# 5. typing.Generator, typing.Iterable, typing.Iterator
# 제네레이터 -> Generator[YieldType, SendType, ReturnType]

from typing import Generator


def echo_round() -> Generator[int, float, str]:
    sent = yield 0
    while sent >= 0:
        sent = yield round(sent)
    return "Done"


# echo_round 함수는 float타입을 이볅받아서 int 타입을 yield 하는 제네레이터이다.
# 음수 값을 받았을 때는 StopIteration 예외와 함께 해당 예외의 값으로 str 타입을 리턴한다.

# 제네레이터는 입력(Send) 값과 리턴 값이 있는 경우보다 yield만 하는 경우가 많다.
# 이런 경우에는 Generator[YieldType, None, None] 으로 명시할 수 있다.
# typing.Iterable[YieldType] 또는 typing:Iterator[YieldType] 사용가능

from typing import Iterator


def random_generator(val: int) -> Iterator[float]:
    for i in range(val):
        yield i


# 6. typing.Callable
# 함수를 인자로 가지는 경우 Callable[[Arg1Type, Arg2Type], ReturnType] 타입을 활용.

from typing import Callable


def on_some_event_happened(callback: Callable[[int, str, str], int]) -> None:
    pass


def do_this(a: int, b: str, c: str) -> int:
    pass


on_some_event_happened(do_this)

# Callable한 객체 역시 사용 가능

# 7. typing.Type
# 일반적으로 클래스의 객체는 해당 타입을 그냥 명시하면 된다.
class Transaction:
    pass


def process_txn(txn: Transaction):
    pass


# 하지만 클래스 그 자체를 인자로 받을 경우에는 typing.Type[Class명]을 사용.

from typing import Type


class Factory:
    pass


class AFactory(Factory):
    pass


class BFactory(Factory):
    pass


def initiate_factory(factory: Type[Factory]):
    pass


# 8. typing.Any
# 어떤 타입이든 관계가 없다면 Any를 사용하면 된다.(가능하면 지양하는게 좋다!)
