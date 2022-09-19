# 시퀀스형 (비 시퀀스 타입 포함)
# 컨테이너 (Container : 서로다른 자료형[List, tuple, collections, deque])
# 플랫(Flat : 한개의 자료형[str, bytes, bytearray, array.array, memoryview])
# 가변(List, bytearray, array.array, memoryview, deque)
# 불변(tuple, str, bytes)
# 해시 테이블
# Key에 value를 저장하는 구조
# 파이썬 dict 해쉬 테이블의 예
# 키 값의 연산 결과에 따라 직접 접근이 가능한 구조
# key 값을 해싱 함수 -> 해쉬 주소 ->key에 대한 value의 위치 참조

# 해시값이 중복됐을 경우 처리 방법??

# Dict 구조
print(__builtins__.__dict__)

# Hash 값 확인

t1 = (10,20, (30, 40, 50))
t2 = (10,20, [30, 40, 50])

print(hash(t1))

# list는 수정이가능한 mutable 이라서 error 발생
# print(hash(t2))

print()
print()

# Dict Setdefault 예제
source = (
    ('k1', 'val1'),
    ('k1', 'val2'),
    ('k2', 'val3'),
    ('k2', 'val4'),
)

new_dict1 = {}
new_dict2 = {}

# No use Setdefault
for k, v in source:
    if k in new_dict1:
        new_dict1[k].append(v)
    else:
        new_dict1[k] = [v]

print(new_dict1)

# Use Setdefault
for k,v in source:
    new_dict2.setdefault(k, []).append(v)

print(new_dict2)

# 주의
new_dict3 = {k :v for k, v in source}

print(new_dict3)