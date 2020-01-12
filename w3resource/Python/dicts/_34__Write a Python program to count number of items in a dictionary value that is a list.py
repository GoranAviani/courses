#34. Write a Python program to count number of items in a dictionary value that is a list.



def fun(item1):
    result = 0
    for k, v in item1.items():
        for x in v:
            result += 1


    return result

if __name__ == "__main__":
    # These "asserts" are used for self-checking and not for testing
    assert fun({'Alex': ['subj1', 'subj2', 'subj3'], 'David': ['subj1', 'subj2']}) == 5

    print('Testing completed!')