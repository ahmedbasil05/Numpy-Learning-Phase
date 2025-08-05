import numpy as np
from time import process_time

#Time taken by a numpy array
np_list = np.arange(1000000)  # or np.array([i for i in range(10000)])
start = process_time()
np_list += 5
end = process_time()
print(end - start)

#Checking the datatype of a numpy array
np_array = np.array([1, 2, 3, 4, 5])
print(np_array)
print(type(np_array))
