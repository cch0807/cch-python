"""
* 데이터 형식에 의존하지 않고, 하나의 값이 여러 다른 데이터 타입들을 가질 수 있는 기술
"""
from typing import Union, Optional, TypeVar, Generic

T = TypeVar("T")
K = TypeVar("K")
# T = TypeVar("T", int, str, float)
# K = TypeVar("K", int, str, float)


class Robot(Generic[T, K]):
    def __init__(self, T: T, K: K):
        self.T = T
        self.K = K

    def decode(self):
        # 암호를 해독하는 코드
        # 복잡
        hash_pw: Optional[T] = None
        pass


Robot1 = Robot[int, int](1231412.234, 12412)
Robot2 = Robot[str, str](63463, "1241")
Robot3 = Robot[float, int](435, 153613613)

print(type(Robot1.T))


class Siri(Generic[T, K], Robot[T, K]):
    pass


Siri1 = Robot[int, int](1231412.234, 12412)
Siri2 = Robot[str, str](63463, "1241")
Siri3 = Robot[float, int](435, 153613613)

print(Siri1.T)

# * function


def test(x: T) -> T:
    print(x)
    print(type(x))
    return x


test([1, 2])
