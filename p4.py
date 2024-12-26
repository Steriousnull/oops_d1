# static and instance in oops

class Person:

    pi = 3.14
    sleepingtime = 8
    wakeup = 12

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.sleepingtime = 10


    @staticmethod
    def Sleep():
        print("everyone should sleep for ",Person.sleepingtime," hours daily")
     
    @classmethod
    def getup(cls):
        print("you shoukd wakeup at ",cls.wakeup,"am")
        
Person.Sleep()
Person.getup()
