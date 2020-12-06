# 28. Write a Python program to find the second largest number in a list.

def fun(item1):
    item1.sort(reverse=True)
    return item1[1]


if __name__ == "__main__":
    #  These "asserts" are used for self-checking and not for testing
    assert fun([1, 2, 3, 0, 4]) == 3
    assert fun([1, 5, 3, 2, 4]) == 4
    assert fun([1, 5, 3, 12, 4]) == 5
    assert fun([111, 5, 3, 12, 4]) == 12

    print('Testing completed!')