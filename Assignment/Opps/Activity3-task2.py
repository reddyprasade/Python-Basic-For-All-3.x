class Dzong:
    def __init__(self,name,location,built):
        self.name=name
        self.location=location
        self.built=built
    def display_history(self):
        print(f"Name: {self.name}")
        print(f"Location: {self.location}")
        print(f"Year: {self.built}")
        
dzong=Dzong("Punakha","Bhutan",1637)
dzong.display_history()
dzong_1=Dzong("Simtokha","Bhutan",1629)
dzong_1.display_history()



