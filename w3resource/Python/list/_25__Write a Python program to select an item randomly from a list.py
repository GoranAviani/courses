# 25. Write a Python program to select an item randomly from a list

import random


def fun(item1):
    return random.randrange(0, len(item1))


if __name__ == "__main__":
    # These "asserts" are used for self-checking and not for testing
    result = fun([2, 4, 3, 1, 5, 6])
    print(result)

    print('Testing completed!')