#39. Write a Python program to convert a list of multiple integers into a single integer.
#Sample list: [11, 33, 50]
#Expected Output: 113350


def fun(item1):
    result = ""
    for x in item1:
        result += str(x)

    return int(result)



if __name__ == "__main__":
    #  These "asserts" are used for self-checking and not for testing
    assert fun([11, 33, 50]) == 113350


    print('Testing completed!')