try:
    print(x)
except:
    print("An exception occured")

#Many exceptions

try:
    print(y)
except NameError:
    print("Variable x is not defined")
except:
    print("Something else went wrong")      


#With else block

try:
    print("Hello")
except:
    print("Something went wrong")
else:
    print("Nothing went wrong")

#Finnally  Block

try:
    print(z)
except:
    print("Something went wrong")
finally:
    print("The 'try except ' is finished")



