# 9. Write a Python program to clone or copy a list.


def fun(text):
    text1 = text[:]
    return text1


if __name__ == "__main__":
    # These "asserts" are used for self-checking and not for testing
    assert fun(["a", "b", "a", "c", "a", "b"]) == ["a", "b", "a", "c", "a", "b"]

    print('Testing completed!')