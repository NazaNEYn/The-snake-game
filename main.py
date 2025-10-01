from turtle import Screen, Turtle
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.colormode(255)

screen.title("Snake Game")
screen.setup(600, 600)
screen.bgcolor("#161724")
screen.tracer(0)


snake = Snake()
food = Food()
scoreboard = Scoreboard()


screen.listen()

screen.onkey(snake.up, "w")
screen.onkey(snake.left, "a")
screen.onkey(snake.bottom, "s")
screen.onkey(snake.right, "d")


game_is_running = True

while game_is_running:
    screen.update()
    time.sleep(0.1)

    snake.move()

    # --- Collision Detection with Food ---
    # Check if the snake's head is within 15 pixels of the food.
    if snake.head.distance(food) < 15:
        food.refresh_location()
        snake.extend()

        scoreboard.increase_score()

    # --- Collision Detection with Wall ---
    # Check if the snake's head has gone beyond the screen boundaries.
    if (
        snake.head.xcor() > 285
        or snake.head.xcor() < -285
        or snake.head.ycor() > 285
        or snake.head.ycor() < -285
    ):

        scoreboard.reset()
        snake.reset()

    # --- Collision Detection with Body ---
    # Loop through each segment of the snake's body.
    for segment in snake.segments[1:]:
        # Check if the head is close to any body segment.
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()

    # --- Important Note on Self-Collision Loop ---
    # The current loop `for segment in snake.segments` is incorrect for self-collision.
    # It will end the game instantly as the head's distance to the first segment
    # (itself) is 0. A better approach is to loop through all segments except
    # the first one. For example: `for segment in snake.segments[1:]:`

screen.exitonclick()
