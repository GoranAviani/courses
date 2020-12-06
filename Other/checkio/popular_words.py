# In this mission your task is to determine the popularity of certain words in the text.
#At the input of your function are given 2 arguments: the text and the array of words
# the popularity of which you need to determine.
#When solving this task pay attention to the following points:
#    The words should be sought in all registers. This means that if you need to find
#    a word "one" then words like "one", "One", "oNe", "ONE" etc. will do.
#   The search words are always indicated in the lowercase.
#   If the word wasn’t found even once, it has to be returned in the dictionary with 0 (zero) value.
#Input: The text and the search words array.
#Output: The dictionary where the search words are the keys and values are the number of times
# when those words are occurring in a given text.
#Precondition:
#The input text will consists of English letters in uppercase and lowercase and whitespaces.

def cleann(y):
    #print(y.strip())
    result = y.strip()
    return result

def replace(y):
    y = y.replace("\n", " ")
    return y

def addOne(word, dict):
    if word in dict:
        # print(result[y])
        dict[word] += 1
    return dict


def popular_words(text: str, words: list) -> dict:
    # your code here

    userText = text
    listOfWords = words


    userText = userText.split(" ")
    userTextSmall = []

    for x in userText:
        userTextSmall.append(x.lower())

    result = {}
    for z in listOfWords:
        result[z] = 0

    for y in userTextSmall:
        y = cleann(y)
        y = replace(y)
        if len(y.split()) > 1:
            p = y.split()
            for n in p:
                result = addOne(n, result)

        result = addOne(y, result)


    #print(result)
    return result
if __name__ == '__main__':
#    print("Example:")
#    print(popular_words('''
#When I was One
#I had just begun
#When I was Two
#I was nearly new
#''', ['i', 'was', 'three', 'near']))

    # These "asserts" are used for self-checking and not for an auto-testing
#    assert popular_words('''
#When I was One
#I had just begun
#When I was Two
#I was nearly new
#''', ['i', 'was', 'three', 'near']) == {
#        'i': 4,
#        'was': 3,
#        'three': 0,
#        'near': 0
#    }

    #assert popular_words("\nWhen I was One\nI had just begun\nWhen I was Two\nI was nearly new\n", ["one", "two", "three"])
    assert popular_words(
'''
    When I was One
    I had just begun
    When I was Two
    I was nearly new
    ''', ["one", "two", "three"]) == {
        'one': 1,
        'two': 1,
        'three': 0
    }





    print("Coding complete? Click 'Check' to earn cool rewards!")