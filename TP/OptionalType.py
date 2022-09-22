# Optional type
from typing import Union, Optional


def foo(name: str) -> Optional[str]:
    if name == "cch":
        return None
    else:
        return name


xxx: Optional[str] = foo("cch")

xxx: Union[str, None] = "cch"

xxx = None

xxx: Optional[str] = "cch"

xxx = None
