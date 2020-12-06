#6. Write a Python program to print a long text, convert the string to a
# list and print all the words and their frequencies.

def fun(item1):
    item1 = item1.split(" ")
    result = {}
    for x in item1:
        if x not in result:
            result[x] = 1
        else:
            result[x] += 1

    return result
if __name__ == "__main__":
    # These "asserts" are used for self-checking and not for testing
    assert fun("a aa a b b c a y") == {"a": 3,"aa":1, "b": 2, "c":1, "y": 1}
    print('Testing completed!')