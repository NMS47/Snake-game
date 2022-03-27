import time
from turtle import Screen
from food import Food
from functions import Snake
from Scoreboard import ScoreBoard

screen = Screen()
screen.bgcolor("black")
screen.setup(800, 800)
screen.title("Snake Game")
screen.tracer(0)
score = ScoreBoard()

largo = 3
create = Snake(largo)
snake = create.snake
food = Food()
screen.listen()
screen.onkey(create.up, "Up")
screen.onkey(create.down, "Down")
screen.onkey(create.left, "Left")
screen.onkey(create.right, "Right")

game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    if create.hit_wall():
        game_on = False
    create.snake_move()
    if create.head.distance(food) < 18:
        food.refresh()
        score.new_score()
        create.add_new_block()

        print("nom nom")

    for block in create.snake[1:]:
        # print(create.head.position())
        # print(block.position())
        # print("-------")
        if create.head.position() == block.position():
            create.color("white")
            create.penup()
            create.hideturtle()
            create.write("Game over", align="center", font=("Arial", 20, "normal"))
            print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
            game_on = False

screen.exitonclick()
