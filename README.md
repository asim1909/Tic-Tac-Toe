# Tic-Tac-Toe
The classic game Tic Tac Toe

This code is an implementation of the classic game Tic Tac Toe, which is played on a 3x3 grid. There are two players, X and O, who take turns marking their symbol on the grid. The first player to get three of their symbols in a row, either horizontally, vertically, or diagonally, wins the game. If all squares on the grid are filled and neither player has won, the game is a tie.

# The code defines three classes:

```
TicTacToe: This class represents the game board and contains methods to check for a winner, print the board, and make a move.
```
```
HumanPlayer: This class represents a human player and prompts the user to enter their move.
```
```
SmartComputerPlayer: This class represents a computer player and makes intelligent moves based on the current state of the board.
```
The play() function is the main driver of the game. It takes three arguments: the game object, the X player object, and the O player object. It runs a loop that alternates between the two players until the game ends in a win or a tie. It also prompts the user to leave or continue playing after the game ends.

### The game is played until there are no more empty squares on the board or a player wins.

If the game ends in a tie, the function prompts the user to either leave the game or start a new one. If a winner is declared, the function simply returns the winner and ends the game.

```
This program implements the classic Tic Tac Toe game using Python programming language. The game is played between a human player and a computer player. The computer player uses a smart algorithm to determine its moves.
```
# How to Play:

Run the program in a Python IDE or through the command line.
The game will begin with an empty Tic Tac Toe board.
Player 'X' (the computer) will make the first move.
The player 'O' (the human) will be prompted to enter a move.
The game will continue until there are no more empty squares or a player wins.
If the game ends in a tie, the user will be prompted to either leave the game or start a new one.
If a player wins, the game will end and the winner will be declared.

# Requirements:
```
Python 3.x
```
# Usage:

Clone or download the repository to your local machine.
Open a terminal or command prompt and navigate to the directory where the files are located.
Run the program using the following command: python tic_tac_toe.py
Follow the on-screen prompts to play the game.

# Credits:
This program was developed or Modified By @asim1909
