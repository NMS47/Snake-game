from turtle import Turtle
MOVE_FORWARD = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
LIMIT = 370


class Snake(Turtle):

    def __init__(self, largo):
        super().__init__()
        self.snake = []
        self.largo = largo
        self.start_position()
        self.head = self.snake[0]
        self.tail = self.snake[-1]

    def start_position(self):
        """Set the starting snake"""
        x = 0
        for block in range(self.largo):
            block = Turtle("square")
            block.color("white")
            block.penup()
            block.setx(x)
            block.speed(20)
            self.snake.append(block)
            x -= 23

    def add_new_block(self):
        block = Turtle("square")
        block.color("white")
        block.penup()
        block.goto(self.tail.position())
        block.speed(20)
        self.snake.append(block)
        self.largo += 1

    def hit_wall(self):
        conditions = [
            self.head.xcor() >= LIMIT,
            self.head.ycor() >= LIMIT,
            self.head.xcor() <= -LIMIT,
            self.head.ycor() <= -LIMIT,
        ]
        if any(conditions):
            self.color("white")
            self.penup()
            self.hideturtle()
            self.write("Game over",  align="center", font=("Arial", 20, "normal"))
            return True

    def snake_move(self):
        """The snake starts moving forwards"""
        reverse_snake = self.snake[::-1]
        i = 1
        for block in reverse_snake[0:-1]:
            new_x = reverse_snake[i].xcor()
            new_y = reverse_snake[i].ycor()
            block.goto(new_x, new_y)
            i += 1
        self.head.forward(MOVE_FORWARD)

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