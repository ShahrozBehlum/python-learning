class Car: #Inheritance
    def __init__(self, brand, model): 
        self.brand = brand
        self.model = model

    def fullName(self):  
        return f"{self.brand} {self.model}"   

class ElectricCar(Car): 
    def __init__(self, brand, model, batterySize):
        super().__init__(brand, model)
        self.batterySize = batterySize

my_tesla = ElectricCar('Tesla', 'Model S', "85KWH")
print(my_tesla.brand)
print(my_tesla.model)
print(my_tesla.batterySize)
print(my_tesla.fullName())

# my_car = Car('Toyota', 'Corolla')     
# print(my_car.brand)
# print(my_car.model)
# print(my_car.fullName())
