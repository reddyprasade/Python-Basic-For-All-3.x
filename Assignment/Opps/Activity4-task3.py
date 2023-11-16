class Calculator:
    def __init__(self):
        self.total = 0

    def add_numbers(self, **kwargs):
        for key in kwargs:
            self.total += kwargs[key]
        return self.total

calculator = Calculator()

result_1 = calculator.add_numbers()
print("Calling method without argument:",result_1)

result_2 = calculator.add_numbers(num1=1, num2=2, num3=3)
print("Calling method with two argument:",result_2)



