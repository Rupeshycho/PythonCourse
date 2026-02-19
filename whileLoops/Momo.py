print("Welcome to Rupesh Dai ko Mo:MO! \n")

wallet = int(input("How much you got bro:\n Rs: "))
momo_price = 50
momo_bought = 0

while wallet >= momo_price:
    print(f"You have Rs.{wallet} in your wallet.")
    buy = input("Do you want to buy a momo for Rs.50? (yes/no)\nAnswer: ").lower()
    
    if buy == 'yes':
        wallet -= momo_price  
        momo_bought += 1
        print(f"MoMo bought: {momo_bought}\n")
    elif buy == 'no':
        print("Okay, maybe next time.\n")
        break 
    else:
        print("Please answer with 'yes' or 'no'.\n")



print("Shopping done! 🛒")
print(f"Total MoMo bought: {momo_bought}")
print(f"Money left in wallet: Rs.{wallet}")
