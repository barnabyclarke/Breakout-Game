from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 15, "normal")
with open("data.txt") as score_data:
    CONTENTS = int(score_data.read())


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.player_score = 0
        self.high_score = CONTENTS
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(x=0, y=280)

    def new_score(self):
        self.player_score += 1

    def reset(self):
        if self.player_score > self.high_score:
            self.high_score = self.player_score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.player_score = 0
        self.score()

    def score(self):
        self.clear()
        self.write(f"Score: {self.player_score} High Score: {self.high_score}", move=False, align=ALIGNMENT, font=FONT)
