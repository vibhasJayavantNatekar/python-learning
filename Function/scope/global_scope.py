x = 300

def myfunc():
    print(x)

myfunc()

print(x)

#global keyword

def myfunc2():
    global x
    x = 300


myfunc2()
print(x) 


