#class and object creation and method operation using it

class Student:
    def __init__(self, name="david", english=12, kannada=23, tamil=65, maths=99, science=101):
        self.name = name
        self.english = english
        self.kannada = kannada
        self.tamil = tamil
        self.maths = maths
        self.science = science

    def TotalMarks(self):
        """self.total = total
        total = self.english + self.kannada + self.maths +self.science + self.tamil"""
        return self.english + self.kannada + self.maths +self.science + self.tamil

    def percentage(self):
        return (self.TotalMarks()/500)*100

    def display_details(self):
        print(f"Name: {self.name}")
        print(f"English: {self.english}")
        print(f"Kannada: {self.kannada}")
        print(f"Tamil: {self.tamil}")
        print(f"Maths: {self.maths}")
        print(f"Science: {self.science}")
        print(f"Total Marks: {self.TotalMarks()}")
        print(f"Percentage: {self.percentage()}")

student1 = Student()
student1.display_details()    
