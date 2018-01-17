#write a program that prints a checkerboard pattern to console
#should not require input & produce output with red * & black space
#black row should be first


for r in range(1,9):
    row = " "
    if r % 2 == 0:
        for x in range(1,9):
            if x % 2 == 0:
                row += '\033[1;31m*'
            else:
                row += ' '
    elif r % 2 == 1:
        for x in range(1,9):
            if x % 2 == 0:
                row += ' '
            else:
                row += '\033[1;31m*'
    print row



print row