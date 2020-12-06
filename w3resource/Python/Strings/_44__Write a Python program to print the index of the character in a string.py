#44. Write a Python program to print the index of the character in a string.

def fun(text):
    text = list(text)
    result = []
    for x in range(0, len(text)):
        result.append("Current character {} position at {}" .format(text[x], x))

    result = "\n".join(result)
    print(result)
    return result

if __name__ == "__main__":
    # These "asserts" are used for self-checking and not for testing
    assert fun("w3r") =="Current character w position at 0\nCurrent character 3 position at 1\nCurrent character r position at 2"


    print('Testing completed!')