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

f = open('27_A.txt')
f.readline()
cl1 = []
cl2 = []
for i in f:
    x, y = map(float, i.replace(',', '.').split())
    if y>10:
        cl1.append((x, y))
    else:
        cl2.append((x, y))

x1, y1 = center(cl1)
x2, y2 = center(cl2)
#print('cl1:', x1, y1)
#print('cl2:', x2, y2)
px = x2
py = y2
print(px*10000, py*10000)
f.close()

f = open('27_B.txt')
f.readline()
cl3 = []
cl4 = []
cl5 = []
for i in f:
    x, y = map(float, i.replace(',', '.').split())
    if y<20:
        cl3.append((x, y))
    elif x<18:
        cl4.append((x, y))
    else:
        cl5.append((x, y))

print(len(cl3), '--cl3  ', len(cl4), '--cl4  ', len(cl5), '--cl5')
x3, y3 = center(cl3)
x4, y4 = center(cl4)
x5, y5 = center(cl5)

q1 = ((x3-x5)**2 + (y3-y5)**2)**0.5

def ro(A, B):
    return ((A[0]-B[0])**2 + (A[1]-B[1])**2)**0.5
    
def maxd(cl):
    x, y = center(cl)
    res = 0
    for star in cl:
        d = ro(star, (x, y))
        if d > res:
            res = d
    return res

ds = []
            
ds.append(maxd(cl3))
ds.append(maxd(cl4))
ds.append(maxd(cl5))

q2 = max(ds)
print(q1*10000, q2*10000)











