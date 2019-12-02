# 29. Write a Python program to get unique values from a list.

def fun(item1):
    result = []
    for x in item1:
        if x not in result:
            result.append(x)

    return result


if __name__ == "__main__":
    #  These "asserts" are used for self-checking and not for testing
    assert fun([1, 2, 2, 3, 1, 0, 4]) == [1, 2, 3, 0, 4]

    print('Testing completed!')