#Unpacking(feat. Algorithm_study)
a, b = map(int, input().split())
# iterable(모든 반복 가능한 객체를 iterable 이라고 함.) 데이터엔 모두 가능한 문법이다.
# 그럼 입력받은 list에서 첫번째, 마지막 값만 얻고 싶거나
# list에서 첫번째, 마지막 값만 제외하고 싶을 때는?

_list = [1, 2, 3, 4, 5]
first_index, *rest, last_index = _list
print(rest) # 2, 3, 4

# 파이썬은 *(asterisk)를 다음과 같은 상황에 사용한다.
# 곱셈, 거듭제곱
# List형 컨테이너를 반복해서 확장
# 가변 인자
# Unpacking

# 위에서 rest에 사용한 것은 가변인자다.

# 그렇다면 Unpacking을 살펴보자

_list = [1, 2, 3, 4, 5]
for num in _list:
    print(num, end = ' ')# 1 2 3 4 5

# list내 원소들을 출력하는 코드이다. 

_list = [1, 2, 3, 4, 5]
print(*_list) # 1 2 3 4 5

# 놀랍게도 동일한 결과를 얻을 수 있다. 이것을 List Unpacking이라 한다.
# 사실 list뿐만이 아니라, 컨테이너형 구조에선 모두 적용할 수 있다.

# Packing도 간단하게 알아보자

a, b, c = [1, 2, 3]
d = a, b, c
print(d) # (1, 2, 3)

# 위와 같이 하나의 변수에 여러값을 할당하게 되면 튜플로 묶이게 된다.

# List Comprehension
# 파이썬의 꽃 중 하나로, 한국어로는 지능형 리스트라고도 한다.
# 기본형은 다음과 같다.
_list = [i for i in range(10)] # 0 1 2 3 4 5 6 7 8 9

# 쉽게 얘기하자면
# (변수를 활용해 만들 값) for (변수 명) in (순회할 수 있는 값)
# 위와같기 때문에 List Comprehension으로 된 코드를 읽을 때는, 앞에부터 읽는게 아니라, for 뒤 부터 읽으면 편하다.


import sys
input = sys.stdin.readline

_ = input()
_set = set(map(int, input().split()))
q = input()
_list = list(map(int, input().split()))

print()

# 물론 다차원 배열도 사용할 수 있다

square = [[x ** 2 for x in range(3)] for _ in range(3)]
print(square) # [[1, 4, 9], [1, 4, 9], [1, 4, 9]]

# 코드의 길이를 확실히 줄일 수 있다는 장점이 있지만, 너무 길면 가독성도 해치고, 코드를 작성하는 본인도 헷갈릴 수 있다.
import random

# 1 ~ 10을 담는 리스트
_list = [i for i in range(10)]

# 2, 4, 6, ..., 20을 담는 리스트
_list = [2 * i for i in range(10)]

# 주어진 리스트를 받아 3의 배수만 담는 리스트
tmp = [random.randrange(1, 100) for i in range(100)]
_list = [i for i in tmp if i % 3 ==0]

# 값이 두개 들어있는 튜플을 받아 리스트를 생성하되, 튜플 내부의 값을 뒤집어서 저장
list_of_tuple = [(i,j) for i in range(100), for j in range(100, 0, -1)]
_list = [(j,i)for i,j in list_of_tuple]

# 주어진 리스트를 그대로 담되, 15가 넘어가는 값은 15로 바꿔서 저장
_list = [i if i<=15 else 15 for i in tmp]

# 두 개의 리스트를 합치되, 가능한 모든 조합을 저장하는 리스트
x = [i for i in range(5)]
y = [i for i in range(5)]
_list = [(i,j) for i in x, for j in y]

# Dictonary 잘 쓰기
# Dictionary와 Set은 Hash Table 구조를 띄고 있다.
# 그래서 삽입, 삭제, 탐색 연산의 시간복잡도는 O(1)이다.

# 초보자들이 가장 많이 하는 실수가, 값을 찾기 위해 list에서 in을 사용한다는 것이다.

data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for i in range(100):
    if i in data:
        print(1)

# 해당 코드는 데이터를 순차적으로 탐색한다. 그러므로 여기선 하나의 숫자를 찾기 위해 최대 10번 데이터를 확인해야 한다.
# 이런 상황에선 set을 사용해야한다.

data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
_data_set = set(data)

for i in range(100):
    if i in data:
        print(1)

# 실제로 몇 백만개의 데이터가 있는 set에 약 10만번 정도의 in 연산을 시행해도 1초도 안걸린다.
# 하지만 list를 사용하게되면 몇 시간 이상 걸릴 수 있다.

# 또한 set의 구조상, 같은 값이 들어올 수 없다. 이걸 응용하면 다음과 같은 것도 가능하다.

i_want_to_erase_duplicate_element = [21, 31, 65, 21, 58, 94, 13, 31, 58]
completed_list = list(set(i_want_to_erase_duplicate_element)) # 21, 31, 65, 58, 94, 13

test_list = ['Test', 'test', 'TEST', 'tteesstt']
converted_list = list(set(map(lambda string: string.lower(), test_list))) # test, tteesstt

# set 은 iterable 한 데이터를 기반으로 만들 수 있으니, 그걸 다시 list로 바꿔주면 중복된 값이 제거된 list가 된다.

# lambda를 익명 함수라고 한다. 뒤에 있는 string은 각각의 값을 string이라고 지칭하는것이다.
# 즉, 각각의 데이터를 소문자로 바꾸고, 그걸 set로 바꾸고, 다시 list로 돌린것이다.
