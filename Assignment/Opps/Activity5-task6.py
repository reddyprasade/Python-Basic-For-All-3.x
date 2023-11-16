class Car:
    def __init__(self,c_name,c_brand,c_color,c_model,c_price):
        self.name = c_name
        self.brand = c_brand
        self.color= c_color
        self.model= c_model
        self.price= c_price
        
    def display_info(self):
        print("Car name:",self.name)
        print("Car brand:",self.brand)
        print("Car color:",self.color)
        print("Car model:",self.model)
        print("Car price:",self.price)
        print("------------------")

class Eon(Car):
    def __init__(self,c_name,c_brand,c_color,c_model,c_price,c_owner):
        self.name = c_name
        self.brand = c_brand
        self.color= c_color
        self.model= c_model
        self.price= c_price
        self.owner =c_owner
        
    def display_owner(self):
        print(f"Owner: {self.owner}")
        print("------------------")

class Santro(Car):
    def display_info(self):
        print("Car name:",self.name)
        print("Car brand:",self.brand)      		

eon = Eon("Eon","Hundai","Red",2011,500000,"Karma")
eon.display_info()

santro=Santro("Santro","Hundai","Red",2011,500000)
eon.display_owner()
santro.display_info()







