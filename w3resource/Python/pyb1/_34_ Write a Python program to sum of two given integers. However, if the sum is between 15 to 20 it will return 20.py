# _34_ Write a Python program to sum of two given integers.
# However, if the sum is between 15 to 20 it will return 20

def summa(x, y):
    """
    Goal: Function takes two integer parameters and returns 20 in the their sum is between
    15 and 20 or sum number for any other value.
    Story: Same as goal.

    :param x: int number
    :param y: int number
    :return: integer 20 or integer sum of x and y
    """
    return 20 if (((x + y) > 14) and ((x + y) < 21)) else x + y


def main():
    assert summa(11, 6) == 20
    assert summa(3, 2) == 5
    assert summa(10, 5) == 20
    assert summa(6, 5) == 11
    print("Coding complete!")


if __name__ == '__main__':
    main()
