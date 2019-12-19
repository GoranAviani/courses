#50. Write a Python program to sort a list of nested dictionaries.



def fun (item1):
    item1.sort(key=lambda e: e['key']['subkey'], reverse=True)
    return item1


if __name__ == "__main__":
    # These "asserts" are used for self-checking and not for testing
    assert fun([{'key': {'subkey': 1}}, {'key': {'subkey': 10}}, {'key': {'subkey': 5}}]) == [{'key': {'subkey': 10}}, {'key': {'subkey': 5}}, {'key': {'subkey': 1}}]


    print('Testing completed!')