#46. Write a Python program to convert a string in a list.


def fun(text):
    return text.split(" ")

if __name__ == "__main__":
    # These "asserts" are used for self-checking and not for testing
    assert fun("kuca mama auto") ==["kuca", "mama", "auto"]
    assert fun("The quick brown fox jumps over the lazy dog.") == ['The', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog.']


    print('Testing completed!')