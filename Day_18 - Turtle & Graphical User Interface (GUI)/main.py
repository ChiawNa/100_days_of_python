from turtle import Turtle, Screen
import random

tim = Turtle()

# draw a square
# for i in range(4):
#     timmy_the_turtle.forward(100)
#     timmy_the_turtle.right(90)


# draw a dashed line
# for _ in range(15):
#     timmy_the_turtle.forward(10)
#     timmy_the_turtle.penup()
#     timmy_the_turtle.forward(10)
#     timmy_the_turtle.pendown()


# # draw a triangle
# for _ in range(3):
#         timmy_the_turtle.color("red")
#         timmy_the_turtle.forward(100)
#         timmy_the_turtle.right(120)

# # draw a square
# for i in range(4):
#     timmy_the_turtle.color("orange")
#     timmy_the_turtle.forward(100)
#     timmy_the_turtle.right(90)

# # draw a pentagon
# for i in range(5):
#     timmy_the_turtle.color("yellow")
#     timmy_the_turtle.forward(100)
#     timmy_the_turtle.right(72)

# # draw a hexagon
# for i in range(6):
#     timmy_the_turtle.color("green")
#     timmy_the_turtle.forward(100)
#     timmy_the_turtle.right(60)

# # draw a heptagon
# for i in range(7):
#     timmy_the_turtle.color("blue")
#     timmy_the_turtle.forward(100)
#     timmy_the_turtle.right(360/7)

# # draw a octagon
# for i in range(8):
#     timmy_the_turtle.color("violet")
#     timmy_the_turtle.forward(100)
#     timmy_the_turtle.right(45)

# # draw a nanogon
# for i in range(9):
#     timmy_the_turtle.color("black")
#     timmy_the_turtle.forward(100)
#     timmy_the_turtle.right(40)

# # draw a decagon
# for i in range(10):
#     timmy_the_turtle.color("pink")
#     timmy_the_turtle.forward(100)
#     timmy_the_turtle.right(36)


# draw different shapes

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]

def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        tim.forward(100)
        tim.right(angle)

for shape_side_n in range(3, 11):
    tim.color(random.choice(colours))
    draw_shape(shape_side_n)

screen = Screen()
screen.exitonclick()

