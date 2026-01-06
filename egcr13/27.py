f = open('27_A_25364.txt')
a = f.readlines()
cl1 = []
cl2 = []

def ro(x1, y1, x2, y2):
    return ((x1 - x2)**2 + (y1 - y2)**2)**0.5

def center(cl):
    min_d = 10**20

    for xi, yi in cl:
        summa = 0
        for xj, yj in cl:
            d = ro(xi, yi, xj, yj)
            summa += d

        if summa < min_d:
            min_d = summa
            point = (xi, yi)
            
    return point


for line in a:
    x, y = map(float, line.replace(',', '.').split())
    if y>10:
        cl1.append((x, y))
    else:
        cl2.append((x, y))

x1, y1 = center(cl1)
x2, y2 = center(cl2)
#print(len(cl1), len(cl2))
print(ro(1, 1, x1, y1)*10000)
print(ro(1, 1, x2, y2)*10000)
p1 = 58605
p2 = 128643
f.close()

f = open('27_B_25364.txt')
cl3, cl4, cl5 = [], [], []
for line in f:
    x, y = map(float, line.replace(',', '.').split())
    if x>23:
        cl3.append((x, y))
    elif y< 22.5:
        cl4.append((x, y))
    else:
        cl5.append((x, y))

x3, y3 = center(cl3)
x4, y4 = center(cl4)
x5, y5 = center(cl5)

#print(len(cl3), len(cl4), len(cl5))
#max len - cl3
q1 = 0
for (x, y) in cl3:
    if ro(x3, y3, x, y) <= 1.2:
        q1 += 1
q2 = 0
for (x, y) in cl3:
    if ro(x3, y3, x, y) <= 0.75:
        q2 += 1
print(p1, p2)
print(q1, q2)

ответ:
58605 128643
358 203
