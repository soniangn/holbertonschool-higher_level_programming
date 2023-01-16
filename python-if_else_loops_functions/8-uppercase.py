#!/usr/bin/python3
def uppercase(str):
    for letter in str:
        letter = ord(letter)
        if letter >= 97 and letter < 123:
            letter = letter - 32
        print("{}".format(chr(letter)), end="")
    print()
