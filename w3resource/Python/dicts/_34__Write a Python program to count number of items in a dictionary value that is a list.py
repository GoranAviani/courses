#34. Write a Python program to count number of items in a dictionary value that is a list.



def fun(item1):
#    result = 0
#    for k, v in item1.items():
#        for x in v:
#            result += 1
#    return result

#assuming we dont know iv values are lists
#string way
#    result = 0
#    for k, v in item1.items():
#        if str(v)[0:1] == "[":
#            for x in v:
#                result += 1

#    return result

#"type" way
    result = 0
    for k, v in item1.items():
        if type(v) is list:
            for x in v:
                result += 1

    return result
if __name__ == "__main__":
    # These "asserts" are used for self-checking and not for testing
    assert fun({'Alex': ['subj1', 'subj2', 'subj3'], 'David': ['subj1', 'subj2']}) == 5
    assert fun({'Alex': ['subj1', 'subj2', 'subj3'], 'David': 1}) == 3

    print('Testing completed!')