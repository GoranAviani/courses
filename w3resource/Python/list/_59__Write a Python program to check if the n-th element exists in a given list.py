#59. Write a Python program to check if the n-th element exists in a given list


def fun(item1, item2):

    try:
        element = item1[item2]
        return True
    except:
        return False



if __name__ == "__main__":
    # These "asserts" are used for self-checking and not for testing
    assert fun([1, 3, 5, 7, 9, 10], 3 ) == True
    assert fun([1, 3], 3) == False

    print('Testing completed!')