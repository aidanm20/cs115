def mult_r(a,b):
    if b == 1:
        return a
    else:
        return a + mult_r(a, b-1)
print(mult_r(5,4))
