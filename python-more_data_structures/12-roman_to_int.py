#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or not isinstance(roman_string, str):
        return 0

    roman_dict = {
        "I": 1,
        "IV": 4,
        "V": 5,
        "IX": 9,
        "X": 10,
        "L": 50,
        "XC": 90,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    res = 0
    for i in range(len(roman_string)):
        current = roman_dict[roman_string[i]]
        if i + 1 < len(roman_string) and roman_dict[roman_string[i + 1]] > current:
            res -= current
        else:
            res += current
    
    return res
