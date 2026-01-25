def try_except_else():
    try:
        age=int(input("Age: "))
        print(age)
        
    except:
        print("Must be a <<number>>")
        
    else:
        print("SUCCESS:: Else when Try: is error-free. ")    
try_except_else()        




def try_except_finally():
    try:
        age=int(input("Age: "))
        income=20000
        risk=income//age/100
        print(age)
        print(f'Risk: {risk}')
    except ValueError:
        print("Must be a <<number>>")
    except ZeroDivisionError:
        print("Age cannot be 0 ")    
    finally:
        print("finally: run every times at last.") 
        
try_except_finally()               