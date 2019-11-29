# 20. Write a Python program access the index of a list.


def fun(list1):
    counter = 0
    result = []
    for x in list1:
        result.append((counter, x))
        counter += 1
    return result


if __name__ == "__main__":
    # These "asserts" are used for self-checking and not for testing
    assert fun([1, 2, 3, 3, 5]) == [(0, 1), (1, 2), (2, 3), (3, 3), (4, 5)]

    print('Testing completed!')