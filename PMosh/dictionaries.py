#dictionaries: key: value pair 
# Name:JOhn smith 
# phone : 1234
# email: John@abc.com

customer={
    "name": "Rupesh Yadav",
    
    "age": 23,
    "is_verified": True,
}
for i,(key,value) in enumerate (customer.items()):
    print(i,(key,value))
    
print(customer.get("birthday"))    
print(customer.get("birthdate","Jan 1 1990")) #Jan 1 1990

customer={
    "name": "Rupesh Yadav",
    
    "age": 23,
    "is_verified": True,
}

customer["name"]="Jack Smith"
print(f'New  name: {customer["name"]}')

#DIgits into Words
phone=input("phone: ")
digits_mapping={
    "1":"one",
    "2": "Two",
    "3":"Three",
    "4":"Four"
}
output=""
for ch in phone:
    output+=digits_mapping.get(ch, "!")+" "
print(output)    
    






ph=(input("Phone: "))
phone={
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four" 
}
for digit in ph:
    print(phone.get(digit), end=" ") #horizontal same line 
print()
for digit in ph:
    print(phone.get(digit), end="\n") #new line (default)
        
    