# reverse string

value = "Hello World"

# 1 reverse
value_list = list(value)
value_list.reverse()
print("".join(value_list))

# 2 reversed
print("".join(list(reversed(value))))

# 3 forloop
temp_list = []
for i in range(len(value) - 1, -1, -1):
    temp_list.append(value[i])
print(temp_list)
print("".join(temp_list))

# 4 while
value_list = list(value)
temp_list = []
while len(value_list) > 0:
    temp_list.append(value_list.pop())
print("".join(temp_list))
