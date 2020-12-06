# 30. Write a Python program to get the frequency of the elements in a list.

def fun(item1):
    result = {}
    for x in item1:
        if x not in result:
            result[x] = 1
        else:
            result[x] += 1

    return result


if __name__ == "__main__":
    #  These "asserts" are used for self-checking and not for testing
    assert fun([1, 2, 2, 3, 1, 0, 4]) == {1: 2, 2: 2, 3: 1, 0: 1, 4: 1}
    assert fun([1, 2, 2, 3, 1, 0, 4, 4, 5, 1, 2, 3]) == {1: 3, 2: 3, 3: 2, 0: 1, 4: 2, 5: 1}

    print('Testing completed!')