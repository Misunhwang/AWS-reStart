# Week2 Homework5
class Car:
    def __init__(self, brand, milage_km):
        self.brand = brand
        self.milage_km = milage_km

    def drive(self, distance_km):
        self.milage_km += distance_km

class ElectricCar(Car):
    def __init__(self, brand, milage_km, range):
        super().__init__(brand, milage_km)
        self.range = range

    def drive(self, distance_km):
        super().drive(distance_km)
        self.range -= distance_km

class IceCar(Car):
    def __init__(self, brand, milage_km, fuel_consumption, fuel_level):
        Car.__init__(self, brand, milage_km)
        self.fuel_consumption = fuel_consumption
        self.fuel_level = fuel_level

    def drive(self, distance_km):
        super().drive(distance_km)
        self.fuel_level -= distance_km * self.fuel_consumption/100

print("---- Electric Car ----")
my_car = ElectricCar("Toyota", 40000, 10000)
print(my_car.__dict__) 
my_car.drive(50)
print(my_car.__dict__) 
my_car.drive(30)
print(my_car.__dict__) 
my_car.drive(20)
print(my_car.__dict__) 

print("\n---- Ice Car ----")
my_ice = IceCar("Ractis", 20000, 100, 800)
print(my_ice.__dict__) 
my_ice.drive(50)
print(my_ice.__dict__) 
my_ice.drive(30)
print(my_ice.__dict__) 
my_ice.drive(20)
print(my_ice.__dict__) 

"""
<Expected results>

---- Electric Car ----
{'brand': 'Toyota', 'milage_km': 40000, 'range': 10000}
{'brand': 'Toyota', 'milage_km': 40050, 'range': 9950}
{'brand': 'Toyota', 'milage_km': 40080, 'range': 9920}
{'brand': 'Toyota', 'milage_km': 40100, 'range': 9900}

---- Ice Car ----
{'brand': 'Ractis', 'milage_km': 20000, 'fuel_consumption': 100, 'fuel_level': 800}
{'brand': 'Ractis', 'milage_km': 20050, 'fuel_consumption': 100, 'fuel_level': 750.0}
{'brand': 'Ractis', 'milage_km': 20080, 'fuel_consumption': 100, 'fuel_level': 720.0}
{'brand': 'Ractis', 'milage_km': 20100, 'fuel_consumption': 100, 'fuel_level': 700.0}
"""