#22.Write a Python program to sort a string lexicographically.

def fun(text):
    text = list(text)
    text = sorted(text)
    text = "".join(text)
    return text

if __name__ == '__main__':
    # These "asserts" are used for self-checking and not for testing
    assert fun("sumama") == "aammsu"
    assert fun("3sumama") == "3aammsu"


    print('Testing completed!')