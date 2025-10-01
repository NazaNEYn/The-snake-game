from turtle import Turtle


class Scoreboard(Turtle):
    """
    A class to manage and display the game score.
    It inherits from the `Turtle` class to use its text-writing capabilities.
    """

    def __init__(self):
        super().__init__()
        with open("highscore.txt") as file:
            self.highscore = int(file.read())
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        """Clears the previous score and writes the current score on the screen."""
        self.clear()
        self.goto(0, 270)
        self.write(
            f"Score: {self.score}   High Score: {self.highscore}",
            align="center",
            font=("lato", 15, "bold"),
        )

    def increase_score(self):
        """Increments the score by one and updates the display."""
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("highscore.txt", "w") as file:
                file.write(str(self.highscore))
        self.score = 0
        self.update_scoreboard()

    # def game_over(self):
    #     """Displays the 'Game Over!!' message in the center of the screen."""
    #     self.goto(0, 0)
    #     self.write("Game Over!!", align="center", font=("Game Over", 60, "normal"))
