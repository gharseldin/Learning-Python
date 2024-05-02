import numpy as np


class Cat():
    def __init__(self, name: str):
        self.name = name


cat_array = np.array([Cat("Tom"), Cat("Lilly"), Cat("Fluffy")])
cat_names = np.array(
    ["Tom", "Lilly", "Fluffy"]
)
cat_numbers = np.array([1, 2, 3, 4, 5])

# array slicing
print(cat_numbers[0])
print(cat_numbers[0::2])
print(cat_numbers[-2:])
"""
1
[1 3 5]
[4 5]
"""

# common array attributes
new_array = np.array([[1, 2, 3, 4, 5, 6, 7, 8], [7, 6, 5, 4, 3, 2, 3, 4]])
print(new_array)
print("new_array dimension :", new_array.ndim)
print("new_array shape :", new_array.shape)
print("new_array data types: ", new_array.dtype)
print("new_array size: ", new_array.size)
"""
[[1 2 3 4 5 6 7 8]
 [7 6 5 4 3 2 3 4]]
new_array dimension : 2
new_array shape : (2, 8)
new_array data types:  int64
new_array size:  16
"""
# reshaping an array
print(new_array.reshape(4, 4))
print(new_array)
"""
[[1 2 3 4]
 [5 6 7 8]
 [7 6 5 4]
 [3 2 3 4]]
 """
reshaped_array = new_array.reshape(1, 16)
print(reshaped_array)
# [[1 2 3 4 5 6 7 8 7 6 5 4 3 2 3 4]]

# fast creation of arrays
zeros_array = np.zeros(10, dtype=np.int64)
print(zeros_array)
ones_array = np.ones(9)
print(ones_array)
# [0 0 0 0 0 0 0 0 0 0]
# [1. 1. 1. 1. 1. 1. 1. 1. 1.]

# sorting an array
reshaped_array.sort()
print(reshaped_array)
# [[1 2 2 3 3 3 4 4 4 5 5 6 6 7 7 8]]

# concatenating arrays
print(np.concatenate((ones_array, zeros_array), axis=0))
# [1. 1. 1. 1. 1. 1. 1. 1. 1. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]

# basic array operations
array_1 = np.array([1, 2])
array_2 = np.array([3, 4])
print(array_1)
print(array_2)
print(array_1 + array_2)
print(array_1 - array_2)
print(array_1 * array_2)
print(array_1 / array_2)
"""
[1 2]
[3 4]
[4 6]
[-2 -2]
[3 8]
[0.33333333 0.5       ]
"""

# basic functions we can run on numpy arrays
array_3 = np.arange(2, 50, 4)
print(array_3)
print(array_3.sum())
print(array_3.min())
print(array_3.max())
print(array_3.mean())
"""
[ 2  6 10 14 18 22 26 30 34 38 42 46]
288
2
46
24.0
"""

# broadcasting operations to all array elements
array_4 = np.array([1, 3, 5, 9])
print(array_4 * 3.14)
# [ 3.14  9.42 15.7  28.26]

# filtering a numpy array based on conditions
array_5 = np.arange(1, 21, 3)
print(array_5[array_5 > 8])
# [10 13 16 19]
print(array_5[(array_5 > 2) & (array_5 < 14)])
# [ 4  7 10 13]

# saving and loading a numpy file from and to an array
np.save("fifth_array", array_5)
array_loaded = np.load("fifth_array.npy")
print(array_loaded)
# [ 1  4  7 10 13 16 19]

# saving and loading a text cvs file from and to an array
np.savetxt("fifth_array_csv.csv", array_5)
loaded_csv = np.loadtxt("fifth_array_csv.csv")
print(loaded_csv)
# [ 1.  4.  7. 10. 13. 16. 19.]
