#41. Write a Python program to create multiple lists


def fun(item1):
    result = {}
    for x in range(1, item1+1):
        result[x] = []

    return result


if __name__ == "__main__":
    #  These "asserts" are used for self-checking and not for testing
    assert fun(3) == {1: [], 2: [], 3:[]}


    print('Testing completed!')