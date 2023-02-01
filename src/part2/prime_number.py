# Prime number
# https://en.wikipedia.org/wiki/prime_number
# A prime number (or a prime) is a natural number greater than 1 that is not a product of two smaller natural numbers

# 2,3,5,6 ...
is_this_prime_number = 4

def is_prime_number(num: int):
    if num > 1:
        is_divisible = False
        for n in range(2, num):
            if num % n == 0:
                print(f"{num} can be cleanly divided by {n}")
                is_divisible = True
                break
        if is_divisible:
            print("Snap! it is not the prime number")
        else:
            print(f"Congrat! {num} is a prime number")
    else:
        print(f"{num} is not the prime number")

is_prime_number(num=is_this_prime_number)