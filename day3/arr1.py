# student1 = 40
# student2 = 60
# student3 = 30
# student4 = 50
# student5 = 55

# print(student1)
# print(student2)
# print(student5)


#           0    1   2  3   4
students = [40, 60, 30, 50, 55]
# print(students[1])

i=0
# while i<5:
#     print(students[i])
#     i += 1
#           0,1,2,3,4
# for i in range(0, 5):
#     print(students[i])

# print(students)
# for i in range(0, 5):
#     print(students[i], end=" ")
# print()

# print(*students)  

# for i in students:
#     print(i)

# l = len(students)
# print(l)


# msg = ['This', 'is', 'a', 'message']
# msgStr = ""
# # print(msgStr)
# # print(*msg)

# for i in msg:
#     msgStr += (i+" ")

# # msgStr += "hello"
# print(msgStr)

# a = 15
# b = 45

# print(a, b)
# # swap = 0
# # swap = a
# # a = b
# # b = swap

# # 1^0 = 1
# # 1^1 = 0
# # 0^0 = 0
# # 0^1 = 1
# # a, b = b, a
# a = a^b    # ^
# b = a^b
# a = a^b



# print(a, b)

msg = ['This', 'is', 'a', 'message']
msgStr = ""

i=0
while i<len(msg):
    msgStr += (msg[i]+" ")
    i += 1

print(msgStr)