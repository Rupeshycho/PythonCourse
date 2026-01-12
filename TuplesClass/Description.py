# Sequance dataType
# -In python  list, tuple, range are sequence types  

# -Sequence Type –
# A Sequence Type refers to an ordered collection of items.
# The items are stored in a specific order.
# Each item can be accessed using its index position.
# -Duplicate values allowed (list, tuple)




# Definition
# A tuple is an ordered collection of items that is immutable (cannot be changed) and allows duplicate values.
# Why use / Reason:
# Store multiple values together
# Keep data safe from accidental modification
# Faster than list for fixed data
# Useful for coordinates, days of the week, fixed info

# Syntax:
# my_tuple = (item1, item2, item3)

# Access Tuple------------
# 	Definition: Retrieve item from tuple using index
# 	Why use: To get specific data

days = ("Sun", "Mon", "Tue", "Wed") 
print("index of days at 0",days[0]) # Sun print(days[-1]) # Wed 
# Real-world: Get first day of week, last month of quarter

# Update Tuple
	# Definition: Tuples are immutable, cannot change individual items directly
	# Why use: If need to modify → convert tuple to list, update, then back to tuple

fruits = ("apple", "banana", "mango") 
fruits_list = list(fruits)
print(fruits_list)

fruits_list[1] = "orange" 
fruits = tuple(fruits_list) 
print("New orange doing list[1]='orange' added:",fruits) 

('apple', 'orange', 'mango')
# Real-world: Store fixed info safely, e.g., coordinates → rarely change

# Unpack Tuple
# Definition: Assign tuple items to separate variables
# Why use: Easily use each element

point = (10, 20, 30) 
x, y, z = point 
print(x, y, z) 

# 10 20 30
# Real-world: Coordinates (x, y, z), RGB color values

#  Loop Tuple
# Definition: Iterate through tuple items
# Why use: Process each item
# (for loop):
fruits = ("apple", "banana", "mango") 
for fruit in fruits: 
    print(fruit) 
#  (while loop):
i = 0 
while i < len(fruits):
    print(fruits[i]) 
    i += 1 
# Real-world: Print all months, process fixed data

# Join Tuple
# Definition: Combine two or more tuples
# Why use: Merge multiple fixed datasets

t1 = (1, 2, 3)
t2 = (4, 5, 6) 
t3 = t1 + t2 
print(t3) 

# (1, 2, 3, 4, 5, 6)
# Real-world: Combine coordinates, combine student IDs

#  Tuple Methods-----
# Definition: Limited methods because tuple is immutable

# Methods:
# count(value) → Count occurrences
# index(value) → Find index of first occurrence

fruits = ("apple", "banana", "apple", "mango")
print(fruits.count("apple")) 
print(fruits.index("banana")) # 1 
# Real-world: Count repeated items, find position of specific data

# Key Points 
# Tuples are ordered, immutable, allow duplicates
# Use tuple when data is fixed or should not change
# Faster than list → useful for large datasets with fixed values
# Methods are limited → only count() and index()







# syntax----------
furits = ("apple", "banana", "cherry ")
print(furits)


#  Access Tuple-------------
days = ("Sun", "Mon", "Tue", "Wed")
print(days[2])
print(days[-1]) # Wed 


#  Update Tuple------------
fruits = ("apple", "banana", "mango")
fruits_list = list(fruits) 
fruits_list[1] = "orange" 
fruits = tuple(fruits_list)
print(fruits) 


# Output:
# ('apple', 'orange', 'mango')


# Unpack Tuple----------

point = (10, 20, 30) 
x, y, z = point 
print(x, y, z) 
# Output:
# 10 20 30



# loop of tuple---------

fruits = ("apple", "banana", "mango") 
for fruit in fruits: 
    print(fruit) 
#  (while loop):

fruits = ("apple", "banana", "mango")

for i in range(len(fruits)):
    print(i + 1, fruits[i])






i = 0 
while i < len(fruits):
    print(fruits[i]) 
    i += 1
    
    
    
    
# Join Tuple---------
# 	Definition: Combine two or more tuples
# 	Why use: Merge multiple fixed datasets

t1 = (1, 2, 3) 
t2 = (4, 5, 6) 
t3 = t1 + t2 
print(t3) 


# Output:
# (1, 2, 3, 4, 5, 6)



# Tuple Methods------
# Definition: Limited methods because tuple is immutable
# Methods:
# count(value) → Count occurrences
# index(value) → Find index of first occurrence

fruits = ("apple", "banana", "apple", "mango") 
print(fruits.count("apple")) 
print(fruits.index("banana")) 
# Real-world: Count repeated items, find position of specific data


