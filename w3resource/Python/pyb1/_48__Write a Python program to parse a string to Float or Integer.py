#48. Write a Python program to parse a string to Float or Integer.


def fun(x):

    #return float(x)
    return int(float(x))
if __name__ == "__main__":
    # These "asserts" are used for self-checking and not for testing
    fun("3122.222") == 3122
    print('Testing completed!')