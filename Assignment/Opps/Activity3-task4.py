class Triangle:
    def __init__(self,side_1,lside_2,side_3):
        self.side1=side_1
        self.side2=side_1
        self.side3=side_1
        
    def cal_perimeter(self):
        return self.side1+self.side2+self.side3
    
triangle = Triangle(5,6,8)
print(f"Perimeter: {triangle.cal_perimeter()}")
