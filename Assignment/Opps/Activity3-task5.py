class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f'{self.name} is {self.age} years old')

f_name=input("Enter the name:")
f_age=int(input("Enter the age:"))
female = Person(f_name, f_age)

m_name=input("Enter the name:")
m_age=int(input("Enter the age:"))
male = Person(m_name, m_age)
female.display()
male.display()
