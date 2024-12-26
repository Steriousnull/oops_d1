# protected method
class School:
        def __init__(self):
                self.Name = "Abc"
                self.place = "chennai"
                self._Revenue = 5500000  #__private

class Faculty(School):
        def Revenue(self):
                print(self._Revenue)
    



faculty1 = Faculty()
faculty1.Revenue()
