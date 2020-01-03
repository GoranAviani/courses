# _82. Write a Python program to wrap a given string into a paragraph of given width.

def fun(**kwargs):
    try:
        item1 = kwargs["item1"]
        item2 = kwargs["item2"]
    except:
        return "Item 1 or 2 are empty."

    #counter = 0
    #item1 = item1.split(" ")
    #resultList = []
    #result = ""
    #for x in item1:
    #    if (len(x) + counter <= item2):
    #        result += x + " "
    #        counter += len(x)
    #    else:
    #        resultList.append(result)
    #        result = ""
    #        counter = 0
    #        result += x + " "
    #        counter += 1
    #if counter > 0:
    #    resultList.append(result)
    #    result = ""


    #proccessedResult = ""
    #for x in resultList:
    #    proccessedResult += x + "\n"

    #return proccessedResult

    #counter = 0
    #item1 = item1.split(" ")
    #resultList = []
    #result = []
    #for x in item1:
    #    if (len(x) + counter <= item2):
    #        result.append(x)
    #        counter += len(x)
    #    else:
    #        resultList.append(" ".join(result))
    #        result = []
    #        counter = 0
    #        result.append(x)
    #        counter += 1
    #if counter > 0:
    #    resultList.append(" ".join(result))
    #joinedResult = "\n".join(resultList)
    #return joinedResult

    import textwrap
    return(textwrap.fill(item1,item2))


if __name__ == "__main__":
    # These "asserts" are used for self-checking and not for testing
    itemOne = {"item1": "The quick brown fox."}
    itemTwo = {"item2": 10}
    assert fun(**itemOne, **itemTwo) == "The quick\nbrown fox."

    print('Testing completed!')