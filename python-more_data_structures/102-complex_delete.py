#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if a_dictionary:
        for key, v in list(a_dictionary.items()):
            if v == value:
                del a_dictionary[key]
        return a_dictionary
