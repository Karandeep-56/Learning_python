import numpy as np
import pandas as pd
from numpy.random import exponential

from Exercises import square, squares, fruits

#creating Arrays
a = np.array([1,2,3])
print(a)

b = np.array([[1,2],[3,4]])
print("print 2D", b)

#printing Array Properties
print("print shape", a.shape)
print("print dimension", a.ndim)
print("print size", a.size)
print("print elements", a.dtype)

#special arrays
print("numpy zeros", np.zeros([2,2]))
print("numpy ones", np.ones([3,3]))
print("numpy full", np.full([3,4],5))
print("np.arrange", np.arange(1,10,2))
print("np.linspace", np.linspace(1,10, num = 5))
print("np.eye", np.eye(3))

#flattening and reshaping
arr = np.arange(1,7)
reshaped = arr.reshape(3,2)
print("r",reshaped)
print("reshaped flattened:\n", reshaped.flatten())

#np.matrix
matrix = np.array([[10,20,30],[40,50,60]])
print("matrix:\n", matrix[0,1])
print("submatrix", matrix[0:1,1:2])

#element wise operations
x = np.array([1,2,3,4])
y = np.array([4,5,6,7])
print("x+y", x+y)
print("x*y:\n", x*y)
print("squareroot:\n", np.sqrt(x))
print("y square\n", np.square(y))
print("exponential:\n", np.exp(x))
print("log:\n", np.log(x))

#matrix multiplication
m1 = np.array([[1,2],[4,5]])
m2 = np.array([[4,3],[2,5]])
product = np.dot(m1,m2)
print("multiply:\n", product)

#aggregate functions
stats = np.array([[1,2,3],[4,5,6]])
print("sum:\n", stats.sum())
print("mean:\n",stats.mean())
print("std:\n", stats.std())
print("min:\n", stats.min())
print("max:\n", stats.max())
print("column wise sum:\n", stats.sum(axis = 0))

#boolean filtering
data = np.array([10,20,30,35,45,34,46,67])
mask = data>30
less = data<=30
print("data greater than 30:\n", data[mask])
print("data less than 30:\n", data[less])

#random numbers
numbering = np.array([6,7,8,9])
print("random number(0,1):\n", np.random.rand(2,3))
print("random numbers:\n", np.random.randn(3))
print("random numbers:\n", np.random.randint(1,10,5))


#unique, sort and cliping
print("unique:\n", np.unique([1,2,2,2,3,3,4,4,5,5]))
print("sorted:\n", np.sort([5,3,1,2,4]))
print("cliped:\n", np.clip([1,5,10],0,8))











































