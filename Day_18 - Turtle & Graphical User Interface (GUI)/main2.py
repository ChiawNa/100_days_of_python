from turtle import Turtle
import random

tim = Turtle()
directions = [0, 90, 180, 270]  # Possible directions: right, up, left, down
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
tim.pensize(10)
tim.speed(10)

for _ in range(200):
    tim.color(random.choice(colours))
    tim.forward(30)
    tim.setheading(random.choice(directions))


