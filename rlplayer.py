import board
import numpy as np

class RLPlayer:
    def __init__(self, piece, size):
        #Create Q-Matrix with one row containing initial state
        #and size^2 action rows
        self.q_matrix = np.zeros((1,size*size))
        self.piece = piece

    def move(self, s):
        return 0


