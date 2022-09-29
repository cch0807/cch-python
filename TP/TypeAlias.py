# https://mypy.readthedocs.io/en/stable/kinds_of_types.html#type-aliases

from typing import Union, List, Tuple, Dict, Optional
from typing_extensions import TypedDict

# * type alias


Value = Union[
    int, bool, Union[List[str], List[int], Tuple[int, ...]], Optional[Dict[str, float]]
]

value: Value = 17


def cal(
    v: Value,
) -> Value:
    return v


# * dict alias

ddd: Dict[str, str] = {"hello": "world", "world": "wow!!"}
ddd: Dict[str, Union[str, int]] = {"hello": "world", "world": "wow!!", "hee": 17}


class Point(TypedDict):
    x: int
    y: float
    z: str

point: Point = {"x": 8, "y": 1.1, "z": "12"}