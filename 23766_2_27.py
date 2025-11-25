f = open('27_A_24898.txt')
f.readline()
cl1 = []
cl2 = []
for i in f:
    x, y = map(float, i.replace(',', '.').split())
    if y > 90:
        cl1.append((x, y))
    else:
        cl2.append((x, y))

def ro(a, b):
    return ((a[0]-b[0])**2 + (a[1]-b[1])**2)**0.5

def center(cl):
    mind = 10**20
    for xi, yi in cl:
        summa = 0
        for xj, yj in cl:
            summa += ro((xi, yi), (xj, yj))
        if summa < mind:
            mind = summa
            point = (xi, yi)

    return point

x1, y1 = center(cl1)
x2, y2 = center(cl2)
#print(len(cl1), 'cl1     ', len(cl2), 'cl2')   #cl2 длиннее
p1 = (x1+y1)*10000
p2 = (x2+y2)*10000
print(p1, p2)
f.close()

f = open('27_B_24898.txt')
f.readline()
cl3 = []
cl4 = []
cl5 = []
for i in f:
    x, y = map(float, i.replace(',', '.').split())
    if y > 41:
        cl3.append((x, y))
    elif y<33:
        cl5.append((x, y))
    else:
        cl4.append((x, y))

x3, y3 = center(cl3)
x4, y4 = center(cl4)
x5, y5 = center(cl5)
#print(ro((x4, y4), (0, 0)), ro((x5, y5), (0, 0)))
qx = x3*10000
qy = y5*10000
print(qx, qy)












      
