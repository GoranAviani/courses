#11. Write a Python program to check the sum of three elements
# (each from an array) from three arrays is equal to a target value.
# Print all those three-element combinations

def fun(item1, item2):
    result = []
    sums = 0

    for x in item1:
        for num in x:
            sums += num
        if sums == item2:
            result.append(x)
        sums = 0

    return result


if __name__ == "__main__":
    # These "asserts" are used for self-checking and not for testing
    assert fun([[10, 20, 20, 20], [10, 20, 30, 40], [10, 30, 40, 20]], 70) == [[10, 20, 20, 20]]
    print('Testing completed!')