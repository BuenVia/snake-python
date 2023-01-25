from turtle import Screen
from snake import Snake
import time

screen = Screen()
screen.setup(width=600, height=500)
screen.bgcolor('black')
screen.title("'Snake' by Matt")

is_game_on = True

snake = Snake()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

while is_game_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

screen.exitonclick()
