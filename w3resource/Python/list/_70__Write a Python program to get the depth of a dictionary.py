# 70. Write a Python program to get the depth of a dictionary.


def fun(**kwargs):
    try:
        item1 = kwargs["item1"]
    except:
        return "Item 1 is empty."

    item1 = str(item1)
    brackets = 0
    for x in item1:
        if x == "{":
            brackets += 1

    return brackets


if __name__ == "__main__":
    # These "asserts" are used for self-checking and not for testing
    itemOne = {"item1": {'a': 1, 'b': {'c': {'d': {}}}}}
    assert fun(**itemOne) == 4

    print('Testing completed!')