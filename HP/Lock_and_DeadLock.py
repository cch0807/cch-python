"""
Multithreading - Thread(4) - Lock, DeadLock
Keyword - Lock, DeadLock, Race condition, Thread synchronization

"""
"""
용어 설명
1. 세마포어(semaphore) : 프로세스간 공유 된 자원에 접근 시 문제 발생 가능성 -> 한개의 프로세스만 접근 처리 고안(경쟁 상태 예방)
2. 뮤텍스(mutex) : 공유된 자원의 데이터를 여러 스레드가 접근하는 것을 막는 것. -> 경쟁 상태 예방
3. Lock : 상호 배제를 위한 잠금(Lock)처리 -> 데이터 경쟁
4. 데드락(Deadlock) : 프로세스가 자원을 획득하지 못해 다음 처리를 못하는 무한 대기 상황(교착 상태)

"""
