def gen_num1(num):
    return [str(i) for i in range(num)]

print(gen_num1(10))

def gen_num2(num):
    return list(map(str, range(num)))

print(gen_num1(10))

import time
# before
start = time.time()
# run
gen_num1(1000)
# after
end = time.time()
diff = end - start
print(diff)

start = time.time()
gen_num2(1000)
end = time.time()
diff = end - start
print(diff)

import timeit
stmt = """
gen_num1(1000)
"""
setup = """
def gen_num1(num):
    return [str(i) for i in range(num)]
"""
t = timeit.timeit(stmt=stmt, setup=setup, number=100)
print(t)

stmt = """
gen_num2(1000)
"""
setup = """
def gen_num2(num):
    return list(map(str, range(100))) 
"""
t = timeit.timeit(stmt=stmt, setup=setup, number=100)
print(t)