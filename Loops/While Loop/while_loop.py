#Python while loop

i =1
while i < 6:
    print(i)
    i += 1

#The break statement

#with break statement we can stop loop even if condition is true
j=0

while j < 6:
    print(j)
    if j == 3:
        break
    j += 1

#The continue  statement

#continue statement can stop current iteration and continue with next

k = 0 

while k < 6:
    k +=1
    if k == 3:
        continue
    print(k)


#else statement in while loop

#run block of code once the condition is false

print("/n")

y =0

while y < 6:
    print(y)
    y += 1
else:
    print("y is no longer less than 6")