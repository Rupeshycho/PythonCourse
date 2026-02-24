from pathlib import Path  
#Absolute path 
# c:\Program Files\Microsoft  

# #relattive path
# path=Path("inheritance")
# print(path.exists()) 

# #rmdir => remove directory 
# path=Path("emails")
# print(path.rmdir())  #None

# if path.exists:
#     path.rmdir()
#     print("Folder deleted successfully.")
    
# else:
#     print("Folder doesn't exists. ")
    
# # path=Path('messages')  #New file 
# # print(path.mkdir())  #False 
from pathlib import Path
path = Path()
# for file in path.glob('*.*.py'):
for file in path.glob('*'):
    print(file)