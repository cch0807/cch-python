# orientation
from dataclasses import dataclass
from typing import Dict


def test(number: int, name: str) -> Dict[str, int]:
    return {name: number}


test(1234, "Kim")
# {'Kim': 1234}

test(1234, 1234)  # 에러가 나진 않음
# {1234: 1234}

# 개발 할 때, hint를 줄 뿐이지 구문 오류와 같은 에러는 발생하지 않음

# dataclasses 모듈은 인스턴스 생성 시, 변수 할당부터 코드의 양을 줄일 수 있는 많은 기능이 생겼다.

# AS-IS
# 클래스로 초기값을 받는다고 가정해보자.


class User:
    def __init__(self, number: int, name: str):
        self.number = number
        self.name = name


user1 = User(123, "Kim")
print(user1)
# <__main__.User object at 0x7fa1381241c0>

user2 = User(123, "Kim")
print(user2)
# <__main__.User object at 0x7fb5f8144910>

print(user1 == user2)
# False

# 인스턴스 변수 할당이 많아진다면 위의 self.number = number 와 같은 코드가 계속 생성되어야 한다.
# 또한 해당 객체 출력 시, 할당된 변수가 나오지 않게 된다. 또한 동일한 클래스에 동일한 값을 할당한 후 대소 비교를
# 하면 메모리 값으로 비교하기 때문에 같지 않다라고 나온다.

# AS-IS 2


class User:
    def __init__(self, number: int, name: str):
        self.number = number
        self.name = name

    def __repr__(self):
        return (
            self.__class__.__qualname__
            + f"(number={self.number!r}, name={self.name!r})"
        )

    def __eq__(self, other):
        if other.__class__ is self.__class__:
            return (self.number, self.name) == (other.number, other.name)
        return NotImplemented


user1 = User(123, "Kim")
print(user1)
# User(number=123, nume='Kim)

user2 = User(123, "Kim")
print(user2)
# User(number=123, name='Kim)

print(user1 == user2)
# True

# 초기값이 추가되면 될 수록 같은 코드의 양이 늘어나게 되므로 상당히 불편하고 좋지 않다.
# 하지만 dataclasses 모듈은 이와같은 상황을 해결할 수 있다.


@dataclass
class User:
    number: int
    name: str

user1 = User(123, 'Choi')
print(user1)

user2 = User(123, 'Choi')
print(user2)

print(user1 == user2)

# 만약, 선언 후 값을 변경할 수 없도록 불변 데이터를 지정하려면 
# dataclass 데코레이터에 frozen=True 옵션을 추가하면 된다.

@dataclass(frozen=True)
class user:
    number: int
    name: str

user1 = User(123, 'Kim')
print(user1)
user1.name = 'Lee' # dataclasses.FrozenInstanceError: cannot assign to field 'name'

# 선언된 클래스 간 대소비교나 정렬을 하려면 아래와 같이 order=True 옵션을 추가하면 된다.

@dataclass(order=True)
class User:
    number: int
    name: str

user1 = User(123, 'Bbb')
user2 = User(122, 'Aaa') 

print(user1 > user2)
print(sorted([user1, user2]))

user1 = User(12, 'A')
user2 = User(12, 'B')

print(user1 < user2)
print(sorted([user1, user2]))

# dataclass는 hash를 지원하지 않는데 만약 set을 사용하고 싶다면 unsafe_hash=True 옵션을 추가한다.

@dataclass(unsafe_hash=True)
class User:
    number: int
    name: str

user = User(123, 'Kim')
user1 = User(123, 'Kim')
user2 = User(122, 'Kim')
user3 = User(122, 'Lee')
print({user, user1, user2, user3}) # user 와 user 1 중복제거

# 변수에 기본값 할당

@dataclass
class User:
    number: int
    name: str = 'Anonymous'

# list와 같은 컨테이너 타입의 빈 값을 기본값으로 할당할 땐, field 함수를 할당받아 사용.

from dataclasses import field
from typing import List

@dataclass
class User:
    number: int
    name: str = 'Anonymous'
    test: List[int] = field(default_factory=list)

from dataclasses import dataclass, field, asdict, astuple

from typing import List

@dataclass
class User:
    number: int
    name: str = 'Anonymous'
    test: List[int] = field(default_factory=list)   

user = User(number=122, name='Kim')

print(asdict(user))
print(astuple(user))

@dataclass
class Work:
    id: str = field(init=False)

work = Work()
# 인자값 추가 시, 오류

from typing import ClassVar

@dataclass
class Work:
    id: ClassVar[int] = 123

work = Work(11111) # 오류