def dell(n, m):
    if n%m == 0:
        return 1
    return 0

def f(x, y):
    res = dell(x, 128) <= (1-(dell(x, y)) <= (1-(dell(x, 80))))
    return res

for a in range(1, 1000):
    if all(f(x, a) for x in range(1, 5000)):
        print(a)
