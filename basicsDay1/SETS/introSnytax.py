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

#Frozenset
#Def:  Immutable set, cannnot add/remove items
#Why use: Store fixed unique elements

# fs= frozenset([1,2,3])
# print(fs)
# fs.add(4)
# print(fs)
#Real-world: Store unchangeable configuratoin values

#Method of list

##1add(): add single item to the set
#why use: To insert a new unique element 


s={1,2,3,4}
s.remove(2)
print(s)


#use Case: remove sold  product, remove old data

##discard()
#Definition: Remove specific item; no error if item  not present
#why use: Safer than remove

s={1,2,3}
s.discard(3)
print(s)

# # pop()
# # Definition: Remove random item from set and return it
# # Why use: Remove element when order doesn’t matter

# s = {1, 2, 3}
# item = s.pop()
# print("Removed:", item)
# print("Set now:", s)

# # Removed: 1
# # Set now: {2, 3}
# # Use case: Remove arbitrary task, random selection

# # clear()
# # Definition: Remove all items from set
# # Why use: Empty the set
# s = {1, 2, 3}
# s.clear()
# print(s)

# # set()
# # Use case: Reset student list, clear dataset

# # union()
# # Definition: Combine two sets; all unique items
# # Why use: Merge sets without duplicates

# a = {1, 2, 3}
# b = {3, 4, 5}
# c = a.union(b)
# print(c)

# # {1, 2, 3, 4, 5}
# # Use case: Merge two class lists, combine datasets

# # update()
# # Definition: Add items from another set into current set
# # Why use: Modify original set with new items

# a = {1, 2, 3}
# b = {4, 5}
# a.update(b)
# print(a)

# # {1, 2, 3, 4, 5}
# # Use case: Add new students to existing set

# # intersection()
# # Definition: Return common items in two sets
# # Why use: Find items present in both sets

# a = {1, 2, 3}
# b = {2, 3, 4}
# print(a.intersection(b))

# # {2, 3}
# # Use case: Find students in both class A and B, common products

# # difference()
# # Definition: Return items in first set but not in second
# # Why use: Find unique items in one set

# a = {1, 2, 3}
# b = {2, 3, 4}
# print(a.difference(b))

# # {1}
# # Use case: Students only in class A, products only in warehouse A

# # symmetric_difference()
# # Definition: Return items in either set but not both
# # Why use: Find items that are unique to each set

# a = {1, 2, 3}
# b = {2, 3, 4}
# print(a.symmetric_difference(b))

# # {1, 4}
# # Use case: Items only in A or B, but not in both


  
# s = 1
# while s <6:
#     s+=1
#     if s ==3:
#         continue
#     print(s)
    
      
      
# for i in range (1,11):
#     for s in range (1,11):
#         print({i *s})
        
    
    




# for i in range (1,11):
#     print(f'\nTable of {i}')  
#     for s in range(1,11):
#         print (f'{i} * {s} = {i*s}')


no = [1,2,4,4,5,6,6,7,]



for i in no:
    print (i)