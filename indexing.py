#Indexing - selecting a specific number from an array

# arr[index] - 1D array
# arr[row, column] - 2D array

import numpy as np

arr = np.array([10,20,30,40,50])
print(arr[0])
print(arr[3])
print(arr[-1])

#Fancy Indexing - selecting multiple elements at once,pass elements as a list

arr = np.array([1,2,3,4,5])
print(arr[1,3,4])