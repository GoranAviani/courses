# 21. Write a Python program to convert a list of characters into a string.

def fun(text):
    result = ""
    for x in text:
        result += x

    return result


if __name__ == "__main__":
    # These "asserts" are used for self-checking and not for testing
    assert fun(["a", "b", "c"]) == "abc"

    print('Testing completed!')