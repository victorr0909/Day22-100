import turtle as t
from turtle import Screen
import random

tim = t.Turtle()
tim.shape("arrow")
t.colormode(255)

def random_color():
    r= random.randint(0,255)
    g= random.randint(0,255)
    b= random.randint(0,255)
    t = (r,g,b)
    return t

directions = [0, 90, 180, 270]
tim.pensize(15)
tim.speed("fastest")

for _ in range(200):
    tim.color(random_color())
    tim.forward(30)
    tim.setheading(random.choice(directions))
