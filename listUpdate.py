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

# Let the user enter 6 names
for i in range(6):
    x = input("Enter the name: ")
    names.append(x.capitalize())   # capitalize before adding

# Filter names that do NOT start with 'A'
group = [name for name in names if name[0]!=("A")]

print("Names not starting with A:", group)

