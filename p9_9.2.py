# Encapsulation using Getter and Setter Method 
class Person:
    def __init__(self):
        self.__name = None
        self.__age = None

    @property   
    def name(self):
        if self.__name is None:
            return "please initialize name"
        else:
            return self.__name


    @name.setter
    def name(self, Value):
        if len(Value)>20:
            print("you cannot set the name having characters more than 20")
        else:
            self.__name = Value
   
    """def Getname(self):
        if self.__name is None:
            return "please initialize name"
        else:
            return self.__name"""
    
    @property
    def age(self):
        return self.__age
    
    @age.setter
    def age(self, value):
        if value <= 0:
            print("age cannot be negative")
        else:
            self.__age = value




    
    

person1 = Person()
person1.name = "chandru"
#print(person1.Getname())
print(person1.name)
person1.age = -12
print(person1.age)
