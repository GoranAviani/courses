# 3. Write a Python program to get the largest number from a list.
def fun(numbers):
    # biggest = 0
    # for x in numbers:
    #   if x > biggest:
    #     biggest = x

    # return biggest

    numbers.sort()
    return numbers.pop()


if __name__ == "__main__":
    # These "asserts" are used for self-checking and not for testing
    assert fun([1, 2, 3]) == 3
    assert fun([1, 2, -3]) == 2
    assert fun([12, -3]) == 12
    assert fun([2, 3, 5, 1, 14, 22, 1, 6, 7, 8, 11, 3, 4, 44, 55, 2, 1, 3, 5, 8, 7, 13, 25]) == 55

    print('Testing completed!')