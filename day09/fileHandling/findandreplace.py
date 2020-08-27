find = input("Enter Word: ")
rep = input("Enter New Word: ")

with open('replace.txt', 'r') as file:
    fileData = file.read()

print("replacing data after input")
var = input()
fileData = fileData.replace(find, rep)


with open('replace.txt', 'w') as file:
    print("check file")
    var = input()
    file.write(fileData)