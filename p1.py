class Human():
    def __init__(self, name, age, height, weight, id):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
        self.id = id

class Details(Human):
    pass

person1 = Details('chandru','23','56','23','1001')

print(person1.name,person1.age,person1.height,person1.weight,person1.id)

person2 = Human("dev","23","123","45","12245")
print(person2.name)
print(person2.age)
print(person2.height)
print(person2.weight)
print(person2.id)
