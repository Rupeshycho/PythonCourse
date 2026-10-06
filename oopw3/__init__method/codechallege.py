class Person:
    def __init__(self, name, age =18):
        self.name = name
        self.age = age
p1 = Person("Rupesh")
print(f'The age is  printed as: {p1.age}')
print(f'The name is printed as: {p1.name}')

class Dog: 
    def __init__(self,  name, age): 
        self.name = name
        self.age = age
    def bark(self): 
        print("Says Woof!")
d1 = Dog("Buddy", 3)
d1.bark()