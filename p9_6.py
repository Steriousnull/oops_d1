# abstraction 
# hiding the implementation
# showing only necessary information
from abc import ABC,abstractmethod
class Vehicle(ABC):
     
     def __init__(self):
         self.Name = "Vehicle"

     @abstractmethod
     def StartEngine(self):
         pass
     
     def brake(self):
         print("brake")

class Car(Vehicle):
    def __init__(self):
        self.model = "2010"
        super().__init__()


    def StartEngine(self):
        super().__init__()
        print("car engine started")

car1 = Car()
car1.StartEngine()
car1.brake()
print(car1.Name)
