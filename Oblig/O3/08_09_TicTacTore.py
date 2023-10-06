import turtle # implemented turtle version as well just for fun. Look at the bottom of the assignment.

player = ['|  X  ', '|  O  ']

# a one dimensional matrix to determine status. -1 means not filled yet
moves = [-1, -1, -1, -1, -1, -1, -1, -1, -1] # 0 = X, 1 = O

# returns game over condition, 1 = a player has won, 2 = it is a draw, 3 = no winner yet
def gameState(currentPlayer):
    # check if winning conditions are met
     # 1. horizontal
    if ((moves[0] == currentPlayer and moves[1] == currentPlayer and moves[2] == currentPlayer) or 
        # 2. horizontal
        (moves[3] == currentPlayer and moves[4] == currentPlayer and moves[5] == currentPlayer) or
        # 3. horizontal
        (moves[6] == currentPlayer and moves[7] == currentPlayer and moves[8] == currentPlayer) or
        # 1. diagonal
        (moves[0] == currentPlayer and moves[4] == currentPlayer and moves[8] == currentPlayer) or # celle [0,0] gir indeks 0, celle [1,1] gir indeks 4, celle [2,2] gir index 8
        # 1. anti-diagonal
        (moves[2] == currentPlayer and moves[4] == currentPlayer and moves[6] == currentPlayer) or
        # 1. vertical
        (moves[0] == currentPlayer and moves[3] == currentPlayer and moves[6] == currentPlayer) or
        # 2. vertical
        (moves[1] == currentPlayer and moves[4] == currentPlayer and moves[7] == currentPlayer) or
        # 3. vertical
        (moves[2] == currentPlayer and moves[5] == currentPlayer and moves[8] == currentPlayer)):  
        return 1

    if (moves.count(-1) == 0):  # check if board is full
        return 2  # It is a draw, winning conditions already checked
    return 0


def isLegalMove(row, col):
    return (moves[to1D(row, col)] == -1)  # not occupied


def main():
    gameLoop()

def swapCurrentPlayer(currentPlayer) -> int:
        #currentPlayer ^= currentPlayer
        if(currentPlayer == 0):
            currentPlayer = 1
        else :
            currentPlayer = 0
        return currentPlayer


def to1D(row, col):
    index = row * 3 + col
    return index


def gameLoop():
    currentPlayer = 0

    graphicsArray = [['|     ','|     ','|     |'],['|     ','|     ','|     |'],['|     ','|     ','|     |']]
    while (True):  # 0 == no winner yet
        print()
        print("current player is " + (player[currentPlayer]).replace('|', '').strip() + "\n")
        row = int(input("Enter row(0,1,2): "))
        col = int(input("Enter column(0,1,2): "))
        print()

        if (isLegalMove(row, col)):
            moves[to1D(row,col)] = currentPlayer # logic storage in 1D array
            board = placeMove(player[currentPlayer], row, col, graphicsArray) # visualize moves in a matrix
            draw(board)
            




            
            state = gameState(currentPlayer)

            if (state == 1):
                print("The winner is " + player[currentPlayer].replace('|', '').strip())
                break

            if (state == 2):
                print("It is a draw! No winner!")
                break
            
            if(row > 2 or row < 0 or col > 2 or col < 0): 
                print("Not valid input for row or column") # test for valid input
            else:
                currentPlayer = swapCurrentPlayer(currentPlayer)
        else:
            print("it is not a legal move! Square already occupied! Try again!")
            
        
def placeMove(player, row, col, board):
    
    for i in range(3):
        for j in range(3):
            if i==row and j == col:
                board[i][j] = player
    return board

def draw(board):
    viz = ''
    for i in range(3):
        viz += '-------------------\n'
        for j in range(3):   
            viz += board[i][j]
            if(board[i][j] == '|  X  ' or board[i][j] == '|  O  ') and j == 2:
                viz += '|'
        viz += '\n'
    viz += '-------------------\n' 
    print(viz)

#Drawcode for Turtle...just for fun
def drawBoard():
    # init turtle
    # set screen
    screen = turtle.Screen()
    turtle.screensize(bg="yellow")
    screen.setup(500,500)
    turtle.hideturtle()
    turtle.pensize(2)
    turtle.color("black")
    turtle.speed(10)
    turtle.penup()

    for i in range(-1, 3):
        turtle.setx(-150)
        turtle.sety(100 * i)
        turtle.pendown()
        turtle.forward(300)
        turtle.penup()

    # turtle.goto(-250, -100)
    turtle.setheading(90)
#
    for i in range(-1, 3):
        turtle.setx(100 * i - 50)
        turtle.sety(-100)
        turtle.pendown()
        turtle.forward(300)
        turtle.penup()
        
    return
def drawPlayer(player, row, col):
    turtle.setheading(0)
    turtle.penup()
  
    if (player == "X"):
        turtle.setpos(200,200)
        turtle.setpos(-95-50 + col * 100, 195 - row * 100)
        turtle.right(45)
        turtle.pendown()
        turtle.forward(125)
        
        turtle.penup()

        turtle.right(90)
        turtle.setpos(-5 -50 + col * 100, 195 - row * 100)
        turtle.pendown()
        turtle.forward(125)
    else:  # player is "O"
        turtle.setpos(-100 + col * 100, 105 - row * 100)
        turtle.pendown()
        turtle.circle(45)
#drawBoard()

main()
