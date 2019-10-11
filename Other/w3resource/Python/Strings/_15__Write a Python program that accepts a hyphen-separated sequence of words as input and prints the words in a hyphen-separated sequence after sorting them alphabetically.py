#15. Write a Python program that accepts a hyphen-separated sequence of
# words as input and prints the words in a hyphen-separated sequence after sorting them alphabetically.



def fun (word):

    wordList = word.split("-")


    wordList = sorted(wordList, key=str.casefold)
    result = "-".join(wordList)

    return result

if __name__ == '__main__':
    # These "asserts" are used for self-checking and not for testing
    assert fun("Po-sumama-i-gorama") == "gorama-i-Po-sumama"
    assert fun("The-date-is-tEnth-of-October") == "date-is-October-of-tEnth-The"

    print('Testing completed!')

