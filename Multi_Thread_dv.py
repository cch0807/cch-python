import time
import threading
from concurrent import futures


def do_something():
    print("Sleeping 1 seconds")
    time.sleep(1)
    print("Done Sleeping...")


def cal_sum(input_list):
    res = 0
    for i in range(input_list[0], input_list[1] + 1):
        res += i
    return res


# Single Thread
# if __name__ == '__main__':
#     start = time.perf_counter()
#     for _ in range(10):
#         do_something()
#     finish = time.perf_counter()

#     print(f'Finished in {round(finish-start, 2)} second(s)')

# --------------------------------------------------------------------
# Multi Thread with threading module
# if __name__ == "__main__":
#     start = time.perf_counter()
#     threads = []
#     for _ in range(10):
#         t = threading.Thread(target=do_something)
#         t.start()
#         threads.append(t)

#     for thread in threads:
#         thread.join()
#     finish = time.perf_counter()

#     print(f'Finished in {round(finish-start, 2)} second(s)')

# --------------------------------------------------------------------
# Use concurrent module

# if __name__ == '__main__':
#     start = time.perf_counter()

#     with futures.ThreadPoolExecutor() as executor:
#         results = [executor.submit(do_something) for _ in range(10)]

#     for f in futures.as_completed(results):
#         print(f.result())

#     finish = time.perf_counter()

#     print(f'Finished in {round(finish-start, 2)} second(s)')

# --------------------------------------------------------------------
# single thread with cal_sum

# if __name__ == '__main__':
#     start = time.perf_counter()

#     results = cal_sum([1, 100000000])
#     print(results)

#     finish = time.perf_counter()

#     print(f'Finished in {round(finish-start, 2)} second(s)')

# -------------------------------------------------------------------
# multi thread with cal_sum

if __name__ == "__main__":
    start = time.perf_counter()

    with futures.ThreadPoolExecutor() as executor:
        sub_routine = [[1, 1000000000 // 2], [10000000000 // 2 + 1, 10000000000]]
        results = executor.map(cal_sum, sub_routine)

    print(sum(results))

    finish = time.perf_counter()

    print(f"Finished in {round(finish-start, 2)} second(s)")
