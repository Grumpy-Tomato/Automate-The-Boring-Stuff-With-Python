import random

numberOfStreaks = 0

for experimentNumber in range(10000):
    # code that creates a list of 100 'heads' or 'tails values.
    listOfHeadsOrTails = []
    for i in range(100):
        randomInteger = random.randint(0, 1)
        if randomInteger == 0:
            listOfHeadsOrTails.append('heads')
        else:
            listOfHeadsOrTails.append('tails')
    # code that checks if there is a streak of 6 heads or tails in a row
    