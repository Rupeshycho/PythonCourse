#create student class 
class Student: 
    def __init__(self, name, grade):
        self.name = name 
        self.grade = grade 
    

#create an object 
s1 = Student("Rupesh Yadav", "A+")

#print the grade 
print("The Final Grade: ",s1.grade)


#Change the grade 
s1.grade = "A"

#print the updated grade 
print("It was written mistakenly: ",s1.grade)
