# 27. Write a Python program to find the second smallest number in a list.

def fun(item1):
    secondSmallest = 0
    if item1[0] == min(item1):
        smallest = item1[1]
    else:
        smallest = item1[0]
    for x in item1:
        if x < smallest:
            secondSmallest = smallest
            smallest = x
        elif (x > smallest) and x < secondSmallest:
            secondSmallest = x

    return secondSmallest


if __name__ == "__main__":
    #  These "asserts" are used for self-checking and not for testing
    assert fun([1, 2, 3, 0, 4]) == 1
    assert fun([1, 5, 3, 2, 4]) == 2
    assert fun([1, 5, 3, 2, 4]) == 2

    print('Testing completed!')