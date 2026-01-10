this_list=["apple ","banana","cherry"]
print(this_list)

print(this_list[0]) #apple
print(this_list[1]) #banana
print(this_list[2]) #cherry

print(f'print last items:{ this_list[-1]}') #cherry

#Python list
#A list is a an ordered collection of items that is mutable (can be changed) and allows duplicate values

#USES
# store multiple in a single variable 
# keep items in order (indexing possible)
#perform operations like add, remove, search, sort
#Useful for shopping lists, student names, task lists, sensor data, ect

#syntax:
#list=[item1, item2, item3]

#Accessing list item-----
#Definition: Retrieve item from list using index
#To get specific data


#Change list Item-----
#Definition: Modify item at a specific index
#why use: Update values


#change task status, update price
fruits=["apple", "banana", "mango"]
fruits[1]= "orange"
print(fruits)

#Add List item----

#Methods:
#Definition: Add new items tolist
#append() -> add at end
#insert() -> add another list 
#extend() -> add another list


fruits.append("grape")
fruits.insert(1,"Kiwi")
fruits.extend(["pinapple", "watermelon"])
print (fruits)

#Real-world: Add new product to inventory, add new student

#Remove(value) -> by value
#pop(index) -> by index
#del list[index] 
name=input('Enter the number:' )
print(f'Welcome Mr. {name}\n I loved to work with you.')
print("---Calculator---")
a = int(input("Enter the first Number:"))
b = int(input("Enter the first Number:"))
print(f'Sum is: {a+b}')

messege=input()
print(message)