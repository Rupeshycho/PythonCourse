#Battery
battery = int(input("Enter the battery percentage: "))

while battery < 100:
    print("Charging phone... Battery at", battery, "%")
    battery += 10

print("Battery is full. Stop charging.")

#Homework is done or not 
hw=input("Are you done homework?(yes/no)\nAnswer: ")

while hw.lower() == 'no':
    
    print("Complete it now..")
    
    hw = input( "Are you done with your homework? (yes/no)\nAnswer: ")
    
print("Homework completed. Time to rest.")

#advanced homework progress checker

print("Welcome to Homework Tracker!\n")

homework_done = False
energy_level = 5 
breaks_taken = 0


while not homework_done:
    hw = input("Are you done with your homework? (yes/no)\nAnswer: ").lower()
    
    if hw == 'no':
        if energy_level > 1:
            print("Keep working! You can do it.")
            energy_level -= 1 
        else:
            print("You are tired. Take a short break to recharge.")
            input("Press Enter after your break...")
            energy_level = 5  
            breaks_taken += 1
        print(f"Current energy level: {energy_level}/5")
    
    elif hw == 'yes':
        homework_done = True 
    else:
        print("Please answer only 'yes' or 'no'. Try again.")


#final 
print("\nCongratulations! Homework completed.")
print(f"You took {breaks_taken} break(s) during study.")
print("Time to rest and enjoy your free time! 🎉")
