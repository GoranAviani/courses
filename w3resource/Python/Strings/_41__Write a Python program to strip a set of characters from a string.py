#41. Write a Python program to strip a set of characters from a string.


def fun(text, chars):
    stripChars = list(chars)
    result = []

    text = list(text)

    for x in text:
        if x in stripChars:
            pass
        else:
            result.append(x)
    result = "".join(result)
    return result

if __name__ == "__main__":
    # These "asserts" are used for self-checking and not for testing
    assert fun("kuca mama auto","a") =="kuc mm uto"
    assert fun("kuca mama auto", "au") == "kc mm to"

    print('Testing completed!')