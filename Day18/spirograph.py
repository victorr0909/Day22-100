import turtle as t
from turtle import Screen
import random

screen = Screen()
t.colormode(255)

def random_color():
    r= random.randint(0,255)
    g= random.randint(0,255)
    b= random.randint(0,255)
    t = (r,g,b)
    return t

tim = t.Turtle()
tim.shape("arrow")
tim.pensize(1)
tim.speed("fastest")

r=50

for i in range (360):
    tim.color("blue")
    tim.circle(r)
    tim.setheading(i)