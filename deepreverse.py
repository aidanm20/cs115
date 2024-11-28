def deepReverse(L):
    """
    returns the reversal of a list with reversing lists witin
    """
    if L == []:
        return 0 or []
    if isinstance(L[0], list): # returns true if x is a list
        return deepReverse(L[1:]) + [deepReverse(L[0])] 
    else:
        return deepReverse(L[1:]) + [L[0]] #Brackets are mu y importante


    
    
print(deepReverse([0, 1,2,3,4]))
