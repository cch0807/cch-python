# * Callable types
from typing import Callable


def add(a: int, b: int) -> int:
    # print(a + b)
    return a + b


# print(add(1, "3"))


def test():
    pass


def foo(func: Callable[[int, int], int]) -> int:
    # return test()
    return func(2, 3)


print(foo(add))
