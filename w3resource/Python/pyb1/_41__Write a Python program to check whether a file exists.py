#41. Write a Python program to check whether a file exists

def fun(item1):
    import os.path
    isFound = os.path.isfile(item1)
    return isFound

if __name__ == "__main__":
    # These "asserts" are used for self-checking and not for testing
    assert fun("_38__Write a Python program to solve (x + y) * (x + y).py") == True
    assert fun("111test.py") == False

    print('Testing completed!')