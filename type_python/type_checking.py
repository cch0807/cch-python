# type hint
# type 검사 x

from typing import List, Tuple, Dict

int_var: int = 88
str_var: str = "hello world"
float_var: float = 88.9
bool_var: bool = True

# list_var: list = [1, 2, 3]
list_var: List[int] = [1, 2, 3]  # 더 좋은 방법

tuple_var: Tuple[int, int, int] = (1, 2, 3)
dic_var: Dict[str, int] = {"hello": 47, "world": 123}


def type_check(obj, typer) -> None:
    if isinstance(obj, typer):
        pass
    else:
        raise TypeError("Type Error: {typer}")


def cal_add(x: int, y: int) -> int:
    # type_check(x, int)
    # type_check(y, int)
    return x + y


print(cal_add(1, 3))
print(cal_add([1, 2], [4, 5]))

# isinstance(obj, class)

print(isinstance(88, int))
print(isinstance(88.9, int))
