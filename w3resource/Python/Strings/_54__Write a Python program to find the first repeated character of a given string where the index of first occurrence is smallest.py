#54. Write a Python program to find the first repeated character
# of a given string where the index of first occurrence is smallest

# extra task: show all repeated characters occurances



# first found will always have the smallest index number.
#def fun(text):
#    allChars = list(text)
##    for x in text:
#         if allChars.count(x) > 1:
#            return x

def fun (text):
    allOccurances ={}
    allChars = list(text)
    for x in range(0, len(allChars)):
        if allChars.count(allChars[x]) > 2:
             if allChars[x] not in allOccurances:
                    allOccurances[allChars[x]] = x
    return allOccurances

if __name__ == "__main__":
    # These "asserts" are used for self-checking and not for testing
    assert fun("aebcedei") == {'e': 1}
    assert fun("aebeqerewrewrecaedei") == {'e': 1, 'r': 6}
    assert fun("ebqrwrwrcadi") == {'r': 3}

    print('Testing completed!')