def center(cl):
    mind = 10**20
    for xi, yi in cl:
        summa = 0
        for xj, yj in cl:
            d = ((xi-xj)**2 + (yi-yj)**2)**0.5
            summa += d
        if summa < mind:
            mind = summa
            point = (xi, yi)
    return point

f = open('27a.txt')
f.readline()
cl1 = []
cl2 = []
for i in f:
    x, y = map(float, i.split())
    if x>40:
        cl1.append((x, y))
    else:
        cl2.append((x, y))
        
print(len(cl1), '-- cl1   ', len(cl2), '--cl2')

x1, y1 = center(cl1)  #max len
x2, y2 = center(cl2)   #min len
print(center(cl1))
print(center(cl2))

p1 = x2+y2
p2 = x1+y1
print(p1*10000, p2*10000)
f.close()

f = open('27b.txt')
f.readline()
cl3 = []
cl4 = []
cl5 = []
for i in f:
    x, y = map(float, i.replace(',', '.').split())
    if y>42:
        cl3.append((x, y))
    elif y>32:
        cl4.append((x, y))
    else:
        cl5.append((x, y))

qx, y3 = center(cl3)
x5, qy = center(cl5)

print(qx*10000, qy*10000)
    


    
