from turtle import Turtle

with open('high_score.txt') as t:
    HIGH_SCORE = int(t.read())


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = HIGH_SCORE
        self.color("white")
        self.penup()
        self.hideturtle()
        self.sety(240)
        self.new_score()

    def new_score(self):
        self.clear()
        self.write(f"Score: {self.score}  High Score: {self.high_score}", align="center", font=("Arial", 20, "normal"))
        self.score += 1

    def new_high_score(self):
        print(self.score)
        print(self.high_score)
        if self.high_score < self.score:
            self.high_score = self.score
            with open('high_score.txt', mode='w') as text:
                text.write(str(self.score))
                print("escribido")



