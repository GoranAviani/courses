# 24. Write a Python program to append a list to the second list.

def fun(item1, item2):
    result = []
    for x in item1:
        result.append(x)
    for x in item2:
        result.append(x)

    return result


if __name__ == "__main__":
    # These "asserts" are used for self-checking and not for testing
    assert fun([2, 4, 3], [1, 5, 6]) == [2, 4, 3, 1, 5, 6]

    print('Testing completed!')