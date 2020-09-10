"""
 In this mission you need to create a password verification function.

Those are the verification conditions:

    the length should be bigger than 6;
    should contain at least one digit, but it cannot consist of just digits;
    having numbers or containing just numbers does not apply to the password longer than 9.
    a string should not contain the word "password" in any case.

Input: A string.

Output: A bool.

Example:
is_acceptable_password('short') == False
is_acceptable_password('short54') == True
is_acceptable_password('muchlonger') == True
is_acceptable_password('ashort') == False
is_acceptable_password('muchlonger5') == True
is_acceptable_password('sh5') == False
is_acceptable_password('1234567') == False
is_acceptable_password('12345678910') == True
is_acceptable_password('password12345') == False
is_acceptable_password('PASSWORD12345') == False
is_acceptable_password('pass1234word') == True
"""

def is_longer_than_ten(password: str):
    if len(password) >= 10:
        return True
    else:
        return False

def is_long_enough(password: str):
    if len(password) < 6:
        return False
    else:
        return True

def is_acceptable_password(password: str) -> bool:
    is_longer = is_longer_than_ten(password)
    if is_longer:
        return True


    is_long = is_long_enough(password)
    if not is_long:
        return False

    has_digit = False
    has_alpha = False
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
    assert is_acceptable_password('short54') == True
    assert is_acceptable_password('muchlonger') == True
    assert is_acceptable_password('ashort') == False
    assert is_acceptable_password('muchlonger5') == True
    assert is_acceptable_password('sh5') == False
    assert is_acceptable_password('1234567') == False
    assert is_acceptable_password('12345678910') == True
    assert is_acceptable_password('password12345') == False
    assert is_acceptable_password('PASSWORD12345') == False
    assert is_acceptable_password('pass1234word') == True
    print("Coding complete? Click 'Check' to earn cool rewards!")