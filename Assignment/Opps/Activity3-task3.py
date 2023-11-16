class Student:
    def __init__(self,name,marks):
        self.s_name = name
        self.s_marks = marks
    def check(self):
        if self.s_marks>=50:
            print(f"Passed with: {self.s_marks}")
        else:
            print(f"Failed with: {self.s_marks}")
#creating an object of Student class
student_1 = Student("Karma",40)

#check student's mark
student_1.check()
