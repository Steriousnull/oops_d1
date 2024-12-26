#  --------********************--------------

# Encapsulation
# access modifiers 
#
# public -- it can be accessed from anywhere, 
# private --only it can be accessed from the class, 
# protected -- it can be accessed from both child class and sub class


class School:
    def __init__(self):
        self.Name = "abc"
        self.__Place = "bangkok"
        self.__Revenue = 6000000  #  __ is private
    
    """def schoolrevenue(self):
        print(self.__Revenue)"""

school1 = School()
print(school1.Name)
#school1.schoolrevenue()

#hack
#object, clas_name, private_keyword
print(school1._School__Revenue)
