# Arguments with Default Values
def write_str_to_file(file, content, mode="w"):
    with open(file, mode=mode) as f:
        f.write(content)


write_str_to_file(file="sample.txt", content="Hello World")

# Unlimited Positional Arguments
def unlimited_func(*args):
    print(args)


unlimited_func(1, 2, 3)


def sum_all(*args):
    total = 0
    for n in args:
        total += n

    return total


print(sum_all(1, 2, 3))

# **kwargs: Keyworded arguments
def calc(**kwargs):
    print(kwargs)


calc(n1=1, n2=3, func="add")


def calc(**kwargs):
    for k, v in kwargs.items():
        print(k)
        print(v)

        if kwargs["func"] == "add":
            return kwargs["n1"] + kwargs["n2"]


print(calc(n1=1, n2=3, n3=5, func="add"))
