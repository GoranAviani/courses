#64. Write a Python program to iterate over two lists simultaneously.

# assuming both lists have the same size

#def fun (item1, item2):
#    result = []
#   for x in range(0, len(item1)):
#        result.append(item1[x]+item2[x])

#    return result


#assuming lists can be but are not necessarily the same size
def fun(item1, item2):
    result = []
    if len(item1) >= len(item2):
        biggerList = item1
        smallerList = item2
    else:
        biggerList = item2
        smallerList = item1

    for x in range(0, len(biggerList)):
        # if this item exits add it to the result, but if not add just the elemenft form the bigger lsit
        try:
            exitsts = smallerList[x]  #wariable to find out if index exists
            result.append(biggerList[x] + smallerList[x])
        except:
            result.append(biggerList[x])

    return result


if __name__ == "__main__":
    # These "asserts" are used for self-checking and not for testing
    assert fun(["1","2","3","4"], ["a","b","c","d"]) == ['1a', '2b', '3c', '4d']
    assert fun(["1", "2", "3", "4"], ["a", "b", "c"]) == ['1a', '2b', '3c', '4']
    assert fun(["1", "2", "3"], ["a", "b", "c", "d"]) == ['a1', 'b2', 'c3', 'd']

    print('Testing completed!')