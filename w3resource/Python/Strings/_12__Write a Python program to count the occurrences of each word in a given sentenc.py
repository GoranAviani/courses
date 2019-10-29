#12. Write a Python program to count the occurrences of each word in a given sentence.

def fun(sentence):

    result ={}
    words =[]
    sentence = sentence.split(" ")
    for x in sentence:
        if x.isalpha():
            words.append(x)

    #print(words)
    for n in words:
        if n not in result:
            result[n] = 1
        else:
            result[n] += 1
    #print(result)
    return result



if __name__ == '__main__':
    # These "asserts" are used for self-checking and not for testing
    assert fun("kudddca") == {"kudddca": 1}
    assert fun('a a a b b b ') == {"a": 3, "b": 3}


    print('Testing completed!')