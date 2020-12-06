# 61. Write a Python program to remove duplicate characters of a given string.

def fun(text):
    result = ""

    for x in text:
        if x == " ":
            result += x
        else:
            if x in result:
                pass
            else:
                result += x
    return result


if __name__ == "__main__":
    # These "asserts" are used for self-checking and not for testing
    assert fun("auto") == ("auto")
    assert fun("auto kuca mama pas") == ("auto kc m ps")

    print('Testing completed!')