'''
Created on 10/23/2024
@author: Aidan Miller
Pledge: I pledge my honor that I have abided b the Stevens Honor System.

CS115 - Lab 6
'''
def isOdd(n):
    '''Returns whether or not the integer argument is odd.'''
    if n % 2 == 0:
        return False
    else:
        return True

    #42 in base 2:
    #42 contains one 32, one 8, and one 4
    #Therefore, 42 is 101010

    #If you are given an odd base-10 number, what will the least-significant
    #bit - the rightmost bit - be in its base-2 representation? Similarly, if
    #you are given an even base-10 number, what will the least-significant
    #bit - the rightmost bit - be in its base-2 representation?

    #If the base-10 number is odd, the rightmost bit is always 1, while when it
    #is even, it is always 0.

    #1010 = 10
    #101 = 5
    #1011 = 11
    #11111 = 31
    #1111 = 15
    #When taking away the last digit, it gives us half the original number via
    #integer division

    #If N is odd, it would be the base-2 representation of Y with a 1 added to
    #the end.
    #If N is even, it would be the base-2 representation of Y with a 0 added to
    #the end.

def numToBinary(n):
    '''Precondition: integer argument is non-negative.
    Returns the string with the binary representation of non-negative integer n.
    If n is 0, the empty string is returned.'''
    if n == 0:
        return ''
    elif isOdd(n):
        return numToBinary(n//2) + '1'
    else:
        return numToBinary(n//2) + '0'

def binaryToNum(s):
    '''Precondition: s is a string of 0s and 1s.
    Returns the integer corresponding to the binary representation in s.
    Note: the empty string represents 0.'''
    if len(s) == 0:
        return 0
    else:
        return binaryToNum(s[:-1])*2 + int(s[-1])

def increment(s):
    '''Precondition: s is a string of 8 bits.
    Returns the binary representation of binaryToNum(s) + 1.'''
    return ('00000000' + numToBinary(binaryToNum(s) + 1))[-8:]

def count(s, n):
    '''Precondition: s is an 8-bit string and n >= 0.
    Prints s and its n successors.'''
    if (n > 0):
        print(s)
        return count(increment(s), n-1)
    print(s)

def numToTernary(n):
    '''Precondition: integer argument is non-negative.
    Returns the string with the ternary representation of non-negative integer
    n. If n is 0, the empty string is returned.'''
    if (n == 0):
        return ''
    return numToTernary(n//3) + str(n % 3)

def ternaryToNum(s):
    '''Precondition: s is a string of 0s, 1s, and 2s.
    Returns the integer corresponding to the ternary representation in s.
    Note: the empty string represents 0.'''
    if (s==''):
        return 0
    return ternaryToNum(s[:-1]) * 3 + int(s[-1])
