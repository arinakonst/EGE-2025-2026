from turtle import *
screensize(3000, 3000)
tracer(0)
k = 10
left(90)
penup()
for x in range(-80, 80):
    for y in range(-80, 80):
        goto(x*k, y*k)
        dot(3, 'red')


goto(0, 0)
down()
fd(30*k); left(60); fd(24*k); right(240)
fd(54*k); left(120); fd(24*k); left(60)
dot(4, 'green')
penup()
fd(30*k)
right(90)
fd(20*k)
left(90)
dot(5, 'green')
down()
for i in range(17):
    fd(6*k)
    left(90)
    fd(80*k)
    left(90)

update()
done()
