# 6. Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples

def fun(text):
    # bubble sort
    for x in range(len(text) - 1, 0, -1):
        for y in range(x):
            if text[y][1] > text[y + 1][1]:
                temp = text[y]
                text[y] = text[y + 1]
                text[y + 1] = temp

    return text


if __name__ == "__main__":
    # These "asserts" are used for self-checking and not for testing
    assert fun([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]) == [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]

    print('Testing completed!')