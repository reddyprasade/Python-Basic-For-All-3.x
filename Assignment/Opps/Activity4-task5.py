class Calculator:
    def __init__(self):
        self.total = 0
    
    def add(self,arg_1,arg_2, *args, **kwargs):
        for value in args:
            self.total += value
            
        for value in kwargs.values():
            self.total += value
            
        return self.total+arg_1+arg_2

    def multiply(self,arg_1,arg_2, *args, **kwargs):
        for value in args:
            self.total *= value
            
        for value in kwargs.values():
            self.total *= value
            
        return self.total+arg_1+arg_2

calculator = Calculator()
result = calculator.add(5,6,n_1=1, n_2=2, n_3=3)
print(result)
