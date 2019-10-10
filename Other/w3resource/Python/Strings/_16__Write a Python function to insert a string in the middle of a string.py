#16. Write a Python function to insert a string in the middle of a string.


def fun(string1, string2):
    if len(string1) % 2 != 0:
        return "Can not find middle"
    stringMid = int(len(string1)/2)

    result = string1[:stringMid] + string2 + string1[stringMid:]
    return result


if __name__ == '__main__':
    # These "asserts" are used for self-checking and not for testing
    assert fun("[[]]", "Python") == "[[Python]]"
    assert fun("[[<<>>]]", "Python") == "[[<<Python>>]]"

    print('Testing completed!')