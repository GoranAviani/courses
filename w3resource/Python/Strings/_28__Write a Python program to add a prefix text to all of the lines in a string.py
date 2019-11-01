#28. Write a Python program to add a prefix text to all of the lines in a string.



def fun (text, prefix):
    addNewPrefix = True # we need to add a prefix on the start
    result = []
    text = text.split()

    for x in text:
        if addNewPrefix == True:
            result.append(prefix + " " + x)
            addNewPrefix = False
        else:
            #TODO
            if x == '\n':
                addNewPrefix = True
            else:
                result.append(x + " ")


    result = "".join(result)
    return result






if __name__ == '__main__':
    # These "asserts" are used for self-checking and not for testing
    assert fun("sumama i gorama.\nsumama i gorama.\nsumama i gorama.", "po ") == "po sumama i gorama.\npo sumama i gorama.\npo sumama i gorama."

    print('Testing completed!')