# 63. Write a Python program to remove leading zeros from an IP address.

def fun(text):
    allWords = text.split(".")
    result = []

    for x in allWords:
        if len(x) == 1:
            result.append(x)
        else:
            if x[:1] == "0":
                result.append(x[1:len(x)])
            else:
                result.append(x)

    result = ".".join(result)
    return result


if __name__ == "__main__":
    # These "asserts" are used for self-checking and not for testing
    assert fun("255.024.01.01") == "255.24.1.1"
    assert fun("127.0.0.01") == "127.0.0.1"

    print('Testing completed!')