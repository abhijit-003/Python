#numpy array attributes

import numpy as np

arr = np.eye(3,dtype=int)
print("array \n",arr)

#1 shape: gives number of element on each dimension(axies)
print("array shape: \n",arr.shape)

#2 size: shows number of element in the array
print("array size: \n",arr.size)

#3 ndim: shows dimensions of array
print("array dimensions: \n",arr.ndim)

#4 dtype: shows data type of array
print("array data type: \n",arr.dtype)

#5 nbytes: size of stored data
print("array data size: \n",arr.nbytes)