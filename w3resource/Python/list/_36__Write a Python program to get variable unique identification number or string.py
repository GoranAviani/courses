# 36. Write a Python program to get variable unique identification number or string.


def fun(item1):
    test = 1
    print(format(id(format), 'x'))
    return (format(id(item1), 'x'))


if __name__ == "__main__":
    #  These "asserts" are used for self-checking and not for testing
    result = fun('p')
    print(result)

    print('Testing completed!')