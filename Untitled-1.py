class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

class Car(Vehicle):
    def __init__(self, brand, model, doors):
        super().__init__(brand, model)
        self.doors = doors

    def description(self):
        return f"{self.brand} {self.model} with {self.doors} doors"

class SUV(Vehicle):
    def __init__(self, brand, model, capacity):
        super().__init__(brand, model)
        self.capacity = capacity

    def description(self):
        return f"{self.brand} {self.model} with {self.capacity} cubic feet capacity"

class Motorcycle(Vehicle):
    def __init__(self, brand, model, type_motorcycle):
        super().__init__(brand, model)
        self.type_motorcycle = type_motorcycle

    def description(self):
        return f"{self.brand} {self.model} which is a {self.type_motorcycle} motorcycle"

class Garage:
    def __init__(self):
        self.vehicles = []

    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)

    def get_vehicle_descriptions(self):
        descriptions = []
        for vehicle in self.vehicles:
            descriptions.append(vehicle.description())
        return descriptions

    def get_vehicle_brands(self):
        brands = []
        for vehicle in self.vehicles:
            brands.append(vehicle.brand)
        return brands

    def get_vehicle_dict(self):
        vehicle_dict = {}
        for vehicle in self.vehicles:
            vehicle_dict[vehicle.model] = vehicle.description()
        return vehicle_dict

    def get_vehicle_types(self):
        vehicle_types = {}
        for vehicle in self.vehicles:
            vehicle_types[vehicle.model] = type(vehicle).__name__
        return vehicle_types

    def get_vehicle_count(self):
        return len(self.vehicles)

# Robimy garage i dodajemu
garage = Garage()
garage.add_vehicle(Car("BMW", "320i", 4))
garage.add_vehicle(SUV("BMW", "X5", 33))
garage.add_vehicle(Motorcycle("BMW", "R1250GS", "adventure"))
garage.add_vehicle(Car("Mercedes", "C200", 4))
garage.add_vehicle(SUV("Mercedes", "GLC300", 36))
garage.add_vehicle(Motorcycle("Mercedes", "AMG Vision", "concept"))

# Praca z listo i slownikem
vehicle_list = garage.get_vehicle_descriptions()
print("Vehicle descriptions list:", vehicle_list)

vehicle_dict = garage.get_vehicle_dict()
print("Vehicle descriptions dictionary:", vehicle_dict)

vehicle_brands = garage.get_vehicle_brands()
print("Vehicle brands list:", vehicle_brands)

vehicle_types = garage.get_vehicle_types()
print("Vehicle types dictionary:", vehicle_types)

vehicle_count = garage.get_vehicle_count()
print("Total number of vehicles:", vehicle_count)

# Electro cary
class ElectricCar(Car):
    def __init__(self, brand, model, doors, battery_capacity):
        super().__init__(brand, model, doors)
        self.battery_capacity = battery_capacity

    def description(self):
        return f"{self.brand} {self.model} with {self.doors} doors and {self.battery_capacity} kWh battery"

garage.add_vehicle(ElectricCar("BMW", "i4", 4, 80))

class ElectricSUV(SUV):
    def __init__(self, brand, model, capacity, battery_capacity):
        super().__init__(brand, model, capacity)
        self.battery_capacity = battery_capacity

    def description(self):
        return f"{self.brand} {self.model} with {self.capacity} cubic feet capacity and {self.battery_capacity} kWh battery"

garage.add_vehicle(ElectricSUV("Mercedes", "EQC400", 50, 85))

# samochody ktore u mnie w domku
garage.add_vehicle(Car("BMW", "M3", 4))
garage.add_vehicle(SUV("BMW", "X3", 28))
garage.add_vehicle(Motorcycle("BMW", "S1000RR", "sport"))
garage.add_vehicle(Car("Mercedes", "E300", 4))
garage.add_vehicle(SUV("Mercedes", "GLE450", 38))
garage.add_vehicle(Motorcycle("Mercedes", "Silver Arrow", "concept"))

# funkcje
def list_vehicles(garage):
    return garage.get_vehicle_brands()

