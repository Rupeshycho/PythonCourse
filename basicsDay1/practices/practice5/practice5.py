#Logical Operators 
has_good_credit=True
has_criminal_record=True

if has_good_credit and not has_criminal_record:
    print("Eligible for loan")
    

#comparisonal operator
temp=int(input("Enter the temperature?"))

if temp>=30:
    print("Hot day")
if temp<30:
    print("its cold")