# As of Python 3.8

# help(print)

# # error due to positional only allwos
# print(value=1)


def plus_one(a: int):
    return a + 1


print(plus_one(a=1))

# restrict to the positional only arguments
def plus_one(a: int, /):
    return a + 1


print(plus_one(a=1))


def say_hello(name, /, greeting="Hi"):
    return f"{greeting}, {name}"


print(say_hello("Jack"))
print(say_hello("Jack", greeting="Hello"))

# error
print(say_hello(name="Jack", greeting="Hello"))

# As of Python 3.0
# keyword only arguments
def convert_to_cm_from_meter(*, meter):
    return meter * 100


# error
print(convert_to_cm_from_meter(meter=10))


def title_format(text, /, padding="*", *, size=50):
    return f" {text} ".center(size, padding)


print(title_format("hello", "*", size=50))
