'''
import numpy as np
# Creating array
arr = np.array([1,2,3,4,5,6]) # 1D array
print(arr)

arr1 = np.array(85) # 0D array
print(arr1)

# check dimension
print(arr.ndim)
print(arr1.ndim)

arr2 = np.array([[1,2,3,4],[4,7,8,9]]) # 2D array
print(arr2)

# check dimension
print(arr2.ndim)

arr3 = np.array([[[1,4,5,7,7],[5,4,3,2,1],[78,85,76,56,45]]])
print(arr3)

# check dimension
print(arr3.ndim)

# number of elements in array & memory size
print(arr.size, arr.nbytes)
print(arr1.size, arr1.nbytes)
print(arr2.size, arr2.nbytes)
print(arr3.size, arr3.nbytes)


# memory size of single element
print(arr3.itemsize)

# Specific element of array
print(arr2[1,1])
print(arr2[0,0])
print(arr3[0,:])

print("@@@@@@@@@@@@@@@@@@@@@@@@@")

arr4 = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
print(arr4)
print(arr4.size)
print(arr4.ndim)
print(arr4.nbytes)
print(arr4.itemsize)
print(arr4[0:])
print(arr4[:10])
print(arr4[14])

print("##########################")
arr5 = arr4.copy()
print(arr5)

# Zero Matrix
print("Zero Matrix")
print(np.zeros((2,5)))



# How to Multiply two matrix?

import numpy as np
# create two array
a = np.array([[1,2,3],[4,5,6],[7,8,9]])
b = np.array([[3,2,1],[6,5,4],[9,8,7]])


# shape of Matrix
print(a.shape);print(b.shape)

# Matrix multiplication
print(a*b)

# Dot product of matric
print(a.dot(b))
print(np.matmul(a,b))

'''

import numpy as np
arr = np.array(['I', 'Ramkumar','I leave in Bidar'])
#print(type(arr))
#print(arr.shape)

# change all char to upper case
upper_char=np.char.upper(arr)
print(upper_char)

# convert all the char to lower case
lower_char=np.char.lower(arr)
print(lower_char)

print(np.char.capitalize(lower_char))

var1=np.char.title(arr)
print(var1)
