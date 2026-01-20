def hod(x):
    res = set()
    if (x*3) %2 == 1:
        res.add(x*3)
    else:
        res.add(0)
    if (x+1)%2 == 1:
        res.add(x+1)
    else:
        res.add(0)
    if (x+3) %2 == 1:
        res.add(x+3)
    else:
        res.add(0)
    if res != {0}:
        res.remove(0)
    return res

game = set(range(1, 51))
print('game', game)

w1 = set([x for x in game if any((step >50) for step in hod(x))])
print('w1', w1)
game -= w1

l1 = set([x for x in game if all((step in w1) for step in hod(x))])
print('l1', l1)
game -= l1

w2 = set([x for x in game if any((step in l1) for step in hod(x))])
print('w2', w2)
game -= w2

l2 = set([x for x in game if all((step in w1|w2) for step in hod(x))])
print('l2', l2)

19: 7
20: 12 14
21: 2

         

