#list of 5 favorite fruits and print it 
fruits=["apple","banana","pineapple","orange","grape"]
print(f'Original List: {fruits}')

# 2.Change the second item to "orange"
fruits.remove("banana")

# 3.Add a new fruit at the end
fruits.insert(1,"Orange")
print(f'banana removed and orange inserted at second: \n{fruits} ')

# 4.Remove the first fruit
fruits.append("kiwi")
print(f'Kiwi added to list\n{fruits}')


# 5.Print all fruits using for loop
fruits.pop(0)
print(f'apple popped(removed) by indexing: \n{fruits}')

i=0
while i<len(fruits):
    #print(fruits[i])
    print(f'{i},  {fruits[i]}')
    i+=1
    
for fruit in fruits:
    print(fruit)
    
squares=[]

#6.Create a list of squares from 1 to 10 using list comprehension
for i in range(1,11):
    squares.append(i**2) 

print(squares)    
    
#7. Sort the list [5,2,9,1] ascending and descending        
list=[5,2,9,1]
list.sort()
print(f'Ascending: {list}')

list2=[5,2,9,1]
list2.sort()
list2.sort(reverse=True)
print(f'Descending: {list2}')



#8. Join two lists [1,2,3] and [4,5,6]
list1=[1,2,3]
print(list1)
list2=[4,5,6]
print(list2)
print(f"Lists joined: {list1+list2}")
