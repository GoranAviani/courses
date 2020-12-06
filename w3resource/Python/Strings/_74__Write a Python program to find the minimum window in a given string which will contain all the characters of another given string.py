# 74. Write a Python program to find the minimum window in a given string which will contain all the characters of another given string


def fun(text1, text2):
    checking = {}
    result = ""
    startSaving = False
    endSaving = False
    counter = 0
    for x in text2:
        checking[x] = False

    for x in text1:
        alreadyChecked = False
        counter = 0
        if x in checking:
            alreadyChecked = True
            startSaving = True
            checking[x] = True
            result += x
            print(result)
            for k, v in checking.items():
                if v == True:
                    counter += 1
                if counter == len(text2):
                    print(result)
                    return result

        if (alreadyChecked == False and startSaving == True):
            result += x


if __name__ == "__main__":
    # These "asserts" are used for self-checking and not for testing
    assert fun("PRWSOERIUSFK", "OSU") == ("SOERIU")
    assert fun("thehouseisbig", "hso") == ("hehous")

    print('Testing completed!')