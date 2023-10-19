class EQ:

    def __init__(self):
        self.__BOARD_SIZE = 8
        self.__queens = 8 * [-1]
        self.__board = [['*' for i in range(8)]
                        for j in range(8)]  # draw empty board

    def get(self, i):
        return self.__queens[i]

    def set(self, i, j):
        self.__queens[i] = j  # denote the position of the queen in the row **
        self.__board[i][j] = 'Q' # 'Q' for Queen

    def checkDiagonals(self):
        ans = [[] for i in range(self.__BOARD_SIZE + self.__BOARD_SIZE - 1)]
        
        for i in range(self.__BOARD_SIZE):
            for j in range(self.__BOARD_SIZE):
                # Build rows representing diagonal of the board
                ans[i + j].append(self.__board[j][i])
            print()

        # check for more than one queen in each row
        for i in range(len(ans)):
            for j in range(len(ans[i])):
                print(ans[i][j], end=" ")
                # if(ans[i][j] == 'X'):
                #     queen_count += 1
                #     if queen_count == 2:
                #         return False
            print()

    def isSolved(self) -> bool:
        # check for more than one queen in rows and columns
        # might not be neccessary to check horizontally, assignment says 'Place one Queen pr. row'
        for row in range(0, self.__BOARD_SIZE):
            # num_queens_horizontal = 0 #reset count for each column
            num_queens_vertical = 0  # reset count for each row
            for col in range(0, self.__BOARD_SIZE):
                # if(board[row][col] == 'X'):
                #     num_queens_horizontal += 1
                #     if num_queens_horizontal == 2:
                #         return False
                if (self.__board[col][row] == 'Q'):
                    num_queens_vertical += 1
                    if num_queens_vertical == 2:
                        return False

        

        self.checkDiagonals()
        self.__board.reverse()
        self.checkDiagonals()

         # check for more than one queen diagonal from right to left

        # cellcount = 2
        # up_counter = 0

        # for i in range(0, cellcount):
        #     if cellcount == self.__BOARD_SIZE:
        #         break
        #     up_counter = 0
        #     print('-----------')
        #     for j in range(cellcount-1,-1,-1):
        #         print(f' {up_counter} {j}')
        #         up_counter += 1
        #     cellcount += 1

        return True

    def printBoard(self):
        for row in range(0, 8):
            print()
            for col in range(0, 8):
                if col == 0:
                    print("|", end="")
                print(f'{self.__board[row][col]}|', end='')

        '''
        0 1
        1 0
        
        0 2
        1 1
        2 0
        
        0 3
        1 2
        2 2
        3 1
        
        0 4
        1 3
        2 2
        3 1
        4 0
        
        0 5
        1 4
        2 3
        3 2
        4 1
        5 0
        
        0 6
        1 5
        2 4
        3 3
        4 2
        5 1
        6 0
        
        0 7
        1 6
        2 5
        3 4
        4 3
        5 2
        6 1
        7 0
        '''
