# 루틴
# 일련의 명령(코드의 흐름)

# 메인 루틴
# 프로그램의 메인 코드 흐름

# 서브 루틴
# 보통의 함수나 메소드 (메인 루틴을 보조하는 역할)
# 하나의 진입점과 하나의 탈출점이 있는 루틴이다.

# 코루틴
# 서브 루틴의 일반화된 형태
# 다양한 진입점과 다양한 탈출점이 있는 루틴이다.
# 파이썬 비동기 함수는 코루틴 함수로 만들 수 있다.

import asyncio

async def test():
    print('test')
    return 123


if __name__ == "__main__":
    asyncio.run(test())

# awaitable?
# coroutine, task, future 3가지 유형

