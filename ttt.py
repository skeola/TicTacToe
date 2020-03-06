import board
import player
import rlplayer
import sys

#Change this to modify board size
board_size = 3
iterations = 10

#Use args to let user select what type of controls
#they want for the players
if len(sys.argv) == 1:
    print("Using default RL vs random")
    p2_AI = 'random'
else:
    p2_AI = sys.argv[1]

#Initialize players
p1 = rlplayer.RLPlayer('X', board_size)
p2 = player.Player('O', p2_AI)

#Iterate through n games
for i in range(0, iterations):
    #Create the board
    myBoard = board.Board(board_size)

    #Game loop
    while not myBoard.draw_check():
        #PLAYER 1 MOVE
        p1.move(myBoard)
        (win, piece) = myBoard.win_check()
        myBoard.display()
        if win == True or myBoard.draw_check():
            p1.update_q(myBoard)
            break

        #PLAYER 2 MOVE
        p2.move(myBoard)
        (win, piece) = myBoard.win_check()
        myBoard.display()
        if win == True or myBoard.draw_check():
            p1.update_q(myBoard)
            break

    #Last check for win to print the winner
    (win, piece) = myBoard.win_check()
    if win == True:
        print(f"{piece} WINS!")
    else:
        if myBoard.draw_check() == True:
            print("DRAW")
        else:
            print("If this prints, we fucked up")

    #Debug print of the q-table values
    print(p1.q_values)