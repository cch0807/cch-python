# dictionaries
# key value
dic = {
    "country": "south korea",
    "city": "seoul",
    "gender": "male",
    "age": 35
}

# print(dic["country"])

for key, value in dic.items():
    print(f"{key}: {value}")

for key in dic:
    print(f"{key}: {dic[key]}")

print(dic.keys())
print(dic.values())

# key error
# print(dic["name"])
# print("name" not in dic)

dic1 = {
    1: 1,
    2: 3
}

print(dic1[2])