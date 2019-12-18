#48. Write a Python program to print a nested lists (each list on a new line) using the print() function.
def fun (item1):
    result = ""
    for x in item1:
        result += str(x)+"\n"

    print(result)
    return result


if __name__ == "__main__":
    # These "asserts" are used for self-checking and not for testing
    assert fun([[1, 2], [3, 10] , [31]]) == "[1, 2]\n[3, 10]\n[31]\n"

    print('Testing completed!')