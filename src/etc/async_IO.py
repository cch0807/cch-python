# def generate_sequence():
#     cnt = 0
#     while True:
#         yield cnt
#         cnt += 1

# seq = generate_sequence()
# print(next(seq)) # 0
# print(next(seq)) # 1
# print(next(seq)) # 2

# import asyncio
# import time

# # synchronous version
# def task():
#     print("hello")
#     time.sleep(1)
#     print("world")

# def main():
#     for _ in range(3):
#         task()

# if __name__ == "__main__":
#     # returns the float value of time in seconds
#     start = time.perf_counter()
#     main()
#     time_took = time.perf_counter() - start
#     print(f"it took {time_took} seconds.")

# single event loop
import asyncio
import time


async def task():
    print("hello")

    # return the control back to "event loop"
    await asyncio.sleep(1)
    print("world")

async def main():
    await asyncio.gather(task(), task(), task())

if __name__ == "__main__":
    # retruns the float value of time in seconds
    start = time.perf_counter()
    asyncio.run(main())
    time_took = time.perf_counter() - start
    print(f"it took {time_took} seconds.")