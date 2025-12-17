'''
Program to swap any two elemenrs in list

Example :- Input: [3,1,0,9,23,89,10] , 2 , 5
Output :- [3,1,89,9,23,0,10]

'''
#Method 1
#Swap using comma separator


list1 = [10,20,30,40,50,60]

print("Initial List : ", list1)

print("Swappig a items:")

list1[1],list1[3] = list1[3],list1[1]

print("List after swapc20 to  40 :", list1)

#Method 2
#Pop Values then inserting them back

list2  = [10,20,30,40,50,60]

print("initial list :" ,list2)
val1 = list2.pop(2)
val2 = list2.pop(5)

list2.insert(5,2)
list2.insert(2,5)

print("List after swapping :" , list2)
