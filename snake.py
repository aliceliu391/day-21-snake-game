from turtle import Turtle
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.segments = []

        x = 0
        y = 0

        for num in range(0, 3):
            self.add_segment(x, y)
            x -= 20

        self.head = self.segments[0]

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)

        self.head.forward(MOVE_DISTANCE)

    def add_segment(self, x, y):
        t = Turtle()
        t.up()
        t.goto(x, y)
        t.color("white")
        t.shape("square")
        self.segments.append(t)

    def extend(self):
        x = self.segments[-1].xcor()
        y = self.segments[-1].ycor()
        self.add_segment(x, y)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
