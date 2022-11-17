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

# dictionary

fruit = ['apple', 'grape', 'orange', 'banana']
price = [3200, 15200, 9800, 5000]
_dict = {}

for i in range(len(price)):
    _dict.append((fruit[i], price[i])) # {'apple': 3200, 'grape': 15200, 'orange': 9000, 'banana': 5000}

# dictionary를 위와 같이 생성한다면 zip을 살펴보자.

fruit = ['apple', 'grape', 'orange', 'banana']
price = [3200, 15200, 9000, 5000]

_dict = dict(zip(fruit, price))

# 생성완료!
# 일반적으로 딕셔너리에서 없는 값을 찾으려고 하면, 오류가 발생한다.

fruit = ['apple', 'grape', 'orange', 'banana']
price = [3200, 15200, 9800, 5000]
_dict = dict(zip(fruit, price))

print(_dict['strawberry']) # Error!

# 그래서 이걸 회피하기 위해, 처음 배우는 분들은 in 옵션을 사용해서 데이터가 있는지 확인하고, 없으면 값을 추가하고, 있으면 출력하는 방식으로 넘어간다.
# 그런데, 꼭 if 를 사용해야할까? 

fruit = ['apple', 'grape', 'orange', 'banana']
price = [3200, 15200, 9800, 5000]
_dict = dict(zip(fruit, price))

print(_dict.setdefault('strawberry', 0)) 
# setdefault는 딕셔너리에 값이 있을 땐 해당 값을 리턴하고, 값이 없을 땐 두번째 인자로 넘겨준 값을 추가하고 추가한 값을 리턴한다.
# 참고로 해당 메소드를 활용한 유사 dictionary가 있다. 우리는 이것을 defaultdict 라고 부른다.

from collections import defaultdict

movie_review = [('Train to Busan', 4), ('Clementine', 5), ('Parasite', 4.5), ('Train to Busan', 4.2), ('Train to Busan', 4.5), ('Clementine', 5)]

index = defaultdict(list)

for review in movie_review:
    index[review[0]].append(review[1])

# defaultdict에서 값을 검색할 때, 값이 없으면 인자로 넘겨준 값이 default 값이 된다. 결국 찾을 때 마다 setdefault를 암묵적으로 실행해준다고 생각하면 된다.
# 위에서 unpacking을 배울 때, 리스트나 튜플에서 사용할 수 있는 방법을 배웠다. 그런데 dictionary는 원소가 쌓이는데, 이걸 어떻게 해야 unpacking할 수 있을까?

fruit = ['apple', 'grape', 'orange', 'banana']
price = [3200, 15200, 9800, 5000]
_dict = dict(zip(fruit, price))

print(*_dict.keys()) # apple grape orange banana
print(*_dict.values()) # 3200 15200 9800 5000
print(*_dict.items()) # ('apple', 3200) ('grape', 15200) ....

# Sorting
# 정렬은 sort() 라는 메소드가 있고, sorted() 라는 함수가 있다.
# 하나는 메소드고 하나는 함수? 정확히 말하자면 전자의 경우 리스트를 내부 정렬하는 메소드 이다.
# 후자는 컨테이너형 데이터를 받아 정렬된 리스트를 돌려주는 함수이다.

_list = [5, 6, 4, 8, 2, 3]
sorted_list = sorted(_list) # 2, 3, 4, 5, 6, 8
_list.sort()
print(_list) # 2, 3, 4, 5, 6 , 8

_set = {65, 12, 15, 156, 31, 54, 94, 82, 31}
_set.sort() # Error
print(sorted(_set)) # 12, 15, 31, 54, 65, 82, 94, 156

# sorted()의 출력값이 리스트라는 것에 주목해야한다. 애초에 dictionary와 셋은 순서가 없다.

# 내림차순 정렬은 쉽다.

_list = [5, 6, 4, 8, 2, 3]
sorted_list = sorted(_list, reversed = True) # 8, 6, 5, 4, 3, 2

# 튜플의 리스트를 정렬하고 싶은데, 첫번째 값으로 오름차순 정렬을 하는데 값이 같으면 두번째 값으로 내림차순 정렬하고 싶다?
# 정렬 기준이 복잡할 때 우선 문제를 해결하기 전에, 정렬 함수의 또 다른 옵션을 보자.

_list = [(1, 3), (8, 2), (2, 5), (4, 7)]
sorted_list = sorted(_list, key = lambda dt: dt[1]) # (8, 2), (1, 3), (2, 5), (4, 7)

# lambda ? 우선 key는 함수를 입력 받는다. 즉, lambda는 함수라는 것을 알 수 있다.

# 정확히 말해서, lambda는 익명 함수라는 것으로, 함수의 이름을 명시하지 않고 일회성으로 사용하기 위해 정의하는 것이다.
# 여기서 dt는 함수에서 사용할 변수명으로, dt는 각각의 튜플을 저런식으로 사용하겠다는 것이다.

