def to3(n):
    s = ''
    while n!=0:
        s += str(n%3)
        n = n//3
    return s[::-1]

def f(n):
    n3 = to3(n)
    if n%3 == 0:
        res = n3 + n3[-2] + n3[-1]
    else:
        summa = 0
        for x in n3:
            summa += int(x)
        summa *= 3
        res = n3 + to3(summa)

    return int(res, 3)

mas = []
for n in range(1, 100):
    r = f(n)
    if r > 208:
        #print(n, r)
        mas.append(r)

print(sorted(mas))  #1ый подходящий - 243
