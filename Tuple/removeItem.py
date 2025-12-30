
#Remove item

thistuple = ("apple" , "banana" , "cherry")
print(thistuple)

#Convert tuple into list , remove item  , and convert back into a tuple

y = list(thistuple)
y.remove("apple")

thistuple = tuple(y)

print(thistuple)
