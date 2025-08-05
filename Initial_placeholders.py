import numpy as np

#create a numpy array for zeros
x = np.zeros((3,5))
print(x)
print("_______________")

#create a numpy array for ones
y = np.ones((2,4))
print(y)
print("_______________")

#create a numpy array for particular value
z = np.full((5,4),7)  #full(shape,value)
print(z)
print("_______________")

#create an identity matrix
a = np.eye(4)
print(a)
print("_______________")

#create a numpy array for random values
b = np.random.random((3,4))
print(b)        #random values will be between 0 and 1
print("_______________")

#create a numpy array for random integer values within specific range
c = np.random.randint(10,50,(3,3))
print(c)
print("_______________")

#create a numpy array for evenly spaced values --> specifying number of values
d = np.linspace(10,40, 6)
print(d)
print("_______________")

#create a numpy array for evenly spaced values --> specifying step
e = np.arange(10,30,5)
print(e)
print("_______________")