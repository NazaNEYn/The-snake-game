from turtle import Turtle
import random

# The following two variables are defined but not used in the class.
# They can be removed as they are not needed for the code to run correctly.
# random_x_cor = random.randint(-280, 280)
# random_y_cor = random.randint(-280, 280)


class Food(Turtle):
    """
    A class to represent the food pellet in the snake game.
    It inherits from the `Turtle` class to use its drawing capabilities.
    """

    def __init__(self):
        """Initializes the Food object with a specific shape, size, and color."""
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.7, stretch_wid=0.7)
        self.color("pink")
        self.speed("fastest")
        self.refresh_location()

    def refresh_location(self):
        """Moves the food to a new, random location on the screen."""
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
