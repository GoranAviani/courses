#53. Write a Python program to find the first repeated character in a given string.


def fun(text):
    allChars = list(text)
    for x in text:
         if allChars.count(x) > 1:
            return x


if __name__ == "__main__":
    # These "asserts" are used for self-checking and not for testing
    assert fun("aebcedei") == "e"
    assert fun("aebcaedei") == "a"

    print('Testing completed!')