# 동기(Sync)
# 코드가 작성된 순서대로 진행하는 것.

import time

def delivery(name, mealtime):
    print(f"{name}에게 배달 완료!")
    time.sleep(mealtime)
    print(f"{name} 완료, {mealtime}초 소요...")
    print(f"{name} 수거 완료")

def main():
    delivery("A", 3)
    delivery("B", 3)
    delivery("C", 4)

if __name__=="__main__":
    start = time.time()
    # main()
    end = time.time()
    print(end - start)

# 비동기(Sync)
# 코드가 반드시 작성된 순서대로 진행하는 것이 아니다.

import time
import asyncio

async def delivery(name, mealtime):
    print(f"{name}에게 배달 완료!")
    await asyncio.sleep(mealtime)
    print(f"{name} 완료, {mealtime}초 소요...")
    print(f"{name} 수거 완료")

async def main():
    # await asyncio.gather(
    #     delivery("A", 3),
    #     delivery("B", 3),
    #     delivery("C", 4),
    # )
    await delivery('A', 3),
    await delivery('B', 3)

if __name__=="__main__":
    start = time.time()
    asyncio.run(main())
    end = time.time()
    print(end - start)