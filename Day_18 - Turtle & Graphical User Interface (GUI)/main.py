from turtle import Turtle, Screen

timmy_the_turtle = Turtle()

for i in range(4):
    timmy_the_turtle.forward(100)
    timmy_the_turtle.right(90)

for _ in range(15):
    timmy_the_turtle.forward(10)
    timmy_the_turtle.penup()
    timmy_the_turtle.forward(10)
    timmy_the_turtle.pendown()


screen = Screen()
screen.exitonclick()

