num = [4]
for i in range(1, 11):
    for j in num:
        print(f"{j} * {i} = {j * i}")
        
# *
# **
# ***
# ****

for i in range(1,5):
    print(i*"*")        

# 1111
# 111
# 11
# 1
for j in range(1,6):
    print(i*"1")
    i-=1

for i in range(1,5):
    for j in range(1,i+1):
        print(j,end="")
    print()

print("\n---Multiplication Table---")    
for i in range(1,6):
    for j in range(1,6):
        print(i*j, end="  ")
    print()            
    
print("\n---Pair Printing---")
for i in range(1, 4):
    for j in range(1, 4):
        print(i,j)
        