#42. Write a Python program to determine if a Python shell is executing in 32bit or 64bit mode on OS.

def fun():
    import struct
    result = struct.calcsize("P") * 8
    return result

if __name__ == "__main__":
    # These "asserts" are used for self-checking and not for testing
    assert fun() == 64


    print('Testing completed!')