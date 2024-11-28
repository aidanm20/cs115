def length(l):
    if l == []:
        return 0
    else:
        return 1 + ength(l[1:])

print(length([1,2,3]))
print(length(['a', 'c', 1, 'r', 5.4, 7]))

def power(n,p):
    if p == 0:
        return 1
    else:
        return n* power(n,p-1)

print(power(4,3))
print(power(2,6))
