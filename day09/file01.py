# fileTxt = open('aboutpython.txt', 'r')

# print(fileTxt) <_io.TextIOWrapper name='aboutpython.txt' mode='w' encoding='UTF-8'>


# for file in fileTxt:
#     print(file)


file = open('students.txt', 'a')

# for i in range(91, 101):
#     file.write('this is line no. {} \n'.format(i))

file.write('\nhey i am new entry 2')
file.close()