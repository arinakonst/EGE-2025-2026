def dels(num):
    d = []
    for x in range(2, int(num**0.5)+1):
        if num%x == 0:
            d.append(x)
            if x != num%x:
                d.append(num//x)

    return d

n = 6500000
cou = 1
while cou < 6:
    itog = dels(n)
    if len(itog) != 0:
        k = str(max(itog) + min(itog))
        if len(dels(n)) == 6 and len(k) == 4:
            print(n, k, cou)
            cou += 1
    n += 1

