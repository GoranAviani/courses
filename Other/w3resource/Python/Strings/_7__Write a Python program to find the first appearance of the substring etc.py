#7. Write a Python program to find the first appearance of the substring 'not' and 'poor' from a given string,
# if 'not' follows the 'poor', replace the whole 'not'...'poor' substring with 'good'. Return the resulting string.


def fun(string):
    string = string.split(" ")
    posNot = []
    posPoor = []
    counter = 0


    for x in string:
        origString = string
        counter += 1
        if x == "not":
            posNot.append(x)

    if x == "poor":
        posPoor.append(x)

    return posNot[0], posPoor[0]

    if origString.find("not") != -1 and origString.find("poor) != -1:
    for x in range(1, len(string)):
        posiNot = find.("not")
    if postPoor == posiNot + 2:
        print("Found them")