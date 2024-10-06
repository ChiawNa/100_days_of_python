from turtle import Turtle, Screen
import random

# Object State and Instances 

# def move_forwards():
#     tim.forward(10)

# def move_backwards():
#     tim.backward(10)

# def counter_clockwise():
#     tim.left(10)

# def clockwise():
#     tim.right(10)

# def clear():
#     tim.reset()

# screen.listen()
# screen.onkey(move_forwards, "w")
# screen.onkey(move_backwards, "s")
# screen.onkey(counter_clockwise, "a")
# screen.onkey(clockwise, "d")
# screen.onkey(clear, "c")


# Understand the turtle coordinate system

race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "yellow", "blue", "purple", "green", "orange"]
Y_positions = [-100, -50, 0, 50, 100, 150]
all_turtles = []

# Create 6 turtles
for turtle_num in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_num])
    new_turtle.goto(x=-230, y=Y_positions[turtle_num])
    all_turtles.append(new_turtle)

if user_bet:
    race_on = True

while race_on:
    for turtle in all_turtles:

        distance = random.randint(0, 10)
        turtle.forward(distance)
    
        #230 is 250 - half the width of the turtle.
        if turtle.xcor() > 230:
            race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won. The winner is {winning_color} turtle.")
            else:
                print(f"You've lose. The winner is {winning_color} turtle.")


screen.exitonclick()