# What is generator?
# Introduced with PEP 255, generator functions are a special kind of function that return a lazy iterator. These are objects that you can loop over like a list However, unlike lists, lazy iterators do not store their contents in memory, For an overview of iterators in Python, take a look at Python "for" Loops (Definite Iteration).
# e.g range()


def get_cubes(n):
    output = []
    for x in range(n):
        output.append(x**3)
    return output


print(get_cubes(5))

# What if we just need to print?
for x in get_cubes(5):
    print(x)


def get_cubes2(n):
    for x in range(n):
        yield x**3


print(get_cubes2(19))

for x in get_cubes2(5):
    print(x)

cubes = get_cubes2(5)
print(cubes)

# returns the next item from the iterator
# print(next(cubes))
# print(next(cubes))
# print(next(cubes))
# print(next(cubes))
# print(next(cubes))
# print(next(cubes)) # Error

s = "Choi"
# print(next(s))

# iter : Convert object to iterator
s_iter = iter(s)
print(next(s_iter))
print(next(s_iter))
print(next(s_iter))
print(next(s_iter))
