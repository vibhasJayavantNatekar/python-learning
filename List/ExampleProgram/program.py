"""
Python Program to print all numbers which are divisible by M and N in the list 

Example  :
input:
list = [10 , 15, 20 , 25,30]
M = 3 , N =5

output :
15
30

"""

#Program

list = [5,10,15,20,25,30,35,40]

M = 2
N = 5

print("List is : ", list)

print(f"Numbers divisible by {M} and {N}")

for num in list :
    if num % M == 0 and num % N == 0 :
        print(num)
