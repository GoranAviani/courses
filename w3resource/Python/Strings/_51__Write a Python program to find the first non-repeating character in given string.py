#51. Write a Python program to find the first non-repeating character in given string.


def fun(text):
    allChars = list(text)
    for x in text:
        if allChars.count(x) == 1:
            return x

if __name__ == "__main__":
    # These "asserts" are used for self-checking and not for testing
    assert fun("aebcedei") == "a"
    assert fun("aebcaedei") == "c"

    print('Testing completed!')