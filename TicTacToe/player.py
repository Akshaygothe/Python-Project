import math
import random

class Player:
    def __init__(self, letter):
        # letter may be x or o
        self.letter = letter
    
    #we want all players to get their next move given a game
    def get_move(self, game):
        pass

class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        # get a random valid spot for for our next move
        square = random.choice(game.available_moves())
        return square 

class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letter + '\'s turn. Input Move (0-8):')
            # we are going to check that this is a correct value by trying to cast it 
            # to an integer, and if its not, then we say it's Invalid
            # if that sopt is not available on the board, we also say it's Invalid.
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True 
            except ValueError:
                print('Invalid Square. Try again.')

        return val