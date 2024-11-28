#
# life.py - Game of Life lab
#
# Name: Aidan Miller
# Pledge: I pledge my honor that I have abided by the Stevens Honor System.
#

import random

def createOneRow(width):
    """Returns one row of zeros of width "width"...  
       You should use this in your
       createBoard(width, height) function."""
    row = []
    for col in range(width):
        row += [0]
    return row

def createBoard(width, height):
    """ returns a 2d array with "height" rows and "width" cols """
    A = []
    for row in range(height):
        A += [createOneRow(width)] # What do you need to add a whole row here?
    return A

#A = createBoard(5,3)
#print(A)

import sys
def printBoard( A ):
    """ this function prints the 2d list-of-lists
    A without spaces (using sys.stdout.write)
    """
    for row in A:
        for col in row:
            sys.stdout.write( str(col) )
        sys.stdout.write( '\n' )


#A = createBoard(5,3)
#printBoard(A)

def diagonalize(width,height):
    """ creates an empty board and then modifies it
    so that it has a diagonal strip of "on" cells.
    """
    A = createBoard( width, height )
    for row in range(height):
        for col in range(width):
            if row == col:
                A[row][col] = 1
            else:
                A[row][col] = 0
    return A
#A = diagonalize(7,6)
#print(A)
#printBoard(A)

def innerCells(w,h):
    '''
    Makes all the cells on the outside 0 and the inside ones 1
    '''
    A = createBoard(w,h)
    for row in range(h):
        for col in range(w):
            if h-1 > row > 0 and w-1 > col > 0:
                A[row][col] = 1
            else:
                A[row][col] = 0

    return A

#A = innerCells(5,5)
#printBoard(A)

def randomCells(w,h):
    '''
    The outer cells will all be 0 but the inner cells are assigned either 0 or 1 randomly
    '''
    A = createBoard(w,h)
    for row in range(h):
        for col in range(w):
            if h-1 > row > 0 and w-1 > col > 0:
                A[row][col] = random.choice([0,1])
            else:
                A[row][col] = 0

    return A

#A = randomCells(10,10)
#printBoard(A)


def copy(A):
    '''
    Deep copies the list A
    '''
    return createBoard(len(A[0]), len(A))
'''
oldA = createBoard(2,2)
printBoard(oldA)

newA = copy(oldA)
printBoard(newA)

oldA[0][0] = 1
printBoard(oldA)

printBoard(newA)
'''

def innerReverse(A):
    '''
    This function returns the reverse of list A except the outer elements which will be 0
    '''
    for row in range(len(A[0])):
        for col in range(len(A)):
            if len(A[0])-1 > row > 0 and len(A)-1 > col > 0:
                if A[row][col] == 0:
                    A[row][col] = 1
                else:
                    A[row][col] = 0
            else:
                A[row][col] = 0

    return A
'''
A = randomCells(8,8)
printBoard(A)
print("")
A2 = innerReverse(A)
printBoard(A2)
'''

def next_life_generation( A ):
    """ makes a copy of A and then advanced one
    generation of Conway's game of life within
    the *inner cells* of that copy.
    The outer edge always stays 0.
    """
    newA = copy(A) 
    for row in range(1, len(A) - 1):  
        for col in range(1, len(A[0]) - 1):
            alive = countNeighbors(row, col, A)
        
            if A[row][col] == 1:  
                if alive < 2 or alive > 3:
                    newA[row][col] = 0 
                else:
                    newA[row][col] = 1  
            else:  
                if alive == 3:
                    newA[row][col] = 1  
    return newA


def countNeighbors(row,col,A):
    counter = 0
    for i in range(max(0, row-1), min(len(A), row+2)):
        for j in range(max(0, col-1), min(len(A[0]), col+2)):
            if (i != row or j != col) and A[i][j] == 1:
                counter +=1

    return counter

A = [ [0,0,0,0,0],
[0,0,1,0,0],
[0,0,1,0,0],
[0,0,1,0,0],
[0,0,0,0,0]]
'''
printBoard(A)
print("")
A2 = next_life_generation( A )
printBoard(A2)

print("")
A3 = next_life_generation(A2)
printBoard(A3)

'''





            
            
