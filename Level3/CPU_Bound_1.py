"""
Concurrency, CPU Bound vs I/O Bound - CPU Bound(1) - Synchronous
Keyword - CPU Bound

"""

# CPU-Bound 예제

import time


# 실행 함수1(계산)
def cpu_bound(number):
    pass


# 실행 함수2
def ind_sums(numbers):
    pass


def main():
    numbers = [3_000_000 + x for x in range(15)]

    # Check
    print(numbers)

    # 실행 시간 측정
    start_time = time.time()

    # 실행
    total = find_sums(numbers)

    # 결과 출력
    print(f"Total list : {total}")
    print()


if __name__ == "__main__":
    main()
