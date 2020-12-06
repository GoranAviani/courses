# 68. Write a Python program to extend a list without append. Go to the editor
# Sample data: [10, 20, 30]
# [40, 50, 60]
# Expected output : [40, 50, 60, 10, 20, 30]


def fun(**kwargs):
    try:
        item1 = kwargs["item1"]
        item2 = kwargs["item2"]
    except:
        return "Item 1 is empty."

    # return item2 + item1

    item2.extend(item1)
    return item2


if __name__ == "__main__":
    # These "asserts" are used for self-checking and not for testing
    itemOne = {"item1": [10, 20, 30]}
    itemTwo = {"item2": [40, 50, 60]}
    assert fun(**itemOne, **itemTwo) == [40, 50, 60, 10, 20, 30]

    print('Testing completed!')