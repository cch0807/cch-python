# from Inheritance import Robot

# test_ro = Robot("test", "1234")


from re import S


class Robot:
    test_num = 0

    def __init__(self):
        self.name = "asdf"
        self.code = 1235
        self.test_num = 0
        self.test = test()

    def ad(self):
        test = test_Robot(1234)
        test.ad()
        print(self.test_num)

    def tests(self):
        # print(self.name, self.code)
        # res = test(self.name, self.code)
        # self.name = res[0]
        # self.code = res[1]
        # print(self.name, self.code)
        # print(self.name2)
        # print(self.code2)
        print(self.test)
        for i in self.test:
            print(i)


class test_Robot:
    def __init__(self, age):
        # super().__init__(name, code)
        super().__init__()
        # self.name = super().name
        self.age = age

    def ad(self):
        self.test_num = 2
        return self.test_num


def test():
    name2 = "test"
    code2 = 1234
    return (name2, code2)


test = Robot().tests()


class ParentEx2:
    def __init__(self):
        self.value = 5

    # def get_value(self):
    #     return self


class ChildEx2(ParentEx2):
    def get_value(self):
        return self

    def sum_value(self):
        test = self.get_value()
        print(test.value)


c = ChildEx2().sum_value()
