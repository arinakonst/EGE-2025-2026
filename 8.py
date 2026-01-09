from itertools import *
words = list(product('агдейсэ', repeat = 6))
k = 0
for i in range(len(words)):
    x = ''.join(words[i])
    if 'егэ' in x:
        k += (i+1)

print(k)  #79143659
