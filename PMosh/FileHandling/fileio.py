f=open("pmosh/filehandling/demo.txt","r")
# data=f.read()
# print(data)

line1=f.readline()
print(line1)
line2=f.readline()
print(line2)
# f.write("Writing to file , truncating ")
line3=f.readline()
print(line3)

f.close()