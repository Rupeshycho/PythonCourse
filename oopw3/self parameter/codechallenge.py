class Car: 
    def __init__(self, brand): 
        self.brand = brand 
    def show(self):
        print(f'The brand is: {self.brand}')
c1 = Car(f"Ford")
c1.show()



#The self parameter is a reference to the current instance of the class. 

# It is used to access properties and methods  that belongs to the class. 

# The self parameter must be the first parameter of any method in the class 

# without self, python would not know which object's properties we want to access. 

# We can access multiple properties using self: 

# we can also call other methods within the class using self.

# call one method from another method using self. 