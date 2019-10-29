#20. Write a Python function to reverses a string if it's length is a multiple of 4.


def fun(text):
    result = []
    if len(text) % 4 != 0:
       return text
    else:
       result = list(text)
       result.reverse()
       return "".join(result)

if __name__ == '__main__':
    # These "asserts" are used for self-checking and not for testing
    assert fun("sumama") == "sumama"
    assert fun("sum") == "sum"
    assert fun("po-sumama-i-gorama--") == "--amarog-i-amamus-op"

    print('Testing completed!')