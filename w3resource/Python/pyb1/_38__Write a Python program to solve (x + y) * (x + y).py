#38. Write a Python program to solve (x + y) * (x + y)
def fun(**kwargs):
    try:
        item1 = kwargs["item1"]
        item2 = kwargs["item2"]
    except:
        return "Item 1 or 2 are empty."

    return ((item1 + item2) * (item1 + item2))


if __name__ == "__main__":
    # These "asserts" are used for self-checking and not for testing
    itemOne = {"item1":  2}
    itemTwo = {"item2": 3}
    assert fun(**itemOne, **itemTwo) == 25

    print('Testing completed!')