def solve(board):
    
    '''
        takes in board
        
        using backtracking concept,
        this fills empty cells with valid number and move on to next.
        if unable to find solution whilst attempting next, it will backtrack to previous solved cell
        and retry with next potential valid number.
        
    '''
    
    find = find_empty(board)
    if find:
        row, col = find
    else:
        return True       # if no more empty cells, board is solved
    
    
    for i in range(1,10):
        if valid_move(board, (row,col), i):
            board[row][col] = i
            
            if solve(board):
                return True
          
            board[row][col] = 0
    
    return False




def find_empty(board):
    
    '''
        takes in incomplete board.
        returns indices of first empty cell (i,j)       
        
    '''
    
    for i in range(len(board)): # i --> row
        for j in range(len(board[0])): # j --> column
            if board[i][j] == 0:
                return(i,j)
    
    return None





def valid_move(board, position, number):
    
    '''
        takes in board, indices of empty cell, and potential number to fill (1-9)
        returns if the attempted number to fill the empty cell is valid or not
        
    '''
    
    
    #check row
    for i in range(0, len(board)):
        if board[position[0]][i] == number and position[1] != i:
            return False
    
    #check column
    for i in range(0, len(board)):
        if board[i][position[1]] == number and position[0] != i:
            return False
        
    #check box
    box_x = position[1] // 3    # Returns box number from 0 to 2, depending on column position
    box_y = position[0] // 3    # Returns box number from 0 to 2, depending on row position
    
    for i in range(box_y*3, box_y*3 + 3):      # Loop through the possible ranges in their respective 3 x 3 box
        for j in range(box_x*3, box_x*3 +3):
            if board[i][j] == number and (i,j) != position:
                return False
    return True





def print_board(bo):
    
    """
        takes in board.
        returns board in a more readable format

    """
    
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - -")
        for j in range(len(bo[0])):
            if j % 3 == 0:
                print(" | ",end="")

            if j == 8:
                print(bo[i][j], end="\n")
            else:
                print(str(bo[i][j]) + " ", end="")


                


###### Checks with 3 different boards


board = [
        [7, 8, 0, 4, 0, 0, 1, 2, 0],
        [6, 0, 0, 0, 7, 5, 0, 0, 9],
        [0, 0, 0, 6, 0, 1, 0, 7, 8],
        [0, 0, 7, 0, 4, 0, 2, 6, 0],
        [0, 0, 1, 0, 5, 0, 9, 3, 0],
        [9, 0, 4, 0, 6, 0, 0, 0, 5],
        [0, 7, 0, 3, 0, 0, 0, 1, 2],
        [1, 2, 0, 0, 0, 7, 4, 0, 0],
        [0, 4, 9, 2, 0, 6, 0, 0, 7]
    ]




print("Original Board")
print_board(board)
print("")
print("Solved Board")
solve(board)
print_board(board)





board_hard = [
        [5, 0, 0, 0, 9, 7, 0, 0, 0],
        [0, 1, 0, 8, 0, 0, 2, 0, 0],
        [0, 7, 9, 2, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 0, 4, 0, 8],
        [3, 0, 0, 0, 0, 0, 0, 0, 1],
        [9, 0, 1, 0, 0, 0, 0, 0, 0],
        [0, 6, 0, 0, 0, 8, 1, 5, 0],
        [0, 0, 5, 0, 0, 1, 0, 6, 0],
        [0, 0, 0, 7, 6, 0, 0, 0, 3]
    ]





print("Original Board")
print_board(board_hard)
print("")
print("Solved Board")
solve(board_hard)
print_board(board_hard)





board_hard2 = [
        [0, 0, 0, 0, 0, 0, 7, 1, 6],
        [5, 1, 0, 0, 9, 3, 0, 0, 0],
        [0, 0, 0, 2, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 5, 8, 0, 0],
        [8, 0, 2, 0, 0, 0, 3, 0, 9],
        [0, 0, 7, 9, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 9, 0, 0, 0],
        [0, 0, 0, 8, 3, 0, 0, 4, 2],
        [1, 7, 4, 0, 0, 0, 0, 0, 0]
    ]





print("Original Board")
print_board(board_hard2)
print("")
print("Solved Board")
solve(board_hard2)
print_board(board_hard2)







