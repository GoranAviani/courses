def fun(word):
    result = ""
    wordList =[]
    for x in word:
        wordList.append(x)

    for x in range(0, len(wordList)):

        result += wordList.pop()

    return result


if __name__ == '__main__':
    #print('Example:')
    #print(checkio("Hello World hello"))

    assert fun("Hello") == "olleH"
    assert fun("aaan") == "naaa"

    print("Coding complete!")