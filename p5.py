#inheritance
#types of inheritance 
# 1.single level inheritance--grandparents-->parents
# 2.multilevel inheritance --grandparents-->parents-->child
# 3.multiple inheritance --child(parents, grandparents)
# 4.heirarchial inheritance --  grandparents
#                                 /      \
#                            parents     child
# 5.hybrid( combination of all types of inheritance)


class Parent:
    def Sing(self):
        print("i know singing")

    def Cricket(self):
        print("i know cricket")

class Child(Parent):

    def Dance(self):
        print("i know dancing")

child1 = Child()
child1.Dance()
child1.Sing()
child2 = Parent()
print("child 2 details")
child2.Cricket()

class Babies(Parent, Child):
    def skills(self):
        return "hi"
    
baby1 = Babies()
baby1.Sing()
baby1.Cricket()
baby1.Dance()
baby1.skills() 
