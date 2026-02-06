class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        
    def move(self):
        print("Move ")
    def draw(self):
        print("draw")
        
point1=Point(20,30)  
point1.x=10
point1.y=20
print(point1.x,point1.y)   
point1.draw()
point2=Point(50,60)
point2.x=100
print(point2.x)
point2.move()

point=Point("1stArgument: x ","2ndArgument: y")
point.x="Update Argument x "
print("Constructor Called.\n",point.x, point.y)

class Person: #Pascalconvention
    def __init__(self,name):  #constructor
        self.name=name
    def talk(self):
        print(f"Hi, we are the lovely couple <<<{self.name}>>> gonna married soon!.")
        
    def dance(self):
        print(f'Hi, I am {self.name}. I dance very smoooth like a MJ')    
        
rupesh=Person("RupeshAnju Yadav")

rupesh.talk()

bob=Person("Bob smith")
bob.dance()

        