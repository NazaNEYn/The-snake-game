from turtle import Screen, Turtle
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# Create a Screen object for the game window.
screen = Screen()

# Set the color mode to 255 (RGB) for more color options.
screen.colormode(255)

# Set the title of the game window.
screen.title("Snake Game")

# Set the dimensions of the game window to 600x600 pixels.
screen.setup(600, 600)

# Set the background color of the screen.
screen.bgcolor("#161724")

# Turn off automatic screen updates to control the animation manually.
screen.tracer(0)


# --- Initialize Game Objects ---
# Create instances of the Snake, Food, and Scoreboard classes.
snake = Snake()
food = Food()
scoreboard = Scoreboard()


# --- Set Up Keyboard Listeners ---
# Tell the screen to listen for keyboard input.
screen.listen()

# Bind specific key presses to the corresponding snake movement methods.
screen.onkey(snake.up, "w")
screen.onkey(snake.left, "a")
screen.onkey(snake.bottom, "s")
screen.onkey(snake.right, "d")


# --- Main Game Loop ---
# A boolean variable to control the game's running state.
game_is_running = True

# The main loop that runs the game.
while game_is_running:
    # Manually update the screen to show the new positions of all turtles.
    screen.update()

    # Pause the game for a short duration to control the snake's speed.
    time.sleep(0.1)

    # Move the snake forward one step.
    snake.move()

    # --- Collision Detection with Food ---
    # Check if the snake's head is within 15 pixels of the food.
    if snake.head.distance(food) < 15:
        # Move the food to a new random location.
        food.refresh_location()

        # Add a new segment to the snake's body.
        snake.extend()

        # Increase the score and update the scoreboard display.
        scoreboard.increase_score()

    # --- Collision Detection with Wall ---
    # Check if the snake's head has gone beyond the screen boundaries.
    if (
        snake.head.xcor() > 285
        or snake.head.xcor() < -285
        or snake.head.ycor() > 285
        or snake.head.ycor() < -285
    ):
        # End the game if a wall collision is detected.
        game_is_running = False

        # Display the "Game Over" message on the scoreboard.
        scoreboard.game_over()

    # --- Collision Detection with Body ---
    # Loop through each segment of the snake's body.
    for segment in snake.segments[1:]:
        # Check if the head is close to any body segment.
        if snake.head.distance(segment) < 10:
            # End the game if a body collision is detected.
            game_is_running = False

            # Display the "Game Over" message on the scoreboard.
            scoreboard.game_over()

    # --- Important Note on Self-Collision Loop ---
    # The current loop `for segment in snake.segments` is incorrect for self-collision.
    # It will end the game instantly as the head's distance to the first segment
    # (itself) is 0. A better approach is to loop through all segments except
    # the first one. For example: `for segment in snake.segments[1:]:`

# Keep the window open until the user clicks on it.
screen.exitonclick()
