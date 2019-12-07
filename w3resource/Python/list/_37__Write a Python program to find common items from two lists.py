# 37. Write a Python program to find common items from two lists.

def fun(item1, item2):
    result = []
    for x in item1:
        if x in item2:
            result.append(x)

    return result


if __name__ == "__main__":
    #  These "asserts" are used for self-checking and not for testing
    assert fun([2, 3, 5, 7], [2, 3, 1, 5, 6]) == [2, 3, 5]

    print('Testing completed!')