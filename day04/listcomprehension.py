# # = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# # arr = []
# # for i in range(1, 10):
# #     arr.append(i)
# #     print(arr)

# # print(arr)


# # List Comprehension

# # arr = [x for x in range(1, 10)]
# # print(arr)


# # evens = [[x, b, c] for x in range(2, 21) b for b in range(2, 21) c for c in range(2, 21) ]
# # print(evens)

# print ([[a,b,c] for a in range(0,2+1) for b in range(0,2+1) for c in range(0,3+1) if a + b + c != 3 ])



x = int(input())
y = int(input())
z = int(input())
n = int(input())

# ans = []
# for i in range(0, x+1):
#     for j in range(0, y+1):
#         for k in range(0, z+1):
#             if i+j+k != n:
#                 ans.append([i, j, k])
# print(ans)

print([[i, j, k] for i in range(0, x+1) for j in range(0, y+1) for k in range(0, z+1) if i+j+k !=n ])