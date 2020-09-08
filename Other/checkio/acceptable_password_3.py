"""
 In this mission you need to create a password verification function.

Those are the verification conditions:

    the length should be bigger than 6;
    should contain at least one digit, but cannot consist of just digits.

Input: A string.

Output: A bool.

Example:
is_acceptable_password('short') == False
is_acceptable_password('muchlonger') == False
is_acceptable_password('ashort') == False
is_acceptable_password('muchlonger5') == True
is_acceptable_password('sh5') == False
is_acceptable_password('1234567') == False
"""

def is_acceptable_password(password: str) -> bool:

    has_digit = False
    has_alpha = False
    if len(password) < 6:
        return False

    for d in password:
        if d.isdigit():
            has_digit = True
        elif d.isalpha():
            has_alpha = True

    if has_alpha == True and has_digit == True:
        return True
    else:
        return False

if __name__ == '__main__':


    # These "asserts" are used for self-checking and not for an auto-testing
    assert is_acceptable_password('short') == False
    assert is_acceptable_password('muchlonger') == False
    assert is_acceptable_password('ashort') == False
    assert is_acceptable_password('muchlonger5') == True
    assert is_acceptable_password('sh5') == False
    assert is_acceptable_password('1234567') == False
    print("Coding complete? Click 'Check' to earn cool rewards!")
