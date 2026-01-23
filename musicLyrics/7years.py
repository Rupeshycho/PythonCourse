import time 
import sys 

RED='\033[91M'
GREEN='\033[92M'
YELLOW='\033[93M'
BLUE='\033[94M'
MAGENTA='\033[95M'
CYAN='\033[96M'
RESET='\033[0M'

lyrics=[
    (RED, "I only see my goals, I don't believe in failure"),
    (GREEN, "Cause I know the smallest voices, they can make it major"),
    (YELLOW, "I got my boys with me, at least those in favor"),
    (BLUE, "And if we don't meet before I leave, I hope I'll see you later"),
    (MAGENTA, "Once I was 20 years old, my story got told"),
    (CYAN, "I was writing'bout everything I saw before me"),
    (RESET, "Once, I was 20 years old"),
]

def animate_text(color,text):
    for char in text: 
        sys.stdout.write(color+char+RESET)                  # character in the specified color
        sys.stdout.flush()                                  #immediately print the character to the screen
        time.sleep(0.05)                                    #for 0.05 seconds paus , before printing next character
        
    print()
    
    
def main():
    for color, line in lyrics: 
        animate_text(color,line)
        time.sleep(0.3) 
        
if __name__=='__main__':
    main()            
        