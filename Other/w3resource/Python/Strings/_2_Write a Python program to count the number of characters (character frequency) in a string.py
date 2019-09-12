#2. Write a Python program to count the number of characters (character frequency) in a string.


def fun(words):

    result = {}
    words1 = list(words)
    for x in words1:
        result[x] = 0

    for x in words1:
        if x in result:
            result[x] += 1


    return result



if __name__ == '__main__':
    # These "asserts" are used for self-checking and not for testing
    assert fun('goran') == {'g': 1, 'o': 1, 'r': 1, 'a': 1, 'n': 1}
    assert fun('mama') == {'m': 2, 'a': 2}


    print('Testing completed!')