def dict_vehicles(garage):
    return garage.get_vehicle_dict()

def count_vehicles(garage):
    return garage.get_vehicle_count()

vehicle_list_full = list_vehicles(garage)
vehicle_dict_full = dict_vehicles(garage)
vehicle_count_full = count_vehicles(garage)

print("Full vehicle brands list:", vehicle_list_full)
print("Full vehicle descriptions dictionary:", vehicle_dict_full)
print("Total number of vehicles in garage now:", vehicle_count_full)

# add opis bez printu
class LuxuryCar(Car):
    def __init__(self, brand, model, doors, luxury_features):
        super().__init__(brand, model, doors)
        self.luxury_features = luxury_features

    def description(self):
        return f"{self.brand} {self.model} with {self.doors} doors and luxury features like {self.luxury_features}"

garage.add_vehicle(LuxuryCar("BMW", "7 Series", 4, "leather seats, panoramic sunroof"))

class LuxurySUV(SUV):
    def __init__(self, brand, model, capacity, luxury_features):
        super().__init__(brand, model, capacity)
        self.luxury_features = luxury_features

    def description(self):
        return f"{self.brand} {self.model} with {self.capacity} cubic feet capacity and luxury features like {self.luxury_features}"

garage.add_vehicle(LuxurySUV("Mercedes", "GLS", 56, "leather seats, ambient lighting"))

# add function
def get_electric_vehicles(garage):
    electric_vehicles = []
    for vehicle in garage.vehicles:
        if isinstance(vehicle, (ElectricCar, ElectricSUV)):
            electric_vehicles.append(vehicle.description())
    return electric_vehicles

def get_luxury_vehicles(garage):
    luxury_vehicles = []
    for vehicle in garage.vehicles:
        if isinstance(vehicle, (LuxuryCar, LuxurySUV)):
            luxury_vehicles.append(vehicle.description())
    return luxury_vehicles

electric_vehicles = get_electric_vehicles(garage)
print("Electric vehicles list:", electric_vehicles)

luxury_vehicles = get_luxury_vehicles(garage)
print("Luxury vehicles list:", luxury_vehicles)

# BMW TOP )
for i in range(1, 4):
    print(f"BMW TOP")

# dop klasy i metody bo juz nwm co pisac
class SportsCar(Car):
    def __init__(self, brand, model, doors, top_speed):
        super().__init__(brand, model, doors)
        self.top_speed = top_speed

    def description(self):
        return f"{self.brand} {self.model} with {self.doors} doors and top speed of {self.top_speed} mph"

garage.add_vehicle(SportsCar("BMW", "M4", 2, 155))

class ClassicCar(Car):
    def __init__(self, brand, model, doors, year):
        super().__init__(brand, model, doors)
        self.year = year

    def description(self):
        return f"{self.brand} {self.model} with {self.doors} doors from year {self.year}"

garage.add_vehicle(ClassicCar("Mercedes", "300SL", 2, 1955))

class OffroadSUV(SUV):
    def __init__(self, brand, model, capacity, offroad_capability):
        super().__init__(brand, model, capacity)
        self.offroad_capability = offroad_capability

    def description(self):
        return f"{self.brand} {self.model} with {self.capacity} cubic feet capacity and offroad capability: {self.offroad_capability}"

garage.add_vehicle(OffroadSUV("BMW", "X6", 35, "high"))

# help metode
def get_sports_cars(garage):
    sports_cars = []
    for vehicle in garage.vehicles:
        if isinstance(vehicle, SportsCar):
            sports_cars.append(vehicle.description())
    return sports_cars

def get_classic_cars(garage):
    classic_cars = []
    for vehicle in garage.vehicles:
        if isinstance(vehicle, ClassicCar):
            classic_cars.append(vehicle.description())
    return classic_cars

sports_cars = get_sports_cars(garage)
print("Sports cars list:", sports_cars)

classic_cars = get_classic_cars(garage)
print("Classic cars list:", classic_cars)

print("I LIKE BMW MORE !!!!!!")