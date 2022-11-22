"""
Concurrency, CPU Bound vs I/O Bound - I/O Bound(2) - Asyncio basic
Keyword - asyncio
"""
"""
동시 프로그래밍 패러다임 변화
싱글 코어 -> 처리향상 미미, 저하 -> 비동기 프로그래밍 -> CPU 연산, DB연동, API 호출 대기 시간 늘어남
파이썬 3.4 -> 비동기(asyncio) 표준라이브러리 등장

"""

import time
import asyncio

# I/O Bound Asyncio 예제
# threading 보다 높은 코드 복잡도 -> Async, Await 적절하게 코딩


async def exe_calculate_async(name, n):
    for i in range(1, n + 1):
        print(f"{name} -> {i} of {n} is calculating...")
        asyncio.sleep(1)
    print(f"{name} - {n} working done!")


def exe_calculate_sync(name, n):
    for i in range(1, n + 1):
        print(f"{name} -> {i} of {n} is calculating...")
        time.sleep(1)
    print(f"{name} - {n} working done!")


def process_sync():
    start = time.time()

    exe_calculate_sync("One", 3)
    exe_calculate_sync("Two", 2)
    exe_calculate_sync("Three", 1)
    end = time.time()

    print(f">>> total seconds : {end - start}")


async def process_async():
    start = time.time()

    await asyncio.wait(
        [
            exe_calculate_async("One", 3),
            exe_calculate_async("Two", 2),
            exe_calculate_async("Three", 1),
        ]
    )

    end = time.time()

    print(f">>> total seconds : {end - start}")


if __name__ == "__main__":
    # Sync(동기) 실행
    # process_sync()

    # Async(비동기) 실행
    # Python 3.7 이상
    asyncio.run(process_async())
    print("start")

    # Python 3.7 이하
    # asyncio.get_evnet_loop().run_until_complete(process_async())
