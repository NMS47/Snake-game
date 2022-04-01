import time
from turtle import Screen
from food import Food
from functions import Snake
from Scoreboard import ScoreBoard

screen = Screen()
screen.bgcolor("black")
screen.setup(600, 600)
screen.title("Snake Game")
screen.tracer(0)


largo = 3


keep_playing = True
game_on = True
food = Food()

while keep_playing:
    create = Snake(largo)
    score = ScoreBoard()
    snake = create.snake
    screen.listen()
    screen.onkey(create.up, "Up")
    screen.onkey(create.down, "Down")
    screen.onkey(create.left, "Left")
    screen.onkey(create.right, "Right")
    while game_on:
        screen.update()
        time.sleep(0.1)
        if create.hit_wall():
            score.new_high_score()
            game_on = False
        create.snake_move()
        if create.head.distance(food) < 18:
            food.refresh()
            score.new_score()
            create.add_new_block()

        for block in create.snake:
            if not create.head == block:
                if create.head.distance(block) < 10:
                    game_on = False

    if screen.textinput("Game Over",  "Keep playing? y or n: ") == "y":
        create.remake()
        score.clear()
        screen.update()
        game_on = True
    else:
        keep_playing = False
        screen.bgcolor("white")
screen.exitonclick()
