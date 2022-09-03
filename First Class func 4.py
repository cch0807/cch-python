# 일급 함수(일급 객체)
# 클로저 기초
# 데코레이터(Decorator)

# 장점
# 1. 중복 제거, 코드 간결, 공통 함수 작성
# 2. 로깅, 프레임워크, 유효성 체크 -> 공통 함수
# 3. 조합해서 사용 용이

# 단점
# 1. 가독성 감소?
# 2. 특정 기능에 한정된 함수는 -> 단일 함수로 작성하는 것이 유리
# 3. 디버깅 불편

# @classmethod
# @classmethod

# 데코레이터 실습
import time
from unittest import result

def perf_clock(func):
    def perf_clocked(*args):
        # 함수 시작 시간
        st = time.perf_counter()
        # 함수 실행
        result = func(*args)
        # 함수 종료 시간
        et = time.perf_counter()
        # 실행 함수명
        name = func.__name__
        # 함수 매개변수
        arg_str = ', '.join(repr(arg) for arg in args)
        # 결과 출력
        print(f'{et} {name} {arg_str}  -> {result}')
        return result
    return perf_clocked
