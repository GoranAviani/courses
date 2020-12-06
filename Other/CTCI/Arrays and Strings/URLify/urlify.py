#URLify: Write a method to replace all spaces in a string with '%20'. You may assume that the string
#has sufficient space at the end to hold the additional characters, and that you are given the "true"
#length of the string. (Note: If implementing in Java, please use a character array so that you can
#perform this operation in place.)

def blanks(word1, result):
    #print(result)
    for x in word1:
        if x == " ":
            result.append("%20")
            word1 = word1[1:-2]
            #print(result)
            return blanks(word1, result)

        else:
            result.append(x)
            word1 = word1[1:]
            #print(result)


    return result


def do_urlify(word1):

    word1 = list(word1)
    result = []
    result = blanks(word1, result)
    #print(result)
    return "".join(result)
print(do_urlify("test auto kuca    "))