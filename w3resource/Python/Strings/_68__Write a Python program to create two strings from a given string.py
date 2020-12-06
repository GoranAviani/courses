# 68. Write a Python program to create two strings from a given string. Create the first string using those character which occurs only once and create the second string which consists of multi-time occurring characters in the said string

def fun(text):
    occursOnce = []
    occursMultiple = []
    for x in text:
        if x != "":
            if text.count(x) > 1:
                occursMultiple.append(x)
            else:
                occursOnce.append(x)

    return occursOnce, occursMultiple


if __name__ == "__main__":
    # These "asserts" are used for self-checking and not for testing
    assert fun("aaaabeeee") == (["b"], ["a", "a", "a", "a", "e", "e", "e", "e"])
    assert fun("stockholm") == (["s", "t", "c", "k", "h", "l", "m"], ["o", "o"],)

    print('Testing completed!')