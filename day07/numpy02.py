import numpy as np

# arr = np.array([[4, 10, 15], [17, 19, 23]])
# print(arr)

arr = np.array([[4, 10, 15], [17, 19, 23]])
print(arr)

print(arr.shape)
print(arr.dtype)
# arr2 = np.array([[4, 10, 15], [17, 19, 23], [45, 69, 36]])
# print("now arr2")

# print(arr2.shape)

# print(arr2.itemsize)

# arr3 = np.array([12.5, 36.2, 45.9])

# print("arr3")
# print(arr3.itemsize)

arr4 = np.array([2,6,9], dtype=complex)

# print(arr4)

arr5 = np.zeros((2, 3))
# print(arr5)

arr6 = np.ones((3,4))
# print(arr6)
arr7 = np.empty((3,4), dtype=int)
print(arr7)