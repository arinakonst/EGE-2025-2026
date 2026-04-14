def d(n):
    dels = []
    i = 2
    n0 = n
    while i*i <= n0:
        if n%i == 0:
            dels.append(i)
            n = n//i
        else:
            i += 1
    return dels

def prost(n):
    res = d(n)
    if len(res) == 0:
        return True
    return False

n = 5000001
cou = 0
while cou < 5:
    save = 0
    if n%100 == 12:
        dels = d(n)
        for x in dels:
            if dels.count(x) == 5:
                save = x
                break
        if save != 0:
            print(n, save)
            cou += 1
    n += 1
