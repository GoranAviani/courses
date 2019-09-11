#12. Write a Python function that checks whether a passed string is palindrome or not





def fun(sentence):
    result = ""
    # 1 way
    return sentence == sentence[::-1]

   

if __name__ == '__main__':

    # These "asserts" are used for self-checking and not for testing
    assert fun('goran') == False
    assert fun('tenet') == True
    print('Testing completed!')