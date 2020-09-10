"""
 Check if a given string has all symbols in upper case.
 If the string is empty or doesn't have any letter in it - function should return False.

Input: A string.

Output: a boolean.

Example:
is_all_upper('ALL UPPER') == True
is_all_upper('all lower') == False
is_all_upper('mixed UPPER and lower') == False
is_all_upper('') == False
"""
"""
import re
def check_for_letter_number(text:str):
    has_letter_number = re.search('[a-zA-Z]', text)
    if not has_letter_number:
        return False
    return True

def is_all_upper(text: str) -> bool:
    if not text:
        return False

    has_letter_number = check_for_letter_number(text)
    if not has_letter_number:
        return False

    for letter in text:
        if letter.isupper() or letter in [' ', ',', '-'] or letter.isdigit():
            pass
        else:
            return False

    return True
"""

import re
def check_for_letter_number(text:str):
    has_letter_number = re.search('[a-zA-Z]', text)
    if not has_letter_number:
        return False
    return True

def is_all_upper(text: str) -> bool:
    has_letter_number = check_for_letter_number(text)
    if not has_letter_number:
        return False

    for letter in text:
        if letter == letter.upper() or letter in [' ', ',', '-']:
           pass
        else:
            return False
    return True

if __name__ == '__main__':


    # These "asserts" are used for self-checking and not for an auto-testing
    assert is_all_upper('ALL UPPER') == True
    assert is_all_upper('all lower') == False
    assert is_all_upper('mixed UPPER and lower') == False
    assert is_all_upper('   ') == False
    assert is_all_upper('') == False
    assert is_all_upper('DIGITS123') == True
    assert is_all_upper('123') == False
    print("Coding complete? Click 'Check' to earn cool rewards!")