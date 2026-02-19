# ================================================
# PYTHON DICTIONARIES – COMPLETE NOTES
# ================================================

# DEFINITION:
# A dictionary is an unordered and mutable collection of key:value pairs in Python.
# - Keys must be unique
# - Values can be of any data type

# WHY USE DICTIONARIES:
# • Store data in key-value format
# • Fast lookup using keys
# • Useful for student records, phonebooks, user profiles, configurations

# SYNTAX:
# my_dict = {"key1": value1, "key2": value2}

# ------------------------------------------------
# 1. ACCESS ITEMS
# ------------------------------------------------
# Definition:
# Retrieve value from a dictionary using a key.

# Why use:
# To access specific data.

# Example:
# student = {"name": "Sandeep", "age": 22, "city": "Kathmandu"}

# print(student["name"])     # Sandeep
# print(student.get("age"))  # 22

# --------------------------------
# Example 1: Normal get()
# --------------------------------
# print(student.get("age"))    # 22
# print(student.get("name"))   # Sandeep

# Explanation:
# • "age" key exists → returns value 22
# • "name" key exists → returns value "Sandeep"

# --------------------------------
# Example 2: Key not present
# --------------------------------
# print(student.get("grade"))  # None

# Explanation:
# • "grade" key does not exist
# • No error occurs, returns None

# --------------------------------
# Example 3: Key not present with default value
# --------------------------------
# print(student.get("grade", "Not Assigned"))  # Not Assigned

# Explanation:
# • Key not found → default value is returned

# --------------------------------
# Why get() is better than dict[key]
# --------------------------------
# # Using [] → Error if key is missing
# # print(student["grade"])   # KeyError

# # Using get() → Safe
# print(student.get("grade")) # None (no error)

# Use cases:
# • Student database → get marks safely
# • Configuration files → access optional settings safely

# Real-world examples:
# • Get student's age
# • Get product price

# ------------------------------------------------
# 2. CHANGE ITEMS
# ------------------------------------------------
# Definition:
# Update the value of an existing key.

# Example:
# student["age"] = 23
# print(student)

# Output:
# {'name': 'Sandeep', 'age': 23, 'city': 'Kathmandu'}

# Real-world use:
# • Update student marks
# • Update product price

# ------------------------------------------------
# 3. ADD ITEMS
# ------------------------------------------------
# Definition:
# Add a new key-value pair to the dictionary.

# Example:
# student["grade"] = "A"
# print(student)

# Output:
# {'name': 'Sandeep', 'age': 23, 'city': 'Kathmandu', 'grade': 'A'}

# Real-world use:
# • Add new student information
# • Add new product details

# ------------------------------------------------
# 4. REMOVE ITEMS
# ------------------------------------------------
# Definition:
# Removing key:value pairs from a dictionary.

# Why use:
# • Remove outdated data
# • Remove incorrect entries
# • Clean database or configuration data

# --------------------------------
# 1. pop(key)
# --------------------------------
# Definition:
# Removes a specific key and returns its value.

# Syntax:
# dict.pop(key)

# Example:
# student = {"name": "Sandeep", "age": 22, "city": "Kathmandu"}

# age = student.pop("age")
# print("Removed value:", age)
# print(student)

# Output:
# Removed value: 22
# {'name': 'Sandeep', 'city': 'Kathmandu'}

# --------------------------------
# 2. del dict[key]
# --------------------------------
# Definition:
# Deletes a specific key (does not return value).

# Example:
# del student["city"]
# print(student)

# Output:
# {'name': 'Sandeep', 'age': 22}

# --------------------------------
# 3. popitem()
# --------------------------------
# Definition:
# Removes the last inserted key-value pair.

# Example:
# removed = student.popitem()
# print("Removed item:", removed)

# Output:
# ('city', 'Kathmandu')

# Use case:
# • Acts like stack (LIFO)
# • Undo last inserted entry

# --------------------------------
# 4. clear()
# --------------------------------
# Definition:
# Removes all items from the dictionary.

# Example:
# student.clear()
# print(student)

# Output:
# {}

# ------------------------------------------------
# SUMMARY TABLE
# ------------------------------------------------
# Method        Action                         Returns
# pop(key)      Remove specific key            Value
# del[key]      Delete key                     None
# popitem()     Remove last inserted pair      (key, value)
# clear()       Remove all items               None

# ------------------------------------------------
# 5. LOOPING DICTIONARIES
# ------------------------------------------------
# Definition:
# Iterating through dictionary keys, values, or key-value pairs.

# Example:
# student = {"name": "Sandeep", "age": 22, "city": "Kathmandu"}

# # Loop keys
# for key in student:
#     print(key)

# # Loop values
# for value in student.values():
#     print(value)

# # Loop key-value pairs
# for key, value in student.items():
#     print(key, ":", value)

# ------------------------------------------------
# 6. COPY DICTIONARY
# ------------------------------------------------
# Definition:
# Creates a shallow copy of a dictionary.

# Why use:
# • Backup data
# • Work on copy without changing original

# Example:
# student_copy = student.copy()
# student_copy["age"] = 25

# ------------------------------------------------
# 7. NESTED DICTIONARY
# ------------------------------------------------
# Definition:
# A dictionary inside another dictionary.

# Example:
# students = {
#     "s1": {"name": "Sandeep", "age": 22},
#     "s2": {"name": "Rita", "age": 21}
# }

# Access:
# print(students["s1"]["name"])  # Sandeep

# Use case:
# • School database
# • Employee records

# ------------------------------------------------
# 8. DICTIONARY METHODS
# ------------------------------------------------
# get()       → Safe access
# keys()      → All keys
# values()    → All values
# items()     → Key-value pairs
# pop()       → Remove key
# popitem()   → Remove last item
# update()    → Add or update items
# clear()     → Remove all items
# copy()      → Shallow copy

# ------------------------------------------------
#  TIPS
# ------------------------------------------------
# • Dictionaries are unordered and mutable
# • Keys must be unique
# • Use get() for safe access
# • Use items() for looping
# • Use nested dictionaries for complex data