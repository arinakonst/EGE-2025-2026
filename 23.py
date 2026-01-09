def f(x, y):
    if x<y or x == 999 or x == 1014:
        return 0
    if x == y:
        return 1
    else:
        return f(x-25, y) + f(x-10, y) + f(x//9, y)

print(f(1024, 2))  #35
