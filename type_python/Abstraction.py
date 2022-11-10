"""
#* 추상화 : abstraction
#* 불필요한 정보는 숨기고 중요한(필요한) 정보만을 표현함으로써
#* 공통의 속성 값이나 행위(methods)를 묶어 이름을 붙이는 것이다.
"""

"""
namespacee : 개체를 구분할 수 있는 범위
__dict__: 네임스페이스를 확인할 수 있다.
dir(): 네임스페이스의 key 값을 확인할 수 있다.
__doc__: class의 주석을 확인한다.
__class__: 어떤 클래스로 만들어진 인스턴스인지 확인할 수 있다.
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

    population = 0

    # 생성자 함수
    def __init__(self, name, code):
        self.name = name
        self.code = code
        Robot.population += 1

    # 인스턴스 함수
    def say_hi(self):
        print(f"Greetings, my masters call me {self.name}")

    # 인스턴스 메서드
    def cal_add(self, a, b):
        print(a + b)

    # 인스턴스 메서드
    def die(self):
        print(f"{self.name} is being destroyed!")

    # 인스턴스 메서드
    def die(self):
        print(f"{self.name} is being destroyed!")
        Robot.population -= 1
        if Robot.population == 0:
            print(f"{self.name} was the last one.")
        else:
            print(f"There are still {Robot.population} robots working.")

    # 클래스 메서드
    @classmethod
    def how_many(cls):
        # self는 인스턴스를 받고 cls 클래스를 받음
        print(f"We have {cls.population} robots.")

    @staticmethod
    def this_is_robot_cls():
        print("yes")

    def __str__(self):
        return f"{self.name} robot!!"

    def __call__(self):
        print("call!!")
        return f"{self.name} call!!"


siri = Robot("siri", 234918512)
jarvis = Robot("jarvis", 15212352)
bixby = Robot("bixby", 123183259)

print(siri.name)
print(siri.code)

jarvis.say_hi()
siri.say_hi()
siri.cal_add(1, 2)

Robot.how_many()

print(Robot.__dict__)

print(siri.__dict__)

print(jarvis.__dict__)

print(siri.name)
print(bixby.name)

siri.cal_add(2, 3)

print(siri.population)

siri.how_many()

# Robot.say_hi()

# 아래 두 줄의 코드는 같은 의미
siri.say_hi()
Robot.say_hi(siri)

print(dir(siri))
print(dir(Robot))

print(Robot.__doc__)

print(siri.__class__)

print(Robot.this_is_robot_cls())

siri.this_is_robot_cls()

print(siri.__str__)
print(siri.__str__())

siri()
