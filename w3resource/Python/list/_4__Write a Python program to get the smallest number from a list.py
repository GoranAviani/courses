# 4. Write a Python program to get the smallest number from a list.
def fun(numbers):
    # result = numbers[0]
    # for x in numbers:
    #   if x < result:
    #     result = x

    # return result

    numbers.sort(reverse=True)
    return numbers.pop()


if __name__ == "__main__":
    # These "asserts" are used for self-checking and not for testing
    assert fun([1, 2, 3]) == 1
    assert fun([1, 2, -3]) == -3
    assert fun([12, -3]) == -3
    assert fun([2, 3, 5, 1, 14, 22, 1, 6, 7, 8, 11, 3, 4, 44, 55, 2, 1, 3, 5, 8, 7, 13, 25]) == 1

    print('Testing completed!')