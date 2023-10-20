class EQ:

    def __init__(self, queens=8 * [-1]):
        self.__BOARD_SIZE = 8
        self.__queens = queens
        self.__board = [['*' for i in range(self.__BOARD_SIZE)]
                        for j in range(self.__BOARD_SIZE)]  # draw empty board
        
        if(self.__queens[0] != -1):
            for count, ele in enumerate(self.__queens):
                self.__board[count][ele] = 'Q'
    
    def get(self, i):
        return self.__queens[i]

    def set(self, i, j):
        self.__queens[i] = j  # denote the position of the queen in the row
        self.__board[i][j] = 'Q'

    def checkDiagonals(self):
        diagonals = [[] for i in range(self.__BOARD_SIZE + self.__BOARD_SIZE - 1)]

        # Build rows representing diagonals of the board
        for i in range(self.__BOARD_SIZE):
            for j in range(self.__BOARD_SIZE):
                diagonals[i + j].append(self.__board[j][i]) # sum of indexes is the same diagonally
            print()

        # check for more than one queen in each row
        for i in range(len(diagonals)):
            queenCount = 0
            for j in range(len(diagonals[i])):
                # print(diagonals[i][j], end=" ")  # [1] print each diagonal in a row
                if (diagonals[i][j] == 'Q'):
                    queenCount += 1
                    if queenCount == 2:
                        return False
            # print()  # [1] new line when finished printing diagonal in row
        return True

    def isSolved(self) -> bool:
        
        # check for number of queens vertically
        for i in self.__queens:
            if (self.__queens.count(i) > 1) and (i != -1):
                return False

        # check for number of queens horizontally
        for row in range(0, self.__BOARD_SIZE):
            num_queens_horizontal = 0  # reset count for each column
            for col in range(0, self.__BOARD_SIZE):
                if (self.__board[row][col] == 'Q'):
                    num_queens_horizontal += 1
                    if num_queens_horizontal == 2:
                        return False

        isValid_1 = self.checkDiagonals() # 1. diagonal
        self.__board.reverse()
        isValid_2 = self.checkDiagonals() # 2. diagonal
        self.__board.reverse() # reverse to original board layout

        return isValid_1 and isValid_2

    def printBoard(self):
        for row in range(self.__BOARD_SIZE):
            print()
            for col in range(self.__BOARD_SIZE):
                if col == 0:
                    print("|", end="")
                print(f'{self.__board[row][col]}|', end='')
