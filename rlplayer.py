import board
import numpy as np
import random

class RLPlayer:
    def __init__(self, piece, size):
        #Create an empty dictionary to hold our q-values
        #key = board state as a string
        #value = q-values for each action
        self.q_values = {}
        #Track the history of states so we can propogate
        #reward backwards at the end
        self.prev_move = None
        self.piece = piece
        #epsilon-greedy parameter
        self.epsilon = 0.1
        #learning parameters
        self.learn_rate = 0.1
        self.discount = 0.9

    #Allows us to change epsilon for subsequent runs
    def set_epsilon(self, eps):
        self.epsilon = eps

    #This function will take the board and make a move using 
    #epsilon greedy action selection. Then it will save the move
    #made to prev_move so we can use it to update Q when we get
    #back to our turn after the opponent moves
    def move(self, s):
        #If this state is new, add it with an array of 0s 
        #as the value
        state_string = s.to_string()
        if not state_string in self.q_values:
            self.q_values[state_string] = np.zeros(s.dim*s.dim)

        #Greedy move
        if np.random.random() > self.epsilon:
            #Choose an action using epsilon-greedy action selection
            #Find the indecies with a max_q value
            curr_q = self.q_values[state_string]
            max_q = np.amax(curr_q)
            valid = s.get_valid_moves()
            move_pool = []
            for i in range(0, s.dim*s.dim):
                #Check if move is greedy and valid
                if curr_q[i] == max_q and valid[i] == 1:
                    move_pool.append(i)

            move_num = random.choice(move_pool)
            s.place(move_num//s.dim,move_num%s.dim, self.piece)

        #Random move
        else:
            valid = s.get_valid_moves()
            move_pool = []
            for i in range(0, s.dim*s.dim):
                #Check if move is valid
                if valid[i] == 1:
                    move_pool.append(i)
            
            move_num = random.choice(move_pool)
            s.place(move_num//s.dim,move_num%s.dim, self.piece)

        #Save our move as previous
        self.prev_move = (state_string, move_num)

    
    def update_q(self, s):
        #Observe current state
        #Add this state to our q matrix if unseen
        state_string = s.to_string()
        if not state_string in self.q_values:
            self.q_values[state_string] = np.zeros(s.dim*s.dim)

        #Calculate reward if any
        (win, piece) = s.win_check()
        #We win
        if win and piece == self.piece:
            reward = 1
        #We draw
        elif s.draw_check():
            reward = 0.5
        #Lose or no game end
        else:
            reward = 0

        #Check for a previous move so we can update Q
        if self.prev_move:
            self.q_values[self.prev_move[0]] += self.learn_rate*(reward+self.discount*np.amax(self.q_values[state_string])-self.q_values[self.prev_move[0]])