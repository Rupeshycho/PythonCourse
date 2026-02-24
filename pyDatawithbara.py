scores =[80,50,60,75]
total=0
for score in scores: 
    total+= score
    print("Current total: ", total)
print("Final total: ", total)

files=['Report.csv', 'Data.csv', 'final.TXT']
for file in files: 
    file=file.strip().strip().lower().replace('.txt', '.csv')
    print(f"processing {file}")
    
for i in range(1,10):
    for j in range(7,77,7):
        print(f'7*{i} = {j}')
        i+=1
    print()
    break
#pass statement 
# for i in (1,2, 3):
#     if i ==2:
#         pass
#     print (i)

for i in (1,2,3):
    print(i)
else: 
    print('End ')

names=["rabin", " rupesh ", "Anju budi of rupesh "]
for name in names: 
    if name =='Anju budi of rupesh ': 
        pass 
        name=name.replace('Anju budi of rupesh ', 'Couple ')
    
    print(f'Name = : {name}')
    
    
emails=[
    'data@gmail.com;',
    'baraa@outlook.de',
    'DROP TABLE USERS;',
    'maria@gmail.com'
    ]

for email in emails: 
    if ';' in email: 
        print('SQL Injection: Hacker Attack')
        break 
    print(f' Processing Email: {email}')

#check for even number 
items =[1,3,4,7]
for i in items: 
    if i%2 =="0":
        print ("Even number found", i )
        break 
    
else: 
    print ("Loop is completed ")

    