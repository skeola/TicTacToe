import board
import player
import sys

if len(sys.argv) == 1:
    print("Using default random vs random")
    p1_AI = 'random'
    p2_AI = 'random'
else:
    p1_AI = sys.argv[1]
    p2_AI = sys.argv[2]

myBoard = board.Board(3)
p1 = player.Player('X', p1_AI)
p2 = player.Player('O', p2_AI)
myBoard.display()
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