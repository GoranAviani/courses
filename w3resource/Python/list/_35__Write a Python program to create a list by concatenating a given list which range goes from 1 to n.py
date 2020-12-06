# 35. Write a Python program to create a list by concatenating a given list which range goes from 1 to n


def fun(item1, n):
    result = []
    for x in range(1, n + 1):
        for y in item1:
            result.append(str(y) + str(x))

    return result


if __name__ == "__main__":
    #  These "asserts" are used for self-checking and not for testing
    assert fun(['p', 'q'], 3) == ['p1', 'q1', 'p2', 'q2', 'p3', 'q3']

    print('Testing completed!')