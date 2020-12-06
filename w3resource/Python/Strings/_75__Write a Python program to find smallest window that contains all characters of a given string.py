# 75. Write a Python program to find smallest window that contains all characters of a given string.

def fun(text1):
    checking = {}
    result = ""
    startSaving = False
    endSaving = False
    counter = 0

    for x in text1:
        if x not in checking:
            checking[x] = False

    for x in text1:
        alreadyChecked = False
        counter = 0
        if x in checking:
            alreadyChecked = True
            startSaving = True
            checking[x] = True
            result += x

            for k, v in checking.items():
                if v == True:
                    counter += 1
                if counter == len(checking):
                    return result

        if (alreadyChecked == False and startSaving == True):
            result += x


if __name__ == "__main__":
    # These "asserts" are used for self-checking and not for testing
    assert fun("iooppooooooiiii") == ("ioop")
    assert fun("iooppoomooooiimmii") == ("iooppoom")

    print('Testing completed!')