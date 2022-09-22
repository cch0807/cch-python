"""
# private vs public
"""


# siri_name = "siri"

# siri_code = 210129301


# def siri_say_hi():
#     # code ....
#     print("say hello!! my name is siri")


# def siri_add_cal():
#     return 2 + 3


# def siri_die():
#     # code....
#     print("siri die")


# jarvis_anme = "javis"

# jarvis_code = 102103912042

# # ....


class Robot:
    """
    [Robot Class]
    Author : 최창현
    Role : ???

    """

    __population = 0

    # 생성자 함수
    def __init__(self, name, age):
        self.__name = name
        # self.age = age # public
        # self._age = age  # protected
        self.__age = age  # private
        Robot.__population += 1

    @property
    def name(self):
        return f"yoon {self.__name}"

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, new_age):
        if new_age < 0:
            raise TypeError("invalid range to age")
        self.__age = new_age

    # 인스턴스 함수
    def say_hi(self):
        print(f"Greetings, my masters call me {self.__name}")

    # 인스턴스 메서드
    def cal_add(self, a, b):
        print(a + b)

    # 클래스 메서드
    @classmethod
    def how_many(cls):
        # self는 인스턴스를 받고 cls 클래스를 받음
        print(f"We have {cls.__population} robots.")


# ss = Robot("yss", 8)


# class Siri(Robot):
#     def __init__(self, name, age):
#         super().__init__(name, age)
#         print(self.name)
#         # print(self.__Age)
#         # self.__age = 999


# # print(ss._age)

# ssss = Siri("iphone8", 9)

# print(ssss._age)

droid = Robot("r2d2", 2)

# print(droid.agesss)

droid.age = 7  # error

print(droid.age)

# droid.age = -999

print(droid.name)
