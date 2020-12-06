# 17. Write a Python program to generate and print a list except for the first 5 elements, where the values are square of numbers between 1 and 30 (both included)

def fun():
    result = []
    for x in range(1, 30):
        result.append(x * x)
    return result[5:]


if __name__ == "__main__":
    # These "asserts" are used for self-checking and not for testing
    assert fun() == (
    [36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400, 441, 484, 529, 576, 625, 676, 729, 784,
     841])

    print('Testing completed!')