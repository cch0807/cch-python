# 시퀀스형 (비 시퀀스 타입 포함)
# 해시테이블(hashtable) -> 적은 리소스로 많은 데이터를 효율적으로 관리
# Dict -> key 중복을 허용x, Set -> 중복 허용 x
# Dict 및 Set 추가

# immutable Dict

from types import MappingProxyType

# 읽기 전용(쓰거나 추가 x)

d = {"key1": "value1"}

# Read Only
d_frozen = MappingProxyType(d)

# print(d, id(d), hash(d))
print(d, id(d))
# print(d_frozen, id(d_frozen), hash(d_frozen))
print(d_frozen, id(d_frozen))

# 수정 불가
# d_frozen['key2'] = 'value2'

# 수정 가능
d["key2"] = "value2"

print(d)

print()
print()

s1 = {"Apple", "Orange", "Apple", "Orange", "Kiwi"}
s2 = set({"Apple", "Orange", "Apple", "Orange", "Kiwi"})
s3 = {3}
s4 = set()
s5 = frozenset({"Apple", "Orange", "Apple", "Orange", "Kiwi"})

s1.add("Melon")

print(s1)

# s5.add('Melon')

print(s1, type(s1))
print(s2, type(s2))
print(s3, type(s3))
print(s4, type(s4))
print(s5, type(s5))

# 선언 최적화
# 바이트 코드 -> 파이썬 인터프리터 실행
from dis import dis

print("-" * 70)
print(dis("{10}"))
print("-" * 70)
print(dis("set([10])"))

# 지능형 집합(Comprehending)
print("-" * 70)

from unicodedata import name

print({name(chr(i), "") for i in range(0, 256)})
