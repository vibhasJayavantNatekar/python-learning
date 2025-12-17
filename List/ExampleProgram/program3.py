'''
Program to create two lists with Even and Odd numbers from the list
Example  :-
input - list[11,22,23,24,25]
output - list with even no - [22,24] , list with odd no - [11,23,25]
'''

list= [11,12,13,14,15,16,17]

evenList = []
oddList =  []

for x in list :
    if x % 2 == 0:
        evenList.append(x)
    else:
        oddList.append(x)

print(evenList)
print(oddList)
