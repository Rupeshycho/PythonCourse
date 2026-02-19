name=input("Enter your name: ")

print(f'Enter your age Mr.{name}')
age=int(input("Whats your age?"))

           
if age>=18:
        if age<60:
            print("Congrats!!!\nYou are able to work as Government Employee")
else:
    print("You should be at least 18 years old.")  
    
is_hot=False
is_cold=True
if is_hot:
    print("It's a hot day.")
    print('Drink plenty of water to make yourself hydrate')
elif is_cold:       
    print("It's a cold day")
    print("Wear warm clothers")    
else:
    print("It's a lovely day")
    
print("Enjoy your day.  ")