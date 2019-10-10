#15. Write a Python program that accepts a hyphen-separated sequence of
# words as input and prints the words in a hyphen-separated sequence after sorting them alphabetically.



def fun (word):
    wordList = word.split("-")
    wordList = sorted(wordList)
    result = "-".join(wordList)

    return result

if __name__ == '__main__':
    # These "asserts" are used for self-checking and not for testing
    assert fun("po-sumama-i-gorama") == "gorama-i-po-sumama"
    assert fun("the-date-is-tenth-of-october") == "date-is-october-of-tenth-the"

    print('Testing completed!')

