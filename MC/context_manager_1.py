"""
Python Advanced(1) - Context Manager(1)
Keyword - Contextlib, __enter__, __exit__, exception

"""

"""
context manager : 원하는 타이밍에 정확하게 리소스를 할당 및 제공, 반환하는 역할
가장 대표적인 with 구문 이해
정확한 이해 후 사용이 프로그램이 개발에 중요(문제 발생 요소 감소를 위해)
"""

# Ex1

# file = open("./testfile1.txt", "w")
# try:
#     file.write("Context Manager Test1\nContextlib Test1")
# finally:
#     file.close


# Ex2

with open("./testfile2.txt", "w") as f:
    f.write("Context Manager Test2\nContextlib Test2.")

# Ex3
# Use Class -> Context Manager with exception heading.


class MyFileWriter:
    def __init__(self, file_name, method):
        print("MyFileWriter started : __init__")
        self.file_obj = open(file_name, method)

    def __enter__(self):
        print("MyFileWriter started : __enter__")
        return self.file_obj

    def __exit__(self, exc_type, value, trace_back):
        print("MyFileWriter started : __exit__")
        if exc_type:
            print("Logging exception {}".format((exc_type, value, trace_back)))
        self.file_obj.close()


with MyFileWriter("./testfile3.txt", "w") as f:
    f.write("Context Manager Test2\nContextlib Test3.")