# 즉, 저 문구를 정리하면, 튜플의 첫번째 값을 기준으로 정렬하겠다. 라는 것이다.

_list = [(1, 3), (8, 2), (2, 5), (4, 7)]
sorted_list = sorted(_list, key = lambda dt: (dt[1], -dt[0])) 

# lambda를 사용하면 정말 다양한 방식으로 정렬할 수 있다.

_list = ['CHicken', 'hamburger', 'Sushi', 'chocolate']

print(sorted(_list)) # ['CHicken', 'Sushi', 'chocolate', 'hamburger']
print(sorted(_list, key = lambda dt: dt.lower())) # ['CHicken', 'chocolate', 'hamburger', 'Sushi']

# 일반적으로 문자열은 대소관계를 비교하기 때문에, 다음과 같이 모두 소문자로 바꿔버리면 대소관계 상관없이 정렬을 할 수 있다.

# 문자열
# 코딩테스트를 파이썬으로 보는 사람들이 일부는 문자열 처리의 장점을 내새운다.
# 실제로 파이썬은 다른 언어보다 문자열 처리가 좀 편하다.

# strip()은 공백을 제거하는 함수다?

print('    asdasd    '.strip()) # asdasd

# 사실 이건 공백을 제거하는 함수가 아니다.

print('====chicken===='.strip('=')) # chicken

# 짜잔! 양 끝에 있는 문자열을 제거하는 함수였다.
# 인자를 넘겨주지 않으면 공백 문자로 인식해서 공백을 제거했던 것일 뿐이다.
# 참고로, 두개 이상의 문자열을 넣어주면, 두개를 모두 지워버린다. and 조건이 아니라 or 조건이다!

# 문자열을 뒤집고 싶을 땐, 두 가지 방법이 있다. 

string = 'I am Hungry...'
print(string[::-1])
print("".join(reversed(string)))

# 전자의 경우, 모든 iterable한 데이터에 사용 가능하다.(즉, 리스트도 튜플도 가능)
# 초보자들은 슬라이싱을 할 때 두개의 변수만 활용하지만, 세번째를 활용하면 더 무궁무진해진다.

# 슬라이싱은 string[시작:종료(포함 안 함):간격] 구조를 띄고 있다.
# 즉, 마지막이 2이면 0, 2, 4... 번째 문자열을 꺼내온다.
# -1은? 역순으로 뽑아온다. 간격도 물론 조정할 수 있다.

# 두번째의 경우 역순으로 뒤집은 iterator (iterable이 아니다!)을 리턴하는데, 그냥 출력하면 메모리 주소가 나오기 때문에
# for i in ~ 구조를 사용하거나 join을 사용한다.

#-------------------------------------------------------------------------------------------------------------

# Combination/Permutation

# 가끔 모든 경우를 탐색해야 하는 상황이 있다. 대표적으로는
# 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열을 모두 구하시오.
# 일반적으로 백트래킹을 활용해서 문제를 푼다. 그렇지만 다음과 같은 기능을 공부하면 굳이 백트래킹을 공부할 필요 없다.

import itertools

_list = [1, 2, 3, 4]

# combination은 모든 조합을 출력한다. 중복이 없고, 순서를 구분하지 않는다.
iter = itertools.combinations(_list, 2) # 12 13 14 23 24 34

# permutation은 순열이다. 중복은 없지만, 순서를 구분한다.
iter = itertools.permutations(_list, 2) # 12 13 14 21 23 24 31 32 34 41 42 43

# combinations_with_replacement는 중복이 가능한 조합이다. 그래서 combination과 구분하여 11, 22, 33, 44가 추가된다.
iter = itertools.combinations_with_replacement(_list, 2) # 11 12 13 14 22 23 34 33 34 44

# product는 모든 가능한 경우의 수를 출력한다.(Cartesian Product라고 한다!)
iter = itertools.product(_list, repeat=2) # 11 12 13 14 21 22 23 24 31 32 33 34 41 42 43 44

#-------------------------------------------------------------------------------------------------------------

# sum
# 파이썬에는 reduce()라는 함수가 있다. iterable한 값에 연속적으로 연산을 해 하나의 결과물을 출력하는 함수이다.
# 다만 Python 3 에서는 사용하지 않기를 권하고 있다.
# reduce에서 떨어져 나온 함수 중에 하나가 sum() 이다. 

_list = [1, 2, 3, 4, 5]
print(sum(_list)) # 15

#-------------------------------------------------------------------------------------------------------------

# join
# 리스트를 출력하고 싶은데, 출력 형태가 좀 특이하다?
# 1, 2, 3, 4, 5, 6, 7, 8 처럼 출력하고싶다면

_list = [1, 2, 3, 4, 5, 6, 7, 8]
print(*_list, sep=', ')# 1, 2, 3, 4, 5, 6, 7, 8

