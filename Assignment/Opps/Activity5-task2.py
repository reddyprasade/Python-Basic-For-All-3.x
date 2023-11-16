class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self, sound):
        print(f"{self.name} makes a {sound} sound.")

    def fetch(self, thing):
        print(f"{self.name} fetches the {thing}.")
    
    def guard(self, thing):
        print(f"{self.name} guards the {thing}.")

dog = Animal("Fido", "Golden Retriever")
dog.fetch("ball")
dog.guard("house")
dog.make_sound("bark")
