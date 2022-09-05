# 병행성(Concurrency)
# 이터레이터, 제네레이터
# iterator, generator

# 파이썬 반복 가능한 타입
# collections, text file, list, Dict, Set, Tuple, unpacking, *args... : iterable

# 반복 가능한 이유? -> iter(x), 함수 호출
t = 'ABCD'

# print(dir(t))

for c in t:
    pass
    # print(c)

# while
w = iter(t)

# print(dir(w))

print(next(w))
print(next(w))
print(next(w))

while True:
    try:
        print(next(w))
    except StopIteration:
        print('stop')
        break

print()

# 반복형 확인
from collections import abc

# print(dir(t))
print(hasattr(t, '__iter__'))
print(isinstance(t, abc.Iterable))

print()
print()

# next
class WordSplitter:
    def __init__(self, text):
        self._idx = 0
        self._text = text.split(' ')
    
    def __next__(self):
        print('Called __next__')
        try:
            word=  self._text[self._idx]
        except IndexError:
            raise StopIteration('Stopped Iteration. ^_^*')
        self._idx +=1 
        return word
    
    def __repr__(self):
        return 'WordSplit(%s)' % (self._text)

wi = WordSplitter('Do Today What you could do tommorrow')

print(wi)
