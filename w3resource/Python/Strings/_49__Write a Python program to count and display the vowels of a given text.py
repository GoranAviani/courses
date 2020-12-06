#49. Write a Python program to count and display the vowels of a given text.


def fun(text):

    vowels ={"a": 0, "e": 0, "i": 0, "o": 0, "u": 0}

    for x in text:
        if x in vowels:
            vowels[x] +=1
    return vowels


if __name__ == "__main__":
    # These "asserts" are used for self-checking and not for testing
    assert fun("abcdei") == {"a": 1, "e": 1, "i": 1, "o": 0, "u": 0}
    assert fun("aaa kuca mama auto") == {"a": 7, "e": 0, "i": 0, "o": 1, "u": 2}
    print('Testing completed!')