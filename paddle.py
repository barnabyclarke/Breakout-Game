from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("white")
        self.shapesize(1, 5)
        self.goto(position)

    def position(self, event):
        i = event.x
        self.goto(i - 300, -350)
