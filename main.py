def outer_func(x, y):
    x = 4

    def inner_func():
        nonlocal x
        x += 2
        return y

    return inner_func()


a = 3
b = 2
print(outer_func(a, b))
