game = set(list(range(1, 129)))

def hod(x):
    return (x+1, x*2)

w1 = set([x for x in game if any(step > 128 for step in hod(x))])
print('w1', w1)
game -= w1

l1 = set([x for x in game if all(step in w1 for step in hod(x))])
print('l1', l1)
game -= l1

w2 = set([x for x in game if any(step in l1 for step in hod(x))])
print('w2', w2)
game -= w2

l2 = set([x for x in game if all(step in w1 or step in w2 for step in hod(x))])
print('l2', l2)

#64
#32 63
#62
