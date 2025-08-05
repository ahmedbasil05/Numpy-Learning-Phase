import numpy as np

#when we do (+,-,*,/) in np array, it is an elements wise operations

a = np.random.randint(0,10,(3,3))
b = np.random.randint(10,20,(3,3))
print(a)
print("_______________")
print(b)
print("_______________")

#Addition
print(np.add(a,b))
print("_______________")

#Subtraction
print(np.subtract(a,b))
print("_______________")

#multiplication
print(np.multiply(a,b))
print("_______________")

#division
print(np.divide(a,b))
print("_______________")