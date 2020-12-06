#38. Write a Python program to change the position of every n-th value with the (n+1)th in a list.

def fun(item1,n):
    for x in range(1,len(item1)):
        if x % n == 0:
            origNumber = item1[x]
            newNumber = item1[x+1]
            item1[x] = newNumber
            item1[x+1] = origNumber
    return item1



if __name__ == "__main__":
    #  These "asserts" are used for self-checking and not for testing
    assert fun([1, 2, 3, 4, 5], 3) == [1, 2, 3, 5, 4]
    assert fun([1, 2, 3, 4, 5, 6], 2) == [1, 2, 4, 3, 6, 5]

    print('Testing completed!')