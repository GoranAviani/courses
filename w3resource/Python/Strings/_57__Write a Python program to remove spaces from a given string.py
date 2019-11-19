#57.Write a Python program to remove spaces from a given string.

def fun(text):
    result = ""
    for x in text:
        if text == " ":
            pass
        else:
            result += x
    return result

if __name__ == "__main__":
    # These "asserts" are used for self-checking and not for testing
    assert fun("kuca kuca auto auto auto") == "kucakucaautoautoauto"
    assert fun("  ku   ca k  uca au to     a uto a ut   o") == "kucakucaautoautoauto"

    print('Testing completed!')