class Person:
    def __init__(self , name ,age):
        self.name = name
        self.__age = age  #Private Property

p1 = Person("Emil" , 25)

print(p1.name)

#  print(p1.__age)  #This will cause an error



class Person2:
    def __init__(self , name ,age):
        self.name = name
        self.__age = age
#Get Private Property value

    def get_age(self):
        return self.__age
    
    def set_age(self , age):
        if age > 0:
            self.__age = age
        else:
            print("Age must be positive")    
    
p2 = Person2("Toblas" , 25)

print(p2.get_age())


p2.set_age(20)
print(p2.get_age())


    
        


        
        