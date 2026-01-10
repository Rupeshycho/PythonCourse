weight=int(input("Weight="))

unit=input("(L)bs: or (K)g:")

if unit.upper()=="L":
    weight=round(weight*0.5,3)
    print(f'You are {weight} kilos')
    
elif unit.upper()=="K":
    weight=round(weight/0.45,3)
    print(f"You are {weight} pounds")    
    
    