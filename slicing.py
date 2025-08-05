#Slicing - extracting subset of data

# [start:end] - start to end-1 (index number)
#[0:4] --> 4-1

import numpy as np
arr = np.array([10,20,30,40,50,60])
print(arr[1:5])
print(arr[:4])  #index 0 to 3
print(arr[::2])  #every second element
print(arr[::-1])  #reverse order

#Boolean masking - Filtering

print(arr[arr > 25])
