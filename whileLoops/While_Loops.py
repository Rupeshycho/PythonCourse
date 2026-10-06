print("---While Loops---")

# while(condtion):
#     ......

i=1
while i<=5:
    print(i*'*')
    i+=1

print("Outside of the looop: done:")

# print hello world 5 times 

choose=input("Enter what to print: ")
count =1
while count <=5:
    print(choose)
    count+=1



# print right angled triangle * 

for j in range(1,5):
    print(j*"*",) #end="  " 
    j+=1
print()  


for i in range(0,4):
    print((4-i)*"*")
    
for i in range(0,4,-1):
    print(i*"*")