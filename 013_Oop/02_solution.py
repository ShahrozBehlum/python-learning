class Car: 
    def __init__(self, brand, model): #constructor that access attributes
        self.brand = brand
        self.model = model

    def fullName(self):  #method
        return f"{self.brand} {self.model}"    

my_car = Car('Toyota', 'Corolla')     
print(my_car.brand)
print(my_car.model)
print(my_car.fullName())

my_new_car = Car('Tata', 'Safari')
print(my_new_car.brand)
print(my_new_car.model)