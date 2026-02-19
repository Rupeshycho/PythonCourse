try:
    name=str(input("Enter the name: ")).strip()
    if len(name)<3:
        print("Error!!! Name must be at least 3 characters ")
    
    elif len(name)>50:
        print("ERROR!! Name can be a maximum of 50 characters")
        if not name:
            raise ValueError("ERROR!!! Name cannot be empty")

    elif not name.replace(" ","").isalpha():
        raise ValueError("Name can only contain letters and spaces. ")
    else:
        print(f'Name Accepted: {name}')
except ValueError as ve:
    print(f'Error: {ve}')
    
 
    
