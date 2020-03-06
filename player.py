import board
import numpy as np

#This function returns a function that the player
#will use to make moves
def select_ai(select, piece):
    #Random move (brute force)
    if select == 'random':
        def random(s):
            #Create a list of all possible moves (as an int)
            mv_list = np.arange(0, s.dim*s.dim)
            np.random.shuffle(mv_list)
            #Try a move till one works
            for mv in mv_list:
                if s.place(mv//s.dim, mv%s.dim, piece) == True:
                    break
        return random
    #Allows human input
    if select == 'human':
        def user_input(s):
            valid = False
            while valid == False:
                mv = int(input(f"Enter a number from 0-{s.dim*s.dim-1}: "))
                if s.place(mv//s.dim, mv%s.dim, piece) == True:
                    valid = True
                else:
                    print("Invalid move, try again!")
        return user_input
    #Default AI is random
    return random

class Player:
    #Creates a tic tac toe player with 'select' as 
    #its AI for how it selects moves
    def __init__(self, piece, select):
        self.piece = piece
        self.move = select_ai(select, piece)
