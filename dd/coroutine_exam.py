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
