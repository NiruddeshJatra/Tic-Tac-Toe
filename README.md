# Tic-Tac-Toe Game by NJ Production

## Introduction
Welcome to the Tic-Tac-Toe Game by NJ Production! This game allows 2 to 4 players to compete on a grid that adapts in size based on the number of players. For 2 players, the game uses a 3x3 grid; for 3 players, a 4x4 grid; and for 4 players, a 5x5 grid. The game includes sound effects and a visual interface using the `turtle` and `pygame` libraries.

## Features
- Support for 2 to 4 players.
- Dynamic grid size based on the number of players.
- Sound effects for various actions.
- Visual interface using the `turtle` graphics library.
- Simple and engaging gameplay.

## Installation
To run the Tic-Tac-Toe game, you need to have Python installed along with the `turtle` and `pygame` libraries. You can install `pygame` using pip:

```bash
pip install pygame
```

## How to Play
1. Run the game script.
2. Enter the number of players (between 2 and 4) when prompted.
3. Players take turns clicking on the grid to place their markers.
4. The first player to get 3 consecutive squares in a row, column, diagonal, or anti-diagonal wins.
5. If all squares are filled and no player has 3 consecutive squares, the game ends in a draw.

## Game Controls
- **Mouse Click**: Place your marker on the grid.
- **Esc**: Exit the game.

## Code Overview
The game is implemented in the `TicTacToe` class, which includes the following key methods:

- **`__init__`**: Initializes the game, sets up the screen, plays the welcome message, and gets the number of players.
- **`setup_screen`**: Configures the game screen.
- **`play_sound`**: Plays a sound file.
- **`play_welcome_message`**: Displays a welcome message and game instructions.
- **`get_number_of_players`**: Prompts the user to enter the number of players.
- **`setup_players`**: Sets up player markers and colors.
- **`draw_grid`**: Draws the game grid based on the number of players.
- **`setup_squares`**: Defines the coordinates of the squares on the grid.
- **`setup_matches`**: Defines the winning combinations for different grid sizes.
- **`draw_marker`**: Draws a player's marker on the grid.
- **`click_handler`**: Handles player clicks and places markers.
- **`is_within_square`**: Checks if a click is within a square.
- **`add_click_listeners`**: Adds click listeners to the grid.
- **`game_over`**: Displays the game-over screen.
- **`check_winner`**: Checks if a player has won the game.
- **`run`**: Runs the game loop.

## Credits
This Tic-Tac-Toe game was created by NJ Production.

### Sound Credits
- **Message Box Sound**: "message_box.mp3"
- **Error Sound**: "error.wav"
- **Click Sound**: "click.wav"
- **Got Bonus Sound**: "got_bonus.wav"
- **End Sound**: "end.mp3"

Enjoy the game with your friends!
