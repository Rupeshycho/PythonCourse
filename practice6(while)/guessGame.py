# i=1
# while i<=5:
#     print('*'*i)
#     i=i+1
# print("--Done--")    

#Guess_Game
while True:
    secret_number=9
    guess_count=0
    guess_limit=3
    while guess_count<guess_limit:
        guess=int(input("Guess: "))
        guess_count+=1
        if guess==secret_number:
            print("That's correct\nYou wonn!!!")
            break
        else:
            print("Hint: The largest one-digit number. ")
    else:
        print("Sorry, you failed....")
        

#Try-Again  

    answer = input("Do you want to play again? (yes/no): ").lower()

    if answer.lower() == "yes":
        continue   # goes back to the SAME loop
    else:
        print("Thanks for playing! 👋")
        break
        
        



  