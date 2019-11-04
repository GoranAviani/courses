#34. Write a Python program to print the following integers with '*' on the right of specified width.


def fun(num, width):

    width = width - len(str(num))

    stars = ""
    for x in range(0, width):
        stars += "*"
    return str(num)+stars

if __name__ == "__main__":
    # These "asserts" are used for self-checking and not for testing
    assert fun(1, 3) == "1**"
    assert fun(123, 6) == "123***"

    print('Testing completed!')