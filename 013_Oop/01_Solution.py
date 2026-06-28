class Car:  #It is a general form/blueprint use it for every car
    def __init__(self, brand, model): #init is also called contructor
        self.brand = brand
        self.model = model

my_car = Car('Toyota', 'Corolla')     
print(my_car.brand)
print(my_car.model)

my_new_car = Car('Tata', 'Safari')
print(my_new_car.brand)
print(my_new_car.model)