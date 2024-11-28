############################################################
# Name: Aidan Miller
# Pledge: I pledge my honor that I have abided by the Stevens Honor System.
# CS115 Lab 9
#
############################################################
def mult(c,n):
    '''
    returns product of c *n
    '''
    result=0
    for i in range(n):
        result = result + c
    return result

#print(mult(6,7))
#print(mult(1.5,28))


def update(c,n):
    """ update starts with z=0 and runs z = z**2 + c
        for a total of n times. It returns the final z.
    """
    z=0
    for i in range(n):
        z = z**2 + c
    return z

#print(update(1,3))
#print(update(-1,3))
#print(update(1,10))
#print(update(-1,10))

def inMSet(c,n):
    '''
    Fuction takes complex number c and integer n. Returns a boolean that's true
    if c is in the Mandelbrot set and false if otherwise.
    '''
    z=0
    for i in range(n):
        z = z**2 + c
        if abs(z) > 2:
            return False
    return True
'''
c=0+0j

print(inMSet(c,25))
c = 3+4j
print(inMSet(c,25))


c = 0.3 + -0.5j # this one is also in the
print(inMSet(c, 25))
    
c = -0.7 + 0.3j # this one is NOT in the set
print(inMSet(c, 25))

c = 0.42 + 0.2j
print(inMSet(c, 25)) # this one seems to be in the set

print(inMSet(c, 50)) # but it turns out that it's not!
'''


from cs5png import * # You may already have this line...
def weWantThisPixel( col, row ):
    """ a function that returns True if we want
    the pixel at col, row and False otherwise
    """
    if col%10 == 0 and row%10 == 0:
        return True
    else:
        return False
    
def test():
    """ a function to demonstrate how
    to create and save a png image
    """
    width = 300
    height = 200
    image = PNGImage(width, height)
    # create a loop in order to draw some pixels
    for col in range(width):
        for row in range(height):
            if weWantThisPixel( col, row ) == True:
                image.plotPoint(col, row)
    # we looped through every image pixel; we now write the file
    image.saveFile()

'''
if col % 10 == 0 and row % 10 == 0 changed to if col % 10 == 0 or row % 10 == 0:,
it will create a grid
'''

def scale(pix,pixelMax,floatMin, floatMax):
    """ scale takes in
        pix, the CURRENT pixel column (or row)
        pixMax, the total # of pixel columns
        floatMin, the min floating-point value
        floatMax, the max floating-point value
        scale returns the floating-point value that
        corresponds to pix
    """
    pixelm = pix/pixelMax
    floatNum = floatMax - floatMin
    result = floatNum*pixelm + floatMin
    return result
'''
print(scale(100, 200, -2.0, 1.0)) # halfway from -2 to 1
print(scale(100, 200, -1.5, 1.5)) # halfway from -1.5 to 1.5
print(scale(100, 300, -2.0, 1.0)) # 1/3 of the way from -2 to 1
print(scale(25, 300, -2.0, 1.0))
print(scale(299, 300, -2.0, 1.0)) # your exact value may differ slightly

'''
def mset():
    """ creates a 300x200 image of the Mandelbrot set
    """
    width = 300
    height = 200
    image = PNGImage(width, height)
    # create a loop in order to draw some pixels
    for col in range(width):
        for row in range(height):
            # here is where you will need
            # to create the complex number, c!
            n = 25
            x = scale(col, width ,-2, 1)
            y = scale(row, height, -1, 1)
            c = x + y*1j
            
            if inMSet( c, n ) == True:
                image.plotPoint(col, row)
    # we looped through every image pixel; we now write the file
    image.saveFile()









    
