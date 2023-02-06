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
