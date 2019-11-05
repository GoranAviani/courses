#36. Write a Python program to format a number with a percentage.

def fun(number):
    number = float(number)
    number *= 100
    number = "{:.2f}".format(number)
    return number+"%"

if __name__ == "__main__":
    # These "asserts" are used for self-checking and not for testing
    assert fun("0.25") == "25.00%"
    assert fun("0.2525") == "25.25%"
    assert fun("-0.2525") == "-25.25%"

    print('Testing completed!')