"""
 In this mission you need to create a password verification function.

Those are the verification conditions:

    the length should be bigger than 6;
    should contain at least one digit, but it cannot consist of just digits;
    having numbers or containing just numbers does not apply to the password longer than 9.
    a string should not contain the word "password" in any case;
    should contain 3 different letters (or digits) even if it is longer than 10

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
is_acceptable_password('aaaaaa1') == False
is_acceptable_password('aaaaaabbbbb') == False
"""
BLOCKED_WORDS = ['password', 'bad_word_1']

def check_for_different_letters(password):
    all_unique_letters = []
    for letter in password:
        if letter not in all_unique_letters:
            all_unique_letters.append(letter)

    if len(all_unique_letters) > 2:
        return True

    return False




def check_for_blocked_words(password: str):
    for word in BLOCKED_WORDS:
        if word in password.lower():
            return True
    return False

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
    has_different_letters = check_for_different_letters(password)
    if not has_different_letters:
        return False


    has_blocked_word = check_for_blocked_words(password)
    if has_blocked_word:
        return False

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
    assert is_acceptable_password('aaaaaa1') == False
    assert is_acceptable_password('aaaaaabbbbb') == False
    assert is_acceptable_password('aaaaaabb1') == True
    assert is_acceptable_password('abc1') == False
    assert is_acceptable_password('abbcc12') == True
    print("Coding complete? Click 'Check' to earn cool rewards!")