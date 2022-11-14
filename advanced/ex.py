# 타입 힌트(type hint)를 언어 차원에서 지원하기 위함.

# List, Dict, Tuple, Set
# 타입 어노테이션을 사용하다 보면 리스트, 사전, 튜플,
# 세트와 같은 파이썬 내장 자료 구조에 대한 타입을 명시해야 할 때가 있다.
# 이 때, typing 모듈에서 제공하는 List, Dict, Tuple, Set를 사용하여 타입 어노테이션을 추가하면 된다.

from typing import List, Dict, Tuple, Set, Final, Union, Optional, Callable, Iterable

nums: List[int] = [1, 2, 3]

countries: Dict[str, str] = {"KR": "South Korea", "US": "United States", "CN": "China"}

user: Tuple[int, str, bool] = (3, "Dale", True)

chars: Set[str] = {"A", "B", "C"}


# 재할당이 불가능한 변수, 즉 상수에 대한 타입 어노테이션을 추가할 때는 typing 모듈의 Final을 사용한다.
TIME_OUT: Final[int] = 10

# 여러 개의 타입이 허용될 수 있는 상황에서는 typing 모듈의 Union을 사용할 수 있다.


def toString(num: Union[int, float]) -> str:
    return str(num)


# typing 모듈의 Optional은 None이 허용되는 함수의 매게 변수에 대한 타입을 명시할 때 유용하다.


def repeat(message: str, times: Optional[int] = None) -> list:
    if times:
        return [message] * times
    else:
        return [message]


# Callable
# 파이썬에서는 함수를 일반 값처럼 변수에 저장하거나 함수의 인자로 넘기거나 함수의 반환값으로 사용할 수 있다.
# typing 모듈의 Callable은 이러한 함수에 대한 타입 어노테이션을 추가 할 때 사용한다.

# 예를 들어, 아래 repeat 함수는 첫 번째 매개 변수 greet 를 통해 함수를 인자로 받고 있다.
# 매개 변수에 타입 어노테이션 Callable[[str], str]를 추가해줌으로써, str 타입의 인자를 하나 받고,


def repeat(greet: Callable[[str], str], name: str, times: int = 2) -> None:
    for _ in range(times):
        print(greet(name))


greet: Callable[[str], str] = lambda name: f"HI, {name}!"
repeat(greet, "Dale")

# 타입 추상화
# 함수의 매개 변수에 대한 타입 어노테이션을 추가해줄 때는 타입을 추상적으로 명시해주는 것이
# 유리한 경우가 많다. 예를 들어, 아래 toStrings() 함수는 nums 매개 변수의 타입을 List[int] 대신에 Iterable[int]로 명시해주고 있다.


def toStrings(nums: Iterable[int]) -> List[int]:
    return [str(x) for x in nums]


# 따라서 위 함수는 리스트 뿐만 아니라 튜플, 세트까지 처리할 수 있는 유연한 API를 가지게 된다.
# typing 모듈은 Iterable 뿐만 아니라 Sequence, Mapping, MutableMapping 와 같은 여러가지 추상 타입을 지원한다.
