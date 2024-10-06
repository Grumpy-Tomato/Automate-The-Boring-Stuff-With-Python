import sys
def collatz(number):
    try: 
        if number % 2 == 0:
            print(number // 2)
            return number // 2
        elif number % 2 == 1:
            print(3 * number + 1)
            return 3 * number + 1
    except:
        print('something went wrong')

print("Choose a number: ")
try:
    userNumber = int(input())
    while userNumber != 1:
        userNumber = collatz(userNumber)
except:
    print("Something went wrong")
    sys.exit()