import numpy as np

# arr = np.full((3,3), 8)
# print(arr)

# arr = np.eye(2)
# print(arr)

# arr = np.random.random((4,4))
# print(arr)

arr = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
arr.shape = (3,4)
# print(arr) 

#    0  1   2   3
# [[ 1  2  3  4]  0
#  [ 5  6  7  8]   1    
#  [ 9 10 11 12]]   2

# print(arr[:2, :3])

# print(arr[1:, 1:])
# [[ 6  7  8]
#  [10 11 12]]


# x = np.array([[1,2],[3,4]])

# y = np.array([[5,6], [7,8]])
# print(x+y)

# print(np.add(x, y))


# x = np.array([[10, 11], [12, 13]])
# y = np.array([[16, 17], [18, 19]])

# # print(x-y)
# print(y-x)
# # print(np.subtract(y, x))


# x = np.array([[10, 12], [14, 16]])
# y = np.array([[2,2], [2,2]])

# print(x*y)


# x = np.array([[4,8], [10, 16]])
# y = np.array([[2,2], [2,2]])
# print(x/2)


x = np.array([[16, 25], [36, 49]])
print(np.sqrt(x))