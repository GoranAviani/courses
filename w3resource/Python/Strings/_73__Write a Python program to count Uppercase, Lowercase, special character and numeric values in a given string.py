# 73. Write a Python program to count Uppercase, Lowercase, special character and numeric values in a given string.


def fun(text):
    countUpper = 0
    countLower = 0
    countNumber = 0
    countSpecial = 0
    for x in text:
        if x.islower():
            countLower += 1
        elif x.isupper():
            countUpper += 1
        elif x.isnumeric():
            countNumber += 1
        else:
            countSpecial += 1

    return (countLower, countUpper, countNumber, countSpecial)


if __name__ == "__main__":
    # These "asserts" are used for self-checking and not for testing
    assert fun("aabcdpr") == (7, 0, 0, 0)
    assert fun("aabCdprA") == (6, 2, 0, 0)
    assert fun("a1abC2dpr2A4") == (6, 2, 4, 0)
    assert fun("a1/abC2dpr2A4") == (6, 2, 4, 1)
    assert fun("a1/abC.2d%pr¤2A$4") == (6, 2, 4, 5)

    print('Testing completed!')