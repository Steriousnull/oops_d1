#compile time polymorhism example

class Person:
    def __init__(self, name, age):
        self.Name = name
        self.Age = age

    #method overloading

    

    def Sleep(self, sleepingHours = None, start=None, end=None):
        if start is not None and end is not None:
            print("sleeping duration is ",abs(end - start))
        else:
            print("sleeping duration is ",sleepingHours)


person1 = Person("chandru",56)
person1.Sleep(start=20,end=6)
