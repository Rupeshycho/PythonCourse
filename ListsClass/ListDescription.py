fruits=["apple", "banana", "mango", "pineapple"]
fruits.append("grape")
fruits.insert(1,"kiwi")
print(fruits)

fruits.extend(["strawberry", "watermelon"])
print(fruits) #['apple', 'kiwi', 'banana', 'mango', 'pineapple', 'grape', 'kiwi', 'watermelon']


fruits.remove("kiwi")
print(f"--Removed kiwi--\n{fruits}")  #kiwi removed


print(f'Pop: {fruits.pop(0)}')

del fruits[1]

#remove sold produts, remove completed task 


fruits.clear()
print(f'Fruits deleted{fruits}')
fruits.extend(["apple", 'banana', 'mango'])
print(f'Extended 3 items in a fruits":{fruits}')

#["apple", 'banana', 'mango']

i=0
while i< len(fruits):
    print(fruits[i])
    i+=2                     #apple mango 
    
    #real-world: print all student names, process all ordders 
    
    #List comprehension-----
    #Defintion: quick way to create lists using one line 
    #Why use: Shorter code, efficient 
    
squares=[x**2 for x in range(1,6)]
print(squares)

#sorting: arange items in order 
#sort() -> ascending 
#sort(reverse=True)-> descending
#sorted(list)-> return new sorted list 

numbers=[5,2,9,1,12,34,56,67,89,54,31,23]
numbers.sort()
print(f'Sorted ascending:{numbers}')

numbers.sort(reverse=True)
print(f'Descending using sort(reverse=True): {numbers}')

#copy list: creating duplicate of list 
#Avoid changing original list 
#methods: copy() 0r list()

fruits_copy=fruits.copy()
print(f'Copy list: {fruits_copy}')

print(list(fruits))

#Join List: combine 2 or more lists 
#+operatior-> concatenate

fruit_2=["avocado", "guava"]
fruit_total=fruits+fruit_2
print(f'Total fruits: {fruit_total}') #add fruit_2 whole items in one 

fruit_total.extend(["Rupesh","Robin"])
print(f'Names added: {fruit_total}')

#Real-world: combine order lists , merge datasets 
#List Methods ----
#append() add item to end 
#insert() add item at specific index
#extend() add multiple items 
#remove() remove by value
#pop() remove by index
#clear() remove all items 
#sort() sort ascending 
#reverse() Reverse list 
#index() find index of item 
#count() count occurences 
#copy()  copy list 

#List exercise-----
rupes=["cricket","code", "html","code"]
rupes.sort()
print(rupes)
rupes.sort(reverse=True)
print(rupes)

rupes_2=["cricket","code", "html","code"]
num=rupes_2.index("code")
print(f'Code is at index: {num}')

count_code=rupes_2.count("code")
print(f'code appeared at {count_code} times')