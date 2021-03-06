#47. Write a Python program to insert an element before each element of a list.
#def fun(item1, n):
#    result = []
#    for x in item1:
#        result.append(n)
#        result.append(x)

#    return result


# New task:
# pick 1 element from a list based on his location and inser it before each other element of a list.
def fun (item1):
    userInput= input("Choose one element by his location from 0 to {}: " .format(len(item1)-1))
    result = []
    #item1 = list(item1)
    for x in range(0, len(item1)):
        result.append(item1[int(userInput)])
        result.append(item1[x])
    return result


if __name__ == "__main__":
    # These "asserts" are used for self-checking and not for testing
 #   assert fun([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 1) == [1,1,1, 2,1, 3,1, 4,1, 5,1, 6,1, 7,1, 8,1, 9,1, 10]
 #   assert fun([1, 2, 3,10], 31) == [31,1,31, 2,31, 3,31,10]
    assert fun([1, 2, 3, 10, 31]) == [31, 1, 31, 2, 31, 3, 31, 10, 31, 31]

    print('Testing completed!')