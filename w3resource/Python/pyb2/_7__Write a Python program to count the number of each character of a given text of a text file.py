#7. Write a Python program to count the number of each character of a given text of a text file.


def fun(item1):
    item1 = list(item1)
    result = {}
    for x in item1:
        if x != " ":
            if x not in result:
                result[x] = 1
            else:
                result[x] += 1

    return result
if __name__ == "__main__":
    # These "asserts" are used for self-checking and not for testing
    assert fun("a aa a b b c a y") == {"a": 5, "b": 2, "c":1, "y": 1}
    print('Testing completed!')