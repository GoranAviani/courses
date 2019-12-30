#61. Write a Python program to create a list of empty dictionaries

def fun(item1):
    result = []
    for x in range(0, item1):
        result.append({})
    return result


if __name__ == "__main__":
    # These "asserts" are used for self-checking and not for testing
    assert fun(2) == [{}, {}]
    assert fun(5) == [{}, {},{}, {},{}]
    assert fun(0) == []

    print('Testing completed!')