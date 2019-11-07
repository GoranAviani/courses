#43. Write a Python program to print the square and cube symbol in the area of a
# rectangle and volume of a cylinder



def fun(volume, decimals):
    if decimals == 2:
        return "The area of the rectangle is {0:.{1}f}cm\u00b2".format(volume, decimals)
    elif decimals == 3:
        return "The volume of the cylinder is {0:.{1}f}cm\u00b3".format(volume, decimals)


if __name__ == "__main__":
    # These "asserts" are used for self-checking and not for testing
    assert fun(1256.66, 2) =="The area of the rectangle is 1256.66cm²"
    assert fun(1254.725, 3) == "The volume of the cylinder is 1254.725cm³"


    print('Testing completed!')