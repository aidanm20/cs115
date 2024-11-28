
#when z is 0, zerodivision error but when y is 0 it goes correctly

try:
    z = int(input("Enter a number"))
    y = 10
    x = y / z
    print(x)
except ZeroDivisionError as error:
    print(error)
except TypeError as err:
    print(err)
except:
    print("some error happen!")
else:
    print("x is calculated correcly")
finally:
    print("Done")

