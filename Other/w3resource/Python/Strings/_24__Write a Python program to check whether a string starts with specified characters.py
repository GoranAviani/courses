#24. Write a Python program to check whether a string starts with specified characters.


def fun(text, spec):
    #return message if spec is longer than text
    if len(spec) > len(text):
        return "specified charactwr are longer than text"

    if text[:len(spec)] == spec:
       return "starts with spec"
    else:
       return "doesnt start with spec"

if __name__ == '__main__':
    # These "asserts" are used for self-checking and not for testing
    assert fun("sumama", "su") == "starts with spec"
    assert fun("sum", "s") == "starts with spec"
    assert fun("po-sumama-i-gorama--", "po-sumama-i-gorama--") == "starts with spec"
    assert fun("po-sumama-i-gorama--", "kuca") == "doesnt start with spec"
    assert fun("po-sumama-i-gorama--", "po-sumq") == "doesnt start with spec"


    print('Testing completed!')