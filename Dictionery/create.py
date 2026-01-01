thisdict = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year"  : 1984
}

print(thisdict)

#Print the value of "brand" in the dictionery

print(thisdict["brand"])

#Duplicate values will overwrite existing values :

thisdict2 = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year"  : 1984,
    "year" : 2005
}

print(thisdict2)


#The dict()  Constructor to  make dictionery

thisdict4 = dict(name = "John" , age = 36 ,country = "Norway")
print(thisdict4)



#Dictionery Length

#Print the numbers items in the dictionery

print(len(thisdict))



#Dictionery items can be any data type 

thisdict3 = {
    "brand" : "Ford",
    "electric" : False,
    "year" : 1964 ,
    "colors" : ["red" , "white" , "blue"]

}

print(thisdict3)
