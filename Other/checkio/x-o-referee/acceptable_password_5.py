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