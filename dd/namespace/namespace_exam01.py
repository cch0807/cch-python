# namespace_example01.py
def outer_func():
    a = 20

    def inner_func():
        a = 30

    inner_func()


a = 10
outer_func()
print("Namespace:", __name__)
print("Namespace:", globals()["__name__"])
