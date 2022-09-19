# 2가지 패턴 실습
# concurrent.futures map
# concurrent.futures wait, as_completed

import os
import time
from concurrent.futures import wait, as_completed, ThreadPoolExecutor, ProcessPoolExecutor

WORK_LIST = [10000, 10000000, 100000000, 100000000]

# 동시성 합계 계산 메인 함수
# 누적 합계 함수(제네레이터)
def sum_generator(n):
    return sum(n for n in range(1, n+1))

# wait
# as_completed
def main():
    # Worker Count
    worker = min(10, len(WORK_LIST))

    # 시작 시간
    start_time = time.time()
    # Futures
    futures_list = []

    # 결과 건수
    # ProcessPoolExecutor
    with ThreadPoolExecutor() as excutor:
        for work in WORK_LIST:
            # future 반환
            future = excutor.submit(sum_generator, work)
            # 스케쥴링
            futures_list.append(future)
            # 스케쥴링 확인
            print('Scheduled for {} : {}'.format(work, future) +'\n')
            print()
        
        # # wait 결과 출력
        # result = wait(futures_list, timeout=7)
        # # 성공
        # print('Completed Tasks' + str(result.done))
        # # 실패
        # print('Pending ones after waiting for 7seconds Tasks : ' + str(result.not_done))
        # # 결과 값 출력
        # print([future.result() for future in result.done])

        # as_completed 결과 출력
        for future in as_completed(futures_list):
            result = future.result()
            done = future.done()
            cancelled = future.cancelled

            # future 결과 확인
            print('Future Result : {}, Done : {}'.format(result, done))
            print('Future Cancelled : {}'.format(cancelled))


    # 종료 시간
    end_time = time.time() - start_time

    # 출력 포멧
    msg = '\n Time : {:.2f}s'
    # 최종 결과 출력
    print(msg.format(end_time))

# 실행
if __name__ == '__main__':
    main()
