#import random #for testing purposes, so that I don't have to enter input every time I want to test

from tkinter import *
from tkinter import messagebox
#import os

class TicTacGui():
    def __init__(self) -> None:
        self.__window = Tk() # Create a root window
        #self.__window.geometry("450x500")
        self.__window.title("Tic tAc toE") # Set title
        self.__buttons = [[1,2,3],[4,5,6],[7,8,9]]
        self.__boardFrame = Frame(self.__window)
        self.__boardFrame.pack()
        self.__players = ["X","O"]
        self.__currentPlayer = 0
        # self.__imgX = PhotoImage(file=os.getcwd() + "\Oblig\O4\TicTacGui\X.png")
        # self.__imgO = PhotoImage(file=os.getcwd() + "\Oblig\O4\TicTacGui\O.png")
        self.__moves = [-1,-1,-1,-1,-1,-1,-1,-1,-1] #a one dimensional matrix to hold the moves. -1 means not filled yet

        #Set size of playing area
        Tk_Width = 450
        Tk_Height = 500

        #calculate coordinates to put root window in center of screen
        x_Left = int(self.__window.winfo_screenwidth()/2 - Tk_Width/2)
        y_Top = int(self.__window.winfo_screenheight()/2 - Tk_Height/2)

         # Write following format for center screen
        self.__window.geometry("+{}+{}".format(x_Left, y_Top))

        print("current player is " + self.__players[self.__currentPlayer])

        for i in range(3):
            for j in range(3):        
                
                self.__buttons[i][j] = Button(self.__boardFrame, height = 2, width = 5, text = " ",
                    font = ("Consolas","40"), command = lambda row = i, col = j :  self.clicked(row,col))
                self.__buttons[i][j].grid(row = i, column = j)

        #self.__replayButton = Button(self.__boardFrame, text = "Refresh/Play again?", command =  self.replay)
        #self.__replayButton.grid(row = 3, column=1)

        self.__window.mainloop()

    #def replay(self):
    #    self.__window.destroy()
    #    TicTacGui()
        
    def clicked(self,row, col):
        if(self.isLegalMove(row,col)):
            index = self.to1D(row,col)
            self.__moves[index] = self.__currentPlayer
            state = self.gameState(self.__currentPlayer)

            if (self.__currentPlayer == 0) :
                self.__buttons[row][col].config(text="X")
            else:
                self.__buttons[row][col].config(text="O")

            replay = False #
            if(state == 1):
                print("The winner is " + self.__players[self.__currentPlayer]) 
                replay  = messagebox.askyesno("Congratulations!","The winner is " 
                    + self.__players[self.__currentPlayer] 
                    +". Do You want to replay?" )
            if(state == 2):
                print("It is a draw! No winner!")
                replay = messagebox.askyesno("It is a draw No winner!", "Do You want to replay?")
                
            if(state == 1 or state == 2):
                self.__window.destroy()
                if(replay == True):
                    TicTacGui() #play again
                else:
                    return
            
            self.__currentPlayer = self.swapCurrentPlayer(self.__currentPlayer)
            print("current player is " + self.__players[self.__currentPlayer])
        
        else:
            print("Not a legal move")


    def gameState(self,currentPlayer) : 
        #returns game over condition, 1 = a player has won, 2 = it is a draw, 3 = no winner yet
        #check winning conditions
        if((self.__moves[0] == currentPlayer and self.__moves[1] == currentPlayer and self.__moves[2] == currentPlayer) or  # 1. horizontal
            (self.__moves[3] == currentPlayer and self.__moves[4] == currentPlayer and self.__moves[5] ==currentPlayer) or # 2. horizontal
            (self.__moves[6] == currentPlayer and self.__moves[7] == currentPlayer and self.__moves[8] ==currentPlayer) or # 3. horizontal
            (self.__moves[0] == currentPlayer and self.__moves[4] == currentPlayer and self.__moves[8] ==currentPlayer) or # 1. diagonal
            (self.__moves[2] == currentPlayer and self.__moves[4] == currentPlayer and self.__moves[6] ==currentPlayer) or # 1. anti-diagonal 1
            (self.__moves[0] == currentPlayer and self.__moves[3] == currentPlayer and self.__moves[6] ==currentPlayer) or # 1. vertical
            (self.__moves[1] == currentPlayer and self.__moves[4] == currentPlayer and self.__moves[7] ==currentPlayer) or # 2. vertical
            (self.__moves[2] == currentPlayer and self.__moves[5] == currentPlayer and self.__moves[8] ==currentPlayer)):  # 3. vertical
            return 1

        if(self.__moves.count(-1) == 0) : #check if board is full
            return 2 # It is a draw, winning conditions already checked 

        return 0

    def isLegalMove(self,row,col):
        #index = row * 3 + col
        return self.__moves[self.to1D(row,col)] == -1 #if not occupied

    def swapCurrentPlayer(self,currentPlayer):
        #currentPlayer = currentPlayer != currentPlayer
        if(currentPlayer == 0):
            currentPlayer = 1
        else :
            currentPlayer = 0
        return currentPlayer

    def to1D(self,row, col):
        index = row * 3 + col # number of columns is 3
        return index

TicTacGui()

