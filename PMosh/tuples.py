#Immutable (Tuples)
numbers=(1,2,3,4,4)
# numbers[0]=10 #cannot change 
print("index of 4: ",numbers[4])

print("Repeatition of 4: ",numbers.count(4))


numbers = (1, 2, 3, 4, 4)

print("Tuple:", numbers)

print("Access by index:", numbers[0], numbers[-1])

print("Index of 4:", numbers.index(4))
print("Repetition of 4:", numbers.count(4))

print("Length:", len(numbers))

print("Slicing:", numbers[1:4])
print("Reverse:", numbers[::-1])

print("Membership check:", 3 in numbers, 10 in numbers)

print("Looping:")
for n in numbers:
    print(n, end=" ")
print()

print("Loop with index:")
for i, n in enumerate(numbers):
    print(i, n)

a, b, c, d, e = numbers
print("Unpacking:", a, b, c, d, e)

t1 = (10, 20)
t2 = (30, 40)
print("Concatenation:", t1 + t2)
print("Repetition:", t1 * 2)

nested = ((1, 2), (3, 4))
print("Nested access:", nested[1][0])

lst = list(numbers)
lst.append(99)
numbers = tuple(lst)
print("Converted back to tuple:", numbers)


#Covering All
numbers = (1, 2, 3, 4, 4)

print("Tuple:", numbers)

print("Access by index:", numbers[0], numbers[-1])

print("Index of 4:", numbers.index(4))
print("Repetition of 4:", numbers.count(4))

print("Length:", len(numbers))

print("Slicing:", numbers[1:4])
print("Reverse:", numbers[::-1])

print("Membership check:", 3 in numbers, 10 in numbers)

print("Looping:")
for n in numbers:
    print(n, end=" ")
print()

numbers = (1, 2, 3, 4, 4)
print("Loop with index:")
for i, n in enumerate(numbers):
    print(i, n)

#Unpacking 
print("Unpacking ".center(40,"="))

coordinates=(1,2,3)

print("coordinates[1]*[2]*[3]=",coordinates[0]*coordinates[1]*coordinates[2])

x,y,z =coordinates

print("x,y,z =coordinates")
print(x)
print(y)
print(z)

print("x*y*z= ",x*y*z)