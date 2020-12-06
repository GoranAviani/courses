#48. Write a Python program to swap comma and dot in a string.

def fun(text):
    #result = ""
    #for x in text:
    #    if x == ",":
    #        result += "."
    #    else:
    #        result += x
    #return result
    return text.replace(",", ".")

if __name__ == "__main__":
    # These "asserts" are used for self-checking and not for testing
    assert fun("30,000,000") == "30.000.000"
    assert fun("the,quickbrown,foxjumpsoverthe,lazydog,") == "the.quickbrown.foxjumpsoverthe.lazydog."


    print('Testing completed!')