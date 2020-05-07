#48. Write a Python program to parse a string to Float or Integer.
def parste_num(x):
    return int(float(x))
if __name__ == "__main__":
    # These "asserts" are used for self-checking and not for testing
    assert parste_num("3122.222") == 3122
    print('Testing completed!')