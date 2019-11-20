# 67. Write a Python program to remove all consecutive duplicates of a given string.


def fun(text):
    result = ""
    for x in text:
        if x not in result:
            result += x
        else:
            pass
    return result


if __name__ == "__main__":
    # These "asserts" are used for self-checking and not for testing
    assert fun("aaaabeeee") == "abe"
    assert fun("aacccaabecceeceaaaf") == "acbef"

    print('Testing completed!')