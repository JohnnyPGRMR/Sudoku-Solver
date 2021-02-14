# Defining the indices.
digits = '123456789'
rows = 'ABCDEFGHI'
cols = digits

def cross(A,B):
    '''Is a modified cross product between 
    A and B (which represents rows and columns in this use case), 
    and builds a list containing every places index value.'''
    return [a + b for a in A for b in B]
    # This whole function could alternatively be written as below:
    # squares = []
    # for a in rows:
    #   for b in cols:
    #       squares.append(a+b)

squares = cross(rows,cols)   

#  Each square in the squares list has 3 units