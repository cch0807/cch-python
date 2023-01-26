# reverse string

value = "Hello World"

# 1 reverse
value_list = list(value)
value_list.reverse()
print("".join(value_list))

# 2 reversed
print("".join(list(reversed(value))))
