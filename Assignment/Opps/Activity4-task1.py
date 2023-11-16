class Area:
    def compute_area(self, shapes,x = None, y = None):
        if shapes == "triangle" and x != None and y != None:
            print("Area of Triangle:",0.5 * x * y)
        elif shapes == "rectangle" and x != None and y != None:
            print("Area of Rectangle:",x * y)
        elif shapes == "square" and x != None:
            print("Area of Square:",x * x)
        else:
            print("Invalid input.") 

area = Area()
area.compute_area("rectangle",5,10)
area.compute_area("square",5)


