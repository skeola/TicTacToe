import board
import player
import rlplayer
import sys

#Change this to modify board size
board_size = 3

#Use args to let user select what type of controls
#they want for the players
if len(sys.argv) == 1:
    print("Using default random vs random")
    p1_AI = 'random'
    p2_AI = 'random'
else:
    p1_AI = sys.argv[1]
    p2_AI = sys.argv[2]

#Initialize board and players
myBoard = board.Board(board_size)
#Reinforcement learners handled in a separate class
if p1_AI == 'RL':
    p1 = rlplayer.RLPlayer('X', board_size)
else:
    p1 = player.Player('X', p1_AI)
if p2_AI == 'RL':
    p2 = rlplayer.RLPlayer('X', board_size)
else:
    p2 = player.Player('O', p2_AI)

#Game loop
while not myBoard.draw_check():
    #PLAYER 1 MOVE
    p1.move(myBoard)
    (win, piece) = myBoard.win_check()
    myBoard.display()
    if win == True:
        break

    #PLAYER 2 MOVE
    p2.move(myBoard)
    (win, piece) = myBoard.win_check()
    myBoard.display()
    if win == True:
        break
   
#Last check for win to print the winner
(win, piece) = myBoard.win_check()
if win == True:
    print(f"{piece} WINS!")
else:
    if myBoard.draw_check() == True:
        print("DRAW")
    else:
        print("If this prints, we messed up")