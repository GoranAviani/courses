#44. Write a Python program to generate groups of five consecutive numbers in a list.


def fun(item1):
    result = []
    temp = []
    counter = 0
    for x in range(1, item1+1):
        counter += 1
        if counter % 5 == 0:
            temp.append(x)
            result.append(temp)
            counter = 0
            temp = []
        else:
            temp.append(x)

    #add end temp list if it has less than 5 items
    if len(temp) > 0:
        result.append(temp)
    return(result)


if __name__ == "__main__":
    #  These "asserts" are used for self-checking and not for testing

    assert fun(10) == [[1,2,3,4,5],[6,7,8,9,10]]
    assert fun(13) == [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10],[11,12,13]]
    assert fun(3) == [[1, 2, 3]]

    print('Testing completed!')