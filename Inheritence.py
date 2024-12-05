class Person:
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname
        
    def printName(self):
        print(self.fname,"",self.lname)

class Student(Person):
    def __init__(self,fname,lname,year):
       super().__init__(fname,lname)
       self.year = year
    def printStudentInfo(self):
        print(self.fname,"",self.lname,"",self.year)


obj = Person('Injamul','Haque')
obj.printName()

obj2 = Student("Mike", "Olsen", 2019)
obj2.printStudentInfo()
