from sys import *
setrecursionlimit(7000)
def f(n):
    if n>=55555:
        return n
    if n<55555:
        return n+8+f(n+8)

print(f(522) - f(7802))


































