from turtle import Turtle
import random
LIMIT = 350


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("red")
        self.shapesize(0.5, 0.5)
        self.goto(random.randint(-LIMIT, LIMIT), random.randint(-LIMIT, LIMIT))
        self.refresh()

    def refresh(self):
        self.goto(random.randint(-LIMIT, LIMIT), random.randint(-LIMIT, LIMIT))



