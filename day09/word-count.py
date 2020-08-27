file = open('words.txt')

count = 0

for i in file:
    ls = i.split(' ')
    for alpha in ls:
        count += len(alpha)

# # print(count)

# Bad implementaion and inefficient

# for i in file:
#     for j in i:
#         if j==' ' or j=='\n':
#             count += 1


print(count)