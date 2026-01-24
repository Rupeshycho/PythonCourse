numbs =[5,2,1,7,4]
numbs.sort()
print(f'Acending order: {numbs}')

numbers=[5,2,1,7,4]
print('numbers=',numbers)
numbers.insert(0, 10)
print(".insert(0,10): ",numbers)

numbers.remove(7)
print("7 removed",numbers)

clear_all=input("Do you wanna clear the numbers(Yes/No): ").lower()

if clear_all=="yes":
    numbers.clear()
    print("numbers= ",numbers)
    
numbers=[5,2,1,7,4]
remove_last=input("Do you wanna remove last number?(y/n): ")
if remove_last=="y":
    numbers.pop()
    print("Last'4' removed (pop): ",numbers)
else: 
    print(numbers)  
#Find index
def index_num():
    try:
        print("Find Index: ".center(40,"="))
           
        numbers=list(range(10,30,2))
        print(numbers)
        
        idx=int(input("Enter the number to find its INDEX: "))
        
        print(f'Index of {idx}: {numbers.index(idx)}')
        print("\n")
            
    except:
        print("Numbers Not found in the list ")
        print("\n")    
    finally:
        print("Bye-Bye, Meet you soon🥹")       
index_num()
