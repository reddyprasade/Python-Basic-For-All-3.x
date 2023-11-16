#definition of the class starts here  
class Person:  
    #defining constructor  
    def __init__(self, personName, personAge):  
        self.name = personName  
        self.age = personAge  
  
    #defining class methods  
    def showName(self):  
        print(self.name)  
  
    def showAge(self):  
        print(self.age)  
  
    #end of class definition  
  
# defining another class  
class Student: # Person is the  
    def __init__(self, studentId):  
        self.studentId = studentId  
  
    def getId(self):  
        return self.studentId  
  
  
class Resident(Person, Student): # extends both Person and Student class  
    def __init__(self, name, age, ids):  
        Person.__init__(self, name, age)  
        Student.__init__(self, ids)  
  
  
# Create an object of the subclass  
resident1 = Resident('Reddy Prasade', 29, '1024,East Baliji Nagar ')  
resident1.showName()  
print(resident1.getId())  
