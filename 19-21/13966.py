def hod(x):
    if x%2 == 0:
        return (x+2, x*2)
    else:
        return (x+1, x*2)

game = set(range(1, 112))
#print('game', game)

w1 = set([x for x in game if any((step >111) for step in hod(x))])
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

19: 54 (false, ans: 27)
20: 27 52
21: 50
