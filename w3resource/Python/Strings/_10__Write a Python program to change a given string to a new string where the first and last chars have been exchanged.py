#10. Write a Python program to change a given
# string to a new string where the first and last chars have been exchanged.



def fun(word):
    #parts separate
    #print(word[0:2])
    #print(word[2:len(word) - 2])
    #print(word[(len(word) - 2):len(word)])

    return (word[(len(word) - 2):len(word)] + word[2:len(word) - 2] + word[0:2])




if __name__ == '__main__':
    # These "asserts" are used for self-checking and not for testing
    assert fun("kudddca") == "cadddku"
    assert fun('not,poor1,poor2,poor3') == "r3t,poor1,poor2,poono"


    print('Testing completed!')