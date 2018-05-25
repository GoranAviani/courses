

def checkio(text):

    result = []

    for x in text:
        if x not in result:
            if text.count(x) == 1:
                result.append(x)

    for y in result:
        for z in text:
            if z == y:
                text.remove(y)

    return text


if __name__ == "__main__":
    print(checkio([1,2,3,2,4]))