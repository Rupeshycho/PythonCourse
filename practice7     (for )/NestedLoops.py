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