secret_num=9
guess_count=0
guess_limit=3
rem_count=2

while guess_count<guess_limit:
    guess=int(input("Guess: "))
    guess_count+=1
    
    if guess==secret_num:
        print("You won")
        
    else:
        print(f"Remaining {rem_count} chances.")
        rem_count-=1    
   
        
else:
    print("Saad! keep trying...")
    