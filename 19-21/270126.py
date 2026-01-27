from functools import *
from sys import *
setrecursionlimit(50000)

#@lru_cache(None)
"""def f(a):
    if a > 67: return '!'
    h = [a+1, a+4, a*5]
    if any(f(i) == '!' for i in h): return 'w1'
    if all(f(i) == 'w1' for i in h): return 'l1'
    if any(f(i) == 'l1' for i in h): return 'w2'
    if all(f(i) == 'w2' for i in h): return 'l2'

    else: return 0

for a in range(67, 0, -1):
print(f(a), a)
"""

#@lru_cache(None)
"""def f(a):
    if a>64: return 1
    h = [a+1, a+2, a*3]
    if any(f(i) == 1 for i in h): return 'w1'
    if all(f(i) == 'w1' for i in h): return 'l1'
    if any(f(i) == 'l1' for i in h): return 'w2'
    if all(f(i) == 'w2' or f(i) == 'w1' for i in h): return 'l2'

    else: return 0

for a in range(1, 65):
    print(f(a), a)"""
    
    
#1349
"""@lru_cache(None)


def f(a):
    if a == 1: return 1
    if a < 1: return 0
    h = []
    if a%2 == 0:
        h.append(a//2)
    else:
        h.append(a-2)
    if a%3 == 0:
        h.append(a//3)
    else:
        h.append(a-3)
        
    if any(f(i) == 1 for i in h): return 'w1'
    if all(f(i) == 'w1' for i in h): return 'l1'
    if any(f(i) == 'l1' for i in h): return 'w2'
    if all(f(i) == 'w2' or f(i) == 'w1' for i in h): return 'l2'

    return -1

for i in range(1, 39):
    print(f(i), i)"""

#850
"""@lru_cache(None)
def f(a, b):
    if (a+b) >= 41:
        return 1
    h = [(a+1, b), (a*2, b), (a, b+1), (a, b*2)]
    if any(f(*i) == 1 for i in h): return 'w1'
    if all(f(*i) == 'w1' for i in h): return 'l1'
    if any(f(*i) == 'l1' for i in h): return 'w2'
    if all(f(*i) == 'w2' or f(*i) == 'w1' for i in h): return 'l2'

    return 0

for i in range(1, 32):
    print(f(i, 9), i)"""

#851
"""@lru_cache(None)
def f(a, b):
    if (a+b) > 44: return 1
    h = [(a+1, b), (a*3, b), (a, b+1), (a, b*3)]

    if any(f(*i) == 1 for i in h): return 'w1'
    if all(f(*i) == 'w1' for i in h): return 'l1'
    if any(f(*i) == 'l1' for i in h): return 'w2'
    if all(f(*i) == 'w2' or f(*i) == 'w1' for i in h): return 'l2'

    return 0

for i in range(1, 41):
    print(f(4, i), i)"""

#18
"""@lru_cache(None)
def f(a, b):
    if (a+b) >= 77:
        return 1
    h = [(a+1, b), (a*2, b), (a, b+1), (a, b*2)]
    if any(f(*i) == 1 for i in h): return 'w1'
    if all(f(*i) == 'w1' for i in h): return 'l1'
    if any(f(*i) == 'l1' for i in h): return 'w2'
    if all(f(*i) == 'w2' or f(*i) == 'w1' for i in h): return 'l2'

    return 0

for i in range(1, 70):
    print(f(i, 7), i)"""
           
#102
"""@lru_cache(None)
def f(a, b):
    if a+b >= 59: return 1
    h = [(a+2, b), (a*2, b), (a, b+2), (a, b*2)]
    if any(f(*i) == 1 for i in h): return 'w1'
    if all(f(*i) == 'w1' for i in h): return 'l1'
    if any(f(*i) == 'l1' for i in h): return 'w2'
    if all(f(*i) == 'w2' or f(*i) == 'w1' for i in h): return 'l2'

    return 0

for i in range(1, 54):
    print(f(i, 5), i)"""
    
































    
    

