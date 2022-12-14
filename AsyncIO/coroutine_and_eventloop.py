# coroutine_and_eventloop.md 참조바람.
# 요구사항은 다음과 같다.
# 10초마다 job이 생성되는데, 각 job은 랜덤한 시간을 소요함.
# 이전 job의 수행시간이 10초를 넘든 안 넘든 상관없이 10초마다 새로 생성되어야 함.
# Job들은 concurrent 하게 실행됨

import asyncio
from datetime import datetime
from random import randint

async def run_job() -> None:
    delay = randint(5, 15)
    print(f'{datetime.now()} sleep for {delay} seconds')
    await asyncio.sleep(delay) # 5~15초 동안 잠자기
    print(f'{datetime.now()} finished {delay} sec')

async def main() -> None:
    while True:
        asyncio.create_task(run_job())
        await asyncio.sleep(10)

if __name__ == "__main__":
    asyncio.run(main())