def fun(word):
    upper=0
    lower = 0

    for x in word:
        if x.isUpper():
            upper+= 1
        elif x.isLower():
           lower += 1

    return upper, lower