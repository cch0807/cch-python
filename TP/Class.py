class Cal:

    # 생성자 : 메모리에 올라오는 순간 즉시 실행
    # self : 클래스로 인스턴스를 만들었을 때 인스턴스를 초기화해줌
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

    def sub(self):
        return self.a - self.b

    def mul(self):
        return self.a * self.b

    def div(self):
        return self.a / self.b


# def add(a, b):
#     return a + b


# def sub(a, b):
#     return a - b


# def mul(a, b):
#     return a * b


# def div(a, b):
#     return a / b

my_cal = Cal(1, 2)

# print(my_cal.a)
# print(my_cal.b)
# print(my_cal.add())
# print(my_cal.sub())
# print(my_cal.mul())
# print(my_cal.div())

my_cal.a = 5

print(my_cal.a)
print(my_cal.b)
print(my_cal.add())
print(my_cal.sub())
print(my_cal.mul())
print(my_cal.div())
