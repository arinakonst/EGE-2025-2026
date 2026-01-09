from csv import *
f = open('9_25278.csv')
a = f.readlines()

def f(s):
    cou = 0
    if len(set(s)) == len(s)-2:
        cou += 1
    sum1, sum2 = 0, 0
    for x in s:
        if s.count(x) == 3:
            sum1 += int(x)
        else:
            sum2 += int(x)

    if sum2 <= sum1:
        cou += 1
    if cou == 2:
        return 1
    return 0

def p(s):
    p = 1
    for x in s:
        if s.count(x) == 1:
            p *= x
    return p

maxim = 0
for s in a:
    s = list(map(int, s.split(',')))
    if f(s):
        if p(s) > maxim:
            ans = sum(s)
            maxim = p(s)

print(ans)  #1171
