from turtle import Turtle
import random

BALL_SPEED = 2


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.ball_speed = BALL_SPEED
        self.shape("circle")
        self.color("blue")
        self.penup()
        self.direction = random.choice([-random.randint(15, 45), random.randint(15, 45)]) + 90
        self.setheading(self.direction)
        self.goto(0, -330)

    def randomizer(self):
        self.direction = random.choice([-random.randint(15, 45), random.randint(15, 45)]) + 90
        self.setheading(self.direction)

    def move(self):
        self.forward(self.ball_speed)

    def top_wall_bounce(self):
        new_heading = (360 - self.direction)
        self.direction = new_heading
        self.setheading(new_heading)

    def side_wall_bounce(self):
        new_heading = (540 - self.direction)
        self.direction = new_heading
        self.setheading(new_heading)

    def paddle_bounce(self, distance):
        if abs(distance) > 40:
            if distance > 0:
                new_heading = 150
            else:
                new_heading = 30
        elif abs(distance) > 30:
            if distance > 0:
                new_heading = 135
            else:
                new_heading = 45
        elif abs(distance) > 20:
            if distance > 0:
                new_heading = 120
            else:
                new_heading = 60
        else:
            if distance > 0:
                new_heading = 105
            else:
                new_heading = 75

        self.direction = new_heading + random.randint(-2, 2)
        self.setheading(new_heading)
        self.ball_speed += 0.2

    def reset_position(self):
        self.goto(0, -330)
        self.ball_speed = BALL_SPEED
        self.randomizer()
