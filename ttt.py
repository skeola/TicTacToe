import board
import player
import rlplayer
import sys
import numpy as np
import matplotlib.pyplot as plt

#Change this to modify board size
board_size = 3
epochs = 100
train_games = 100
test_games = 100

#Use args to let user select what type of controls
#they want for the players
if len(sys.argv) == 1:
    print("Using default RL parameters")
    eps = 0.1
    lr = 0.1
    disc = 0.9
    delta = 0.01
else:
    eps = float(sys.argv[1])
    lr = float(sys.argv[2])
    disc = float(sys.argv[3])
    delta = float(sys.argv[4])

#Initialize players
p1 = rlplayer.RLPlayer('X', board_size, eps, lr, disc, delta)
p2 = player.Player('O', 'random')

match_record = None

#Iterate through epochs
for i in range(0, epochs):
    #In each epoch, we first train for 10 games
    for j in range(0, train_games):
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
        else:
            if myBoard.draw_check() == True:
                print("DRAW")
            else:
                print("If this prints, we messed up")
        
        #Reset the RL player after each game
        p1.game_reset()

    #Then we test over 100 games
    total_score = 0

    for j in range(0, test_games):
        #Create the board
        myBoard = board.Board(board_size)

        #Game loop
        while not myBoard.draw_check():
            #PLAYER 1 MOVE
            p1.move(myBoard, True) #set flag to always make greedy move
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
                total_score+= 1
        else:
            if myBoard.draw_check() == True:
                print("DRAW")
                total_score += 0.5
            else:
                print("If this prints, we messed up")
        
        #Reset the RL player after each game
        p1.game_reset()
    
    #Reduce the epsilon value by delta each epoch
    p1.reduce_epsilon()

    print(f"EPOCH {i}: {total_score}")
    epoch_record = np.array([[i, total_score/test_games]])
    if match_record is None:
        match_record = epoch_record
        print(match_record)
    else:
        match_record = np.concatenate((match_record, epoch_record), axis=0)

#Debug print of the match record
#print(match_record)

avg = np.average(match_record[int(test_games*0.8): ,1])
print(avg)

plt.plot(match_record[:,0], match_record[:,1])
plt.ylabel('Total Score/# of Games')
plt.xlabel('Epoch')
plt.title('ε={}, Δ={}, γ={}, η={}'.format(eps, delta, disc, lr))
plt.legend(['Avg last 20% = {0:.2f}'.format(avg)], loc='lower right')
plt.savefig('e{}d{}g{}l{}.png'.format(int(eps*10), int(delta*100), int(disc*10), int(lr*10)))
plt.show()