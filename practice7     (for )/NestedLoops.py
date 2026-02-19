for x in range(4): 
    
     #0 1 2 3 starts with 0 & value excluded in range
    for  y in range(3):
        #1st: it completes for 0,0 0,1 0,2 and the outside of this looop go to the first one and continue after 1 
        print(f'({x},{y})')

#Challenge F shape  with x
'''
XXXXX
XX
XXXXX
XX
XX 
'''
numbers=[5,2,5,2,2] 
for counter in numbers:
    print('X'*counter)

#complex method- Mosh(coz i find it complex )

for x_count in numbers:
    output=''
    for count in range(x_count):
        output+='x'
    print(output)    

#Index[starts from 0]
names=['RupeshAnju','Aarti','Ram','shyam','Alex']
print(names[0])#RupeshAnju    
print(names[-1]) #alex
print(names[2:])  #starts from the 2(Ram) to including last 
print(names[1:4]) # prints from 1(Aarti) to shyam no inclusion of  4th index 
print(names[1:]) #now include all items by including  1

print(f'Print all items\n{names[:]}')

print(f'Original list: {names}')
names[0]='AnjuRupesh'
print(names)

#WAP to find the largest number in a list
numbers = [6,28,4,30,10]
max= numbers[-1]
for num in numbers:
    if num> max:
        max = num
print(max)      
matrix=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

#print a matrix rows 
for row in matrix:
    print(row)

#print all items of matrix
for row in matrix:
    for item in row:
        print(item)    
print(row) #print last row 

numbers2=[1,2,3]
for numb in numbers2:
    print(numb)    

        