# 2. Write a Python program to multiplies all the items in a list.
def fun(numbers):
    result = 1
    for x in numbers:
        result *= x

    return result


if __name__ == "__main__":
    # These "asserts" are used for self-checking and not for testing
    assert fun([1, 2, 3]) == 6
    assert fun([1, 2, -3]) == -6
    assert fun([12, -3]) == -36
    assert fun([2, 3, 3]) == 18

    print('Testing completed!')