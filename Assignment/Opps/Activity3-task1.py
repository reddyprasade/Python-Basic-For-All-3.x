class Dzong:
    def __init__(self):
        self.name="Punakha"
        self.location="Bhutan"
        self.year=1637

    def display_history(self):
        print(f"Name: {self.name}")
        print(f"Location: {self.location}")
        print(f"Year: {self.year}")

dzong_1=Dzong()
dzong_1.display_history()

dzong_2=Dzong()
dzong_2.display_history()


