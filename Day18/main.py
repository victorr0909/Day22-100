from turtle import Turtle , Screen

timmy = Turtle()
timmy.shape("turtle")  
timmy.color("gray20")

for i in range (0,10):
    timmy.forward(10)
    timmy.penup()
    timmy.forward(10)
    timmy.pendown()
    timmy.forward(10)
    timmy.penup()

screen = Screen()
screen.exitonclick()