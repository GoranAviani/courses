# 14. Write a Python program to print the numbers of a specified list after removing even numbers from it.

def fun(text):
    result = []
    for x in text:
        if x % 2 == 0:
            pass
        else:
            result.append(x)

    return result


if __name__ == "__main__":
    # These "asserts" are used for self-checking and not for testing
    assert fun([1, 2, 3, 4, 5, 6, 7, 8, 9]) == [1, 3, 5, 7, 9]
    assert fun([1, 22, 3, 43, 51, 6, 71, 8, 9]) == [1, 3, 43, 51, 71, 9]

    print('Testing completed!')