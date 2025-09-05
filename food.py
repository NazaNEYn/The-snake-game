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
        # Calls the constructor of the parent class (Turtle) to initialize it.
        super().__init__()

        # Sets the shape of the food pellet to a circle.
        self.shape("circle")

        # Lifts the pen so the food can move without drawing a line.
        self.penup()

        # Stretches the circle to be a smaller size (14x14 pixels, as the default is 20x20).
        self.shapesize(stretch_len=0.7, stretch_wid=0.7)

        # Sets the color of the food pellet.
        self.color("pink")

        # Sets the animation speed to the fastest possible, so the food appears instantly.
        self.speed("fastest")

        # Calls the refresh_location method to place the food at a random starting location.
        self.refresh_location()

    def refresh_location(self):
        """Moves the food to a new, random location on the screen."""
        # Generates a random x-coordinate within the screen boundaries.
        random_x = random.randint(-280, 280)

        # Generates a random y-coordinate within the screen boundaries.
        random_y = random.randint(-280, 280)

        # Moves the food object to the new random coordinates.
        self.goto(random_x, random_y)
