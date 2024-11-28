def factorial(n):
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)

def copies(n,ls):
    if n <= 0:
        return []
    else:
        return [(n*ls[0])] + copies(n - 1, ls[1:])
