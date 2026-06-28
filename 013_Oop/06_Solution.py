class Car: #Class variable track total created cars

    total_car = 0

    def __init__(self, brand, model): 
        self.brand = brand
        self.model = model
        Car.total_car += 1

    def fullName(self):  
        return f"{self.brand} {self.model}"  

    def fuel_type(self):
        return 'Petrol / Diesel'
    
my_tesla = Car('Tesla', 'Model S')
safari = Car('Tata', 'Safari')
print(Car.total_car)