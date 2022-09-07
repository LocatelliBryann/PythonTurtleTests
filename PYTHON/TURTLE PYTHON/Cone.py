from turtle import *

speed(0)
bgcolor('black')
color('orange')
hideturtle()

n = 1
p = True

while True:
    circle(n)
    if p:
        n = n - 1
    else:
        n = n + 1
