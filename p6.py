class Parent:
    def __init__(self, NetWorth):
        self.NetWorth = NetWorth

class Child(Parent):
    def __init__(self, Networth):
      #to use property from parent class
        super().__init__(Networth)
        print("child constructor is invoked")

    def ChildNetWorth(self):
        print(self.NetWorth//2)

child1 = Child(10000)
print(child1.NetWorth)
child1.ChildNetWorth()
