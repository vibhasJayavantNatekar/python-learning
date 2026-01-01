#Nested Dictioneries

mytfamily = {
    "child1" : {
        "name" :"Emil",
        "year" : 2004
    },
    "child2" : {
        "name" : "Tobies",
        "year" :2007
    },
    "child3" : {
        "name" :"Linus",
        "year" : 2011
    }
}

print(mytfamily)

#Access item in nested dictionery

print(mytfamily["child1"]["name"])

