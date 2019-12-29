#57. Write a Python program to check if all items of a list is equal to a given string.


def fun(item1, item2):

    for x in item1:
        if x != item2:
           return False
    return True

if __name__ == "__main__":
    # These "asserts" are used for self-checking and not for testing
    assert fun(['1', '2', '3', '1', '1'], "1") == False
    assert fun(['1', '1', '1', '1'], "1") == True

    print('Testing completed!')