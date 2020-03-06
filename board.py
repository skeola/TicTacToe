import numpy as np

class Board:
    #Create a dim x dim numpy array and track 
    #the size of the board for future use
    def __init__(self, dim):
        if dim<3:
            print("Board size too small, setting to 3")
            self.dim = 3
        else:
            self.dim = dim
        #Fill board with spaces (easier for printing)
        self.board = np.full((dim,dim), ' ')
        #This is the max number of legal moves we can make
        #Used to find draws easily
        self.mv_count = dim*dim

    #Simple display of the board 
    #Change to formatted display later!
    def display(self):
        print('_'*(self.dim+2))
        for row in self.board:
            print('|', end='')
            for j in row:
                print(j, sep='', end='')
            print('|')
        print('¯'*(self.dim+2))
        
    #Checks if a move is valid, returns True if the move is successful
    def place(self, x, y, piece):
        if self.board[x][y] != ' ':
            return False
        else:
            self.board[x][y] = piece
            self.mv_count -= 1
            return True

    def draw_check(self):
        if self.mv_count <= 0:
            return True
        else:
            return False

    #Checks for a victory for any side
    #Returns a tuple (Victory, piece)
    def win_check(self):
        #Check horizontal victory
        (win, piece) = self.check_hori()
        if win==True:
            return (win, piece)
        (win, piece) = self.check_vert()
        if win==True:
            return (win, piece)
        (win, piece) = self.check_diag()
        if win == True:
            return (win, piece)
        return (False, ' ')

    #Checks for win by row
    def check_hori(self):
        piece = ' '
        win = False
        for i in range(0, self.dim):
            if self.board[i][0] == ' ':
                continue
            else:
                piece = self.board[i][0]
            for j in range(1, self.dim):
                if self.board[i][j] == piece:
                    win = True
                else:
                    win = False
                    break
            if win==True:
                return (win, piece)
        return (False, ' ')

    #Checks for win by column
    def check_vert(self):
        piece = ' '
        win = False
        for i in range(0, self.dim):
            if self.board[0][i] == ' ':
                continue
            else:
                piece = self.board[0][i]
            for j in range(1, self.dim):
                if self.board[j][i] == piece:
                    win = True
                else:
                    win = False
                    break
            if win==True:
                return (win, piece)
        return (False, ' ')

    #Checks the board diagonals for a win
    def check_diag(self):
        win = True

        #Check for the first piece to be valid
        if self.board[0][0] != ' ':
            piece = self.board[0][0]
            #Compare to all following pieces
            for i in range(1, self.dim):
                #If one piece isn't matching, set flag 
                # to false and break
                if piece != self.board[i][i]:
                    win = False
                    break
            #If all pieces were matching, return
            if win == True:
                return (win, piece)

        win = True
        #Otherwise, we check the harder diagonal
        if self.board[0][self.dim-1] != ' ':
            piece = self.board[0][self.dim-1]
            #Compare to all following pieces
            for i in range(1, self.dim):
                #If any piece doesn't match, set flag and break
                if piece != self.board[i][self.dim-i-1]:
                    win = False
                    break
            #If all pieces matched, return
            if win == True:
                return (win, piece)

        return (False, ' ')
        
    #Inverts the state of the board based on input
    #pieces. Dependent on correctly passing the
    #two piece chars as p1 and p2.
    #Not sure if this is necessary for Q-learning
    #from both sides of the board
    def invert(self, p1, p2):
        for i in self.board:
            for j in range(0, self.dim):
                if i[j] == p1:
                    i[j] = p2
                else:
                    if i[j] == p2:
                        i[j] = p1

    #Returns a 1x(n*n) array where valid moves are 1
    #and invalid moves are 0
    def get_valid_moves(self):
        num_elem = self.dim*self.dim
        ret = np.zeros(num_elem)
        for i in range(0, num_elem):
            if self.board[i//self.dim][i%self.dim] == ' ':
                ret[i] = 1
        return ret

    #Returns the board state as a string
    #Given a piece value, we will convert it to a
    #universal format where X is our player and O is
    #the opponent
    def to_string(self, piece='X'):
        ret = ""
        for i in range(0, self.dim):
            for j in range(0, self.dim):
                if self.board[i][j] == piece:
                    ret += piece
                elif self.board[i][j] == ' ':
                    ret += ' '
                else:
                    ret += 'O'
        return ret
