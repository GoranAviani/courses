#8. Write a Python function that takes a list of words and returns the length of the longest one

#Lets assume the list of words comes as a string with comma (,) in between words.
def fun(listOfWords):
    listOfWords = listOfWords.split(",")
    length = 0
    longestWord =""
    for x in listOfWords:
        if len(x)>length:
            length = len(x)
            longestWord = x
    print(length)
    print(longestWord)
    return [length, longestWord]


if __name__ == '__main__':
    # These "asserts" are used for self-checking and not for testing
    assert fun('not,poor,is,he,poor') == [4, "poor"]
    assert fun('not,poor1,poor2,poor3') == [5, "poor1"]
    assert fun('kuca,mama,auto,mazda3') == [6, "mazda3"]


    print('Testing completed!')