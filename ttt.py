import board
import player
import rlplayer
import sys
import numpy as np
import matplotlib.pyplot as plt

#Change this to modify board size
board_size = 3
iterations = 10

#Use args to let user select what type of controls
#they want for the players
if len(sys.argv) == 1:
    print("Using default RL parameters")
    eps = 0.1
    lr = 0.1
    disc = 0.9
    delta = 0.01
else:
    eps = sys.argv[1]
    lr = sys.argv[2]
    disc = sys.argv[3]
    delta = sys.argv[4]

#Initialize players
p1 = rlplayer.RLPlayer('X', board_size, eps, lr, disc, delta)
p2 = player.Player('O', p2_AI)

match_record = None

for i in range(0, iterations):
    #Iterate through n games
    win_rate = 0
    for j in range(0, iterations):
        #Create the board
        myBoard = board.Board(board_size)

        #Game loop
        while not myBoard.draw_check():
            #PLAYER 1 MOVE
            p1.move(myBoard)
            p1.update_q(myBoard)
            (win, piece) = myBoard.win_check()
            #myBoard.display()
            if win == True or myBoard.draw_check():
                break

            #PLAYER 2 MOVE
            p2.move(myBoard)
            (win, piece) = myBoard.win_check()
            #myBoard.display()
            if win == True or myBoard.draw_check():
                p1.update_q(myBoard)
                break
        
        myBoard.display()
        #Last check for win to print the winner
        (win, piece) = myBoard.win_check()
        if win == True:
            print(f"{piece} WINS!")
            if piece == p1.piece:
                win_rate += 1
        else:
            if myBoard.draw_check() == True:
                print("DRAW")
                win_rate += 0.5
            else:
                print("If this prints, we messed up")
        
        p1.game_reset()

    print(f"EPOCH {i}: {win_rate/iterations}")
    epoch_record = np.array([[i, win_rate]])
    if match_record is None:
        match_record = epoch_record
        print(match_record)
    else:
        match_record = np.concatenate((match_record, epoch_record), axis=0)

#Debug print of the match record
#print(match_record)

plt.plot(match_record[:,0], match_record[:,1])
plt.ylabel('Total Score')
plt.xlabel('Epoch')
plt.title('')
plt.show()