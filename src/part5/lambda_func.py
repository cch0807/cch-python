# lambda expressions

# It his small anonymous function

# lambda arguments : expression


def square(num):
    return num**2


print(square(3))

square = lambda num: num**2
print(square(3))

number_list = [1, 2, 3, 4, 5]
print(list(map(lambda num: num**2, number_list)))
