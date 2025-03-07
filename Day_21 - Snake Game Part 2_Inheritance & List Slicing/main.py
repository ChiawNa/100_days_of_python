from turtle import Screen
import time
from snake import Snake
from food import Food

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("The Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# position = [(0,0), (-20,0), (-40,0)]
# all_segments = []


# # Create 3 segments
# for i in range(0,3): # 0 - 2
#     segment = Turtle("square")
#     segment.color("white")
#     segment.penup()
#     segment.goto(position[i])
#     all_segments.append(segment)

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

# Detect collision with food
if snake.head.distance(food) < 15:
    food.refresh()

# # moves the segments in reverse order (from the last to the first)
#     for seg_num in range(len(all_segments)-1, 0, -1): # for seg_num in range(2, 0, -1)
#         new_x = all_segments[seg_num-1].xcor()
#         new_y = all_segments[seg_num-1].ycor()
#         all_segments[seg_num].goto(new_x, new_y)

#     all_segments[0].forward(20)


screen.exitonclick()