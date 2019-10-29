#3. Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string.
# If the string length is less than 2, return instead of the empty string.


def fun(word):
    if len(word) > 1:
        return word[:2]+word[-2:]
    else:
        return ""

if __name__ == '__main__':
    # These "asserts" are used for self-checking and not for testing
    assert fun('goran') == "goan"
    assert fun('mama') == "mama"
    assert fun('a') == ""
    assert fun('sweden is the') == "swhe"
    print('Testing completed!')