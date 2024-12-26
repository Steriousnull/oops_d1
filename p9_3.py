# Encapsulation using Getter and Setter Method 


class Person:
    def __init__(self):
        self.__firstname = "chandru"
        self.__lastname = "david"

    @property     #property is used to convert a method into variable
    def FullName(self):
        return self.__firstname + " " + self.__lastname
    
person1 = Person()
print(person1.FullName)
