#20. Write a Python program to detect the number of local variables declared in a function.


def fun():
    x = 1
    y = 2
    str1 = "w3resource"


    return(fun.__code__.co_nlocals)

if __name__ == "__main__":
    # These "asserts" are used for self-checking and not for testing
    assert fun() == 3

    print('Testing completed!')