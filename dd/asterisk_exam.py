def some_func(*args) -> int:
    return 0


def some_func2(**kwargs):
    return 0


# 함수의 매개변수 정의 앞에 *이 1개 붙어있는 경우
def print_args(*args):
    print("Positional:", args)
    print("Type:", type(args))


print_args(1, 2)

# 위와 같이 매개변수를 가변 갯수의 위치 인수로 설정하였기 때문에 임의의 변수들인 1,2 를
# 매개변수로 입력해줘도 잘 동작하는것을 확인할 수 있다.
# 또한 입력받은 매개변수 1,2는 튜플 형태로 입력되는 것도 추가적으로 확인할 수 있다.
# 함수를 정의할 때 매개변수를 가변적으로 그리고 따로 이름을 가지지 않은 위치 인수로 정의하고 싶다면 *


def get_summation(*args):
    return sum(args)


print(get_summation(1, 2, 3, 4))

# 매개변수 kwargs 앞에 *가 2개 붙어있는 경우
# 매개변수 args를 가변적인 갯수를 가진 키워드 인수로 정의하겠다는 의미


def print_kwargs(**kwargs):
    print("Keyword:", kwargs)
    print("Type:", type(kwargs))


print_kwargs(foo=1, bar=2)

# *이 1개 붙어있는 경우와는 다르게 입력된 kwargs가 딕셔너리 형태로 전달되었다는 것을 확인할 수 있다.
# 딕셔너리 형태로 전달된 키워드 인수 각각을 사용하고 싶다면,
# 함수 내부에서 딕셔너리의 각 요소에 접근하면 된다.


def get_summation(**kwargs):
    for key, val in kwargs.items():
        print(f"{key}: {sum(val)}")


get_summation(first_semester=[40, 60, 50], second_semester=[30, 80, 90])

# 아래는 튜플을 함수의 매개변수로 넘기는 방법에 대한 예제


def some_func(first_val, second_val, third_val):
    print("first:", first_val)
    print("second:", second_val)
    print("third:", third_val)


some_args = 4, "foo", "bar"
print(some_args)

some_func(*some_args)
