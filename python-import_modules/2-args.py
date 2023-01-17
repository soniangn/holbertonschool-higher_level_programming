#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    number = len(sys.argv) - 1

    if number == 0:
        print("0 arguments.")
    elif number == 1:
        print("{} argument:".format(number))
    else:
        print("{} arguments:".format(number))

    for i in range(1, number + 1):
        print("{}: {}".format(i, sys.argv[i]))
