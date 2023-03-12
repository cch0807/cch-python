import zoneinfo
from datetime import datetime, timezone
from zoneinfo import ZoneInfo

for tz in sorted(zoneinfo.available_timezones()):
    print(tz)

# Africa/Abdjan
# Africa/Accra
# Africa/Addis_Ababa

utc_time = datetime.utcnow()
# datetime.datetime(2023, 1, 6, 22, 43, 35, 515169)

utc_time_aware = utc_time.replace(tzinfo=timezone.utc)
# datetime.datetime(2023, 1, 6, 22, 43, 35, 515169, tzinfo = datetime.timezone.utc)

utc_time_aware = utc_time.replace(tzinfo=timezone.utc)
# datetime.datetime(2023, 1, 6, 22, 43, 35, 515169, tzinfo=datetime.timezone.utc)

tz_asia_seoul = ZoneInfo("Asia/Seoul")

utc_time_aware.astimezone(tz_asia_seoul)
# datetime.datetime(2023, 1, 7, 7, 43, 35, 515169, tzinfo=zoneinfo.Zoneinfo(key='Asia/Seoul'))

# Annotated Type Hints
# before
# def convert_m2cm(m: "meter") -> "centi":
#     return m * 100

# after 3.9
from typing import Annotated


def convert_m2cm(m: Annotated[int, "meter"]) -> Annotated[int, "centimeter"]:
    return m * 100


# math improvements
import math

# greatest common divisor support 3 or more
math.gcd(30, 48, 6)
# 6

# added least common multiple
math.lcm(7, 1, 4)
# 28

# Updating the dictionaries
a = {"x": 1}
b = {"y": 2}
{**a, **b}
# {'x': 1, 'y': 2}

{"x": 1} | {"y": 2} | {"z": 3}
# {'x': 1, 'y': 2, 'z': 3}

# the latter one will overwrite
{"x": 2} | {"x": 3, "y": 2} | {"z": 3}
# {'x': 3, 'y': 2, 'z': 3}

{"x": 3, "y": 2} | {"z": 3} | {"x": 2}
# {'x': 2, 'y': 2, 'z': 3}

# TypeHint for list

# before
from typing import List

numbers: List[float]

# after 3.9
numbers: list[float]

# removeprefix & removesuffix
print("Welcome to Python World".removeprefix("Welcome to "))

print("Computer Enginnering World".removesuffix(" World"))
