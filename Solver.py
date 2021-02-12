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
print(board)


def print_board(bo):
    """
    prints the board
    :param bo: 2d List of ints
    :return: None
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

print_board(board)