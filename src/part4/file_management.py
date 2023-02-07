# file management
file = open("README.txt", "r")
print(file.read())
file.close()

# memory management
# early days
# 1. Forgetting to free your memory
# 2. Freeing your memory too soon
# modern language
# - GC

# # no close any more
with open("README.txt", "r") as file:
    print(file.read())

with open("WIRTEME.txt", "w") as file:
    print(file.write("Thanks"))
