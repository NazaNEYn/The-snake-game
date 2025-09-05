from turtle import Turtle


class Scoreboard(Turtle):
    """
    A class to manage and display the game score.
    It inherits from the `Turtle` class to use its text-writing capabilities.
    """

    def __init__(self):
        """Initializes the Scoreboard object and sets up its initial state."""
        # Calls the constructor of the parent class (Turtle) to inherit its properties.
        super().__init__()

        # Initializes the score attribute to 0.
        self.score = 0

        # Sets the text color to white.
        self.color("white")

        # Lifts the pen to prevent drawing a line when moving the turtle.
        self.penup()

        # Hides the turtle icon from the screen.
        self.hideturtle()

        # Calls the method to display the initial score on the screen.
        self.update_scoreboard()

    def update_scoreboard(self):
        """Clears the previous score and writes the current score on the screen."""
        # Clears any previously written text by this turtle.
        self.clear()

        # Moves the turtle to the top-center position for the score display.
        self.goto(0, 270)

        # Writes the formatted score string to the screen.
        self.write(f"Score: {self.score}", align="center", font=("lato", 15, "bold"))

    def increase_score(self):
        """Increments the score by one and updates the display."""
        # Adds 1 to the current score.
        self.score += 1

        # Calls the update method to reflect the new score on the screen.
        self.update_scoreboard()

    def game_over(self):
        """Displays the 'Game Over!!' message in the center of the screen."""
        # Moves the turtle to the center of the screen.
        self.goto(0, 0)

        # Writes the "Game Over!!" message.
        self.write("Game Over!!", align="center", font=("Game Over", 60, "normal"))
