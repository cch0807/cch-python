from queue import Queue

# 1

q = Queue()
q.put(1)
q.put(2)
print(q.get())
print(q.get())

# 2
q = Queue()
try:
    q.get(timeout=1)
except Exception as e:
    print("Queue is empty")
    print(str(e))

# 3

# q = Queue()
# print(q.get(False))
# print(q.get_nowait)
