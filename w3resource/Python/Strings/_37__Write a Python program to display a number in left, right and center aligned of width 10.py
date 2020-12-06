#37. Write a Python program to display a number in left, right and center aligned of width 10.



def fun(number):
    zeroNumLeftRight = 10
    zeroNumLeftRight -= len(str(number))



    return str(number) + " "*zeroNumLeftRight


if __name__ == "__main__":
    # These "asserts" are used for self-checking and not for testing
    assert fun("22") == "22        "
    #assert fun("22") == "        22"
    #assert fun("22") == "    22    "

    print('Testing completed!')