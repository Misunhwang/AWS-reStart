from .Car import Car

class ElectricCar(Car):
    def __init__(self, brand, milage_km, range):
        super().__init__(brand, milage_km)
        self.range = range

    def drive(self, distance_km):
        super().drive(distance_km)
        self.range -= distance_km