import random
def getComputersChoice():
    choices = ['stone', 'paper', 'scissor']
    index = random.randrange(0, len(choices))
    return choices[index]


print(getComputersChoice())