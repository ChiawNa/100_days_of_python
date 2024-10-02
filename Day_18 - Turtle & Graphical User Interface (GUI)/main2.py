# from turtle import Turtle
# import random

# tim = Turtle()
# directions = [0, 90, 180, 270]  # Possible directions: right, up, left, down
# colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
# tim.pensize(10)
# tim.speed(10)

# for _ in range(200):
#     tim.color(random.choice(colours))
#     tim.forward(30)
#     tim.setheading(random.choice(directions))

import turtle as t 
import random

tim = t.Turtle()
t.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)    
    b = random.randint(0, 255)
    
    random_color = (r,g,b)
    return random_color


directions = [0, 90, 180, 270]  # Possible directions: right, up, left, down
tim.pensize(10)
tim.speed(10)

for _ in range(200):
    tim.color(random_color())
    tim.forward(30)
    tim.setheading(random.choice(directions))