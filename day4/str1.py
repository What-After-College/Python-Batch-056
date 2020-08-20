# a = 'this_is_string'
# print(a[2:])

# print(a[2:5])
# print(a[-2])


# greet = "hi"
# greet += " hello"

# print(greet)

# greet += " goodbye"

# print(greet)

# index = greet.find('l')
# print(index)

# k = list(greet)
# print(k)

# name = 'r'
# print(name.upper())

# name = 'L'
# print(name.lower())


# Que:
# input: ricky ponting
# output: Ricky Ponting

fullName = input()
sp = fullName.split(' ')
firstName = sp[0]
lastName = sp[1]
# firstName = firstName[0].upper()+firstName[1:]
# lastName = lastName[0].upper()+lastName[1:]

firstName = firstName.capitalize()
lastName = lastName.capitalize()

print(firstName+" "+lastName)