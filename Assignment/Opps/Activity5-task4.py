class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self, sound):
        print(f"{self.name} makes a {sound} sound.")

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, species="Dog")
        self.breed = breed

    def fetch(self, thing):
        print(f"{self.name} fetches the {thing}.")
    
    def guard(self, thing):
        print(f"{self.name} guards the {thing}.")
        
class Cat(Animal):
    def climb(self, thing):
        print(f"{self.name} climbs {thing}.")

dog = Dog("Fido", "Golden Retriever")
dog.fetch("ball")
dog.guard("house")
dog.make_sound("bark")
print("-----------------------")
cat=Cat("Caty","Cat")
cat.climb("Tree")



