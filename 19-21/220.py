def hod(x):
    return (x+1, x+5, x*3)

game = set(list(range(1, 41)))
win1 = set([x for x in game if any(step > 40 for step in hod(x))])
print('win1', win1)
game -= win1

los1 = set([x for x in game if all(step in win1 for step in hod(x))])
print('los1', los1)
game -= los1

win2 = set([x for x in game if any(step in los1 for step in hod(x))])
game -= win2
print('win2', win2)

los2 = set([x for x in game if all(step in win1|win2 for step in hod(x))])
print('los2', los2)
#19 - 13
#20 - 812
#21 - 711
