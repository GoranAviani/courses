#41. Write a Python program to check whether a file exists
import os.path

def check_file(filename):
    isFound = os.path.isfile(filename)
    return isFound

if __name__ == "__main__":
    # These "asserts" are used for self-checking and not for testing
    assert check_file("_38__Write a Python program to solve (x + y) * (x + y).py") == True
    assert check_file("111test.py") == False

    print('Testing completed!')