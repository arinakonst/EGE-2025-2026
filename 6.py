from turtle import *
tracer(0)
k = 10
screensize(2000, 2000)
left(90)
up()
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x*k, y*k)
        dot (3, 'red')

home()
down()
for i in range(101):
    fd(10*k)
    left(90)
    fd(4*k)
up()

fd(5*k)
right(90)

down()

for i in range(201):
    bk(12*k)
    right(90)

for i in range(301):
    fd(11*k)
    left(90)
    fd(4*k)

home()
update()
        
