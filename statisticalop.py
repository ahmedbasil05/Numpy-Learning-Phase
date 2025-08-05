import numpy as np

#Statistical Operations

data = np.array([1,2,3,4,5])
print(data)

print(np.mean(data))  #mean value 
print(np.median(data))  #median value
print(np.std(data))  #standard deviation
print(np.max(data))  #maximum value
print(np.min(data))   #minimum value
print(np.percentile(data, 75))
print(np.sqrt(data))  #square root
print(np.exp(data))   #exponential
print(np.var(data))