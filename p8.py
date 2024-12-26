#  encapsulation
# private method
class School:
        def __init__(self):
                self.Name = "Abc"
                self.__place = "chennai"
                self.__Revenue = 5500000  #__private

        def __PrivateMethod(self):
                print(self.__Revenue)

        
        def Publicmethod(self):
                print(self.__Revenue)


school1 = School()
print(school1.Name)
school1.Publicmethod()

school1.__PrivateMethod()
