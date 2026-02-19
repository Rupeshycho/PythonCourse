#Made by me with some errors.
'''while True:
    user_input=input("Type help for details!\n ")
    
    if user_input=="help":
        print("Start - to start the car\nStop - to stop the car \nquit - to exit ")
        car_simulation=input("What do you want to do?").lower()
        if car_simulation=="start":
            print("Car started🚕🍃🍃🍃 Ready to go!")    
        elif car_simulation=="stop":
            print("Car stopped🚕")
            
        elif car_simulation=="quit":
            print("Exiting....")
            break 
        else:
            print("I can't understand that..")
            
            
    else:
        print("I cant understand")                
'''
#Claude-fixed 
'''car_started = False

while True:
    if not car_started:
        user_input = input("Type help for details!\n").lower()
    else:
        user_input = input("What do you want to do? ").lower()
    
    if user_input == "help":
        print("Start - to start the car\nStop - to stop the car\nQuit - to exit")
        
    elif user_input == "start":
        if not car_started:
            print("Car started 🚕🍃🍃🍃 Ready to go!")
            car_started = True
        else:
            print("Car is already running!")
            
    elif user_input == "stop":
        if car_started:
            print("Car stopped 🚕")
            car_started = False
        else:
            print("Car is already stopped!")
            
    elif user_input == "quit":
        print("Exiting....")
        break
        
    else:
        print("I can't understand that..")
'''              

#Short & Easy 
command =""
started=False
while True:      #command.lower()!="quit":
    command=input(">").lower() 
    
    if command=="start":
        if started: 
            print("Car is already started!..")
        else:
            started=True
            print("Car started.....") 
        
    elif command=="stop":
        if not started:
            print("Car is already stopped!")
        else:
            started= False    
            print("Car stopped.")
    elif command=="help":
        print("""
start - to start the car  
stop -  to stop the car
quit - to quit
""")
        
    elif command=="quit": 
        print("Exiting....")
        break
    else:
        print("Sorry, I don't understand that.")   
                
            