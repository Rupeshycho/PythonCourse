for i in range(1,5):
    print(i*'2')

for item in 'python':
    print(item)
    
    
for item in ['RupeshAnju', 'John', 'sarah']:
    print(item)   
for num in [1,2,3,4]:
    print(num)

for number in {1,2,3,4,5,5}:
    print(number)

for num in range(10):
    print(num)

#print odd number
print("--Even number--")
num=(int(input("Enter the last number:")))
for i in range(2,num+1,2):
    print(i)
    
print("--odd number--")
for i in range(1,num+1,2):
    print(i)    

#Calculate total price in a list
prices=[10,20,30]
print(f"Given prices={prices}")
total =0
for item in prices:
    total +=item
print(f'Total: {total}')          