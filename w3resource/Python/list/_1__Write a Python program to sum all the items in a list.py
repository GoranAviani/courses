# 1. Write a Python program to sum all the items in a list.
def fun(numbers):
    result = 0
    for x in numbers:
        result += x

    return result


if __name__ == "__main__":
    # These "asserts" are used for self-checking and not for testing
    assert fun([1, 2, 3]) == 6
    assert fun([1, 2, -3]) == 0
    assert fun([1, 12, -3]) == 10
    assert fun([1, -2, -3]) == -4

    print('Testing completed!')