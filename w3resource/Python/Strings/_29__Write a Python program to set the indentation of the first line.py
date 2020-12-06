#29. Write a Python program to set the indentation of the first line

#Here we will assume that the user provides the size of the indentation along with the multiline text
def fun(text, indentation):
    text = text.split("\n")
    firstIndentation = False
    indent = ""
    result = []

    for x in text:
        if firstIndentation == False:
            firstIndentation = True
            for y in range(0, indentation):
                indent += " "
            row = indent + x
            result.append(row)
        else:
            result.append(x)

    result = "\n".join(result)
    print(result)
    return result

if __name__ == '__main__':
    # These "asserts" are used for self-checking and not for testing
    assert fun("kuca i auto\nsumama i gorama.\nkuca i auto", 4) == "    kuca i auto\nsumama i gorama.\nkuca i auto"
    assert fun("123\n12", 4) == "    123\n12"
    assert fun("kuca", 12) == "            kuca"

    print('Testing completed!')