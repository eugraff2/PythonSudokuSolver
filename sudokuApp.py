# basic method to print out the contents the sudoku board (2D array) 
def print_board(arr):
    for i in range(9):
        print(arr[i])

# iterates through the array to find 0's indicating an empty space
# l is a list that will be passed from solve_sudoku to keep track of the row and col
def find_empty(arr, l):
    for row in range(9):
        for col in range(9):
            if(arr[row][col] == 0): # if empty space is found
                l[0] = row
                l[1] = col
                return True
    return False # when no more empty spaces are found

# returns true if a number in the given row matches the specified num and false otherwise
def used_in_row(arr, row, num):
    for i in range(9):
        if(arr[row][i] == num):
            return True
    return False

# returns true if a number in the given column matches the specified num, and false otherwise
def used_in_col(arr, col, num):
    for i in range(9):
        if(arr[i][col] == num):
            return True
    return False

# returns true if a number in the given 3x3 box matches the specified num, and false otherwise
def used_in_box(arr, row, col, num):
    for i in range(3):
        for j in range(3):
            if(arr[i + row][j + col] == num):
                return True
    return False

# checks whether or not the number can be assigned to a certain space
# AKA no repeats of the number in the row, column, or 3x3 box
def check_legal_assignment(arr, row, col, num):

    return (not used_in_row(arr, row, num) and
    not used_in_col(arr, col, num) and 
    not used_in_box(arr, (row - row % 3), (col - col % 3), num)
    )
            

##################################################################################################
###################################################################################################            

# the primary function of the project, take a partially filled sudoku grid as the only parameter
# attempts to assign values to all empty locations such that the Sudoku grid can be solved
# returns True if the board is solvable and False otherwise
def solve_sudoku(arr):

    # keeps track of the row and column for check_legal_assignment
    l = [0,0]

    # checks to see if there are no more unassigned locations AKA board is solved
    if (not find_empty(arr, l)):
        return True

    row = l[0]
    col = l[1]
    
    for num in range(1,10):

        if (check_legal_assignment(arr, row, col, num)):
            # if the number isn't found in the row, column, or box
            arr[row][col] = num

            # recursive call
            if (solve_sudoku(arr)):
                return True
            # else changes the value back to 0 to indiciate it is still unassigned
            arr[row][col] = 0

    # triggers the backtracking
    return False


##################################################################################################
##################################################################################################

if __name__ == "__main__":
    # instantiating a grid full of 0's
    board1 = [[0 for x in range(9)] for y in range(9)]

    # example of a solveable Sudoku board from the internet
    board1 =[[3, 0, 6, 5, 0, 8, 4, 0, 0],
          [5, 2, 0, 0, 0, 0, 0, 0, 0],
          [0, 8, 7, 0, 0, 0, 0, 3, 1],
          [0, 0, 3, 0, 1, 0, 0, 8, 0],
          [9, 0, 0, 8, 6, 3, 0, 0, 5],
          [0, 5, 0, 0, 9, 0, 6, 0, 0],
          [1, 3, 0, 0, 0, 0, 2, 5, 0],
          [0, 0, 0, 0, 0, 0, 0, 7, 4],
          [0, 0, 5, 2, 0, 6, 3, 0, 0]]

    if (solve_sudoku(board1)):
        print_board(board1)
    else:
        print ("No solution")


    print("____________________________________")

    # creating another grid
    board2 = [[0 for x in range(9) for y in range(9)]]

    # the same board from above but with a few values changed to make it unsolvable
    # changed values are at [0,0], [1,1], and [0, 1]
    board2 =[[2, 0, 6, 5, 0, 8, 4, 0, 0],
          [5, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 8, 7, 0, 0, 0, 0, 3, 1],
          [0, 0, 3, 0, 1, 0, 0, 8, 0],
          [9, 0, 0, 8, 6, 3, 0, 0, 5],
          [0, 5, 0, 0, 9, 0, 6, 0, 0],
          [1, 3, 0, 0, 0, 0, 2, 5, 0],
          [0, 0, 0, 0, 0, 0, 0, 7, 4],
          [5, 0, 5, 2, 0, 6, 3, 0, 0]]

    if (solve_sudoku(board2)):
        print_board(board2)
    else:
        print ("No solution")
