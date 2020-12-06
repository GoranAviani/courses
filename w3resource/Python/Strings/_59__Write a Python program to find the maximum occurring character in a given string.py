# 59. Write a Python program to find the maximum occurring character in a given string.

def fun(text):
    allChars = list(text)
    results = {}
    for x in text:
        if x not in results:
            results[x] = 1
        else:
            results[x] += 1

    highestChar = ""
    highestNum = 0
    isFirst = False

    for k, v in results.items():
        if isFirst == False:
            highestChar = k
            highestNum = v
            isFirst = True

        else:
            if v > highestNum:
                highestChar = k
                highestNum = v

    return highestChar, str(highestNum)


if __name__ == "__main__":
    # These "asserts" are used for self-checking and not for testing
    assert fun("aebcedei") == ("e", "3")

    print('Testing completed!')