#Assigning and display none value:

x = None
print(x)

#use type() to see type of a None value.

y =None
print(type(y))

#Comparing to None

result = None
if result is None:
    print("No result yet")
else:
    print("Result is ready")

#None evauetes to False in a boolean context.

print(bool(None)) #False


#Function that returning none

def myfunc():
    x =5

x = myfunc()
print(x)    

