
#checkio("Hello World!") == "l"
#checkio("How do you do?") == "o"



def checkio(text):
    text = text.lower()
    text = text.replace(" ", "")
    result = {}
    letter = ""
    highest = 0

    for x in text:
        if not x.isdigit() and x.isalpha():
            if x not in result:
                result[x] = 1
            else:
                result[x] += 1

    for k, v in sorted(result.items()):
        if highest < v:
            highest = v
            letter = k

    return(letter)


if __name__ == "__main__":
    print(checkio("hellooooo world!!!000000000!-----------"))