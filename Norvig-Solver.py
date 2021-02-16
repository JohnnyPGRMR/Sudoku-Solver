# Definitions that make up the sudoku board.
# A Sudoku puzzle is a GRID of 81 squares; commonly the columns are labeled 1-9, 
# the rows A-I, and the collection of nine suqares (whether in column, row or box) 
# a UNIT, squares sharing a unit are called PEERS.
test_board = '000157004000923150010000003006735410002000500054261300500000090083576000600892000'
# Defining the indices.
digits = '123456789'
rows = 'ABCDEFGHI'
cols = digits

def cross(A,B):
    '''Is a modified cross product between 
    A and B (which represents rows and columns in this use case), 
    and builds a list containing every places index value.'''
    #### GAH!  These are LIST COMPREHENSIONS!!!
    return [a + b for a in A for b in B]
    # This whole function could alternatively be written as below:
    # squares = []
    # for a in rows:
    #   for b in cols:
    #       squares.append(a+b)
    ##### PS, this is a list comprehension!! #####

squares = cross(rows,cols)  

# Generate a list of all the units for each square in the board.  
# Each square has a row, column, & square associated with it.

# First line works because "cols" is a string of integers and rows is a string 
# of letters, running the cross function on them generates the rows making up 
# the board.
unit_list = ([cross(rows,c) for c in cols] + 
# Second line works because "rows" (which is being iterated through)is a string 
# of letters, and "cols" is a string of integers.  Running the cross function 
# on them generates a list for each column in the board.
            [cross(r, cols) for r in rows] + 
# Third line generates nested lists where each list is one of the squares 
# making up the board.
            [cross(rs, cs) for rs in ('ABC','DEF','GHI') for cs in ('123', '456', '789')])

# Create a dictionary with each square as the key, and each unit, 
# row and column associated with it.
units = dict((s,[u for u in unit_list if s in u]) for s in squares)

# Create a dictionary with each square as the key for the remaining squares 
# (peers) making up each unit on the board.  
# Dictionary is in the form of a key value with an associated set of peers.
peers = dict((s, set(sum(units[s],[]))-set([s])) for s in squares)

def grid_values(grid):
    '''Convert grid into a dict of {square: char} with '0' or '.' for empties.'''
    # Building list of values making up the grid using the above conditions 
    # for denoting empty squares.
    chars = [c for c in grid if c in digits or c in '0.']
    # Check if the characters built equal the total number of squares in a board.
    assert len(chars) == 81
    return dict(zip(squares, chars))

# This function below is the core function that works to solve the board.
def eliminate(values, s, d):
    '''Eliminate d (digits) from values[s]; propagate when values or places <= 2.
    Return values, except return False if a contradiction is detected.'''
    if d not in values[s]:
        return values   ## Extra digits already eliminated.
    values[s] = values[s].replace(d,'')
    ### (1) If a square s is reduced to one value d2, then eliminate d2 from the peers.
    if len(values[s]) == 0:
        return False    ## Contradiction: removed last value.
    elif len(values[s]) == 1:
        d2 = values[s]
        if not all(eliminate(values, s2, d2) for s2 in peers[s]):
            return False
    
    ### (2) If a unit u is reduced to only one place for a value d, then put it there.
    for u in units[s]:
        dplaces = [s for s in u if d in values[s]] 
        if len(dplaces) == 0:
            return False    ## Contradiction: no place for this value
        elif len(dplaces) == 1:
        # d can only be in one place in unit; assign it there.
            if not assign(values, dplaces[0], d):
                return False
    return values

def assign(values, s, d):
    '''Eliminate all the other values (except d) from values[s] and propagate.
    Return values, except return False if a contradiction is detected.'''
    other_values = values[s].replace(d, '')
    if all(eliminate(values, s, d2) for d2 in other_values):
        return values
    else:
        return False

def parse_grid(grid):
    '''Convert grid to a dictionary of possible values, {square: digits}, 
    or return False if a contradiction is detected.'''
    # To start, create the dictionary with every square can be any digit.
    values = dict((s,digits) for s in squares)
    for s,d in grid_values(grid).items():
        if d in digits and not assign(values, s, d):
            return False    ## Fail if we can't assign d (digit) to square s.
        return values

def display(values):
    '''Display these values as a 2-D grid.'''
    width = 1 + max(len(values[s]) for s in squares)
    line = '+'.join(['-'*(width*3)]*3)
    for r in rows:
        print(''.join(values[r+c].center(width) + ('|' if c in '36' else '') for c in cols))
        if r in 'CF':
            print(line)
    print()

def some(seq):
    '''Return some element of seq that is true.'''
    for e in seq:
        if e:
            return e
    return False
    
def search(values):
    '''Using depth-first search and propagation, try all possible values.'''
    if values is False:
        return False ## Failed earlier.
    if all(len(values[s]) == 1 for s in squares):
        return values  ## Solved!
    ## Choose the unfilled square s with the fewest possibilities.
    n,s = min((len(values[s]),s) for s in squares if len(values[s]) > 1)
    return some(search(assign(values.copy(), s, d))
        for d in values[s])