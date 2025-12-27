f = open('17.txt')
a = list(map(int, f.readlines()))

def f(mas):
    c = 0
    for x in mas:
        if len(str(abs(x))) == 4:
            c += 1
    if c >= 2:
        return 1
    return 0

k = 0
sums = []
mins =[]
for n in a:
    if n > 0 and len(str(n)) == 4:
        mins.append(n)

minim = min(mins)
for i in range(0, len(a)-2):
    n1, n2, n3 = a[i], a[i+1], a[i+2]
    if f([n1, n2, n3]) == 1 and sum([n1, n2, n3]) <= minim:
        sums.append(sum([n1, n2, n3]))
        k += 1
print(k)
print(max(sums))
