age=21
age+=5
print(f'The age after 5 years is: {age}')

h=2.57
h_cm=h*100
print(f'The height({h}m) in cm is: {int(h_cm)}')

name="  Rupesh Yadav  "
print(f'The length of name is: {len(name)}')
print(name.upper())
print(name.lower())
print(name.capitalize())
print(name.rstrip())
print(name.lstrip())


user_age=int(input("Enter your age:"))
if user_age >= 18 and user_age <= 60 :
    print(f"The result is stored and you are ready to vote.")
else:
    print(f"Error!!!\nAge must be greater than 18")
