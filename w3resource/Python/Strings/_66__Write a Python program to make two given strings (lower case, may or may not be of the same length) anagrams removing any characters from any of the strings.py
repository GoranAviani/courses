# 66. Write a Python program to make two given strings (lower case, may or may not be of the same length) anagrams removing any characters from any of the strings

def fun(text1, text2):
    if len(text1) != len(text2):
        return False
    else:
        if (sorted(text1.lower()) == sorted(text2.lower())):
            return True
        else:
            return False


if __name__ == "__main__":
    # These "asserts" are used for self-checking and not for testing
    assert fun("kuca", "acku") == True
    assert fun("cars have wheels", "arlscav hee wehs") == True
    assert fun("cart", "cars") == False

    print('Testing completed!')