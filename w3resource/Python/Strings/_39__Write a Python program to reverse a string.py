#39. Write a Python program to reverse a string.


def fun(text):
    text1 = list(text)
    result = ""
    for x in range(0, len(text)):
        result += text1.pop()
    return result

if __name__ == "__main__":
    # These "asserts" are used for self-checking and not for testing
    assert fun("kuca") == "acuk"
    assert fun("kuca je velika") == "akilev ej acuk"

    print('Testing completed!')