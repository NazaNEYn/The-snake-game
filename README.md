# Classic Snake Game

![sssss](https://github.com/user-attachments/assets/fe7e534a-04c3-44c9-b572-a923062d4be7)
<br>

A modern take on the classic arcade game, built with Python's `turtle` module. Navigate the snake to eat the food, grow longer, and beat your high score—but be careful not to hit the walls or your own tail!
<br>

### You can check out the demo **[here](https://www.youtube.com/watch?v=ffHKf57doVE)**

<hr>


## Table of Contents
- [About the Game](#about-the-game)
- [Features](#features)
- [How to Play](#how-to-play)
- [Installation](#installation)
- [Project Structure](#project-structure)

## About the Game

This project is a recreation of the classic arcade game "Snake." The player controls a snake that moves around a bounded screen, consuming food to grow longer. The game ends if the snake hits the wall or collides with its own body.

## Features

- **Continuous Movement**: The snake moves forward automatically.
- **Keyboard Controls**: Use the W, A, S, and D keys to change the snake's direction.
- **Growing Snake**: The snake grows longer each time it eats the food.
- **Dynamic Scoreboard**: The score updates in real-time on the screen.
- **Collision Detection**: The game ends if the snake hits the wall or its own body.

## How to Play

Controls
* `W`: Move Up

* `A`: Move Left

* `S`: Move Down

* `D`: Move Right


## Installation

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/NazaNEYn/python-snake-game.git](https://github.com/NazaNEYn/python-snake-game.git)
    ```
2.  **Navigate to the project directory:**
    ```bash
    cd python-snake-game
    ```
3.  **Run the game:**
    ```bash
    python main.py
    ```

## Project Structure

The game is built using Object-Oriented Programming (OOP) principles, with each major component as a separate class for better organization and readability.<br>

.  <br>
├── main.py             # The main game loop and setup <br>
├── snake.py            # Contains the Snake class  <br>
├── food.py             # Contains the Food class  <br>
└── scoreboard.py       # Contains the Scoreboard class  <br>

- **`main.py`**: Initializes the game screen, sets up the game objects (snake, food, scoreboard), and contains the main `while` loop that drives the game logic.
- **`snake.py`**: Defines the `Snake` class, which handles the creation, movement, and direction of the snake's body segments.
- **`food.py`**: Defines the `Food` class, which handles the food's appearance and its random placement on the screen.
- **`scoreboard.py`**: Defines the `Scoreboard` class, responsible for tracking and displaying the player's score and the "Game Over" message.

