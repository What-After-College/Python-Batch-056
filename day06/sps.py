import random


userpoints = 0
computersPoint = 0


def getComputersChoice():
    choices = ['stone', 'paper', 'scissor']
    index = random.randrange(0, len(choices))
    return choices[index]


def selectWinner(user, comp):
    global userpoints
    global computersPoint
    if user == comp:
        return
    elif user == 'stone' and comp == 'paper':
        computersPoint += 1
        return
    elif user == 'paper' and comp == 'stone':
        userpoints += 1
        return
    elif user == 'scissor' and comp == 'stone':
        computersPoint += 1
        return
    elif user == 'stone' and comp == 'scissor':
        userpoints += 1
        return
    elif user == 'paper' and comp == 'scissor':
        computersPoint += 1
        return
    elif user == 'scissor' and comp == 'paper':
        userpoints += 1
        return



while userpoints<5 and computersPoint <5:
    print()
    usersChoice = input("Enter Your Choice: ")
    usersChoice = usersChoice.lower()
    if usersChoice not in ['stone', 'paper', 'scissor']:
        print("incorrect Choice")
        break
    computersChoice = getComputersChoice()
    print("Your Choice: {}          Computers Choice: {}".format(usersChoice, computersChoice) )

    selectWinner(usersChoice, computersChoice)
    print("Your Points: {}          Computers Point: {}".format(userpoints, computersPoint) )


if userpoints>computersPoint:
    print("You Win !")
else:
    print("You loose !")