# 기존 요구사항
# 10초마다 Job이 생성되는데, 각 job은 랜덤한 시간을 소요함.
# 이전 Job의 수행시간이 10초를 넘든 안 넘든 상관없이 10초마다 새로 생성되어야 함.
# Job들은 concurrent 하게 실행됨.

# 새로 추가되는 항목
# 각 Job이 끝났을 때 총 수행 시간을 출력함.
# Job 이 성공/실패(예외 발생) 여부와 상관없이 출력되야 함.

# 구현 1. Job 수정
# 가장 간단한 방법은 Job이 직접 출력을 하도록 수정.

from abc import ABCMeta
import asyncio
from datetime import datetime
import functools
from random import randint
import time


async def run_job() -> None:
    before = time.time()

    try:
        delay = randint(5, 15)
        await asyncio.sleep(delay) # 5~15초 동안 잠자기
    finally:
        after = time.time()
        print(f'Job duration: {after - before} sec')

async def main() -> None:
    while True:
        asyncio.create_task(run_job())
        await asyncio.sleep(10)

asyncio.run(main())

# 위와 같은 간단한 예제에는 이렇게 구현해도 큰 무리가 없지만, 
# 어플리케이션에 사용하기엔 문제가 있을 수 있다.
# 대부분은 이렇게 구현하면 SOLID의 단일 책임 원칙을 어기는 코드를 만들게 된다.
# 만약 이 예제 코드가 주기적으로 Job을 스케줄링하는 라이브러리라고 생각하면,
# 모니터링 기능을 위해서 사용자가 Job을 수정해야 하는 상황이 발생한다.

# --------------------------------------------------------------------

# 구현 2. 콜백

async def run_job() -> None:
    delay = randint(5, 15)
    await asyncio.sleep(delay) # 5~15초 잠자기

def print_wall_time(before: float, _: asyncio.Future[None]) -> None:
    after = time.time()
    print(f'Job duration: {after-before} sec')

async def main() -> None:
    while True:
        before = time.time()
        future = asyncio.create_task(run_job())
        future.add_done_callback(functools.partial(print_wall_time, before))
        await asyncio.sleep(10)

asyncio.run(main())

# Future에서 제공하는 콜백기능을 이용해 구현했다.
# run_job()은 이전 구현 그대로 변한 것이 없고,
# main()에 모니터링을 위해 콜백을 등록하는 코드가 추가되었다.
# 또한, 모니터링을 위한로직이 하나의 함수 print_wall_time()으로 분리되었다.
# Future.add_done_callback()은 Future 정상 종료, 예외 발생, cancle()을 통한
# 취소 등 종료만 된다면 항사 실행되기 때문에 try-finally 같은 코드가 없이도 목적을 달성할 수 있다.

# Future는 콜백함수 파라미터로 객체 자신을 넘겨주기 때문에 원한다면
# Job의 결과까지 모니터링할 수 있다.

async def run_job() -> int:
    delay = randint(5, 15)
    await asyncio.sleep(delay) # 5~15초 동안 잠자기
    return randint(0, 1000) # 임의의 연산 결과

def print_wall_time(before: float, future: asyncio.Future[int]) -> None:
    after = time.time()
    if future.exception() is not None:
        print(f'Error occurred: {future.exception()}, duration: {after - before} sec')
    else:
        print(f'Result: {future.result()}, duration: {after - before} sec')

async def main() -> None:
    while True:
        before = time.time()
        future = asyncio.create_task(run_job())
        future.add_done_callback(functools.partial(print_wall_time, before))
        await asyncio.sleep(10)

asyncio.run(main())

# 활용 2. Future 발행
# asyncio 모듈의 많은 유틸들이 (Queue, gather, as_completed 등) 내부적으로는
# 내부적으로는 Future 기반으로 작성되어있다.

# 인터페이스 & 테스트 코드

# 인터페이스
class Semaphore(metaclass=ABCMeta):
    _value: int

    def __init__(self, initial_value: int = 1) -> None:
        self._value = initial_value
    
    async def acquire(self) -> None:
        raise NotImplementedError
    
    def release(self) -> None:
        raise NotImplementedError

# 테스트 코드
async def run_job(sem: Semaphore, job_id: int) -> None:
    await sem.acquire()
    print(f'{datetime.now()} - start job {job_id}')
    await asyncio.sleep(1)
    print(f'{datetime.now()} - job {job_id} finished')
    sem.release()

async def main() -> None:
    # sem = SomeSemaphore(2) # 구현체로 변경 필요
    pass

asyncio.run(main())

# busy waiting

class BusyWaitingSemaphore(Semaphore):
    async def acquire(self) -> None:
        while self._value <= 0:
            await asyncio.sleep(0.1)
        self._value -= 1
    
    def release(self) -> None:
        self._value += 1