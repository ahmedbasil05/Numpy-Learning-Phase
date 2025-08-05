import numpy as np

#Linear Algebra

A = np.array([(1,2),(3,4)])
B = np.array([(5,6),(7,8)])

print(np.dot(A,B))   #multiply both
print(A.T)         #Transpose of A
print(np.linalg.det(A))   #determinant
print(np.linalg.inv(A))   #inverse
print(np.linalg.eig(A))   #eigen values