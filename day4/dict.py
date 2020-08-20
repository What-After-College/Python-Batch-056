# user1 = ['mjontop', 100, 'offline']


# user2 = ['ronaldo', 'offilne' , 5000]
# print(user1[2])
# print(user2[2])


user1 = { 
    'username':'mjontop',
    'status': 'online', 
    'followers': '100'
 }

#  user2 = {}


user2 ={
    #key :     value
    'followers': 5000,
    'status': 'online',
    'username': 'ronaldo'

}

# print(user1['username'])
# print(user2['username'])

# user1['following'] = 50
# del user1['status']

# print(user1)
# print(user2)


user2.update({'status':'offline'})

# for value in user1.values():
#     print(value)

# print(user2)
# user2.clear()
# print(user2)


def checkODD():
    print(__name__)


print(__name__)

checkODD()