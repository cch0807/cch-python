import random

lower_alphabets = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]
upper_alphabets = []
for alphabet in lower_alphabets:
    upper_alphabets.append(alphabet.upper())
alphabets = lower_alphabets + upper_alphabets
numbers = [str(i) for i in range(0, 10)]
symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

num_of_alphabets = 9
num_of_numbers = 3
num_of_symbols = 2

strong_password = []
for i in range(0, num_of_alphabets):
    strong_password.append(alphabets[random.randint(0, len(alphabets) - 1)])

for i in range(0, num_of_numbers):
    strong_password.append(alphabets[random.randint(0, len(alphabets) - 1)])

for i in range(0, num_of_symbols):
    strong_password.append(alphabets[random.randint(0, len(alphabets) - 1)])

random.shuffle(strong_password)

print("".join(strong_password))
