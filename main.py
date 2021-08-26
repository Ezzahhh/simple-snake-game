from scoreboard import Scoreboard
from turtle import Screen
import time
from snake import Snake
from food import Food

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0, 1)

game_running = True
snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()

screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)

while game_running:
    screen.update()
    time.sleep(0.05)
    snake.move()

    if abs(snake.head.xcor()) >= 290 or abs(snake.head.ycor()) >= 290:
        scoreboard.reset()
        snake.reset()

    for snk in snake.snake_parts[1:]:
        if snake.head.distance(snk) <= 10:
            scoreboard.reset()
            snake.reset()

    if snake.head.distance(food) < 18:
        food.new_location()
        snake.add_snake_part()
        scoreboard.add_score()

screen.exitonclick()
