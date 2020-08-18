# fruit = "mango"

# for i in fruit:
#     print(i)

# fruit = input("enter fruit: ")
# for i in fruit:
#     print(i)

# range(5) ====> 0,1,2,3,4
# range(10) ===> 0,1,2,3,4,5,6,7,8,9

# range(4, 15) ===> 4,5,6,7,8,9,10,11,12,13,14
# range(10, 30, 2) ===> 10,12,14,16,18,20,22,24,26,28

# for i in range(5):
#     print(i, end=",")

# for i in range(4, 15):
#     print(i, end=",")

# for i in range(10, 30, 2):
#     print(i, end=", ")

# num = int(input("Enter a number: "))
# sum = 0
# for i in range(1, num+1):
#     sum += i
# print(sum)


# num = int(input("Enter a number: "))
# sum = 0
# for i in range(1, num+1):
#     if i%3 !=0:
#         # print(i)
#         sum += i
# print(sum)


# num = int(input("Enter a number: "))
# sum = 0
# for i in range(1, num+1):
#     if not i%3 ==0:
#         # print(i)
#         sum += i
# print(sum)

# num = int(input("Enter a number: "))
# sum = 0
# for i in range(1, num+1):
#     if i%3 ==0:
#         pass
#     else:
#         sum += i
# print(sum)

for i in range(15, 30):
    print(i)
    if i%7 ==0:
        print("bye")
        break