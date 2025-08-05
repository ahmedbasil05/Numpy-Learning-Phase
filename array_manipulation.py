import numpy as np

np_array = np.random.randint(0,10,(2,3))
print(np_array)
print(np_array.shape)
print("__________")

#Transpose 
trans = np.transpose(np_array)
print(trans)
print(trans.shape)

trans2 = np_array.T  #other way to find transpose


#Reshaping an array
a = np.random.randint(0,10,(2,3))
print(a)

b = a.reshape(3,2)
print(b)


#Insert an element into an array

#  np.insert(array, index, value, axis=None
#  array - original array
#  index - where to insert
#  value - actual data
#  axis = 0 - row-wise, axis = 1 - column-wise

arr = np.array([10,20,30,40,50])
new = np.insert(arr,2, 60, axis=0)
print(arr)
print(new)

#Insert a row in 2D array at index 1
arr_2d = np.array([[1,2],[3,4]])
new_2d = np.insert(arr_2d,1,[5,6], axis=0)
print(new_2d)

#Append an element at the end

ar = np.array([10,20,30])
n = np.append(ar, 40)
print(n)

#Concatenate 2 arrays
a1 = np.array([1,2,3])
b1 = np.array([4,5,6])
new = np.concatenate(a1,b1)
print(new)

#Removing an element
x= np.array([10,20,30,40])
d = np.delete(x,40)
print(d)

#Removing a 2D array
y = np.array([1,2,3],[4,5,6])
n1 = np.delete(y, 0)
print(n1)