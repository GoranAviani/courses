#6. Write a Python program to add 'ing' at the end of a given
# string (length should be at least 3). If the given string already
# ends with 'ing' then add 'ly' instead.
# If the string length of the given string is less than 3, leave it unchanged.

def fun(word):
    if len(word) < 4:
        return word

    if (word[(len(word)-3):len(word)] == "ing"):
        return word[:(len(word)-3)] + "ly"
    else:
       return word + "ing"


if __name__ == '__main__':
    # These "asserts" are used for self-checking and not for testing
    assert fun('aaa') == "aaa"
    assert fun('rnk split') == "rnk spliting"
    assert fun('aaaing') == "aaaly"

    print('Testing completed!')