import random

numberOfStreaks = 0

for experimentNumber in range(10000):

    CoinFlip = [] 
    for i in range(100):
        CoinFlip.append(random.randint(0,1))

    streak = 1
    for i in range(1, len(CoinFlip)):
        if CoinFlip[i] == CoinFlip[i-1]:
            streak += 1 
        else:
            streak = 1

        if streak == 6:
            numberOfStreaks += 1
            break

print('Chance of streak: %s%%' % (numberOfStreaks / 100))