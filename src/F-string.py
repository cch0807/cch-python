# 과거 스타일
name = "Joon"
age = 30
print("Hello, %s." % name)
print("Hello, %s, I am %s" % (name, age))

# 하지만, 만약 프린트로 표현해야될 변수들이 많다면?

# Python 2.6
print("Hello, {}. I am {}.".format(name, age))
print("Hello, {1}. I am {0}.".format(age, name))

person = {"name": "Joon", "age": 17}
print("Hello, {name}. I am {age}.".format(name=person["name"], age=person["age"]))
print("Hello, {name}. I am {age}.".format(**person))

# Python 3.6
print(f"Hello, {name}. I am {age}.")
print(f"Hello, {name}. I am {age}.")
print(f"{name.lower()} is cool.")
