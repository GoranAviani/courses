#28. Write a Python program to add a prefix text to all of the lines in a string.


def fun (text, prefix):
    result = []
    text = text.split("\n")
    print(text)
    for x in text:
        result.append(prefix + " " + x)


    result = "\n".join(result)
    return result


if __name__ == '__main__':
    # These "asserts" are used for self-checking and not for testing
    assert fun("sumama i gorama.\nsumama i gorama.\nsumama i gorama.", "po") == "po sumama i gorama.\npo sumama i gorama.\npo sumama i gorama."

    print('Testing completed!')