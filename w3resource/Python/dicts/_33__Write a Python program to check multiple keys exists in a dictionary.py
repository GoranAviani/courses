#33. Write a Python program to check multiple keys exists in a dictionary.


def fun(item1, item2):

    for x in item2:
        if x in item1:
            pass
        else:
            return False


    return True
if __name__ == "__main__":
    # These "asserts" are used for self-checking and not for testing
    assert fun({11: 10, 12: 20, 23: 30, 34: 40, 15: 50, 16: 60}, [11, 34]) == True
    assert fun({11: 10, 12: 20, 23: 30, 34: 40, 15: 50, 16: 60}, [111, 34]) == False
    assert fun({11: 10, 12: 20, 23: 30, 34: 40, 15: 50, 16: 60}, [11, 34, 23, 16]) == True

    print('Testing completed!')