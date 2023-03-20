# List: [], mutable
# Dictionary: {}, mutable
# Set: {}, immutable
# Tuples: (), immutable

# List
my_list = [1, 2, 3]
my_list.append(4)
print(my_list)

# Dictionary
# As of Python3.7, it is ordered
my_dictionary = {"country": "south korea", "city": "seoul"}
print(my_dictionary)
my_dictionary["country"] = "USA"
print(my_dictionary)

# Set
# it is unchangeable, but can add or remove
# cannot subcript, unique
my_set1 = set((1, 2, 3))
print(my_set1)
# print(my_set1[1])
my_set1.add(1)
print(my_set1)
L = [1, 2, 3, 4, 1, 2, 3, 4]
print(list(set(L)))
my_set2 = {1, 2, 3}
print(my_set2)
my_set2.add(4)
print(my_set2)
my_set2.remove(4)
print(my_set2)

# Tuples
# Once it is created, you cannot change
# it is immutable
# Creation is fater than list
my_tuples = (1, 2, 3)
print(my_tuples[1])
