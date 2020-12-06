# 16. Write a Python program to generate and print a list of first and last 5 elements where the values are square of numbers between 1 and 30 (both included)


def fun():
    result = []
    for x in range(1, 30):
        result.append(x * x)
    return result[:5], result[-5:]


if __name__ == "__main__":
    # These "asserts" are used for self-checking and not for testing
    assert fun() == ([1, 4, 9, 16, 25], [625, 676, 729, 784, 841])

    print('Testing completed!')