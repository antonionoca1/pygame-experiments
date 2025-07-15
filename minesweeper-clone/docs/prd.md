This document outlines the core requirements for a Minesweeper clone game.

* Game Board: A grid of cells, with a configurable size (e.g., 9x9, 16x16, 30x16).
* Mines: A configurable number of hidden mines randomly distributed across the board.

# Cell States

* Unrevealed: Initial state of all cells.
* Revealed (Empty): A cell clicked by the user that does not contain a mine and has no adjacent mines.
* Revealed (Numbered): A cell clicked by the user that does not contain a mine but has one or more adjacent mines. The number indicates the count of adjacent mines.
* Revealed (Mine): A cell clicked by the user that contains a mine, resulting in game over.
* Flagged: A cell marked by the user as a suspected mine location.
* Question Mark: An optional state for users to mark a cell as uncertain.

# User Interaction

* Left-click: Reveal a cell. If it's a mine, the game ends. If it's an empty cell with no adjacent mines, it should automatically reveal all adjacent empty cells and numbered cells (flood fill).
* Right-click (or equivalent): Toggle between Flag, Question Mark (optional), and Unrevealed states.
* Chord Click (Left + Right click on a numbered cell): If the number of flags around a revealed numbered cell matches its number, reveal all unflagged adjacent cells.

# Game Logic

* Mine Placement: Mines should not be placed on the first clicked cell.
* Win Condition: All non-mine cells are revealed.
* Loss Condition: A mine cell is revealed.

# Game State

* Timer: Tracks the elapsed time for the current game.
* Mine Counter: Displays the number of remaining unflagged mines.