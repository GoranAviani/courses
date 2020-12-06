# 62. Write a Python program to compute sum of digits of a given string.

def fun(text):
    allWords = text.split(" ")
    result = 0

    for x in text:
        if x.isdigit():
            result += int(x)
    return result


if __name__ == "__main__":
    # These "asserts" are used for self-checking and not for testing
    assert fun("auto 2 2") == 4
    assert fun("auto ima 4 kuca 2 mama 5 pas 1") == 12

    print('Testing completed!')