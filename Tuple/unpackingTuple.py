
fruits = ("apple", "banana" , "cherry")

#Unpacking a tuple

(green , yellow , red) = fruits

print(green)
print(yellow)
print(red)

#Unpacking using a Asterisk*

fruits2 = ("apple" , "banana" , "cherry" , "strawberry" , "raspberry")

#Assign the rest of the values as a list called "red".

(green , yellow , *red) = fruits2


print(green)
print(yellow)
print(red)