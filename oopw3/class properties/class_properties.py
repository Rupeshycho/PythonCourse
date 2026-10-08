class Person: 
    def __init__(self, name, age):
        self.name = name 
        self.age = age
p1 = Person("Rupesh", 36)
print("The name is: ",p1.name)
print("His age is: ", p1.age)

class Car: 
    def __init__(self, brand, model):
        self.brand = brand 
        self.model = model

car1 = Car("Toyota", "Corolla")
print(car1.brand)
print(car1.model)

print("Tobias".center(20, "-"))
p1 = Person("Tobias", 25)
print(p1.age)

p1.age = 26
print("Modified: ",p1.age)

# del p1.age
print(p1.age)

#Properties are variables taht belong to the class. They store data for each object created from the class. 
#You can access object propertiess by using dot notation. 

#You can modify the value of properties on object. 
# delete properties using del keyword
#Class properties vs Object properties:

    #Properties defined inside __Init_() belong to each object(Instance Properties). 
    #Propertiess defined outside __init__() belong to the class(Class Properties).

class person: 
    species = "Human"

    def __init__(self, name, age):
        self.name = name 
        self.age = age
    
p1 = person("Rupesh",5)
p2 = person("Tobias", 45)

print(p1.species)
print(p2.species)

print("The name is: ",p1.name)
print("Person 2 name is: ",p2.name)

#Modifying class Properties: 
class Yadavas: 
    lastname = ""
    def __init__(self, name): 
        self.name = name 
y1 = Yadavas("Rupesh")
y2 = Yadavas("Anju")

Yadavas.lastname  = "Yadaw"
print(y1.lastname)
print(y2.lastname)

#Add new properties : Add new properties to existing objects: 

class Human: 
    def __init__(self, name): 
        self.name= name 
h1 = Human("Rupesh")

h1.age = 25 
h1.city = "Rajbiraj"

print("This name is from the object: ",h1.name)
print("This age is from the modified:  ",h1.age)
print("This is the modified city:  ",h1.city)