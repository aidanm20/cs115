############################################################
# Name: Aidan Miller
# Pledge: I pledge my honor that I have abided b the Stevens Honor System.
# CS115 Lab 1
#
############################################################

from math import factorial
from functools import reduce

def inverse(n):
    '''
    returns inverse of n
    '''
    return float(1.0 / n)
    

def e(n):
    '''
    This function approximates the mathematical value e using a Taylor expansion
    '''
    numbers = list(range(n+1))
    factorialed = map(factorial, numbers)
    inversed = map(inverse, factorialed)
    return reduce((lambda x, y: x + y), inversed)

