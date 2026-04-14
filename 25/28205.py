def d(n):
    dels = []
    i = 2
    n0 = n
    while i*i <= n0:
        if n%i == 0:
            dels.append(i)
            n = n//i
        else:
            i += 1
    return dels

def prost(n):
    res = d(n)
    if len(res) == 0:
        return True
    return False

from itertools import *
n = 20262026+1
cou = 0
while cou < 5:
    dels = d(n)
    sums = []
    for x in list(permutations(dels, 2)):
        sums.append(sum(list(x)))
    if 2026 in sums:
        print(n, max(dels))
        cou += 1
    n += 1
