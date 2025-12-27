from csv import *
f = open('9.csv')
a = f.readlines()

def f(line):
    cou = 0
    for num in line:
        if num%2 == 0:
            cou += 1
    if cou == 3:
        return 1
    return 0
            
for s in a:
    s = list(map(int, s.split(',')))
    if s == sorted(s) and f(s) == 1:
        print(sum(s))   #855
        break

