
dictionery = {
    "brand" : "Ford",
    "model" : "Mustang",
    "year"  : 1964
}

#Get the value of "model" key

x = dictionery["model"]

print(x)

#get() give you same result

get = dictionery.get("model")

print(get)

#keys() method will return a list of the keys in the dictionery

keys =  dictionery.keys()

print(keys)

#Values method will return a list of all the values in the dictionery

v =  dictionery.values()

print(v)

