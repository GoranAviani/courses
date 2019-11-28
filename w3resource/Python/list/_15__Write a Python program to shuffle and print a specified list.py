# 15. Write a Python program to shuffle and print a specified list.
from random import shuffle


def fun(text):
    shuffle(text)
    print(text)


if __name__ == "__main__":
    # These "asserts" are used for self-checking and not for testing
    fun([1, 2, 3, 4, 5, 6, 7, 8, 9])

    print('Testing completed!')