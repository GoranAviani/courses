# 71. Write a Python program to check if all dictionaries in a list are empty or not.


def fun(**kwargs):
    try:
        item1 = kwargs["item1"]
    except:
        return "Item 1 is empty."

    try:
        for x in item1:
            for k, v in x.items():
                print(k)
                thisKey = k
    except:
        return False

    return True


if __name__ == "__main__":
    # These "asserts" are used for self-checking and not for testing
    itemOne = {"item1": [{}, {}, {}]}
    assert fun(**itemOne) == True

    itemOne = {"item1": [{1, 2}, {}, {}]}
    assert fun(**itemOne) == False

    print('Testing completed!')