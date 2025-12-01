from itertools import *

def fun(s):
    s2 = ''
    for x in s:
        if x in 'гпрбл':
            s2 += '1'
        elif x in 'иеоа':
            s2 += '0'
    if s2[0] != '0' and s2[-1] != '0' and '101' not in s2:
        return 1
    else:
        return 0
    
k = 0
a = list(product('гипербола', repeat = 6))
for x in a:
    if fun(x) == 1:
        k += 1

print(k)    #68025
