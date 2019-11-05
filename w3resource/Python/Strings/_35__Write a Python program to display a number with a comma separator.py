#35. Write a Python program to display a number with a comma separator.



def fun (number):
    number = list(number)
    result = []
    result1 = []
    commaCounter = 0
    for x in range(len(number)-1, -1, -1):
        commaCounter += 1
        if commaCounter % 3 == 0:
            result.append(","+number[x])
        else:
            result.append(number[x])

    for y in range(len(result)-1, -1, -1):
        result1.append(result[y])
    result1 = "".join(result1)
    print(result1)
    return result1



if __name__ == "__main__":
    # These "asserts" are used for self-checking and not for testing
    assert fun("30000000") == "30,000,000"
    assert fun("1231") == "1,231"


    print('Testing completed!')
