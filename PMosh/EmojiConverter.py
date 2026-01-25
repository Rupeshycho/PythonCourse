message=input(">")
words=message.split()
# good morning :) into 3 words 
emojis={
    ":)": "🙂",
    ":(": "😔"
    }
output=''
for word in words:
    output+= emojis.get(word, word)+" "
print(output)   
    
