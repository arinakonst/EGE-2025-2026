def f(s):
    if s.count('n') == 2 and 'nn' in s:
        return 1
    
from itertools import *
nums = list(product('0123456789Annn', repeat = 6))
k = 0
for num in nums:
    num = ','.join(num).replace(',', '')
    if num[0] != '0' and num.count('4') >= 1:
        if f(num) == 1:
            k += 1

print(k)    #196929
