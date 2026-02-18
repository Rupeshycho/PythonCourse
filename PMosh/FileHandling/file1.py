with open('PMosh\FileHandling\welcome.txt', 'r+') as f: #for read and write use r+ mode
    print(f.read())
    print(f.write('Welcome to Python Programming!'))  # This will raise an error because the file is opened in read mode
    
f=open('PMosh/FileHandling/welcome.txt','r+')
print(f.read())    
    
