#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None

    max = -1

    for number in my_list:

        if number > max:
            max = number
        else:
            continue
    return max
