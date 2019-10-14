#19. Write a Python program to get the last part of a string before a specified character.

def fun(character, words):

    result = []
    wordsList = []
    for z in words:
        wordsList.append(z)

    for x in range(len(words)-1, 0, -1):
        if wordsList[x] == character:
            break
        else:
            result.append(wordsList[x])

    #TODO reverse the wordsList and make it a string

    #return result



if __name__ == '__main__':
    # These "asserts" are used for self-checking and not for testing
    assert fun("-", "Po-sumama-i-gorama") == "gorama"

    print('Testing completed!')