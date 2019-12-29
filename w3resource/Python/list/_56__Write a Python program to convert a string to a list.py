#56. Write a Python program to convert a string to a list

def fun(item1):
    return item1.split(" ")

if __name__ == "__main__":
    # These "asserts" are used for self-checking and not for testing
    assert fun("1 2 3") == ['1','2','3']


    print('Testing completed!')