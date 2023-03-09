# How to use *args and **kwargs
# unpack iterables using single asterisk(*)
# unpack dictionaries using double asterisk(*)
# mix standard, args and kwargs
# unpacking bonus to recap

# args
def adding_numbers(*args):
    # args is just name of variable
    _sum = sum([arg for arg in args])
    return _sum


print(adding_numbers(1, 2, 3))

# kwargs
def concat_str(**kwargs):
    return "".join([kw for kw in kwargs])


print(concat_str(str1="a", str2="b", str3="c"))


def concat_str(**kwargs):
    return "".join([kw for kw in kwargs.values()])


print(concat_str(str1="a", str2="b", str3="c"))

# mix standard, args and kwargs
def mix_args(x, y, *args, **kwargs):
    lst = [x, y]
    lst.extend([arg for arg in args])
    lst.extend([kw for kw in kwargs.values()])
    return lst

print(mix_args('x', 'y', 'z', a='1'))

#unpacking bonus to recap
print({**{"a": 1}, **{"b": 2}})

lst = [1,2,3,4,5,6]

a, *b, c = lst

print(a)

print(b)

print(c)
