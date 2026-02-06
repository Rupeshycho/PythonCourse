# class Dog: 
#     def walk(self):
#         print("Walking Dog ")
        

# class Cat:
#     def walk(self):
#         print("Walk")        


class Mammal:
    def walk(self):
        print("Walking")
        
class Dog(Mammal):
    def bark(self):
        print("Dog is barking ")
          
class Cat(Mammal):
    def be_annoying(self):
        print("Cat is annoying compared to dogs ✨🤣")        

Dog1=Dog()
Dog1.walk()
Dog1.bark()

cat1=Cat()
cat1.walk()
cat1.be_annoying()
        