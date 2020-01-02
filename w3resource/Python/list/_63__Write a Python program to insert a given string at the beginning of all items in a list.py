#63. Write a Python program to insert a given string at the beginning of all items in a list.
#Sample list : [1,2,3,4], string : emp
#Expected output : ['emp1', 'emp2', 'emp3', 'emp4']

def fun (item1, item2):
    result = []
    for x in item1:
        result.append(x+item2)

    return result
if __name__ == "__main__":
    # These "asserts" are used for self-checking and not for testing
    assert fun([1,2,3,4], "emp") == ['emp1', 'emp2', 'emp3', 'emp4']

    print('Testing completed!')