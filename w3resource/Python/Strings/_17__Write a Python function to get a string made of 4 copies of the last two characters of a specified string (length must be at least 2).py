#17. Write a Python function to get a string made of 4
# copies of the last two characters of a specified string (length must be at least 2).


def fun(word):
    result =""
    lastTwo = word[len(word)-2:]
    for x in range(0,4):
        result += lastTwo
    return result

if __name__ == '__main__':
    # These "asserts" are used for self-checking and not for testing
    assert fun("Python") == "onononon"
    assert fun("stockholm") == "lmlmlmlm"


    print('Testing completed!')