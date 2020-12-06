# 70. Write a Python program to create a string from two given strings concatenating uncommon characters of the said strings.

def fun(text1, text2):
    result1 = ""
    result2 = ""
    for x in text1:
        if x not in text2:
            result1 += x

    for x in text2:
        if x not in text1:
            result2 += x

    return result1 + result2


if __name__ == "__main__":
    # These "asserts" are used for self-checking and not for testing
    assert fun("abcdpr", "abcdty") == ("prty")
    assert fun("abcdprlmn", "abcdtylmn") == ("prty")
    assert fun("abcdprlmn", "abcdtylmnwz") == ("prtywz")

    print('Testing completed!')