
#Join Sets

#using Union()

set1 = {"a" , "b" , "c"}

set2 = {1 , 2 , 3}

setUnion =set1.union(set2)

print(setUnion)

# join multiple set using union()

set3 = {"John" , "Elena"}
set4 = {"apple" , "bananas"  , "cherry"}


setmulJoin = set1.union(set2,set3,set4)

print(setmulJoin)

# join multiple set using  |

setjoin = set1 | set2 | set3 | set4

print(setjoin)

#Join a set and a Tuple

#using union()

x = {"a" , "b" , "c"}    #set

y = (1 , 2 , 3)         #tuple

z = x.union(y)

print(z)


#Update ()
#This method inserts the items in set2 into set1 :

set1.update(set2)
print(set1)


# intersection()

# returns an new set that only contain the duplicates

setnew = {"a"  , "d" , "c"}

setIntersection = set1.intersection(setnew)

print(setIntersection)

#Differnce

#This method will return a new set that will contain only the item from first set that are not present in the other set.

setDifference = set1.difference(setnew)

print(setDifference)

#symmentric difference 

#keep items that are NOT present in both sets

setSymDiff = set1.symmetric_difference(setnew)

print(setSymDiff)

# alternately you can use ^ operator  

setsydiff2 = set1 ^ setnew 
print(setsydiff2)








