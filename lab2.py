############################################################
# Name: Aidan Miller
# Pledge: I pledge my honor that I have abided b the Stevens Honor System.
# CS115 Lab 2
#
############################################################

def dot(L, K):
    """
    This function returns the dot product of L and K
    """
    if L == []:
        return 0
    if K == []:
        return 0
    else:
        return L[0] * K[0] + dot(L[1:], K[1:])
    
def explode(S):
    """
    This function converts string S to a list of characters
    """
    if S == "":
        return []
    else:
        return [S[0]] + explode(S[1:])
    
def ind(e, L):
    """
    This function returns the first index of e is found within sequence L
    """
    if L == [] or L == "":
        return 0
    elif L[0] == e:
        return 0
    else:
        return 1 + ind(e, L[1:])
    
def removeAll(e, L):
    """
    This function returns L without all elements e
    """
    if L == []:
        return []
    elif L[0] == e:
        return removeAll(e, L[1:])
    else:
        return [L[0]] + removeAll(e, L[1:])
        
def myFilter(fn, L):
    """
    This function returns elements of L where fn equals True
    """
    if L == []:
        return []
    elif fn(L[0]) == True:

        return [L[0]] + myFilter(fn, L[1:])
    else:
        return myFilter(fn, L[1:])
    
def deepReverse(L):
    """
    Returns the reversal of list L. Any element within list L is also reversed.
    """
    if L == []:
        return []
    else:
        if isinstance(L[0], list):
            return deepReverse(L[1:]) + [deepReverse(L[0])]
        else:
            return deepReverse(L[1:]) + [L[0]]

