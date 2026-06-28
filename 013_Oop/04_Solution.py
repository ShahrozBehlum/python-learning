class Car: #Encapsulation
    def __init__(self, brand, model):
        self.__brand = brand  #Now brand become private not access outside class only access by method 
        self.model = model

    def fullName(self):
        return f"{self.__brand} {self.model}"  

    def get_brand(self):
        return self.__brand + '!'  

my_car = Car('Toyota', 'Corolla')     
# print(my_car.brand) #give error b/c brand is private
print(my_car.get_brand())
