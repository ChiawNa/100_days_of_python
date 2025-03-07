from turtle import Turtle
import random

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5) #default is 20x20, so now becomes 10x10
        self.color("blue")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = random.randint(-280, 280) #basically the x-axis and y-axis is from -300 to 300
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)

        