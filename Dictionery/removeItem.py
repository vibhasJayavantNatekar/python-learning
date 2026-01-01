#Removes an item from dictionery

thisdict = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year"  : 1984
}

#pop() method remove specific item

thisdict.pop("model")

print(thisdict)

#popitem() removes the last inserted item


thisdict.popitem()

print(thisdict)

#clear() method empties the dictionery

thisdict.clear()
print(thisdict)