import time
import threading
from queue import Queue


def sender(q):
    data = [2020, 8, 12, 1, 55]
    while data:
        d = data.pop(0)
        q.put(d)
        print(f"sender : {d}")
        print("* sender waiting ...")
        print("")
        # time.sleep(1)
        q.join()
    q.put(None)
    print("sender done")


def receiver(q):
    while True:
        data = q.get()
        if data is None:
            break
        print(f"receiver : {data}")
        time.sleep(2)
        q.task_done()
    print("receiver done")


if __name__ == "__main__":
    q = Queue()
    t1 = threading.Thread(target=sender, args=(q,))
    t2 = threading.Thread(target=receiver, args=(q,))
    t1.start()
    t2.start()
