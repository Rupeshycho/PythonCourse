def greet_user():
    
    name=input("What's your name?\n")
    
    print(f'Hey there, {name}.')
    age=input("What's your age?\n")
    print(f'so you are {int(age)} years old.')
    return name
print(">>>Interview>>>")    
name=greet_user()   
print(f'Thank you Mr.{name}.\n')

#parameters
def greeting(first_name, last_name):
    print(f"Hi there Mr. {first_name} {last_name} !")
    print("Welcome aboard")

print(">>>Start>>>")    

print("Rupesh", "Yadav")
greeting(last_name="Newton ", first_name="Isaac") 

print("Finish!")

#RETURN STATEMENT
def square(number):
    return number**2

result=square(3)
print(f'Square(3) is: {result}')   

def quotient(num1, num2):
    print(num1//num2)

print(quotient(19191,2))    #9 None


#REUSABLE FUNCTIONS 
def emoji_converter(message):
    words=message.split(" ")
    emojis={
        ":)": "🙂",
        ":(":"😔"
    }
    output=""
    for word in words: 
        output+=emojis.get(word,word)+" "
    return output


#usage
message=input("Your feelings: ")
print(emoji_converter(message))