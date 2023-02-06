# Assignment Operator(=)
# Assignment with an = on lists does not make a copy. Instead, assignment
# makes the two variables point to the one list in memory.

colors = ["red", "blue", "green"]
b = colors
b.append("white")
print(b)
print(colors)

# # Shallow Copy
# # A shallow copy constructs a new compound object and then (to the extent possible)
# inserts references into it to objects found in the original.
a = [[1, 2], [2, 4]]
b = a[:]  ## shallow copy
b.append([3, 6])
print(b)
print(a)

b[0].append(3)
print(b)
print(a)

# # Deep Copy
# # A deep copy constructs a new compound object and then, recursively,
# inserts copies into it of the objects found in the original.

a = [[1, 2], [2, 4]]
import copy

b = copy.deepcopy(a)  ## deep copy
b[0].append(4)
print(b)
print(a)
