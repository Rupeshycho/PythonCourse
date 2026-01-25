def greet_user():
    
    name=input("What's your name?\n")
    
    print(f'Hey there, {name}.')
    age=input("What's your age?\n")
    print(f'so you are {int(age)} years old.')
    return name
print(">>>Interview>>>")    
name=greet_user()   
print(f'Thank you Mr.{name}.\n')

#parameters
def greeting(name):
    print("Hi there!")
    print("Welcome aboard")

print(">>>Start>>>")    
greeting("John")    
print("Finish!")