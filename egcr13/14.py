def to27(n):
    s = ''
    a = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    while n != 0:
        s += a[n%27]
        n = n//27
    return s[::-1]

for x in range(1, 1000):
    r = 3*27**9 + 2*27**6 + 27**3 - x
    if to27(r).count('0') == 6:
        print(x)
        break   #27
