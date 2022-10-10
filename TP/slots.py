"""
객체 내에 있는 변수들은 __dict__를 통해서 관리가 된다.
__slots__ 을 통해 변수를 관리 :
파이썬 인터프리터에게 통보 해당 클래스가 가지는 속성을 제한한다.
__dict__를 통해 관리되는 객체의 성능을 최적화 -> 다수의 객체 생성시 메모리 사용 공간 대폭 감소.
"""


class WithoutSlotClass:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.value = 0


wos = WithoutSlotClass("cch", 12)

print(wos.__dict__)

wos.__dict__["hello"] = "world"

print(wos.__dict__)


class WithSlotClass:
    __slots__ = ["__name", "__age", "value", "value2"]

    def __init__(self, name, age):
        self.value = 0
        self.value2 = 3
        self.__name = name
        self.__age = age

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name):
        self.__name = new_name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, new_age):
        self.__age = new_age

    @name.deleter
    def name(self):
        del self.__name

    @age.deleter
    def age(self):
        del self.__age

    def test_value(self):
        return self.value, self.value2


ws = WithSlotClass("cch", 12)

# print(ws.__dict__)
print(ws.__slots__)

import timeit

# 메모리 사용량
# 슬롯을 사용했을 때가 사용하지 않았을 때보다 메모리 엑세스가 더 빠르다.
# 즉 슬롯을 사용하면 메모리 효율이 좋다.


def repeat(obj):
    def inner():
        obj.name = "cch"
        obj.age = 12
        obj.value = 30
        del obj.name
        del obj.age

    return inner


def test_de(obj):
    # obj.value = 20
    obj.name = "asdf"
    print(obj.test_value())
    return obj.value, obj.name


use_slot_time = timeit.repeat(repeat(ws), number=99999)
no_slot_time = timeit.repeat(repeat(wos), number=99999)

print(ws.value)
print("use slot: ", min(use_slot_time))
print("no slot: ", min(no_slot_time))

test = test_de(ws)

print(test)
