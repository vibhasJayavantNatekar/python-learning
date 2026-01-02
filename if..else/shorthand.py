a = 5
b = 2

#Shorthand if

if a > b: print("a is greater than b")

#Short hand if... else

print("A") if a > b else print("B")

#Assigning value with if... else

bigger = a if a > b else b
print("Bigger is " , bigger)



#Multiple Conditions on one line

print("A") if a > b else print(" = ") if a == b else print("B")

#Setting a default value

username = ""

display_name = username if username else "Guest" 

print("Welcome ,",display_name)

