"""
* [클래스 상속]
1. 부모 클래스가 갖는 모든 메서드와 속성이 자식 클래스에 그대로 상속.
2. 자식 클래스에서 별도의 메서드나 속성을 추가할 수 있다.
3. 메서드 오버라이딩
4. super()
5. Python의 모든 클래스는 object 클래스를 상속한다. : 모든 것을 상속한다.

* MyClass.mro() --> 상속 관계를 보여준다.
"""


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
        return a + b

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


class Siri(Robot):
    def __init__(self, name, age):
        # self.name = name
        # Siri.population += 1
        super().__init__(name, 1241243)
        self.age = age

    def call_me(self):
        print("네?")

    def cal_mul(self, a, b):
        self.a = a
        return a * b

    def cal_flexable(self, a, b):
        return self.cal_mul(a, b) + self.cal_add(a, b) + super().cal_add(a, b)

    @classmethod
    def hello_apple(cls):
        print(f"{cls} hello")

    def say_hi(self):
        print(f"Greetings, my masters call me {self.name}. \nby apple.")

    # 클래스 메서드
    @classmethod
    def how_many(cls):
        # self는 인스턴스를 받고 cls 클래스를 받음
        print(f"We have {cls.population} robots. by apple.")


bixby = Siri("bixby", 12031951)

print(bixby)

bixby.this_is_robot_cls()
bixby.cal_add(1, 2)

bixby.call_me()

print(bixby.cal_mul(5, 2))
print(bixby.a)
bixby.hello_apple()

siri = Siri("iphone8", 12535215)

siri.say_hi()

siri.how_many()

print(siri.age)
print(siri.name)

print(siri.cal_flexable(1, 3))

print(
    Siri.mro()
)  # [<class '__main__.Siri'>, <class '__main__.Robot'>, <class 'object'>]

print(Robot.mro())  # [<class '__main__.Robot'>, <class 'object'>]

# 모든 클래스는 object를 상속받는다.

print(object)

print(dir(object))

print(object.__name__)

print(int.mro())

print(int.__init__(8.9))
print(int(8.9))


class A:
    pass


class B:
    pass


class C:
    pass


class D(A, B, C):
    pass


print(D.mro())
