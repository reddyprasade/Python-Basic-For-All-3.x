class Dzong:
    name="Punakha Dzong" #Initialization of class attributes
    location="Punakha"   #Initialization of class attributes
    year_built=1631      #Initialization of class attributes
	
    def display_history(self): #Method
        print(f"Name: {self.name}")
        print(f"Location: {self.location}")
        print(f"Year:{self.year_built}")
        
dzong=Dzong() #Creation of objects
dzong.display_history() #calling method


