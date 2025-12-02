from turtle import *
screensize(2000, 2000)
tracer(0)
k = 10
left(90)
penup()
for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x*k, y*k)
        dot(4, 'red')

home()
pendown()
for x in range(95):
    fd(34*k)
    bk(34*k)
    right(48)

penup()
