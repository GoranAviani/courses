# 32. Write a Python program to check whether a list contains a sublist.


def fun(item1, item2):
    if len(item1) < len(item2):
        return False

    for x in item2:
        if x not in item1:
            return False

    return True


if __name__ == "__main__":
    #  These "asserts" are used for self-checking and not for testing
    assert fun([1, 2, 2, 3, 1, 0, 4], [1, 2, 2, 3, 1, 0, 4, 4, 5, 1, 2, 3]) == False
    assert fun([1, 2, 2, 3, 1, 0, 4], [1, 2]) == True

    print('Testing completed!')