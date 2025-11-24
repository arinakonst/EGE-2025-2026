#24760
def center(cl):
    min_d = 10**20

    for xi, yi in cl:
        summa = 0
        for xj, yj in cl:
            d = ((xi-xj)**2 + (yi-yj)**2)**0.5
            summa += d

        if summa < min_d:
            min_d = summa
            point = (xi, yi)

    return point

f = open('27A.txt')
f.readline()
cl1 = []
cl2 = []
for i in f:
    x, y = map(float, i.split())
    if x>10:
        cl1.append((x, y))
    else:
        cl2.append((x, y))

print(len(cl1), len(cl2))

x1, y1 = center(cl1)
x2, y2 = center(cl2)
sredxA = (x1+x2)/2*10000
sredyA = (y1 + y2)/2*10000
print(sredxA, sredyA)
f.close()

f = open('27B.txt')
f.readline()
cl3 = []
cl4 = []
cl5 = []

for i in f:
    x, y = map(float, i.split())
    if y>20:
        cl3.append((x, y))
    elif x>10:
        cl4.append((x, y))
    else:
        cl5.append((x, y))

x3, y3 = center(cl3)
x4, y4 = center(cl4)
x5, y5 = center(cl5)
print((x4+x5+x3)/3*10000)
print((y3+y4+y5)/3*10000)
f.close()

#24898
f = open('27_A.txt')
f.readline()
cl1 = []
cl2 = []
for i in f:
    x, y = map(float, i.split())
    if x<40:
        cl1.append((x, y))
    else:
        cl2.append((x, y))

print(len(cl1), 'cl1')
print(len(cl2), 'cl2')

x1, y1 = center(cl1)
x2, y2 = center(cl2)

p1 = (x1 + y1)*10000
p2 = (x2 + y2)*10000
print(p1, p2)
f.close()

f = open('27_B.txt')
f.readline()
cl3 = []
cl4 = []
cl5 = []
for i in f:
    x, y = map(float, i.split())
    if x>10:
        if y > 42:
            cl3.append((x, y))
        elif y > 32:
            cl4.append((x, y))
        else:
            cl5.append((x, y))

x3, y3 = center(cl3)
x4, y4 = center(cl4)
x5, y5 = center(cl5)

qx = x3
qy = y5
print(qx*10000, qy*10000)

        



















    
