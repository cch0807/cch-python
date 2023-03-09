# pickle
# Library to save Python data structure such as list, dictionary, set and object

a = {"a": 1}
b = {"b"}
c = {1,2,3}

import pickle
with open("combine.pckl", "wb") as f:
    pickle.dump(a, f)
    pickle.dump(b, f)
    pickle.dump(c, f)

with open("combine.pckl", "rb") as f:
    x = pickle.load(f)
    y = pickle.load(f)
    z = pickle.load(f)

print(x)
print(y)
print(z)