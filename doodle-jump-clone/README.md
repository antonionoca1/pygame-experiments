# Doodle Jump (Pygame)

A simple, addictive vertical platformer game implemented in Python using Pygame. Guide your character upwards by jumping on platforms, avoiding obstacles, and collecting points.

## Features

- **Vertical Scrolling:** The game world scrolls as the player ascends.
- **Player Character:** Automatically jumps upon landing on platforms.
- **Platforms:** Static platforms randomly placed; disappear when below the screen.
- **Scoring:** Points reflect the player's maximum height achieved.
- **Game Over:** Occurs when the player falls off the bottom of the screen.

## User Interface

- **Main Menu:** Start game or exit.
- **In-Game HUD:** Displays current score and FPS.
- **Game Over Screen:** Shows final score and options to retry or quit.

## Controls

- **Left Arrow:** Move left
- **Right Arrow:** Move right
- **R:** Restart the game from the game over screen
- **ESC:** Quit the game from any screen

## Requirements

- Python 3.x
- Pygame

## Setup

1. Create and activate a virtual environment:
    ```
    python -m venv .venv
    .venv\Scripts\activate
    ```
2. Install dependencies:
    ```
    pip install pygame
    ```

## Running the Game

Use the provided batch file:
```
run.bat
```
Or run manually:
```
python main.py
```

## Testing

Run unit tests with:
```
test.bat
```
Or manually:
```
python -m unittest test_main.py
```

## File Structure

- `main.py` — Main game logic
- `run.bat` — Launches the game
- `test.bat` — Runs unit tests
- `docs/prd-phase1.md` — Product requirements
