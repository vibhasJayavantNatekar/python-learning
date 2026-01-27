class Person:
    def __init__(self , name , age):
        self.name = name
        self.age =age


p1 = Person("Emil",36)

print(p1.name)
print(p1.age)

#Default value in __init__()

class Person2:
    def __init__(self , name , age = 18):
        self.name = name
        self.age = age

n1 = Person2("Vibhas")
n2 = Person2("sam", 12)

print(n1.name , n1.age)
print(n2.name , n2.age)


