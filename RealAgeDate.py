#This python code reveals your Real Age

from datetime import datetime

b=datetime.strptime(input("Enter DOB (YYYY-MM-DD): "), "%Y-%m-%d")
print("\n")
d=datetime.now()-b
print("Total Age: ".center(40,"="))
print(d.days//365,"Years")

print(d.days//30,"Months")

print(d.days,"Days")

print(d.total_seconds(), "Seconds")

