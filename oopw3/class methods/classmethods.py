# Methods are functions that belongs to a class. 
# They define the behavior of objects created from the class

class Person: 
    def __init__(self, name, age): 
        self.name = name 
        self.age = age
    def greet(self): 
        print("Hello, my name is ", self.name)
p1= Person("Rupesh", 23)
p1.greet()

class Calculator: 
    def add(self, a, b): 
        return a +b
    
    def multiply(self, a, b): 
        return a * b
calc = Calculator()
print(calc.add(5,10))
print(calc.multiply(4,7))

class Person: 
    def __init__(self, name ,age):
        self.name = name 
        self.age = age 
    def get_info(self):
        return f'Mr. {self.name} is {self.age} Years old'
    
p1 = Person("Rupesh", 23)
print(p1.get_info())


class Human: 
    def __init__(self, name, age): 
        self.name = name 
        self.age = age 
    def celeberate_birthday(self): 
        self.age += 1
        print(f'Happy Birthday {self.name}! You are now {self.age} years old.')
h1 = Human("Rupesh", 23)
h1.celeberate_birthday()
h1.celeberate_birthday()

#__Str__() method is a speacial method that controls what is returned when the object is printed. 
#It is used to provide a human-readable string representation of the object and is often used for  debugging and logging purposes. 

class Homo: 
    def __init__(self, name, age): 
        self.name = name 
        self.age = age 

    def __str__(self): 
        return f'{self.name} ({self.age})'
h11 = Homo("Samir", 19)
print(h11)

class Romo: 
  def __init__(self, name, age): 
    self.name = name 
    self.age = age 
h1 = Romo("Samir", 19) 
print(h1) 


class Personn: 
    def __init__(self, name, age): 
        self.name = name 
        self.age = age 
p11= Personn("Tobias", 36)
print(p11)