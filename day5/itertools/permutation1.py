# # import math

# from math import floor

# num = -75.8
# # print(math.sqrt(num))
# # print(math.ceil(num))  # (big or equal) and nearest
# # print(math.floor(num)) # (small or equal) and nearest

# print(floor(num)) # (small or equal) and nearest

from itertools import permutations

# pr = permutations([4,5,6])

# for i in pr:
#     print(i)


pr = permutations([1, 2, 3, 5], 2)

for i in pr:
    print(i)