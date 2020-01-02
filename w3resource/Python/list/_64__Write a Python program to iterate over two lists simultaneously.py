#64. Write a Python program to iterate over two lists simultaneously.

# assuming both lists have the same size

def fun (item1, item2):
    result = []
    for x in range(0, len(item1)):
        result.append(item1[x]+item2[x])

    return result
if __name__ == "__main__":
    # These "asserts" are used for self-checking and not for testing
    assert fun(["1","2","3","4"], ["a","b","c","d"]) == ['1a', '2b', '3c', '4d']

    print('Testing completed!')