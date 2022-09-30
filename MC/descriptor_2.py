"""
Python Advanced(3) - Descriptor(2)
Keyword - descriptor vs property, low level(descriptor) vs high level(property)

"""

"""
dsecriptor
1. 상황에 맞는 메소드 구현을 통한 객체 지향 프로그래밍 구현
2. Property와 달리 reuse(재사용) 가능
3. ORM Framework 사용
4. 

"""

# Ex1
# Descriptor 예제(1)

import os


class DirectoryFileCount:
    def __get__(self, obj, objtype=None):
        print(os.listdir(obj.dirname))
        return len(os.listdir(obj.dirname))


class DirectoryPath:
    # Descriptor instance
    size = DirectoryFileCount()

    def __init__(self, dirname):
        self.dirname = dirname


# 현재 경로
s = DirectoryPath("./")
# 이전 경로
g = DirectoryPath("../")

# 헷갈릴 때 출력 용도
print("Ex1 > ", dir(DirectoryPath))
print("Ex1 > ", DirectoryPath.__dict__)

s.size

g.size

if s.size != g.size:
    print("worng")
