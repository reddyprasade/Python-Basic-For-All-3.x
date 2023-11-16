class ElectricalAppliance:
    def __init__(self, name, power_consumption):
        self.name = name
        self.power_consumption = power_consumption

    def calculate_energy(self, hours_used):
        return self.power_consumption * hours_used

class Fridge(ElectricalAppliance):
    def __init__(self, name, power_consumption, volume):
        super().__init__(name, power_consumption)
        self.volume = volume

class TV(ElectricalAppliance):
    def __init__(self, name, power_consumption, screen_size):
        super().__init__(name, power_consumption)
        self.screen_size = screen_size

fridge = Fridge("fridge", 0.5, 200)
tv = TV("tv", 0.1, 42)

fridge_energy = fridge.calculate_energy(24)
tv_energy = tv.calculate_energy(4)

print("Energy used by fridge:", fridge_energy)
print("Energy used by TV:", tv_energy)
