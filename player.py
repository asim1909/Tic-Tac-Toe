import math
import random

class Player():
    def __init__(self, letter):
        self.letter = letter

    def get_move(self, game):
        pass

class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        # Prompt the user to input a valid move
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letter + '\'s turn. Input move (0-9): ')
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True
            except ValueError:
                print('Invalid square. Try again.')
        return val

class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        # Choose a random valid move
        square = random.choice(game.available_moves())
        return square

class SmartComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        if len(game.available_moves()) == 9:
            # If all squares are empty, choose a random square
            square = random.choice(game.available_moves())
        else:
            # Use the minimax algorithm to choose the best move
            square = self.minimax(game, self.letter)['position']
        return square

    def minimax(self, state, player):
        max_player = self.letter  # yourself
        other_player = 'O' if player == 'X' else 'X'

        # Check if the previous move was a winning move
        if state.current_winner == other_player:
            return {'position': None, 'score': 1 * (state.num_empty_squares() + 1) if other_player == max_player else -1 * (
                        state.num_empty_squares() + 1)}
        elif not state.empty_squares():
            # If all squares are full and there is no winner, it's a tie
            return {'position': None, 'score': 0}

        if player == max_player:
            # If it's the maximizing player's turn, initialize the best score to negative infinity
            best = {'position': None, 'score': -math.inf}
        else:
            # If it's the minimizing player's turn, initialize the best score to positive infinity
            best = {'position': None, 'score': math.inf}

        # Loop through all available moves
        for possible_move in state.available_moves():
            state.make_move(possible_move, player)
            # Recursively call minimax to simulate the game after making this move
            sim_score = self.minimax(state, other_player)

            # Undo the move and reset the winner to None
            state.board[possible_move] = ' '
            state.current_winner = None
            # Set the position to the current move, which represents the optimal next move
            sim_score['position'] = possible_move

            if player == max_player:  # X is max player
                # If it's the maximizing player's turn, choose the move with the highest score
                if sim_score['score'] > best['score']:
                    best = sim_score
            else:
                # If it's the minimizing player's turn, choose the move with the lowest score
                if sim_score['score'] < best['score']:
                    best = sim_score

        return best
