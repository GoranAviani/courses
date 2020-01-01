# _62__Write a Python program to print a list of space-separated elements

def fun(item1):
    result = ""
    for x in range(0, len(item1)):
        if x == len(item1) - 1:
            result += str(item1[x])
        else:
            result += str(item1[x]) + " "

    return result


if __name__ == "__main__":
    # These "asserts" are used for self-checking and not for testing
    assert fun([1, 3, 5, 7, 9, 10]) == "1 3 5 7 9 10"

    print('Testing completed!')