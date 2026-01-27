from functools import *
@lru_cache(None)

def f(a, b):
    if a+b >= 68: return 1
    h = [(a+1, b), (a+b, b), (a, b+1), (a, b+a)]
    if any(f(*i)  == 1 for i in h): return 'w1'
    if all(f(*i) == 'w1' for i in h): return 'l1'
    if any(f(*i) == 'l1' for i in h): return 'w2'
    if all(f(*i) == 'w2' or f(*i) == 'w1' for i in h): return 'l2'
    return 0

for i in range(1, 60):
    print(f(8, i), i)
#18
#17 29
#28
