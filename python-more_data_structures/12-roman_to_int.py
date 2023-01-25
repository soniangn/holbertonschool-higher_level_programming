#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None:
        return 0
    if not isinstance(roman_string, str):
        return 0

    number = list(roman_string)
    res = 0

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

    idx = 0

    if len(number) > 1:
        for i in number:
            if i != number[len(number)-1]:
                if number[idx] == 'I' and number[idx + 1] == 'V':
                    number[idx:idx + 2] = [''.join(number[idx:idx + 2])]
                elif number[idx] == 'I' and number[idx + 1] == 'X':
                    number[idx:idx + 2] = [''.join(number[idx:idx + 2])]
                elif number[idx] == 'X' and number[idx + 1] == 'C':
                    number[idx:idx + 2] = [''.join(number[idx:idx + 2])]
                else:
                    idx += 1

    for key, value in roman_dict.items():
        for i in number:
            if i == key:
                res += value
    return res
