from Inheritance import Robot

test_ro = Robot("test", "1234")


class test_Robot(Robot):
    def __init__(self, name, code, age):
        super().__init__(name, code)
        self.age = age

    def ad(self):
        print(super().name)


test = test_Robot("hi", 12314, 6543)

print(test.ad())
