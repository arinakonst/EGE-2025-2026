def f(s):
    rez = ''
    cou = 0
    pairs = list(product('BCD', repeat = 2))
    flag = 1
    for x in s:    #на то,что именно рядом стоят
        if x in 'BCD':
            rez += '1'
        else:
            rez += '0'
    if ('010' in rez) or (rez[0:2] == '10') or (rez[4:6] == '01'):
        flag = 0
        
    for x in pairs:   #считаем комбинации рядом
        if ','.join(x).replace(',', '') in s:
            cou += 1
            
    if flag == 1 and cou == 1:
        return 1
    return 0
        

from itertools import *
nums = list(product('0123456789ABCD', repeat = 6))
k = 0
mas = []
for num in nums:
    num = ','.join(num).replace(',', '')
    if num[0] != '0' and num.count('4') >= 1:
        if f(num) == 1:
            mas.append(num)
            k += 1

print(k)    #201465
print(mas)
