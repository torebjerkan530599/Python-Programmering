import turtle
#import random #for testing purposes, so that I don't have to enter input every time I want to test

player = ["X","O"]
moves = [-1,-1,-1,-1,-1,-1,-1,-1,-1] #a one dimensional matrix to hold the moves. -1 means not filled yet

def drawBoard():
    #init turtle
    # set screen
    turtle.screensize(canvwidth=500, canvheight=500,
                  bg="yellow")
    turtle.pensize(2)
    turtle.color("black")
    turtle.speed(10)
    #turtle.hideturtle()
    #turtle.backward(250)
    #begin drawing
    turtle.penup()

    
    for i in range(-1,3):
        turtle.setx(-100)
        turtle.sety(100 * i)
        turtle.pendown()
        turtle.forward(300)
        turtle.penup()
    
    #turtle.goto(-250, -100)
    turtle.setheading(90)
#
    for i in range(-1,3):
        turtle.setx(100 * i)
        turtle.sety(-100)
        turtle.pendown()
        turtle.forward(300)
        turtle.penup()

    turtle.pendown()
    #turtle.done()
    #return

#not yet implemented, will draw X or O on board using turtle
def drawPlayer(player):
    t = turtle.Turtle()
    t.speed(10)
    # TODO:turtle.addshape()
    if(player == "X"):
        turtle.heading(45)
        turtle.forward(100)
        turtle.penup()
        turtle.goto(150,-50)
        turtle.pendown()
        turtle.left(90)
        turtle.forward(100)
    else: #player is "O"
        t.circle(20)

def gameState(currentPlayer) : #returns game over condition, 1 = a player has won, 2 = it is a draw, 3 = no winner yet
    #check if winning conditions
    if((moves[0] == currentPlayer and moves[1] == currentPlayer and moves[2] == currentPlayer) or  # 1. horizontal
        (moves[3] == currentPlayer and moves[4] == currentPlayer and moves[5] ==currentPlayer) or # 2. horizontal
        (moves[6] == currentPlayer and moves[7] == currentPlayer and moves[8] ==currentPlayer) or # 3. horizontal
        (moves[0] == currentPlayer and moves[3] == currentPlayer and moves[6] ==currentPlayer) or # 1. diagonal
        (moves[2] == currentPlayer and moves[4] == currentPlayer and moves[6] ==currentPlayer) or # 1. anti-diagonal
        (moves[0] == currentPlayer and moves[3] == currentPlayer and moves[6] ==currentPlayer) or # 1. vertical
        (moves[1] == currentPlayer and moves[4] == currentPlayer and moves[7] ==currentPlayer) or # 2. vertical
        (moves[2] == currentPlayer and moves[5] == currentPlayer and moves[8] ==currentPlayer)):  # 3. vertical
        return 1

    if(moves.count(-1) == 0) : #check if board is full
        return 2 # It is a draw, winning conditions already checked 
    
    return 0

def isLegalMove(row,col):
    #index = row * 3 + col
    if(moves[to1D(row,col)] == -1): # not occupied
        return True
    return False

def main():
    gameLoop()

def swapCurrentPlayer(currentPlayer):
    if(currentPlayer == 0):
        currentPlayer = 1
    else :
        currentPlayer = 0
    return currentPlayer
    

def to1D(row, col):
    index = row * 3 + col # number of columns is 3
    return index

def gameLoop():
    currentPlayer = 0
    state = gameState(currentPlayer)
    while(True): # 0 == no winner yet  
        print("current player is " + player[currentPlayer])
        
        row = int(input("Enter row(0,1,2): "))
        col = int(input("Enter column(0,1,2): "))

        drawPlayer(player[currentPlayer])

        if(isLegalMove(row,col)):
            #TODO: drawPlayer(currentPlayer)
            index = to1D(row,col)
            moves.insert(index,currentPlayer)
            state = gameState(currentPlayer)

            if(state == 1): 
                print("The winner is " + player[currentPlayer])
                break
            
            if(state == 2):
                print("It is a draw! No winner!")
                break
            #if(x > 2 or x < 0): print() # test for valid input
            currentPlayer = swapCurrentPlayer(currentPlayer)
        else:
            print("it is not a legal move! Square already occupied! Try again!")
        

drawBoard()
main()


