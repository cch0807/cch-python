class ClassExample:
    a = 10
    print(dir())


class_instance = ClassExample()
print(dir())

# 클래스 네임스페이스 반환: 내장변수 __dict__

"""
파이썬의 클래스는 각각의 네임스페이스를 갖는다.
또한 dir 메서드를 통해 현재 네임스페이스의 이름 리스트를 반환 받을 수 있다.
만약 이름 리스트가 아닌 실제 네임스페이스의 사본을 반환받으려면 파이썬 내장함수 __dict__ 를 사용하면 된다.

"""
