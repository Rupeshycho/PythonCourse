import time

print("MAKE YOU MINE:".center(30,"="))
lyrics = [
    
    (2.5, "Put your hand in mine "),
    (4.4, "\nYou know that I want to be "),
    (6.2,"With you all the time "),
    (9.1, "\nYou know that I wont't Stop "),
    (10.15,"Until I make you mine.."),
    (13.5, "\nYou know that I wont't Stop "),
    (15.7,"Until I make you mine.."),
    (19.2,"\nUNTIL I MAKE YOU MINE..")
]

def print_chars(text, char_delay=0.095):
    for ch in text:
        print(ch, end='', flush=True)
        time.sleep(char_delay)
    print()  # new line

start_time = time.time()

for timestamp, line in lyrics:
    # wait until the correct timestamp
    while time.time() - start_time < timestamp:
        time.sleep(0.01)

    print_chars(line)
    
    
    
 