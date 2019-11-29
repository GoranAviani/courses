# 23. Write a Python program to flatten a shallow list

def fun(items):
    result = []
    for x in items:
        for y in x:
            result.append(y)
    return result


if __name__ == "__main__":
    # These "asserts" are used for self-checking and not for testing
    assert fun([[2, 4, 3], [1, 5, 6], [9], [7, 9, 0]]) == [2, 4, 3, 1, 5, 6, 9, 7, 9, 0]

    print('Testing completed!')