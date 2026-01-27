#411
from functools import *
@lru_cache(None)
def f(a, b):
    if a+b >= 87: return 1
    h = [(a+1, b), (a*2, b), (a, b*2), (a, b+1)]
    if any(f(*i)  == 1 for i in h): return 'w1'
    if all(f(*i) == 'w1' for i in h): return 'l1'
    if any(f(*i) == 'l1' for i in h): return 'w2'
    if all(f(*i) == 'w2' or f(*i) == 'w1' for i in h): return 'l2'
    return 0

for i in range(1, 78):
    print(f(9, i), i)
#19 - 20
#20 - 34 38
#21 - 33
