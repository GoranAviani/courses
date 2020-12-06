#7. Write a Python program to find the first appearance
# of the substring 'not' and 'poor' from a given string,
# if 'not' follows the 'poor', replace the whole
# 'not'...'poor' substring with 'good'. Return the resulting string.


def fun(string):
    string = string.split(" ")
    posNot = []
    posPoor = []
    counter = 0

    origString = string

    for x in string:
        counter += 1
        if x == "not":
            posNot.append(counter)

        if x == "poor":
            posPoor.append(counter)
    print("{},{}" .format(posNot[0], posPoor[0]))
    return "{},{}" .format(posNot[0], posPoor[0])

#    if origString.find("not") != -1 and origString.find("poor) != -1:
#    for x in range(1, len(string)):
#        posiNot = find.("not")
#    if postPoor == posiNot + 2:
#        print("Found them")

if __name__ == '__main__':
    # These "asserts" are used for self-checking and not for testing
    assert fun('not poor is he poor') == "1,2"
    assert fun('not poor poor poor') == "1,2"
    assert fun('a a a a not poor is he poor') == "5,6"


    print('Testing completed!')