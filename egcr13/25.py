def f(n):
    dels = []
    for d in range(2, n//2 + 1):
        if n%d == 0:
            dels.append(d)

    for x in dels:
        if x%100 == 11 and x!= 11:
            return x
    return 0

num = 1350051
cou = 0

while num:
    res = f(num)
    if res != 0:
        print(num, res)
        cou += 1
    if cou == 5:
        break
    num += 1

ответ:
1350051 311
1350055 270011
1350062 511
1350063 40911
1350066 225011
