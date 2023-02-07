import pandas as pd

data = pd.read_csv("sample.csv")

# # DataFrame : General 20 labeled, size-mutable tubular structure
# with potentially heterogeneously-typed column
print(type(data))
print(data.to_dict())

# # Series : 1D labeled homogeneously-typed array
print(type(data["country"]))
print(data["country"].to_list())

# sum / max
print(type(data["country"]))
print(data["population"].max())

# differect way to access to the column
# print(data.population)

# # row data
# print(data(data.country == "USA"))

print(data[data.population == data.population.max()])

# from scratch
