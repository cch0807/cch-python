# list comprehension

country_list = ["USA", "South Korea", "Japan"]
lower_case_list = []
for country in country_list:
    lower_case_list.append(country.lower())

print(lower_case_list)

# convert into list conprehension

new_lower_case_list = []
new_lower_case_list = [country.lower() for country in country_list]

print(new_lower_case_list)

# string list comprehension
sample = "silicon valley"
print(ch for ch in sample)

# conditional list comprehension
sampling = [2, 3, 1, 1, 2, 3, 4]
filtered_sampling = [sample for sample in sampling if sample > 1]
print(filtered_sampling)
