from classes import IceCar, ElectricCar

def main():
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

if __name__ == "__main__":
    main()    