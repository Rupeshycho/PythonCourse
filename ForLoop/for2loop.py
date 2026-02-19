# *****
# ****
# ***
# **
# *
for i in range(5, 0,-1):
    print(i * "*")
    



    
# 1
# 22
# 333
# 4444
# 55555

for i in range(1,6):
    for j in range(1,i+1):
        print(f'{i}',end=" ") 
            #print(i,end="")
    print()




print("\nIncreasing pattern 1 to 12345")    
# 1
# 12
# 123
# 1234
# 12345
for i in range(1,6):
    for j in range(1,i+1):
        print(j,end=" ")
    print()     




# *****
# *****
# *****
# *****
# *****

print("\nSquare * pattern") 
for i in range(1,5):
    print(5*"*")
    
#     *
#    **
#   ***
#  ****
# *****

print("\nRight-Aligned * Pattern")
for i in range(1,5):
    print(" "*(5-i)+"*"*i)
    