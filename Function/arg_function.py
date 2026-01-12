def my_function(fname): #fname is a parameter
    print(fname +  " Refnes")

my_function("Emil") #"Emil" is a argument
my_function("Toblas") #"Toblas" is a argument
my_function("Linus") #"Linus" is a argument

#Default Parameter

def default_function(name = "friend"):
    print("Hello" , name)

default_function("Emil")
default_function("Toblas")
default_function()   
default_function("Linus")    

#We can send argument with key = Value syntax

def my_function2(animal , name):
    print("I have a" , animal)
    print("My " , animal  +'s name is ' , name)


my_function2(animal= "dog" , name="Buddy")

