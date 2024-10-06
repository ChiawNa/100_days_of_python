from turtle import Turtle, Screen
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("The Snake Game")
screen.tracer(0)


position = [(0,0), (-20,0), (-40,0)]
all_segments = []


# Create 3 segments
for i in range(0,3): # 0 - 2
    segment = Turtle("square")
    segment.color("white")
    segment.penup()
    segment.goto(position[i])
    all_segments.append(segment)

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)

# moves the segments in reverse order (from the last to the first)
    for seg_num in range(len(all_segments)-1, 0, -1): # for seg_num in range(2, 0, -1)
        new_x = all_segments[seg_num-1].xcor()
        new_y = all_segments[seg_num-1].ycor()
        all_segments[seg_num].goto(new_x, new_y)

    all_segments[0].forward(20)

# segment_1 = Turtle("square")
# segment_1.color("white")

# segment_2 = Turtle("square")
# segment_2.color("white")
# segment_2.goto(-20, 0)

# segment_3 = Turtle("square")
# segment_3.color("white")
# segment_3.goto(-40, 0)


screen.exitonclick()