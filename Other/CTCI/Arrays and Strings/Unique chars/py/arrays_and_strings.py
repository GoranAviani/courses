#Is Unique: Implement an algorithm to determine if a string has all unique characters. What if you
#cannot use additional data structures?
#Hints: #44, #7 7 7, #732

#def unique(word):
#    for x in word:
#        if word.count(x) > 1:
#            return False
#    return True


#without count
def unique(word):
    result = []
    for x in word:
        if x in result:
            return False
        else:
            result.append(x)

    return True




print(unique("aaabb"))
