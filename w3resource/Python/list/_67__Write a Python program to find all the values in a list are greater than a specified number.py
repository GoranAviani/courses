# 67. Write a Python program to find all the values in a list are greater than a specified number.


def fun(**kwargs):
    try:
        item1 = kwargs["item1"]
        item2 = kwargs["item2"]
    except:
        return "Item 1 is empty."

    result = []
    for x in item1:
        if x > item2:
            result.append(x)

    return result


if __name__ == "__main__":
    # These "asserts" are used for self-checking and not for testing
    itemOne = {"item1": [1, 2, 3, 6, 7, 1, 2, 3, 9, 9]}
    itemTwo = {"item2": 5}
    assert fun(**itemOne, **itemTwo) == [6, 7, 9, 9]

    print('Testing completed!')