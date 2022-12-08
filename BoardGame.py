def drawBoard():
    for i in range(4):
        for j in range(4):
            print(gameBoard[i+j], end='')
        print("\n")


gameBoard = []
for i in range(4):
    for j in range(4):
        gameBoard.append("X")
drawBoard()
rowChosen = int(input("Which Row would you like to select?  "))
columnChosen = int(input("Which Column would you like to select?  "))
gameBoard[rowChosen + columnChosen] = "O"
drawBoard()