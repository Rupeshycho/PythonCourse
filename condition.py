def age_checker():
    while True:  
        try:
            age=int(input("Enter your age: "))
            if age<=0:
                print("Invalid age")
                
            elif age>100:
                print("Your age  must be under than 100.")    
                
            elif age>=18:
                print("You can vote.")
            else:
                print("You are under 18.")
                
        except ValueError:
            print("Ony type Numbers")  
            
        exit_choice=input("If, you want to exit the loop, type 'yes': ").lower()
        if exit_choice=='yes':
            print("---Good bye---")    
            break        


def odd_even():
    num=[1,2,3,4,5,6,8,98,7,5,32,12,23,67]
    even=[]
    odd=[]
    for n in num: 
        if n%2==0:
            even.append(n)
        else:
            odd.append(n)
    print("Even Numbers: ",even)
    print("Odd Numbers:",odd)
            

def list_set():   
    while True:
        try:
            count=int(input("Enter the count of numbers: "))  

            numbers=[]

            for i in range(1,count+1):
                num=int(input(f'Enter the number {i}:'))
                numbers.append(num)
            print(f'Stored numbers: {numbers}')
            set_list=set(numbers)
            print(f'In set: {set_list}')
        except ValueError:
            print("It must be number, bruh...")
            continue
        
        exit_choice=input("Do you wanna exit? (y/n)").lower()
        if exit_choice=="y":
            print("Exiting....")
            print("Thank you! ! !")
            break
        if exit_choice=='n':
            continue
print(f'{"Vote Eligibility".center(70,"-")}\n')
age_checker()

print(f'{"Odd or Even ".center(70,"-")}\n')
odd_even()

print("\n")

print(f'{"User choosen count of numbers in a list".center(70,"-")}\n')
list_set()

            