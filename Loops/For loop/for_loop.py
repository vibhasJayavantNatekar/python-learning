#Python for loop

fruits = ["apple" , "banana" , "cherry"]

for x in fruits:
    print(x)

#looping through an string

print("looping through an string")

for y in "banana":
    print(y)

#the break statement
# 

for x in fruits:
    print(x)
    if x == "banana":
        break

#the continue statement

for x in fruits:
    if x == "banana":
        continue
    print(x)

#range() function

for x in range(6):
    print(x)

#range() with start parameters

for x in range(2 , 6):
    print(x)

#range() with start and increament parameters

for x in range(2 , 30,3):
    print(x)

#Else in for loop 

for x in range(6):
    print(x)
else:
    print("Finnally finished!")        

#Nested Loops

adj = ["red" , "big" , "tasty"]
fruits= ["apple" , "banana" , "cherry"]

for x in adj:
    for y in fruits:
        print(x , y)



