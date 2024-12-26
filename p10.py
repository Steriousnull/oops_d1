# Encapsulation using Getter and Setter Method 
# we can set the private name by implemting method within the class and we can also get the private variable with the help of implementing another method
class Person:
    def __init__(self):
        self.__name = None

    def Setname(self, Value):
        self.__name = Value
   
    def Getname(self):
        return self.__name
    

person1 = Person()
person1.Setname("chandru")
print(person1.Getname())
