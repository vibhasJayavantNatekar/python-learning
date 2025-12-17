'''
Print list after removing EVEN numbers

Example :
input - list = [11,22,33,44,55]
output - list after removing Even numbers  list = [11,33,55]
'''

list = [11,22,33,44,55]
print(list)

for x in list:
    if x % 2 != 0:
        list.remove(x)


print("List after removing Even numbers .")
print(list)

#2 Approach
#Using list comprehension

mixList = [10,20,30,11,21,31,40,41]
print(mixList)

neslist2 = [x for x in mixList if x % 2 != 0 ]

print("List after removing EVEN numbers :")
print(newList2)

print("List after removing Even numbers :")
print(newList2)


#3 Approach
#Using filter and  Lamda functions

list2 = [11,22,33,44,55]
print("Original List")
print(list2)

newList = list(filter(lambda x: (x % 2 != 0) ,list2))

print("list after removing Even numbers:")
print(newList)
               


