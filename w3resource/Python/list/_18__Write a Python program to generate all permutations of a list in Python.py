

# 18. Write a Python program to generate all permutations of a list in Python
import itertools


def fun(numbers):
    result = []
    result = list(itertools.permutations(numbers))

    return result


if __name__ == "__main__":
    # These "asserts" are used for self-checking and not for testing
    assert fun([1, 2, 3]) == [(1, 2, 3), (1, 3, 2), (2, 1, 3), (2, 3, 1), (3, 1, 2), (3, 2, 1)]

    print('Testing completed!')