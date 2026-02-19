f = open("demo.txt", "a")  
f.write("\nAfter that ,NOde.js ")

f.close()


# f2=open("sample.txt","w")
f2=open("sample.txt","w+") 
                            #r+ - add at the start and replace the previous 
# f2.write("1.(r+) ")


f2.write("Truncated the original one ")
print(f2.read())
f2.read()
f.close()

f3=open("sample3.txt","a+")
f3.write("Append mode (a+)")

f3.close()

with open("rupesh.txt","w+") as f:  #alias => tony stark= Iron man 
    f.write("This is a With open as f one")
    f.seek(0)   
    print(f.read())


    
import os
os.remove("deleted.txt")