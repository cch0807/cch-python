"""
Python Advanced(3) - Meta Class(3)
Keyword - Type Inheritance, Custom metaclass
"""
"""

메타클래스 상속
1. type클래스 상속
2. metaclass 속성 사용
3. 커스텀 메타 클래스 생성\

"""

# Ex1
# 커스텀 메타클래스 생성 예제(Type 상속X)


def cus_mul(self, d):
    for i in range(len(self)):
        self[i] = self[i] * d


def cus_replace(self, old, new):
    while old in self:
        self[self.index(old)] = new

    # self.cus_mul([1, 2, 3, 4], 7)
    # print(self.num)


# list를 상속받음, 메소드 2개 추가

CustomList1 = type(
    "CustomList1",
    (list,),
    {"desc": "커스텀 리스트1", "cus_mul": cus_mul, "cus_replace": cus_replace},
)

c1 = CustomList1([1, 2, 3, 4, 5, 6, 7])
c1.cus_mul(1000)
c1.cus_replace(1000, 7777)

print("Ex1 > ", c1)
print("Ex1 > ", c1.desc, c1.__repr__())

# Ex2
# 커스텀 메타클래스 생성 예제(Type 상속)

# class MetaClassName(type):
#     def __new__(metacls, name, bases, namespace):
#         # 코드
#         pass


class test_class:
    def __init__(self, num):
        self.num = num

    def test_pr(self):
        print(self.my_list)


# new -> init -> call 순서
class CustomListMeta(type, test_class):
    # 생성된 인스턴스 초기화
    def __init__(self, object_or_name, bases, dict):
        print("__init__ -> ", self, object_or_name, bases, dict)
        self.mydict = dict
        super().__init__(object_or_name, bases, dict)

    # 인스턴스 실행
    def __call__(self, *args, **kwargs):
        print("__call__ -> ", self, *args, **kwargs)
        return super().__call__(*args, **kwargs)

    # 클래스 인스턴스 생성(메모리 초기화)
    def __new__(metacls, name, bases, namespace):
        print("__new__ -> ", metacls, name, bases, namespace)
        namespace["desc"] = "커스텀 리스트2"
        namespace["cus_mul"] = cus_mul
        namespace["cus_replace"] = cus_replace

        return type.__new__(metacls, name, bases, namespace)


CustomList2 = CustomListMeta("CustomList2", (list,), dict())

c2 = CustomList2([1, 2, 3, 4, 5, 6, 7, 8, 9])
c2.cus_mul(1000)
c2.cus_replace(1000, 7777)

print("Ex2 > ", c2)
