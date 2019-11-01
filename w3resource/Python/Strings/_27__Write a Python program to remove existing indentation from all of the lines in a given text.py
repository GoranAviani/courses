#27. Write a Python program to remove existing indentation from all of the lines in a given text.

def fun(text):
    text = list(text)
    result = []
    counter = 0
    if text[0] == ' ':
        cleanStart = True
    else:
        cleanStart = False



    for x in text:

        # Taking care that all empty spaces in the start get removed
        if cleanStart == True:
            if x == '\n':
                result.append(x)
                cleanStart = False
                continue
            elif x == ' ':
                pass
            else:
                result.append(x)
                cleanStart = False

        else:
            if x == '\n':
                result.append(x)
                cleanStart = True
            else:
                result.append(x)


    result = ("").join(result)

    return result





if __name__ == '__main__':
    # These "asserts" are used for self-checking and not for testing
    assert fun("    po sumama i gorama.\n  po sumama i gorama.\n          po sumama i gorama.") == "po sumama i gorama.\npo sumama i gorama.\npo sumama i gorama."
    assert fun("po sumama i gorama.\n  po sumama i gorama.\n          po sumama i gorama.") == "po sumama i gorama.\npo sumama i gorama.\npo sumama i gorama."
    assert fun("   po sumama i \ngorama.\n  po sumama\n i gorama.\n   po sumama i gorama.") == "po sumama i \ngorama.\npo sumama\ni gorama.\npo sumama i gorama."

    print('Testing completed!')