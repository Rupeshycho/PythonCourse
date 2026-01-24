numbs =[5,2,1,7,4]
numbs.sort()
print(f'Acending order: {numbs}')

numbers=[5,2,1,7,4]
print('numbers=',numbers)
numbers.insert(0, 10)
print(".insert(0,10): ",numbers)

numbers.remove(7)
print("7 removed",numbers)

numbers=[5,2,1,5,7,4]
print(50 in numbers) #Boolean Value: True or False
print(5 in numbers) #True

print(f"Number'5' is {numbers.count(5)} times")

#Descending Orders 
numbers.sort()
numbers.reverse()
print(numbers)

numbers=[5,2,1,5,7,4]
numbers2=numbers.copy()
numbers.append(10)

print("numbers will be same no changes with append:\n",numbers2)

# WAP to remove the duplicates in a list.
