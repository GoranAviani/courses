# 83. Write a Python program to print four values decimal, octal, hexadecimal (capitalized), binary in a single line of a given integer.


def fun(**kwargs):
    try:
        item1 = kwargs["item1"]
    except:
        return "Item 1 or 2 are empty."
    return str(item1) + " " + str(oct(item1)) + " " + hex(item1) + " " + str(bin(item1))



if __name__ == "__main__":
    # These "asserts" are used for self-checking and not for testing
    itemOne = {"item1": 25}

    assert fun(**itemOne) == "25 0o31 0x19 0b11001"

    print('Testing completed!')