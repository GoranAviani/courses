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
    for d in password:
        if d.isdigit():
            if len(password) > 6:
                return True
            else:
                return False
    return False


if __name__ == '__main__':
    print("Example:")
    print(is_acceptable_password('short'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert is_acceptable_password('short') == False
    assert is_acceptable_password('muchlonger') == False
    assert is_acceptable_password('ashort') == False
    assert is_acceptable_password('muchlonger5') == True
    assert is_acceptable_password('sh5') == False
    print("Coding complete? Click 'Check' to earn cool rewards!")


def is_acceptable_password(password: str) -> bool:
    # your code here
    return False


if __name__ == '__main__':
    print("Example:")
    print(is_acceptable_password('short'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert is_acceptable_password('short') == False
    assert is_acceptable_password('muchlonger') == False
    assert is_acceptable_password('ashort') == False
    assert is_acceptable_password('muchlonger5') == True
    assert is_acceptable_password('sh5') == False
    assert is_acceptable_password('1234567') == False
    print("Coding complete? Click 'Check' to earn cool rewards!")
