# 67. Write a Python program to remove all consecutive duplicates of a given string.


def fun(text):
    #  result = ""
    #  for x in text:
    #    if x not in result:
    #      result += x
    #    else:
    #      pass
    #  return result
    result = []
    text = list(text)
    for x in text:
        if x not in result:
            result.append(x)
        else:
            pass

    result = "".join(result)
    return result


if __name__ == "__main__":
    # These "asserts" are used for self-checking and not for testing
    assert fun("aaaabeeee") == "abe"
    assert fun("aacccaabecceeceaaaf") == "acbef"

    print('Testing completed!')