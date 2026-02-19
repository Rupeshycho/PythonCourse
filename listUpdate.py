print("List 1 ".center(40,"-"))
num=[]
for x in range(1,31):
    num.append(x)
print(num)

print("List 2 ".center(40,"-"))
nums=[x for x in range(1,51)]
print(nums)

print("List 3 ".center(40,"-"))
nums=[x for x in range(10)]
print(nums)

print("List 4 ".center(40,"-"))
nums=[ x for x in range(10)]
print(nums)

#<variable> = [<expression> for <item> in <iterable>]
# <iterable>: any iterable obj: range, lists, tuples, strings, sets

print("list 5".center(40,"-"))
nums=[x**2 for x in range(0,11)]
print(f'Squares upto 10:\n{nums}')

nums=[x*2 for x in range(0,11)]
print(f'Mult. Table of 2:\n{nums}')

print("List6".center(40,"-"))
nums=[x+1 for x in range(10)] #x+1 : expression 
print(nums)

tags = ["travel", "vacation", "journey"]
hashtags=["#"+x for x in tags]
print(hashtags)

print("\n")
cities=['madrid', 'paris','lisabon']
cities_cap=[x.capitalize() for x in cities]
print(f"Cities(in Capitals):\n{cities_cap}")

users=["Brandon","Emma","Brian","Sophia","Ethan","Ava","Benjamin", "Mia","Chloe"]
group=[x for x in users if x[0]=="B"]
print(f'Starting with b(x[0]=B): {group}')

# names=[]
# while True:
#     x=input("Enter the name: ")
#     for x in range(6):
#         names.append(x)
# group=[x for x in names if x[0]!="A"]

names = []
for i in range(6):
    x = input("Enter the name: ")
    names.append(x.capitalize())  
    
group = [name for name in names if name[0]!=("A")]

print("Names not starting with A:", group)

# Ask user how many names they want to input
n = int(input("How many names do you want to enter? "))

names = []

# Loop exactly n times
for i in range(n):
    x = input(f"Enter name {i+1}: ")
    names.append(x.capitalize())   # capitalize before storing

# Filter names that do NOT start with 'A'
group = [name for name in names if not name.startswith("A")]

print("Names entered:", names)

print("Names not starting with A:", group)

sports=["Football", "Basketball", "Tennis","Golf", "Volleyball"]
group=[x  for x in sports if "ball" in x] 
print(f'Sports ending with ball:{group}')



scores=[68,44,87,87,99,76,78]
group=[x for x in scores if x > 80]
print(f'Marks(>0): {group}')


print("Word length Longer that 4 letters".center(40,"-"))
words=["tree","RupeshAnju","AnjuRupesh","RamSita","Sitaram","pray","keep"]
new_list=[x for x in words if len(x)>4]
print(f'More than 4 letters: {new_list}')


