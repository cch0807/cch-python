"""
Multithreading - Thread(2) - Deamon,Join
Keyword - DaemonThread, Join
"""
"""
DaemonThread(데몬스레드)
1. 백그라운드에서 실행
2. 메인스레드 종료 시 즉시 종료
3. 주로 백그라운드 무한 대기 이벤트 발생 부분 담당 -> JVM(가비지 컬렉션), 자동 저장
4. 
"""

import logging
import threading
import time

# 스레드 실행 함수
def thread_func(name, d):
    logging.info("Sub-Thread %s: starting", name)
    for i in d:
        print(i)
    logging.info("Sub-Thread %s: finishing", name)


# 메인 영역
if __name__ == "__main__":
    # Logging format 설정
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")
    logging.info("Main-Thread: before creating thread")

    # 함수 인자 확인
    x = threading.Thread(target=thread_func, args=("First", range(200000)), daemon=True)
    y = threading.Thread(target=thread_func, args=("two", range(100000)), daemon=True)
    logging.info("Main-Thread: before running thread")

    # 서브 스레드 시작
    x.start()
    y.start()

    # DaemonThread 확인
    print(x.isDaemon())
    print(y.isDaemon())

    # # 주석 전후 결과 확인
    # x.join()

    # while True:

    logging.info("Main-Thread: wait for the thread to finish")
    logging.info("Main-Thread: all done")
