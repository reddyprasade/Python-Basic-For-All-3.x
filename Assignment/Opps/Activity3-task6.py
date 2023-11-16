class ElectricalAppliance:
    def __init__(self, name, power_consumption):
        self.name = name
        self.power_consumption = power_consumption

    def calculate_energy(self):
        return self.power_consumption * 24

fridge = ElectricalAppliance("fridge", 250)
tv = ElectricalAppliance("tv", 300)

fridge_energy = fridge.calculate_energy()
tv_energy = tv.calculate_energy()

print(f'Enery consumption: {fridge_energy+tv_energy}')
