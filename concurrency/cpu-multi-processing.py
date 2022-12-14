import os
import threading
import time
from concurrent.futures import ProcessPoolExecutor
import sys
sys.set_int_max_str_digits(100000)

nums = [10, 13, 22]

def cpu_bound_func(num):
    print(f"{os.getpid()} process | {threading.get_ident()} thread")
    numbers = range(1, num)
    total = 1
    for i in numbers:
        for j in numbers:
            for k in numbers:
                total *= i * j * k
    return total

def main():
    executor = ProcessPoolExecutor(max_workers=100)
    results = list(executor.map(cpu_bound_func, nums))
    # for num in nums:
    #     cpu_bound_func(num)
    print(results)

if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print(end-start)





