board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7] 
] # you can make your own board in this format and make this program solve it

# row = y-axis,
# column = x-axis 

def print_board(board):
    for i in range(len(board)):
        if i%3==0 and i!=0:
            print("------+-------+------")

        for j in range(len(board[0])):
            if j%3==0 and j!=0:
                print("| ", end="")
            if (j+1)%9==0 and j!=0:
                print(board[i][j])
            else:
                print(board[i][j],end=" ")

def empty_finder(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 0:
                return (i, j) # x, y
    return None

def valid(board, num, pos):
    # Checking columns
    for i in range(len(board)):
        if board[pos[0]][i]==num:
            return False
    
    # Checking Row
    for i in range(len(board)):
        if board[i][pos[1]]==num:
            return False
    
    # Checking Box
    box_x = (pos[0]//3)*3
    box_y = (pos[1]//3)*3
    for i in range(box_x, box_x+3):
        for j in range(box_y, box_y+3):
            if board[i][j] == num:
                return False

    return True

def solve(board):
    find = empty_finder(board)
    if not find:
        return True
    else:
        row, column = find
    
    for i in range(1,10):
#        print_board(board) # If you uncomment this it will look cool to see the computer solve the sudoku
#        print("\n")
        if valid(board, i, (row, column)):
            board[row][column] = i
            if solve(board):
                return True
            board[row][column] = 0
    return False

print_board(board)
solve(board)
print_board(board)
