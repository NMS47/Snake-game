from turtle import Turtle

LIMIT = 370


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.sety(320)
        self.write(f"Score: {self.score}", align="center", font=("Arial", 20, "normal"))

    def new_score(self):
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score}", align="center", font=("Arial", 20, "normal"))

