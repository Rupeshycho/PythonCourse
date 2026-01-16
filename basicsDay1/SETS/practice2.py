# Python Sets  
# # Definition:
# # A set is an unordered collection of unique items.
# # Duplicate values are not allowed.

# # Why use / Reason:
# # Store unique items
# # Perform operations like union, intersection
# # Fast membership test
# # Useful for unique IDs, unique elements in a list, removing duplicates

# # Syntax:
# # my_set = {item1, item2, item3}

# # Access Set Item-------------
# # Definition: Sets are unordered, so indexing is not possible
#NO INDEXING in sets 

fruits={"apple", "banana", "mango"}
print("apple" in fruits) #True
print("grape"  in fruits)  #False

##Real-world: check if student ID exists in registered list
##Add set Item-----

#Defintion: Add single item using add()
##add(): insert new unique element

fruits={'apple', "banana", 'mango'}
fruits.add("mango")
print(fruits) 

##Real-world: Add new unique product ID

##Remove Set Item 
#Defintion: Remove item using: 
#remove(value) -> throws error if not exist 
#discard(value)-> no error if not exist
#why use: Delete specific item 

fruits={"apple","banana","mango"}

#fruits.remove('bnana') #throw error cause 'bnana' doesn't exist
fruits.remove('banana') #
print(fruits)

##{'apple','banana','mango'}
fruits={"apple","banana","mango",'pineapple','pineapple'}
print(fruits)   #no pineapple coz: duplication is not allowed 

fruits.discard('cherry') #no error if not exists
print(fruits)

fruits.discard('mango') #remove mango  but if cherry passed instead of mango there will be no error in discard("value")
print(fruits)

#Real-world: Print all registered students, all product IDS

##join sets: combine 2 sets
#Methods:  
#union()  -> all unique elements
#update() -> add  items from another set
a={1,2,8,9}
b={3,4,5,6}
c=a.union(b)
print(c)


a.update(b)   
print(a)
#Real world: merger two class student lists, merge two datesets 


#frozenset: Immutable set, cannot add/remove items
#Store fixed unique elements

fs=frozenset([1,2,3])
# print(fs)
# fs.add(3) #error: cannot add/remove items 

# print(fs)

#methods of list 
# add: add single item to the set
#uses to insert a new unique element

s={1,2,3,4}
s.remove(2)
print(s)

#use case: remove sold  product, remove old data

#discard(): remove specific item; no error it item not present 
#why use: safer than remove

s={1,2,3}
s.discard(3) #discard doesnot show error if not exists
print(s)

#pop()
s={1,2,3,4}
item=s.pop()
print("removed: pop():", item )
print("Set now:",s)
#use case : Remove arbitrary task, random selection 

#clear(): remove all items from set #use in empty set 
s={1,2,3}
s.clear() #cant put value inside clear 
print(s)

#union(): combine two sets: all unique items 
#Merge sets witout duplicate 
a = {1, 2, 3}
b = {3, 4, 5}
c = a.union(b)
print(c)


a = {1, 2, 3}
b = {4, 5}
a.update(b)
print("Update b:",a)

# intersection()
# Definition: Return common items in two sets
# Why use: Find items present in both sets

a = {1, 2, 3}
b = {2, 3, 4}
print(f'intersection: {a.intersection(b)}')

print(f'Union: {a.union(b)}')

#{2,3}
#Use case: Find students in both class A and B, common products 

#difference()
#Difinition: Return items in first set but not in second
#Why use: Find unique items in one set 

#{1,2,3}
#Use case: Students only in class A, products only in warehouse A

a={1,2,3,4,5,6}
b={4,5,6,7}
print(f'Difference: {a.difference(b)}')

#symmetric_difference()
#Definition: Return items in either set but not both 
#Find items that are unique to each set 
a={1,2,3,4,5,6}
b={4,5,6,7}
print(f'symmetric_difference: {a.symmetric_difference(b)}')

# Use case : items only in A or b , but not in both 

s=1
while s< 6: 
    s+=1
    if s ==3:
        continue
    print(s)
    
    
for i in range(1,6):
    print(f'\nTable of {i}')
    for s in range(1,11): #multiples upto 10 
        print(f'{i}*{s}={i*s}')
        
        

# Print table headers
print("Horizontal Table")
for i in range(1, 11):
    print(f"Table {i}".ljust(12), end="")
print()  # new line

# Print table values row by row
for s in range(1, 11):
    for i in range(1, 11):
        print(f"{i}×{s}={i*s}".ljust(12), end="")
    print()  # move to next row

set={1,2,3,4,4,4,5,6,6,7}
print(f'Set={set}')
for i in set: 
    print(i,end=" ")
print(" \n")
list_items={1,2,3,4,4,5,6,6,7}
print(f'List items= {list_items}')
for i in list_items:
    print(i, end=" ")