f = open('9.csv')
from csv import *
a = f.readlines()
for line in a:
    line = list(map(int, line.split(',')))
    if sorted(line) == line and len(line) == len(set(line)):
        c2, c1 = 0, 0
        for num in line:
            if num%2 == 0:
                c2 += 1
            else:
                c1 += 1
        if c2 == c1:
            print(sum(line))    #1119
            break
