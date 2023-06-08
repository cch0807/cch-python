# Iterator
"""
Python에서 Iterator라는 것은 __iter__() 와 __next__() method를 가진 객체를 의미한다.

* __iter__() : Iterator object(__next__() method를 가진) 객체를 리턴
* __next__() : 호출될 때 마다 다음 값을 리턴

즉, 해당 객체에서 __iter__() method를 이용해서 iterator를 얻고,
__next__() method를 이용해서 반복되는 값을 얻는다.
"""


class Counter(object):
    def __iter__(self):
        iter = Iterator()
        return iter


class Iterator(object):
    def __init__(self):
        self.index = 0

    def __next__(self):
        if self.index > 10:
            raise StopIteration
        n = self.index * 2
        self.index += 1
        return n


# 실제 확인은 iterator object를 얻는 builtin iter() 함수와, 이 iterator object에서 다음 값을 얻는 builtin next() 함수를 사용할 수 있다.

c = Counter()
i = iter(c)
print(next(i))
print(next(i))

# Iteration의 종료는 위 예와 같이 StopIteration exception을 발생 시키면 된다.

c = Counter()
for i in c:
    print(i)  # 0~20 까지 짝수 출력

"""
즉, for 루프에 객체를 넘기는 경우 __iter__ method가 존재하는지 확인하여
iterator로 동작되도록 언어 자체에서 지원

Iterator의 장점은 위와 같이 loop에서 사용할 수 있음
iterator로 data structure 와 algorithm을 분리할 수 있음

정리하면 다음과 같다.

- Iterator -
Python for loop는 객체에 __iter__() method가 있으면 이를 이용 iterator를 얻음
Iterator의 __next__()로 StopIteration exception 이 발생할 때 까지 반복하여 값을 얻어
loop를 반복 수행
동일한 동작은 built-in 함수인 next()를 이용하여 사용 가능

"""

# Generator (yield 키워드)
"""
Iterator를 좀 더 편하게 사용하는 방법은 다른 언어처럼 yield를 이용하여 coroutine을 지원하는 것이다.
"""


def test1():
    print("print 1")
    yield 1
    print("print 2")
    yield 2


def test2():
    for i in range(10):
        yield i * 2


"""
Generator는 함수안에 yield keyword가 있다는 것을 제외하고는 일반 함수와 동일

- 일반 함수 호출 시: 함수의 body가 실행
- Generator(yield가 있는 함수) 호출 시: Generator가 실행되는 것이 아니라 이 함수를 감싸는 'generator' 객체가 리턴
Generator 객체는 iterator와 동일하게 __next__()를 가진 객체
"""

g = test1()
type(g)
dir(g)
next(g)

next(g)
next(g)
# StopIteration
