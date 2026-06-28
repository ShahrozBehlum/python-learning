class Car: #Polimorphism
    def __init__(self, brand, model): 
        self.brand = brand
        self.model = model

    def fullName(self):  
        return f"{self.brand} {self.model}"  

    def fuel_type(self):
        return 'Petrol / Diesel'

class ElectricCar(Car): 
    def __init__(self, brand, model, batterySize):
        super().__init__(brand, model)
        self.batterySize = batterySize

    def fuel_type(self):
        return 'Electric Charge'    

my_tesla = ElectricCar('Tesla', 'Model S', "85KWH")
print(my_tesla.fuel_type())

safari = Car('Tata', 'Safari')
print(safari.fuel_type())


