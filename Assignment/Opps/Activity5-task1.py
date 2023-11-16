class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self, sound):
        print(f"{self.name} makes a {sound} sound.")

dog = Animal("Fido", "Golden Retriever")
dog.make_sound("bark")
