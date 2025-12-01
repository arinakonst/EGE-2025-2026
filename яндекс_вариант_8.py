from itertools import *

def fun(s):
    s2 = ''
    for x in s:
        if x in 'гпрбл':
            s2 += '1'
        else:
            s2 += '0'
    if s[0] != '0' and s[-1] != '0' and '101' not in s:
        return 1
    else:
        return 0
    
word =''
k = 0
for a in 'гипербола':
    word += a
    for b in 'гипербола':
        word += b
        for c in 'гипербола':
            word += c
            for d in 'гипербола':
                word += d
                for e in 'гипербола':
                    word += e
                    for f in 'гипербола':
                        word += f
                        if fun(word) == 1:
                            k += 1
                        word = ''

print(k)    #531441
