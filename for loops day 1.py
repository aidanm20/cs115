for char in "this string":
    print(char)
#range(start index, end index, step)
#10, 10 - 2, 8 - 2, 6 - 2 < 5
for i in range(10, 5, -2):
    print(i)

total = 0
for num in range(10, 25):
    total += num
    print(total)

for odd in range(1, 66, 2):
    print(odd)

'''
while(condition):
    instruction
'''
i=0
while i<100:
    print(i)
    i+=1

#prints squared version 
def mapSqr(L):
    i=0
    final = []
    for index in range(len(L)):
        L[index] = L[index] ** 2
    retur L

def mapSqr(L):
    for num in L:
        final[i] = num ** 2
        i += 1
    return final

def mapSqr(L):
    return [i ** 2 for i in L]

 
