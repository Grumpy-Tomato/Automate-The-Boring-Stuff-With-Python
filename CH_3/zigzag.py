import time, sys
indent = 0 # how many space to indent.
indentIncreasing = True # whether the indentation is increasing or not

try:
    while True: # the main program loop
        print(' ' * indent, end='')
        print('********')
        time.sleep(0.1) # pause for 1/10 of a second

        if indentIncreasing:
            # increase the number of spaces
            indent = indent + 1
            if indent == 50:
                # change direction:
                indentIncreasing = False
        else:
            # decrease the number of spaces:
            indent = indent - 1
            if indent == 0:
                #change direction:
                indentIncreasing = True
    
except KeyboardInterrupt:
    sys.exit()