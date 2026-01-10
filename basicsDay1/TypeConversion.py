print("TYPE CONVERSION:")

birth_year=int(input('Birth year: '))  
print(type(birth_year))

age=2026-birth_year
print(f'You are {age} years old.')

print(type(age))


weight=float(input("Enter your weight in pounds: "))
weight_km=weight*0.45
print(f'The weight in KG is: {weight_km}')
