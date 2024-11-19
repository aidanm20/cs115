from functools import reduce

############################################################
# Name: Aidan Miller
# Pledge: I pledge my honor that I have abided b the Stevens Honor System.
# CS115 HW 1
#
############################################################
def factorial(n):
    '''
    This function finds the factorial
    '''
    sKidBidilist = list(range(1,n+1))
    return reduce((lambda x, y: x * y), sKidBidilist)

def mean(L):
    '''
    This function finds the mean
    '''
    add = reduce((lambda x, y: x + y), L)
    return add / len(L)
