'''
check for #queens in row
check for #queens in col
check for #queens in diagonal left
check for #queens in diagonal right

if any count above 2, return false
 
'''

def isSolved(board) -> bool:
    
    board_length = 8
    # check for more than one queen in rows and columns
    
    for row in range(0, board_length):
        num_queens_horizontal = 0 #reset count for each column
        num_queens_vertical = 0 #reset count for each row
        for col in range(0,board_length):
            if(board[row][col] == 'Queen'):
                num_queens_horizontal += 1
                if num_queens_horizontal == 2:
                    return False 
            if(board[col][row] == 'Queen'):
                num_queens_vertical += 1
                if num_queens_vertical == 2:
                    return False 
    
    # check for more than one queen diagonally
    
    for i in range(0, board_length):
        for j in range(board_length,-1,-1):
            print (board[i][j])
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
          
    return True