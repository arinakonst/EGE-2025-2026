a = 7*512**120 - 6*64**100 + 8**210 - 255

def perevod(x, p):
    alpha = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    res = ''
    while x != 0:
        res += alpha[x%p]
        x = x//p

    return res[::-1]

for p in range(2, 37):
    res = perevod(a, p)
    if res[-3::] == '001':
        print(p)     #2, потом 4
#ans: 4
