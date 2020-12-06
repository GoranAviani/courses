#58. Write a Python program to replace the last element in a list with another list.

def fun(item1, item2):
    result = []

    for x in range(0, len(item1)-1):
        result.append(item1[x])
    for x in item2:
        result.append(x)

    return result


if __name__ == "__main__":
    # These "asserts" are used for self-checking and not for testing
    assert fun([1, 3, 5, 7, 9, 10], [2, 4, 6, 8]) == [1, 3, 5, 7, 9, 2, 4, 6, 8]

    print('Testing completed!')