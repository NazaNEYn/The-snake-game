from turtle import Turtle

# A constant list of tuples representing the initial positions of the snake segments.
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]

# A constant integer representing the distance the snake moves in one step.
MOVE_DISTANCE = 20


class Snake:
    """
    A class to represent the snake in the game.
    It manages the snake's body segments, movement, and direction.
    """

    def __init__(self):
        """Initializes the Snake object with an empty list of segments."""
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        """Creates the initial three-segment snake body."""
        for position in STARTING_POSITION:
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)

    def reset(self):
        for segment in self.segments:
            segment.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def extend(self):
        """Adds a new segment to the end of the snake."""
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()

        # Gets the position of the last segment to place the new one.
        last_segment_position = self.segments[-1].position()
        new_segment.goto(last_segment_position)
        self.segments.append(new_segment)

    def move(self):
        """Moves the snake forward by having each segment follow the one in front of it."""
        # Loops backward from the second-to-last segment down to the first.
        for seg_num in range(len(self.segments) - 1, 0, -1):
            # Gets the coordinates of the segment in front.
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()

            # Moves the current segment to the position of the segment in front.
            self.segments[seg_num].goto(new_x, new_y)

        # Moves the head forward by the defined distance.
        self.segments[0].forward(MOVE_DISTANCE)

    def up(self):
        """Changes the snake's head direction to face upwards."""
        self.head.setheading(90)

    def left(self):
        """Changes the snake's head direction to face left."""
        self.head.setheading(180)

    def bottom(self):
        """Changes the snake's head direction to face downwards."""
        self.head.setheading(270)

    def right(self):
        """Changes the snake's head direction to face right."""
        self.head.setheading(0)
