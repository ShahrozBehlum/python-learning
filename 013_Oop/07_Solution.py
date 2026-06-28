class Car: 

    def __init__(self, brand, model): 
        self.brand = brand
        self.model = model

    def fullName(self):  
        return f"{self.brand} {self.model}"  

    def fuel_type(self):
        return 'Petrol / Diesel'

    @staticmethod  #decorators
    def general_description():
        return 'Cars are means of transport'
    
my_tesla = Car('Tesla', 'Model S')
safari = Car('Tata', 'Safari')
print(Car.general_description())
