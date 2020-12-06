#55.Write a Python program to find the first repeated word in a given string.


def fun(text):
    allWords = text.split(" ")
    for x in allWords:
       if allWords.count(x.lower()) > 1:
           return x

if __name__ == "__main__":
    # These "asserts" are used for self-checking and not for testing
    assert fun("kuca kuca") == "kuca"
    assert fun("kuca auto kuca nebo") == "kuca"
    assert fun("auto kuca dog nebo dog nebo") == "kuca"

    print('Testing completed!')