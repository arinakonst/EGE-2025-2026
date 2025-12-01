def f(x, y):
    if x==y:
        return 1
    if x>y or x == 25:
        return 0
    else:
        return f(x+3, y) + f(2*x, y) + f(5*x, y)

print(f(5, 115))
