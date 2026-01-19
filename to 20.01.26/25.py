def prost(n):
    cou = 0
    dels = []
    for i in range(2, int(n**0.5)+1):
        if n%i == 0:
            cou += 1
            if n != i*i:
                dels.append(i)
                dels.append(n/i)
            else:
                dels.append(i)
    if cou == 0:
        return 0
    return sum(dels)

k = 0
for n in range(1500000, 2000000):
    r = prost(n)
    if r != 0 and prost(r) == 0:
        print(n, r)
        k += 1
        if k == 5:
            break
#1500022 755233.0
#1500046 882433.0
#1500072 2786327.0
#1500120 3552839.0
#1500126 1658273.0
