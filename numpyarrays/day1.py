import numpy as np 
import pip 
print("NumPy version: ",np.__version__)
print("pip version: ",pip.__version__)

arr=np.array([1,2,3,4,5])
print(arr)

arr1=np.array([10,20,30,40])
print(f'1D array: {arr1}')

arr2=np.array([[1,2,3],
               [4,5,6]])
print(f'2D array:\n {arr2}')

arr3=np.array([
    [[1,2],[3,4]],
    [[5,6],[7,8]]
])
               
print(f'3D  array: \n{arr3} ')
print(f'Shape of 3D array: {arr3.shape}')

print('\narange(range in py list)')
arr4=np.arange(1,10)
print(arr4)

print('\nZeroes Matrix')
zero_arr=np.zeros((3,2,1,4))
print(zero_arr)

print('\nOnes')
ones_arr=np.ones((3,4))
print(ones_arr)

print('\nFull')
full_arr=np.full((3,4),7)
print(full_arr)

print('\nIdentity(eye)')
arr_eye= np.eye(4)
print(arr_eye)

print('\nfloat')
arr_float=np.array([1,2,3.43], dtype=float)
print(arr_float)

arr_eye= np.eye(4)
print(arr_eye)

arr_7=np.full((3,4),7)
np.fill_diagonal(arr_7,1)
print(arr_7)

print("size pf arr7: ",arr_7.size)
print("Dimension of arr3: ",arr3.ndim)

print(f'{zero_arr.dtype}')
print(f'{arr_eye.dtype}')
print(f'{arr.dtype}')

print("\n")
print("Reshape".center(40,"="))
print("Ones Array= ",ones_arr)
reshape_ones=ones_arr.reshape(4,3)
print(f'Reshaped Ones Array: {reshape_ones}')
print('#Reshape from a*b into b*a like 4*5 into 5*4')

print("\n\n\n","Flatten".center(40,"="),    "\n#Flattens to 1D" )
print(reshape_ones.flatten())

print("\n\n","Slicing".center(40,"="))
arr=np.array([10,20,30,40])
print(arr[0])
print(arr[2])
print(arr[-1])

print(arr[1:4])

matrix=np.array([[1,2,3],
                 [4,5,6],
                 [7,8,9]])
print('5 is in 2*2 originally since its indexing in py\n',matrix[1,1])

print('1st Row: ',matrix[0])
print('2nd Row: ',matrix[1])
print('3rd Row: ',matrix[2])

print(f'3rd Column: {matrix[:,2]}')

print(matrix[0:2, 1:3])

arr_bool=np.array([2,3,5,7,8,0,13,21,45,6,89])
print("Array= ",arr_bool)
print('Array greater than 8: ',end=" ")
print(arr_bool[arr_bool>8])