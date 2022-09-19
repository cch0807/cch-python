# 쓰레드(Thread)는 프로그램의 실행 흐름이다.
# 하나의 프로세스 안에서 여러 개의 쓰레드를 만들 수 있다.
# 프로세스란 말은 메모리에 할당되어 있는 한 개의 프로그램을 의미하고,
# 프로그램 안에서 여러개의 프로세스를 운영할 수 없기 때문에 프로그램이 하나의 프로세스라는 개념이다.
# 한 개의 프로세스에서 여러 개의 쓰레드를 가지는 병렬 처리 방식이라고 생각하면 된다.

# import time
# if __name__ == "__main__":
#     increased_num = 0

#     start_time = time.time()
#     for i in range(10000000):
#         increased_num += 1
    
#     print("--- %s second ---" % (time.time() - start_time))

#     print("increased_num=", end=""), print(increased_num)
#     print("end of main")

# import threading
# import time

# shared_number = 0

# def thread_1(number):
#     global shared_number
#     print(f"number = {number}")

#     for i in range(number):
#         shared_number += 1

# def thread_2(number):
#     global shared_number
#     print(f"number = {number}")

#     for i in range(number):
#         shared_number += 1

# # def thread_3(number):
# #     global shared_number
# #     print(f"number = {number}")

# #     for i in range(number):
# #         shared_number += 1

# if __name__== "__main__":

#     threads= []

#     start_time = time.time()

#     t1 = threading.Thread(target= thread_1, args=(50000000,))
#     t1.start()
#     threads.append(t1)

#     t2 = threading.Thread(target= thread_2, args=(50000000,))
#     t2.start()
#     threads.append(t2)

#     # t3 = threading.Thread(target= thread_3, args=(50000000,))
#     # t3.start()
#     # threads.append(t3)

#     for t in threads:
#         t.join()
    
#     print("--- %s seconds ---" % (time.time() - start_time))

#     print(f'shared_number={shared_number}')
#     print(f'end of {__name__}')


import threading
import time

shared_number = 0
lock = threading.Lock() # threading에서 Lock 함수 가져오기

def thread_1(number):
    global shared_number
    print(f"number = {number}")

    lock.acquire() # 작업이 끝나기 전까지 다른 쓰레드가 공유데이터 접근 금지
    for i in range(number):
        shared_number += 1
    lock.release() # lock 해제

def thread_2(number):
    global shared_number
    print(f"number = {number}")

    lock.acquire() # thread_2 잠금
    for i in range(number):
        shared_number += 1
    lock.release() # lock 해제

# def thread_3(number):
#     global shared_number
#     print(f"number = {number}")

#     for i in range(number):
#         shared_number += 1

if __name__== "__main__":

    threads= []

    start_time = time.time()

    t1 = threading.Thread(target= thread_1, args=(50000000,))
    t1.start()
    threads.append(t1)

    t2 = threading.Thread(target= thread_2, args=(50000000,))
    t2.start()
    threads.append(t2)

    # t3 = threading.Thread(target= thread_3, args=(50000000,))
    # t3.start()
    # threads.append(t3)

    for t in threads:
        t.join()
    
    print("--- %s seconds ---" % (time.time() - start_time))

    print(f'shared_number={shared_number}')
    print(f'end of {__name__}')