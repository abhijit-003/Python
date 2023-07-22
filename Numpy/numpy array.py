#numpy array 

import numpy as np

# 1D array
arr_1d = np.array([1, 2, 3, 4, 5])

# 2D array
arr_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Initialize an array of zeros
zeros_array = np.zeros((3, 3))

# Initialize an array of ones
ones_array = np.ones((2, 4))

# Accessing elements in a 1D array
print(arr_1d[0])     # Output: 1
print(arr_1d[1:4])   # Output: [2 3 4]

# Accessing elements in a 2D array
print(arr_2d[1, 2])  # Output: 6
print(arr_2d[0:2, 1:3])  # Output: [[2 3] [5 6]]

a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

# Element-wise addition
result_add = a + b  # Output: [5 7 9]

# Element-wise subtraction
result_sub = a - b  # Output: [-3 -3 -3]

# Element-wise multiplication
result_mul = a * b  # Output: [4 10 18]

# Element-wise division
result_div = a / b  # Output: [0.25 0.4  0.5]

# Sum of all elements in an array
total_sum = np.sum(arr_1d)

# Mean of all elements in an array
mean_val = np.mean(arr_1d)

# Standard deviation of all elements in an array
std_dev = np.std(arr_1d)