# 나쁘지 않지만, sep은 추력 할 때만 사용할 수 있기 때문에, 문자열 조작과정에선 사용할 수 없다.


_list = [1, 2, 3, 4, 5, 6, 7, 8]
print(', '.join(_list))

# join에 대한 정의는 다음과 같다.
# iterable 의 문자열들을 이어 붙인 문자열을 돌려준다.

# 정확히 말하면 str 클래스의 메소드인데, iterable한 데이터들 사이 사이에 문자열을 붙여서 문자열로 되돌려 준다.
# 그렇기 때문에 굳이 출력할 때가 아니라도 사용할 수 있다는 장점이 있다.

#-------------------------------------------------------------------------------------------------------------

# swap

# C 스타일의 언어를 사용하다 보면, 두 값을 서로 바꿔야 할 때가 있다.
# 파이썬은 간단하다.

a, b = b, a

#-------------------------------------------------------------------------------------------------------------

# for, while문 에서의 else

# 사용할 때 신중하게 사용해야 한다.
# 이중 이상의 반복문을 사용하다가 중간에 break를 해야 할 때가 있다. 

# for i in range(_):
#     for j in range(_):
#         if sample[i][j] != 1:
#             break
#     else:
        # Some Code...
    
# 굉장히 낯선 코드이다.
# for과 while 구문을 진행하다가 else가 나오면, 반복문을 break로 탈출하지 않았다면 진입하는 구간으로 의미가 변경된다.
# 다만, 코드를 줄이는덴 좋긴 하지만, 상황에 따라 본인도 코드를 헷갈려 할 수 있다.
# 이걸 사용하기 전엔 한 번 사용해보고 (익숙해지고 싶다면 주석을 사용해도 된다.) 사용하는걸 권장한다.

#-------------------------------------------------------------------------------------------------------------

# Enumerate

# for 를 사용하면 일반적으로 range를 사용해서 범위를 표시하거나, iterable한 데이터를 가져와서 내용물을 꺼낸다.

_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
# 목표 : (1, a), (2, b), (3, c) ....

# 분명 iterable하게 for를 쓰고 싶지만, 앞에 있는 숫자 때문에 할 수 없이

_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
for i in range(len(_list)):
    print(i, _list[i])

# 이렇게 쓰곤 한다. 이걸 개선해보자.

_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
for idx, val in enumerate(_list):
    print(idx, val)

# enumerate 라는 단어는 '열거하다' 라는 의미를 갖고 있다. enumerate를 사용하면 (인덱스, 값) 의 형태의 튜플을 돌려준다.
# 즉, 힘들게 range()를 사용하지 않아도 된다.

# Counter
# 가끔, 문자열에 들어간 글자를 셀 필요가 있다.
# 일반적으로는 딕셔너리를 사용해서 해결하곤 한다.

def countLetters(word):
    counter = {}
    for letter in word:
        counter.setdefault(letter, 0)
        counter[letter] += 1
    return counter

countLetters('Hello World') # {'H': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'W': 1, 'r': 1, 'd': 1}

# 이것도 쓸만하지만, 더 python답게 사용해보자!

from collections import Counter
Counter('hello world') # Counter({'l': 3, 'o': 2, 'h': 1, 'e': 1, ' ': 1, 'w': 1, 'r': 1, 'd': 1})
Counter('hello world').most_common() # [('l', 3), ('o', 2), ('h', 1), ('e', 1), (' ', 1), ('w', 1), ('r', 1), ('d', 1)]
Counter('hello world').most_common(2) # [('l', 3), ('o', 2)]

# most_common()을 사용하면 전체 결과를 튜플의 리스트로 리턴하고, 숫자를 명시하면 상위 n개에 해당하는 결과만 출력한다.

#-------------------------------------------------------------------------------------------------------------

# 배열 회전하기

# 코테에서 다양한 구현 문제를 풀다보면, 생각보다 귀찮은 친구가 여러가지 있다.
# 그 중 가장 귀찮을 수 있는 것은 바로 배열 회전하기이다.

def rotate(arr):
    return list(zip(*arr[::-1]))

print(rotate([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
# [(7, 4, 1), (8, 5, 2), (9, 6, 3)]

# 먼저, arr[::-1] 이므로 배열을 뒤집는다. 이렇게 되면 [[7, 8, 9], [4, 5, 6], [1, 2, 3]]
# *을 사용했으니 배열이 언패킹이 된다. 즉, [7, 8, 9], [4, 5, 6], [1, 2, 3]으로 분리된다.
# 위의 세 배열에 대해 zip()을 수행한다. 각각의 배열을 묶어주므로, (7, 4, 1), (8, 5, 2), (9, 6, 3)이 된다.
# zip()의 반환값은 zip 객체이므로, 리스트로 변환한다.