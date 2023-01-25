#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dict = dict(a_dictionary)
    new_dict.update((key, a_dictionary[key] * 2)
                     for key, a_dictionary[key] in a_dictionary.items())
    return new_dict
