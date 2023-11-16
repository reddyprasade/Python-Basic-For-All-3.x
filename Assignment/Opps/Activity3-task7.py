class ElectricalAppliance:

    def __init__(self, name, power_consumption):
        self.name = name
        self.power_consumption = power_consumption

    def calculate_energy(self,hours_used):
        return self.power_consumption * hours_used

hours=int(input("Enter the duration in hours:"))
fridge = ElectricalAppliance("fridge", 250)
tv = ElectricalAppliance("tv", 300)

fridge_energy = fridge.calculate_energy(hours)
tv_energy = tv.calculate_energy(hours)

print(f'Enery consumption: {fridge_energy+tv_energy}')
