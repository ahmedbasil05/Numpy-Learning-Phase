#Handling missing values

#.nan() --> detect missing values
import numpy as np
arr = np.array([1,2,np.nan,4,5,np.nan])
print(arr)

#.nan_to_num() --> replace nan values
arr = np.array([1,2,np.nan,4,5,np.nan])
clean = np.nan_to_num(arr)
print(clean)

#np.isinf() --> check for infinity
arr = np.array([1,2,np.inf,4,5,np.inf])
print(arr)

#replace nan values
clean = np.nan_to_num(arr, posinf=100, neginf=-100)

