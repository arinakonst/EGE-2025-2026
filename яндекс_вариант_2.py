print('a', 'c', 'b', 'd', 'F')
for a in (0, 1):
    for b in (0, 1):
        for c in (0, 1):
            for d in (0, 1):
                F = (((a and b) <= c) and ((b and c) <= d))
                if F == 0:
                    print(a, c, b, d, F)

