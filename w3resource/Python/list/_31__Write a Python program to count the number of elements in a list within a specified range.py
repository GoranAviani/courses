# 31. Write a Python program to count the number of elements in a list within a specified range.

def fun(item1, minNum, maxNum):
    result = {}

    for x in item1:
        if x > minNum and x < maxNum:
            if x not in result:
                result[x] = 1
            else:
                result[x] += 1

    return result


if __name__ == "__main__":
    #  These "asserts" are used for self-checking and not for testing
    assert fun([1, 2, 2, 3, 1, 0, 4], 2, 4) == {3: 1}
    assert fun([1, 2, 2, 3, 1, 0, 4, 4, 5, 1, 2, 3], 1, 5) == {2: 3, 3: 2, 4: 2}

    print('Testing completed!')