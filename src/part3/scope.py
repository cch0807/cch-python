# scope
# local scope / global scope / enclosed scope / enclosing scope
# namespace

my_score = 50


def inside_value_function():
    my_score = 80
    print(f"my score inside is {my_score}")


inside_value_function()
print(f"my score outside is {my_score}")

# # What about if condition
did_extra_work = True
if did_extra_work:
    my_score = 90

print(f"my score outside is {my_score}")

# nonlocal
def a():
    x = 10
    def b():
        nonlocal x
        x = 20
    b()
    print(x)

# How Python search the variable?
# (LEGB rule)
# 1. local
# 2. enclosing
# 3. global
# 4. built-in