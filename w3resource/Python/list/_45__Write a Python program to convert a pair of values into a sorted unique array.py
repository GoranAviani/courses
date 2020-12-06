#45. Write a Python program to convert a pair of values into a sorted unique array.

def fun(item1):
    result =[]
    for x in item1:
        for y in x:
            if y in result:
                pass
            else:
                 result.append(y)
    return sorted(result)


if __name__ == "__main__":
    # These "asserts" are used for self-checking and not for testing
    assert fun([(1, 2), (3, 4), (1, 2), (5, 6), (7, 8), (1, 2), (3, 4), (3, 4),
 (7, 8), (9, 10)]) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print('Testing completed!')