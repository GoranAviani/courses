#12. Write a Python function that checks whether a passed string is palindrome or not





def fun(sentence):
    result = []
    # 1 way
    #return sentence == sentence[::-1]

    # 2 way
    result = list(sentence)
    backward = []
    for x in range(1, len(result)+1):
        #print(result[-x])
        backward.append(result[-x])

    if (result == backward):
        return True
    else:
        return False


if __name__ == '__main__':

    # These "asserts" are used for self-checking and not for testing
    assert fun('goran') == False
    assert fun('tenet') == True
    print('Testing completed!')