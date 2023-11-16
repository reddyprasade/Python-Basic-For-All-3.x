class Calculator:
    def __init__(self):
        self.total=0
        
    def add_numbers(self,*args):
        self.total = 0
        for number in args:
            self.total += number
        return self.total

calculator=Calculator()
result_empty=calculator.add_numbers()
print("Calling method without argument:",result_empty)

result1=calculator.add_numbers(9,4)
print("Calling method with two argument:",result1)

result2=calculator.add_numbers(3,20,4)
print("Calling method with three argument:",result2)
