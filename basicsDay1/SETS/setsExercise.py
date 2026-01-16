# # WAP to take n numbers from the user and store only unique values using a set.
# n=int(input("Enter the number of elements: "))
# unique_numbers=set()
# for i in range(n):
#     num=int(input(f'Enter number {i+1}:'))
#     unique_numbers.add(num)
# print(f'Unique values are: {unique_numbers}')

# #copy() , add() takes exactly 1 elment 
# print("method: copy()")
# set1={1,2,3,4}
# set2=set1.copy()
# set2.add(11)
# #add takes exactly  1 argument 
# print(set2)

#WAP to remove duplicate elements from a list using a set.
# lst = [10, 20, 30, 20, 40, 10, 50]

# print("Original list:", lst)
# print(f'into set: {set(lst)}')
# print(f'Now set into list:{list(set(lst))} ')

# unique_list = list(set(lst))
# print("List after removing duplicates:", unique_list)

# #wap to count a number of words in a sentence
# sentence=input("Enter the sentence(repeate words):")
# a=sentence.split()
# into_set=set(a)
# print(f'Into set: {into_set}')
# print("Unique words Length:", len(into_set))

#Print common elements between two user

#set Before input("sentence") with .split()
harshit=set(input("Harshit's regular words: ").split())
rupesh=set(input("Rupesh regular words: ").split())

common=harshit.intersection(rupesh)
print(f'Common words: {common}')


#WAP to check two sets are equal or not 
print("Checking Sets are equal or not ")
print("-"*40)
set1 = set(input("Enter elements of first set: ").split())
set2 = set(input("Enter elements of second set: ").split())

if set1 == set2:
    print("Both sets are equal")
else:
    print("Sets are not equal")

# 1. Find missing numbers from 1 to 10 using sets
print("Program 1: Find Missing Numbers")
print("-" * 40)

complete_set = set(range(1, 11))  # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

given_numbers = {1, 3, 5, 7, 8, 10}

missing = complete_set - given_numbers

print("Complete set (1-10):", complete_set)
print("Numbers we have:", given_numbers)
print("Missing numbers:", sorted(missing))
print("\n")    

# 2. Find common characters between two strings using sets
print("Program 2: Find Common Characters")
print("-" * 40)

str1 = "hello"
str2 = "world"

set1 = set(str1)  # {'h', 'e', 'l', 'o'}
set2 = set(str2)  # {'w', 'o', 'r', 'l', 'd'}

common = set1 & set2

print("First string:", str1)
print("Second string:", str2)
print("Set from first string:", set1)
print("Set from second string:", set2)
print("Common characters:", common)
print("\n")


# 2. Find common characters between two strings using sets

print("Program 2: Find Common Characters")
print("-" * 40)

# Two strings
str1 = "hello"
str2 = "world"

# Convert strings to sets (removes duplicates automatically)
set1 = set(str1)  # {'h', 'e', 'l', 'o'}
set2 = set(str2)  # {'w', 'o', 'r', 'l', 'd'}

# Find common characters using & (intersection)
common = set1 & set2

print("First string:", str1)
print("Second string:", str2)
print("Set from first string:", set1)
print("Set from second string:", set2)
print("Common characters:", common)
print("\n")

#Remove common elements from two sets 
print("Remove common elements from two sets")
print("-"*40)
def remove_common_elements():
    set1 = {1, 2, 3, 4, 5}
    set2 = {4, 5, 6, 7, 8}
    
    print(f"Set 1: {set1}")
    print(f"Set 2: {set2}")
    
    
    result = set1 ^ set2
    print(f"After removing common elements (symmetric difference): {result}")
    
    
    set1_only = set1 - set2
    print(f"Set 1 after removing common: {set1_only}")
    
    
    set2_only = set2 - set1
    print(f"Set 2 after removing common: {set2_only}")

print("Program 4: Remove Common Elements")
remove_common_elements()
print("\n" + "-"*50 + "\n")

# 5. Create a set of squares using set comprehension
print("Creating a set of squares ")
print("-"*40)
def create_squares_set():
    squares = {x**2 for x in range(1, 11)}
    print(f"Set of squares from 1 to 10: {sorted(squares)}")
    
    # Alternative: using set() with generator
    squares_alt = set(x**2 for x in range(1, 11))
    print(f"Using generator: {sorted(squares_alt)}")

print("Program 5: Set of Squares")
create_squares_set()

print("="*50+"\n")