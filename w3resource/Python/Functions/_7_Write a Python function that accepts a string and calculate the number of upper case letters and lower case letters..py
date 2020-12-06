def fun(word):
    upper=0
    lower = 0

    for x in word:
        if x.isupper():
            upper+= 1
        elif x.islower():
           lower += 1

    return [upper, lower]



if __name__ == '__main__':
    #print('Example:')
    #print(checkio("Hello World hello"))

    assert fun("kuca") == [0, 4]
    assert fun("To") == [1, 1]
    assert fun("StockholM") == [2, 7]


    print("Coding complete!")