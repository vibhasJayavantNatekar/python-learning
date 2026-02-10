#Method Accessing Properties

class Person:
    def __init__(self , name , age):
        self.name = name
        self.age = age

    #Mthos Accessing Properties
    def get_info(self):
        return f"{self.name} is {self.age} years old"
    
    #Method Modifying Properties

    def celebrate_birthday(self):
        self.age +=1
        print(f"Happy birthday ! You are now {self.age}")


p1 = Person("Toblas" , 28)
print(p1.get_info())        
p1.celebrate_birthday()
p1.celebrate_birthday()

