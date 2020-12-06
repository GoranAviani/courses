#Question:
#Define a function which can generate a list where the values are square of numbers between 1 and 20 (both included).
# Then the function needs to print the first 5 elements in the list.
#Hints:
#Use ** operator to get power of a number.
#Use range() for loops.
#Use list.append() to add values into a list.
#Use [n1:n2] to slice a list

def first_5_square():
    resultList=[]
    for x in range(1,21):
        resultList.append(x)

    #last 5 items , reversed
    print(resultList[:len(resultList)-6:-1])
    #last 5 items
    print(resultList[len(resultList)-5:])
    # first 5 items
    print(resultList[:5:])
    # first 5 items, reversed
    print(resultList[4::-1])
    #mid 10 items
    print(resultList[5:len(resultList)-5:])
    print(resultList[len(resultList)-6:4:-1])


first_5_square()
