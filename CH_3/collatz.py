import sys # import the system module

def collatz(number): # define collatz function
    if number % 2 == 0: # if the number is even
        return number // 2 # divide the number by 2 and return it
    elif number % 2 == 1: # if the number is odd
        return 3 * number + 1 # multiply the number by 3 and add one, then return it

print("Choose an integer: ") # tell the user to enter an integer

while True: # main loop
    try:
        userNumber = int(input()) # put user input into a variable called userNumber
        while userNumber != 1: # while the user number is not equal to 1, keep running the loop running
            userNumber = collatz(userNumber) # make userNumber equal to the return value of collatz
            print(userNumber)
        sys.exit() # once the function returns 1, exit the program
    except ValueError: # handle exception for if user inputs a value that doesn't convert to an integer
        print("You must enter an integer, try again:") # tell the user to try again with an integer instead
    except KeyboardInterrupt: # handle exception for if the user hits control-c
        sys.exit() # exit the program