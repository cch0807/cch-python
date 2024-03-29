# 파이썬에서는 보통 메인 모듈의 구성이 다음과 같이 되어있다.


def main() -> None:
    pass


if __name__ == "__main__":
    main()

"""
파이썬은 스크립트 언어이며 다른 컴파일 언어들과는 다르게 자동으로 실행되는 메인함수가 없다.
따라서 일단 실행을 하게되면 들여쓰기가 되지 않은 모든 코드(Level 0 코드)를 실행하게 되며,
함수 및 클래스는 정의만 하게 되고 실행되지는 않는다.
"""

# 파이썬의 네임스페이스
"""
네임스페이스(namespace, 이름 공간)란 프로그래밍 언어에서 특정한 객체(Object)를 이름(Name)에 따라
구분할 수 있는 범위를 의미한다. 파이썬 내부의 모든것은 객체로 구성되며 이들 각각은 특정 이름과의 매핑 관계를
갖게 되는데, 이 매핑을 포함하고 있는 공간을 네임스페이스라고 한다.

네임스페이스가 필요한 이유는 다음과 같다.
프로그래밍을 수행하다보면 모든 변수 이름과 함수 이름을 정의하는 것이 중요한데,
이들 모두를 겹치지 않게 정하는 것은 사실상 불가능하다.

따라서 프로그래밍언어에서는 네임스페이스라는 개념을 도입하여,
특정한 하나의 이름이 통용될 수 있는 범위를 제한한다.
즉, 소속된 네임스페이스가 다르다면 같은 이름이 다른 개체를 가리키도록 하는 것이 가능해진다.

파이썬의 네임스페이스는 3가지로 분류된다.

전역 네임스페이스: 모듈별로 존재하며, 모듈 전체에서 통용될 수 있는 이름들이 소속된다.
지역 네임스페이스: 함수 및 메서드 별로 존재하며, 함수 내의 지역 변수들이 이름들이 소속된다.
빌트인 네임스페이스: 기본 내장 함수 및 기본 예외들이 이름들이 소속된다. 파이썬으로 작성된 모든 코드 범위가 포함된다.

"""

# 파이썬의 네임스페이스는 다음과 같은 특징들을 가지고 있다.
"""
- 네임스페이스는 딕셔너리 형태로 구현된다.
- 모든 이름 자체는 문자열로 되어있고 각각은 해당 네임스페이스의 범위에서 실제 객체를 가리킨다.
- 이름과 실제 객체 사이의 매핑은 가변적(Mutable)이므로 런타임동안 새로운 이름이 추가될 수 있다.
- 다만, 빌트인 네임스페이스는 함부로 추가하거나 삭제할 수 없다.

파이썬 공식 홈페이지의 튜토리얼에서는 네임스페이스를 ' 이름들과 실제 객체들 사이의 매핑 ' 이라고 정의한다.

"""

# 파이썬의 변수 스코프

"""
위에서 밝혔듯이 네임스페이스는 프로그래밍의 아무 위치에서나 접근이 가능한 것이 아니다.
변수 스코프는 이러한 네임스페이스의 접근성에 대해 고려하기 위한 개념이다.

변수 스코프(Variable Scope)란 접두어(Prefix)없이 
어떤 네임스페이스에 직접 접근이 가능한 프로그래밍의 어떤 부분이라고 정의할 수 있다.
C++ 처럼 중괄호({...})를 통해서 블록을 나누는 경우에는 블록을 기준으로 변수스코프가 결정된다.
따라서 중괄호 내에서 선언된 변수는 중괄호를 빠져나오면 폐기가 된다.
반면, 파이썬에서는 C++과는 다르게 블록 단위의 스코프가 존재하지 않으며
오직 전역 변수 스코프 및 지역 변수 스코프만이 존재한다.

프로그래밍을 하는 도중에는 어떤 경우에도 다음과 같은 중첩된 변수 스코프를 확인할 수 있다.

- 지역 이름들을 포함하는 현재 함수의 스코프(지역 네임스페이스)
- 전역 이름들을 포함하는 현재 모듈의 스코프(전역 네임스페이스)
- 빌트인 이름들을 포함하는 최외곽의 스코프(빌트인 네임스페이스)

만약 새로운 함수가 실행된다면 그 함수의 지역 이름들을 포함하는 
새로운 스코프가 생겨서 중첩되게 된다. 
또한 현재 변수의 이름이 참조하는 객체가 무엇인지를 검색하는 경우에는
가장 내부의 지역 네임스페이스부터 검색해 나가며 그 다음에는 보다 바깥에 있는
지역 네임스페이스를, 그리고 마지막에는 전역 네임스페이스를 검색한 이후에 최종적으로
빌트인 네임스페이스를 검색하게 된다.

"""


# namespace_example01.py
def outer_func() -> None:
    a: int = 20

    def inner_func() -> None:
        a = 30
        print("a = %d" % a)

    inner_func()
    print("a = %d" % a)


a = 10
outer_func()
print("a = %d" % a)

# if __name__ == '__main__': 의 의미
