#31. Write a Python program to print the following floating numbers upto 2 decimal places with a sign.


def fun(num):
    result = ("{:.2f}".format(num))
    if result[len(result) - 3:len(result)] == ".00":
        result = result[:len(result) - 3]

    #Only add + when needed, - comes as a part of parameter
    #if float(result) > 0:
    #    result = "+" + str(result)

    print(result)
    #Another way, for fun:
    # assuming there is - when needed if there is no + it needs to be placed.
    if result[0:1] != "+" and result[0:1] != "-":
        result = "+" + result

    return result

if __name__ == "__main__":
    # These "asserts" are used for self-checking and not for testing
    assert fun(3.1415926) == "+3.14"
    assert fun(-12.9999) == "-13"

    print('Testing completed!')