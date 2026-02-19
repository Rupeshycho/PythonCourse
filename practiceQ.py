with open("practice.txt","w+") as f: 
    data=f.write("HI everyone\nWe are learning File I/O\nusing Java.\nI like programming in Java.")
    f.seek(0)
    data=f.read()
    print(data)
    
new_data=data.replace("Java","Python")
print(new_data)

with open("practice.txt","w+") as f: 
    f.write(new_data)



def check_for_word():
    word="learning"
    with open("practice.txt","r") as f: 
        data=f.read()
        if(data.find(word)!= -1):
    
            print("Found.")
        else: 
            print("Not found")
check_for_word()


