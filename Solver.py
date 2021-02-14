# This script can solve any given Sudoku puzzle using a backtracking algorithm.

# Here is an example sudoku board I will be using for the moment hard coded in.
board = [
    [0,0,0,0,6,0,1,0,0],
    [0,0,4,0,9,5,0,6,8],
    [0,6,1,0,7,0,9,3,0],
    [0,5,0,0,0,0,4,0,7],
    [1,0,0,4,2,9,0,0,6],
    [4,0,6,0,0,0,0,1,0],
    [0,2,5,0,3,0,7,4,0],
    [6,1,0,7,4,0,5,0,0],
    [0,0,9,0,8,0,0,0,0],
]
def plot_board(bo):
    ''' Draws a sudoku board in the terminal window.
    Input parameter bo is the 2d array of board values.
    :return: None.'''

    # Where i represents the index of the row of values (board after all is a 2d array of numbers).
    for i in range(len(bo)):
        # This is more of a cosmetic choice, 
        # the i != 0 condition changes where the first seperation line gets drawn.
        if i % 3 == 0 and i != 0:  
            print("- - - - - - - - - - - -")

        # Where j represents the index of the column of values.  
        # Since it is an N x N matrix either 0 or i could be put in the for the index of the variable "bo".
        for j in range(len(bo[i])):
            # Cosmetic choice, but is the simplest way to draw a board, 
            # changing it will require more lines of code to completely draw a symmetric board.
            if j % 3 == 0 and j != 0:  #
                # Print has an additional parameter "end" that by default does a carriage return, 
                # change to "" so the next print command plots on the same line.
                print(" | ",end="")

            # If confused and thinking should check for j == 9 remember that python starts indexing at 0.  
            # So 8 is the position of the 9th number!
            if j == 8:
                # Default for print is to do a carriage return, which we want at the end of the board (the 9th position).
                print(bo[i][j])
            # The else statement below is what actually prints the numbers in the board.
            else:
                print(str(bo[i][j]) + " ", end="")

def check_empty(bo):
    '''This function checks which indexes are empty (equals 0) in 
    a 2d array of values that is being used in this script to solve a sudoku board.'''
    for i in range(len(bo)):
        for j in range(len(bo[i])):

            if bo[i][j] == 0:   # Check if empty.

                # return the indices of that empty value.
                return (i,j)    # where i represents row index number and j represents the column index number.

checker = check_empty(board)


# class Board():

#     def __init__(self):
#         self.board = board