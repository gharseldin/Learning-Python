import numpy as np

random_array = np.random.randint(1, 101, (5, 5))
print(random_array)
print(random_array.mean())
print(random_array.std())

print("--------------------------------------")

identity_matrix = np.eye(5)
print(identity_matrix)
identity_matrix_scaled = identity_matrix + 5
print(identity_matrix_scaled)
multiplier = np.random.randint(1, 11, (5, 1))
print(multiplier)
result = np.multiply(identity_matrix_scaled, multiplier)
print(result)

print("--------------------------------------")

random_matrix_1 = np.random.randint(1, 101, (3, 3))
print(random_matrix_1)
random_matrix_2 = np.random.randint(1, 101, (3, 3))
print(random_matrix_2)
result = random_matrix_1 * random_matrix_2
print(result)

print("--------------------------------------")

long_array = np.random.randint(1, 1001, (1, 1000))
long_array_cumulative_sum = long_array.cumsum()
print(long_array_cumulative_sum[9])
print(long_array_cumulative_sum[99])
print(long_array_cumulative_sum[449])

print("--------------------------------------")

random_matrix_10_by_10 = np.random.randint(1, 101, (10, 10))
print(random_matrix_10_by_10)
minimum_value = random_matrix_10_by_10.min()
minimum_index = random_matrix_10_by_10.argmin()
maximum_value = random_matrix_10_by_10.max()
maximum_index = random_matrix_10_by_10.argmax()
print("Maximum is :", maximum_value, "and is found at index :", maximum_index)
print("Minimum is :", minimum_value, "and is found at index :", minimum_index)

print("--------------------------------------")

random_floats = np.random.uniform(0, 1, (5, 5))
maximum_index = random_floats.argmax()
print(random_floats)
row = maximum_index // 5
column = maximum_index % 5
random_floats[row, column] = 0
print(random_floats)

print("--------------------------------------")

A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
B = A[1:3, 0:2]
B[0, 0] = 100
print(B)

print("--------------------------------------")

one_dimensional_array = np.random.randint(1, 101, (1, 20))
even_mask = one_dimensional_array % 2 == 0
even_result = one_dimensional_array[even_mask]
even_numbers = np.size(even_result)
odd_numbers = 20 - even_numbers
print("Even numbers :", even_numbers)
print("Odd numbers :", odd_numbers)

print("--------------------------------------")

A = np.arange(1, 17).reshape(4, 4)
B = A[:, ::-1]
print(B)

print("--------------------------------------")

border_array = np.zeros((8, 8), np.int64)
border_array[0:1, 0:8] = 1
border_array[7:8, 0:8] = 1
border_array[0:8, 0:1] = 1
border_array[0:8, 7:8] = 1
print(border_array)
