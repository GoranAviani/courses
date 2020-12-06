#32. Write a Python program to print the following floating numbers with no decimal places.


def fun(num):

    return str(round(num))

if __name__ == "__main__":
    # These "asserts" are used for self-checking and not for testing
    assert fun(3.1415926) == "3"
    assert fun(12.9999) == "13"

    print('Testing completed!')