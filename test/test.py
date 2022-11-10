class tdm:
    def __init__(self):
        self.tdm_value = 100


class test_cls:
    def __init__(self):
        self.value = 20

    def test_func_call(self):
        self.tdm = tdm()
        test_in_class(self.tdm)
        print(self.tdm.tdm_value)


def test_def(tc):
    print(tc)
    # print(dir(tc.__init__))

    print(tc.__hash__())
    tc.value += 30
    print(tc.value)


def test_in_class(tc):
    tc.tdm_value += 30


tc = test_def(test_cls())

# wdm.result_code_list = [None] * len(wdm.commands_list)

test_list = [None] * 3

print(test_list)

test_set = (1, 2, 3)

print(test_set[0])

# test_load_config = "s".load_config

test_tdm = test_cls()

test_tdm.test_func_call()

#########################################
# 클래스 to 클래스


class test_cls1:
    def __init__(self):
        self.value = 50

    def call_tc2(self):
        self.tc2 = test_cls2(self)

        print(self.tc2.tc1.value)


class test_cls2:
    def __init__(self, tc1):
        self.tc1 = tc1


test_tc1 = test_cls1()

test_tc1.call_tc2()

test_set = (1, 2, 3)
print(test_set[0])

test_dict = {"one": 1, "two": 2}

print(test_dict["one"])

for i in range(10):
    print(i)


def set_test_func():
    return (1, 2)


num1, num2 = set_test_func()

print(num1, num2)
