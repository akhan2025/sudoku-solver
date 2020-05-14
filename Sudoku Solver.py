import time
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
]

def print_board(board):
    for i in range(len(board)):
        #if statement creates a barrier between 3x3 squares
        if i % 3 == 0 and i != 0:
                print("- - - - - - - - - - - - - ")
        
        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                #creates new line
                print(board[i][j])
            else:
                #does not create a new line
                print(str(board[i][j]) + " ", end="")


def find_empty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j)  # row, column


    return None

def solve(bo, comparisons):
    find = find_empty(bo)
    if not find:
        print(comparisons)
        return True
    else:
        row, col = find

    for i in range(1,10):
        if valid(bo, i, (row, col)):
            bo[row][col] = i
            #time.sleep(1)
            if solve(bo, comparisons):
                return True
            comparisons += 1
            bo[row][col] = 0

    return False

def valid(bo, num, pos):
    # Check row
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False

    # Check column
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False

    # Check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            if bo[i][j] == num and (i,j) != pos:
                return False

    return True


def possible_values(row, column):
    subset = []
    for i in range(1,10):
        if valid(board, i, (row, column)):
            subset.append(i)
            continue
    return subset

def easy_solve(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] != 0:    
                continue
            possible = possible_values(i, j)
            if len(possible) == 1:
                #time.sleep(1)
                board[i][j] = possible[0]
    

    

print_board(board)
for i in range(7):
    easy_solve(board)
print("___________________")
print_board(board)
solve(board, 0)
print("___________________")
print_board(board)
        