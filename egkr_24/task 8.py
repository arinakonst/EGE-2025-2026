def f(s):
    rez = ''
    cou =0
    pairs = list(product('BCD', repeat = 2))
    flag = 1
    for x in s:
        if x in 'BCD':
            rez += '1'
        else:
            rez += '0'
    #print(rez)
    if '010' in rez or rez[0:2] == '10' or rez[4:6] == '01':
        flag = 0
    #print('flag 1 -- ', flag)
        
    for x in pairs:
        if ','.join(x).replace(',', '') in s:
            #print(x)
            if cou > 0:
                flag = 0
            if cou == 0:
                cou += 1
    if cou == 0:
        flag = 0

    if flag == 1:
        return 1
    return 0
        

from itertools import *
nums = list(product('0123456789ABCD', repeat = 6))
k = 0
for num in nums:
    num = ','.join(num).replace(',', '')
    if num[0] != '0' and num.count('4') >= 1:
        if f(num) == 1:
            k += 1

print(k)    #201465
