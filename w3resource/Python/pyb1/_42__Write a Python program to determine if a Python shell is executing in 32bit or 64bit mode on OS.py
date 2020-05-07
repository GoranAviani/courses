#42. Write a Python program to determine if a Python shell is
# executing in 32bit or 64bit mode on OS.
import struct

def fun():
    result = struct.calcsize("P") * 8
    return result

def main():
    # These "asserts" are used for self-checking and not for testing
    assert fun() == 64

if __name__ == "__main__":
    main()


    print('Testing completed!')