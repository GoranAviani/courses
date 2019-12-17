#46. Write a Python program to select the odd items of a list.

def fun(item1):
    result =[]
    for x in item1:
        if x % 2 == 0:
            pass
        else:
            result.append(x)
    return result


if __name__ == "__main__":
    # These "asserts" are used for self-checking and not for testing
    assert fun([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [1, 3, 5, 7, 9]
    print('Testing completed!')