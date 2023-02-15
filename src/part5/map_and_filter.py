# map function


def square(num):
    return num**2


print(square(3))

number_list = [1, 2, 3, 4, 5]

print(map(square, number_list))
