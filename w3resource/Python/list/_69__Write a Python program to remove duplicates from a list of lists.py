# 69. Write a Python program to remove duplicates from a list of lists.


def fun(**kwargs):
    try:
        item1 = kwargs["item1"]
    except:
        return "Item 1 is empty."

    result = []
    for x in item1:
        if x not in result:
            result.append(x)

    return result


if __name__ == "__main__":
    # These "asserts" are used for self-checking and not for testing
    itemOne = {"item1": [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]}
    assert fun(**itemOne) == [[10, 20], [40], [30, 56, 25], [33]]

    print('Testing completed!')