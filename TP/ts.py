# from Inheritance import Robot

# test_ro = Robot("test", "1234")


class Robot:
    test_num = 0

    def __init__(self):
        self.name = "asdf"
        self.code = 1235
        self.test_num = 0

    def ad(self):
        test = test_Robot(1234)
        test.ad()
        print(self.test_num)

    def tests(self):
        print(self.name, self.code)
        res = test(self.name, self.code)
        self.name = res[0]
        self.code = res[1]
        print(self.name, self.code)


class test_Robot:
    def __init__(self, age):
        # super().__init__(name, code)
        super().__init__()
        # self.name = super().name
        self.age = age

    def ad(self):
        self.test_num = 2
        return self.test_num


def test(name, code):
    name = name
    code = code
    name = "fdas"
    code = 6546
    return (name, code)


test = Robot().tests()
