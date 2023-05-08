# Tic-Tac-Toe
The classic game Tic Tac Toe

This code is an implementation of the classic game Tic Tac Toe, which is played on a 3x3 grid. There are two players, X and O, who take turns marking their symbol on the grid. The first player to get three of their symbols in a row, either horizontally, vertically, or diagonally, wins the game. If all squares on the grid are filled and neither player has won, the game is a tie.

# The code defines three classes:

""" TicTacToe: This class represents the game board and contains methods to check for a winner, print the board, and make a move. """

""" HumanPlayer: This class represents a human player and prompts the user to enter their move. """

""" SmartComputerPlayer: This class represents a computer player and makes intelligent moves based on the current state of the board. """

The play() function is the main driver of the game. It takes three arguments: the game object, the X player object, and the O player object. It runs a loop that alternates between the two players until the game ends in a win or a tie. It also prompts the user to leave or continue playing after the game ends.

To run the game, simply run the script in a Python environment. The game will prompt the user to make moves and display the board after each move. The computer player will make intelligent moves based on the current state of the board. The user can choose to leave or continue playing after the game ends.
