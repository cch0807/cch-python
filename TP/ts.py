# # from Inheritance import Robot
import time

# # test_ro = Robot("test", "1234")


# from re import S


# class Robot:
#     test_num = 0

#     def __init__(self):
#         self.name = "asdf"
#         self.code = 1235
#         self.test_num = 0
#         self.test = test()

#     def ad(self):
#         test = test_Robot(1234)
#         test.ad()
#         print(self.test_num)

#     def tests(self):
#         # print(self.name, self.code)
#         # res = test(self.name, self.code)
#         # self.name = res[0]
#         # self.code = res[1]
#         # print(self.name, self.code)
#         # print(self.name2)
#         # print(self.code2)
#         print(self.test)
#         for i in self.test:
#             print(i)


# class test_Robot:
#     def __init__(self, age):
#         # super().__init__(name, code)
#         super().__init__()
#         # self.name = super().name
#         self.age = age

#     def ad(self):
#         self.test_num = 2
#         return self.test_num


# # def test():
# #     name2 = "test"
# #     code2 = 1234
# #     return (name2, code2)


# tests = test_Robot(3)

# print(tests.age)
# print(test_Robot.__dict__)


# class ParentEx2:
#     def __init__(self):
#         self.value = 5

#     # def get_value(self):
#     #     return self


# class ChildEx2(ParentEx2):
#     def get_value(self):
#         return self

#     def sum_value(self):
#         test = self.get_value()
#         print(test.value)


# # c = ChildEx2().sum_value()


class test:
    def __init__(self):
        self.__test_num = 1
        self.__test_str = "str"

    def get_value(self):
        return {"test_num": self.__test_num, "test_str": self.__test_str}


def add_num(i):
    while True:
        i += 1
        print("add_num 호출", i)
        time.sleep(0.5)


def test_set():
    return 1, "asdf", 3


if __name__ == "__main__":
    # add_num(1)
    # print(1)

    ts = test_set()

    ts = (1, 2, *ts)
    print(*ts)

    ts = test().get_value()

    print(ts)
