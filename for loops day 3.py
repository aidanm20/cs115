#A[row][col]
A = [[2,1,1],
     [1,4,1],
     [0,0,1]]

print(A[2][2], A[1][0])
print(A[1][1] + A[0][0])
print(A[1][1] * A[0][0])

def f():
    L=[1,2,3,4]
    g(L)
    return L

def g(List):
    List[0] = 42

newL = f()
print(newL[0])


def f():
    L =[1,2,3,4]
    M = g(L)
    print(L)
    print(M)
 

def g(List):
    return list(map(lambda x: x, List))
f()

#___________________________________________________________________________________
def f():
    L =[1,2,3,4]
    M = g(L)
    L[0] = 42
    print(L)
    print(M)
    #L and M provide different answers because now L and M have
    #different memory addressses

def g(List):
    return list(map(lambda x: x, List))
# map allocates 1 item from the list and put them in 1 by 1 & creates new address

f()

'''
Assignment copies one reference
x = 2020
y = x
x -> 2020
y -> 2020 (Same 2020 as x,in other words same addess as 2020)
then if i do x=42
x will now point to 42 (x -> 42)
but 42 is in different memory address than 2020

'''
x=2020
print(x)
y=x
print(y)
x=42
print(x)
print(y)

#lists are mutable, contents are references
'''
A shallow copy creates a new array, but it does not create new copies of the
elements within the array. Instead, it points to the same elements as the
original array. A deep copy, on the other hand, creates a completely
independent copy of both the array and its data. It does not share any data
with the original array
'''
#z = w is a shallow copy





