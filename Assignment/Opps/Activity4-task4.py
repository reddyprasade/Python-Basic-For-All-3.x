class Calculator:
    def __init__(self):
        self.total = 0
    
    def add(self, *args, **kwargs):
        for value in args:
            self.total += value
            
        for value in kwargs.values():
            self.total += value
            
        return self.total
     
    def multiply(self, *args, **kwargs):
        for value in args:
            self.total *= value
            
        for value in kwargs.values():
            self.total *= value
            
        return self.total
    

calculator = Calculator()

result_1 = calculator.add()
print("Calling method without argument:",result_1)

result_2 = calculator.add(5,6,n_1=1, n_2=2, n_3=3)
print("Calling method without argument:",result_2)



