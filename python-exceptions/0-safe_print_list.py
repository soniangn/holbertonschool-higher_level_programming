#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    numbers = 0
    try:
        for numbers in range(x):
            print("{:d}".format(my_list[numbers]), end='')
            numbers += 1
        print()
    except IndexError:
        print()
    return numbers
