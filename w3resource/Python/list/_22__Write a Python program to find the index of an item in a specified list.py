# 22. Write a Python program to find the index of an item in a specified list.

def fun(text, item):
    result = {}
    counter = 0
    for x in text:
        result[x] = counter
        counter += 1

    for x in result:
        if item == x:
            return result[x]


if __name__ == "__main__":
    # These "asserts" are used for self-checking and not for testing
    assert fun(["a", "b", "c"], "b") == 1

    print('Testing completed!')