# Higher order function
# 1. A function is an instance of the Object type.
# 2. You can store the function in a variable
# 3. You can pass the function as a parameter to another function.
# 4. You can return the function from a function.
# 5. You can store them in data structures such as hash tables.


def add(num1, num2):
    return num1 + num2


add2 = add


def substract(num1, num2):
    return num1 - num2


def multiply(num1, num2):
    return num1 * num2


def divide(num1, num2, is_floor=True):
    if is_floor:
        return num1 // num2
    else:
        return num1 / num2


def calc(num1, num2, func):
    return func(num1, num2)


# print(calc(num1=10, num2=5, func=add2))

# Decorator
# Wrap another functions to extend the functionality without change the original code


def higher_order_example(func):
    def inside():
        print("start ...")
        func()
        print("end ...")

    return inside


@higher_order_example
@higher_order_example
def sample_example():
    print("I am inside")


sample_example()


def higher_order_example(func):
    def inside():
        print("start ...")
        num = 1
        func(num)
        print("end ...")

    return inside


@higher_order_example
def sample_example(num):
    print(f"I am inside {num}")


sample_example()
