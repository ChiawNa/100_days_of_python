from turtle import Turtle

POSITION = [(0,0), (-20,0), (-40,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        self.all_segments = []
        self.create_snake()

    def create_snake(self):

        # Create 3 segments
        for i in range(0,3): # 0 - 2
            segment = Turtle("square")
            segment.color("white")
            segment.penup()
            segment.goto(POSITION[i])
            self.all_segments.append(segment)

    def move(self):

        # moves the segments in reverse order (from the last to the first)
        for seg_num in range(len(self.all_segments)-1, 0, -1): # for seg_num in range(2, 0, -1)
            new_x = self.all_segments[seg_num-1].xcor()
            new_y = self.all_segments[seg_num-1].ycor()
            self.all_segments[seg_num].goto(new_x, new_y)

        self.all_segments[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.all_segments[0].heading() != DOWN:
            self.all_segments[0].setheading(UP)

    def down(self):
        if self.all_segments[0].heading() != UP:
            self.all_segments[0].setheading(DOWN)

    def left(self):
        if self.all_segments[0].heading() != RIGHT:
            self.all_segments[0].setheading(LEFT)
    
    def right(self):
        if self.all_segments[0].heading() != LEFT:
            self.all_segments[0].setheading(RIGHT)