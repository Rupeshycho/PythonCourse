# ================================================
# PYTHON CONDITIONAL STATEMENTS – COMPLETE NOTES
# (if–else and match–case)
# ================================================

# -----------------------------------------------
# 1. PYTHON if–else (CONDITIONAL STATEMENTS)
# -----------------------------------------------

# DEFINITION:
# if–else is a decision-making statement in Python.
# - If the condition is True, one block of code runs
# - If the condition is False, another block runs

# WHY USE if–else:
# • Decision making
# • Perform different actions based on conditions
# • Implement real-world logic

# -----------------------------------------------
# 1️⃣ Python if Statement
# -----------------------------------------------
# Definition:
# The if statement executes code only when the condition is True.

# Syntax:
# if condition:
#     statement

# Example:
# age = 20

# if age >= 18:
#     print("You are adult")

# Explanation:
# • age >= 18 → True
# • Condition is True, so the statement executes

# Use cases:
# • Age verification
# • Login validation

# -----------------------------------------------
# 2️⃣ Python elif Statement
# -----------------------------------------------
# Definition:
# elif (else if) is used to check multiple conditions.

# Syntax:
# if condition1:
#     statement
# elif condition2:
#     statement

# Example:
# marks = 75

# if marks >= 80:
#     print("A Grade")
# elif marks >= 60:
#     print("B Grade")

# Explanation:
# • marks >= 80 → False
# • marks >= 60 → True
# • "B Grade" is printed

# Use cases:
# • Grading system
# • Multiple-choice decisions

# -----------------------------------------------
# 3️⃣ Python else Statement
# -----------------------------------------------
# Definition:
# else executes when all conditions are False.

# Syntax:
# if condition:
#     statement
# else:
#     statement

# Example:
# age = 16

# if age >= 18:
#     print("Adult")
# else:
#     print("Minor")

# Explanation:
# • age >= 18 → False
# • else block executes

# Use cases:
# • Pass / Fail system
# • Access denied logic

# -----------------------------------------------
# 4️⃣ Shorthand if (One-line if–else)
# -----------------------------------------------
# Definition:
# Used to write simple if–else in a single line.

# Syntax:
# statement_if_true if condition else statement_if_false

# Example:
# a = 10
# b = 5

# print("A is big") if a > b else print("B is big")

# Explanation:
# • a > b → True
# • "A is big" is printed

# Use cases:
# • Short decisions
# • Clean and compact code

# -----------------------------------------------
# 5️⃣ Logical if (and / or / not)
# -----------------------------------------------
# Definition:
# Logical operators are used to check multiple conditions.

# Example:
# age = 22
# has_id = True

# if age >= 18 and has_id:
#     print("Entry allowed")

# Explanation:
# • age >= 18 → True
# • has_id → True
# • and → both True → allowed

# Use cases:
# • Login systems
# • Permission checks

# -----------------------------------------------
# 6️⃣ Nested if
# -----------------------------------------------
# Definition:
# An if statement inside another if statement.

# Syntax:
# if condition:
#     if condition:
#         statement

# Example:
# age = 20
# has_license = True

# if age >= 18:
#     if has_license:
#         print("You can drive")

# Explanation:
# • First if → age check
# • Second if → license check

# Use cases:
# • Complex decisions
# • Multi-level validation

# -----------------------------------------------
# 7️⃣ pass Statement
# -----------------------------------------------
# Definition:
# pass is a placeholder statement that does nothing.
# Used to avoid errors when code is incomplete.

# Example:
# age = 20

# if age >= 18:
#     pass
# else:
#     print("Minor")

# Explanation:
# • if block is empty
# • pass prevents syntax error

# Use cases:
# • Incomplete programs
# • Future implementation

# -----------------------------------------------
# REAL-WORLD LOGIN EXAMPLE
# -----------------------------------------------
# username = "admin"
# password = "1234"

# if username == "admin" and password == "1234":
#     print("Login success")
# else:
#     print("Login failed")

# -----------------------------------------------
# QUICK SUMMARY (if–else)
# -----------------------------------------------
# Statement        Purpose
# if               Execute when True
# elif             Check multiple conditions
# else             Execute when all False
# shorthand if     One-line decision
# logical if       Multiple conditions
# nested if        Complex logic
# pass             Empty placeholder

# ================================================
# 2. PYTHON match–case STATEMENT
# ================================================

# DEFINITION:
# match–case is a decision-making statement similar to switch-case.
# It compares one value with multiple cases and executes the matching case.

# -----------------------------------------------
# WHY USE match–case:
# -----------------------------------------------
# • Avoid long if–elif chains
# • Cleaner and more readable code
# • Useful for menus, commands, options

# -----------------------------------------------
# BASIC SYNTAX:
# -----------------------------------------------
# match variable:
#     case value1:
#         statement
#     case value2:
#         statement
#     case _:
#         statement   # default case

# (case _ works like else)

# -----------------------------------------------
# 1️⃣ Simple Example
# -----------------------------------------------
# day = 3

# match day:
#     case 1:
#         print("Sunday")
#     case 2:
#         print("Monday")
#     case 3:
#         print("Tuesday")
#     case _:
#         print("Invalid day")

# Explanation:
# • day = 3
# • case 3 matches
# • Output: Tuesday

# Use cases:
# • Day selection
# • Menu systems

# -----------------------------------------------
# 2️⃣ match with String
# -----------------------------------------------
# command = "start"

# match command:
#     case "start":
#         print("Program started")
#     case "stop":
#         print("Program stopped")
#     case _:
#         print("Unknown command")

# Use cases:
# • CLI commands
# • Button actions

# -----------------------------------------------
# 3️⃣ match with Multiple Values
# -----------------------------------------------
# choice = "a"

# match choice:
#     case "a" | "e" | "i" | "o" | "u":
#         print("Vowel")
#     case _:
#         print("Consonant")

# Explanation:
# • | means OR
# • If any value matches, code runs

# Use case:
# • Character classification

# -----------------------------------------------
# 4️⃣ match with Numbers (Calculator)
# -----------------------------------------------
# a = 10
# b = 5
# op = "+"

# match op:
#     case "+":
#         print(a + b)
#     case "-":
#         print(a - b)
#     case "*":
#         print(a * b)
#     case "/":
#         print(a / b)
#     case _:
#         print("Invalid operator")

# Use cases:
# • Calculator
# • Menu-driven programs

# -----------------------------------------------
# 5️⃣ match vs if–elif
# -----------------------------------------------
# if–elif:
# if day == 1:
#     print("Sunday")
# elif day == 2:
#     print("Monday")

# match–case:
# match day:
#     case 1:
#         print("Sunday")
#     case 2:
#         print("Monday")

# ✔ match–case is cleaner and more readable  
# ✔ Best when many options exist

# -----------------------------------------------
# REAL-WORLD MENU EXAMPLE
# -----------------------------------------------
# print("1. Add")
# print("2. Delete")
# print("3. Update")

# choice = 2

# match choice:
#     case 1:
#         print("Add item")
#     case 2:
#         print("Delete item")
#     case 3:
#         print("Update item")
#     case _:
#         print("Invalid choice")

# -----------------------------------------------
# QUICK SUMMARY (match–case)
# -----------------------------------------------
# Feature        Explanation
# match          Compares value
# case           Matching option
# case _         Default case
# Cleaner        Than if–elif