import board
import player

myBoard = board.Board(10)
p1 = player.Player('E', 'human')
p2 = player.Player('S', 'human')
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