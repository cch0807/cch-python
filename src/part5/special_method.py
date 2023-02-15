# special, magic, dunder ___xxx___


class Tesla(object):
    def __init__(self, owner, color):
        self.owner = owner
        self.color = color

    def __str__(self):
        return f"This is {self.color} color {self.owner}'s car"

    def __len__(self):
        return len(self.owner)

    def __del__(self):
        print("This car has been deleted")

    def __eq__(self, other):
        return self.color == other.color


tesla = Tesla("Choi", "Black")
print(tesla)

# del tesla
# print(tesla)

tesla1 = Tesla("Chang", "Black")
print(tesla == tesla1)
