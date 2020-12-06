# 66. Write a Python program to find the list in a list of lists whose sum of elements is the highest.
# Sample lists: [1,2,3], [4,5,6], [10,11,12], [7,8,9]
# Expected Output: [10, 11, 12]


def fun(**kwargs):
    try:
        item1 = kwargs["item1"]
    except:
        return "Item 1 is empty."

    sumOld = 0
    sumNew = 0
    result = []
    for x in item1:
        for n in x:
            sumNew += n
        if sumNew > sumOld:
            result = x
            sumOld = sumNew
        sumNew = 0
    return result


if __name__ == "__main__":
    # These "asserts" are used for self-checking and not for testing
    item = {"item1": [[1, 2, 3], [4, 5, 6], [10, 11, 12], [7, 8, 9]]}
    assert fun(**item) == [10, 11, 12]

    item = {"item1": [[1, 2, 3], [4, 5, 6], [10, -11, 12], [7, 8, 9]]}
    assert fun(**item) == [7, 8, 9]

    print('Testing completed!')