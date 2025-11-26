d = {}

for x in range(0, 15):
    d[x] = []
    for y in range(0, 15):
        a = 2 + x*14 + 5*14**2 + y*14**3 + 4*14**4 + 1*14**5
        b = 3 + y*14 + 2*14**2 + x*14**3 + 1*14**4 + 3*14**5
        s = a+b
        if s%9 == 0:
            d[x].append(s)

minim = 0
print(d.values())
for x in d:
    print(x, ':', d[x])
    
