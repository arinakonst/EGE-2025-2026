from sys import *
def f(n):
    if n <= 10:
        return 1000000+n
    else:
        return 6*f(n-5) - 4*f(n-6) - f(n-10)

print(f(31) - f(30))  #4757
