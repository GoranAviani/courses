#56. Write a Python program to find the second most repeated word in a given string
import operator
def fun(text):
    allWords = text.split(" ")


    result = {}
    for x in allWords:
        if x not in result:
            result[x] = 1
        else:
            result[x] += 1


    result = sorted(result.items(), key=operator.itemgetter(1), reverse=True)
    result = result[0][0]
    return result

if __name__ == "__main__":
    # These "asserts" are used for self-checking and not for testing
    assert fun("kuca kuca auto auto auto") == "auto"

    print('Testing completed!')