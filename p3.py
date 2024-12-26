# constructor and constructor overloading

class Person:
    def __init__(self, name=None, age=None, phn = None):
        self.Name = name
        self.Age = age
        self.No = phn

person1 = Person(phn=233444)

print(person1.Name)
print(person1.Age)
print(person1.No)
