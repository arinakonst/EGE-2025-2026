#18548_8
from itertools import *
def f(s):
    if s[0] != 'е' and s[-1] not in 'бж':
        if 'еее' not in s and 'ббб' not in s and 'жжж' not in s:
            if s[5:8] == 'ебж':
                return 1
    return 0

def to_str(tupl):
    s = ''
    for x in tupl:
        s += x
    return s

k = 0     
words = list(product('ебж', repeat = 13))
for x in words:
    x = to_str(x)
    if f(x) == 1:
        k += 1
print(k)  #6050

#18549_9
from csv import *

def povtor(spisok):
    for x in set(spisok):
        if spisok.count(x) == 3:
            return x
    return 0

def f141(s, alls):
    for num in set(s):
        if alls.count(num) == 142:
            return 1
    return 0

f = open('9_18549.csv')
a = f.readlines()
alls = []
for s in a:
    s = list(map(int, s.split(';')))
    for num in s:
        alls.append(int(num))
        
for s in a:
    s = list(map(int, s.split(';')))
    if len(set(s)) == 3:
        if povtor(s)%2 == 1:
            if f141(s, alls) == 1:
                print(s)  #выведет 2 строки, ответ - 2

#18552_12             
def f(s):
    while '18' in s or '388' in s or '888' in s:
        if '18' in s:
            s = s.replace('18', '1')
        if '388' in s:
            s = s.replace('388', '83')
        if '888' in s:
            s = s.replace('888', '3')
    return s

cou = 0
for n in range(4, 10000+1):
    s = '1'+'8'*n
    s2 = f(s)
    if s2.count('3') == 7:
        print(s2)
        cou += n

print(cou) #69
        
    
        



        

                    
    
