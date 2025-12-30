x = ("apple" , "banana" , "cherry")

#First convert the tuple into list to be able to change it :

y = list(x)

y[1] = "kiwi"

x = tuple(y)

print(x)

