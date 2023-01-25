#!/usr/bin/python3
def remove_char_at(str, n):
    new = ""
    i = 0
    for letter in str:
        if i != n:
            new += letter
        i += 1
    return new
