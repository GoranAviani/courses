# 60. Write a Python program to capitalize first and last letters of each word of a given string.

def fun(text):
    allWords = text.split(" ")
    result = []

    for x in allWords:
        fixedWord = x[:1].upper() + x[1:len(x) - 1] + x[len(x) - 1: len(x)].upper()
        result.append(fixedWord)

    result = " ".join(result)
    return result


if __name__ == "__main__":
    # These "asserts" are used for self-checking and not for testing
    assert fun("auto") == ("AutO")
    assert fun("auto kuca mama pas") == ("AutO KucA MamA PaS")
    assert fun("longwordsarecoming mama pas products") == ("LongwordsarecominG MamA PaS ProductS")

    print('Testing completed!')