#!/usr/bin/python3
def roman_to_int(roman_string):
    try:
        roman_string = roman_string.upper()
    except AttributeError:
        return 0
    else:
        num = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
    res = 0
    skip = False

    end_index = len(roman_string) - 1

    for i in range(end_index, -1, -1):
        if skip:
            skip = False
            continue

        if roman_string[i] in num.keys():
            curr = num[roman_string[i]]
            next = num[roman_string[i - 1]]

            if i == 0:
                next = 1000000

            if curr > next:
                res += (curr - next)
                skip = True
            else:
                res += curr
        else:
            return 0
    return res
