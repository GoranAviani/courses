# 71. Write a Python program to move all spaces to the front of a given string in single traversal.

def fun(text1):
    counter = 0
    spaces = ""
    result = ""
    for x in text1:
        if x == " ":
            counter += 1
        else:
            result += x

    spaces = counter * " "
    return spaces + result


if __name__ == "__main__":
    # These "asserts" are used for self-checking and not for testing
    assert fun("abc dpr") == (" abcdpr")
    assert fun(" a b c d p r") == ("      abcdpr")

    print('Testing completed!')