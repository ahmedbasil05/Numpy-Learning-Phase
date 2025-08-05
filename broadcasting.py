#Broadcasting - numpy way to perform operations on diff. arrays without using loops

import numpy as np

prices = np.array([100,200,300])
discount = 10
f_prices = prices - (prices * discount/100)

print(f_prices)

#Single value

arr = np.array([10,20,30])
new = arr * 2
print(arr)

#1D to 2D array 

ar = np.array([[10,20,30],[40,50,60]])
arr_1d = np.array(10,20,30)

print(ar + arr_1d)