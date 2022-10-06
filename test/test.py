class test_cls:
    def __init__(self):
        self.value = 20


def test_def(tc):
    print(tc)
    # print(dir(tc.__init__))

    print(tc.__hash__())
    tc.value += 30
    print(tc.value)


tc = test_def(test_cls())
