class Person: 
    def __init__(self, name, age =18):
        self.name = name
        self.age = age

    def greet(self): 
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")
p1 = Person("Rupesh")
p1.greet()

class Person: 
    def __init__(self, name, age =18):
        self.name = name
        self.age = age

    def greet(self): 
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")  
p1 = Person("Rupesh")
p1.greet()


class Car: 
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def display_info(self): 
        print(f'{self.year} {self.brand} {self.model}')
car1 = Car("Toyota", "Corolla", 2020)
car2 = Car("Mercedes", "benz", 2021)
car3 = Car("Toyota", "supra", 2022)
car1.display_info()
car2.display_info()
car3.display_info()
