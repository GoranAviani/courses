# 42. Write a Python program to find missing and additional values in two lists.
# Sample data : Missing values in second list: b,a,c
# Additional values in second list: g,h

def fun(item1, item2):
    missing = []
    additional = []
    for x in item1:
        if x not in item2:
            missing.append(x)
    for y in item2:
        if y not in item1:
            additional.append(y)

    return (missing, additional)


if __name__ == "__main__":
    #  These "asserts" are used for self-checking and not for testing
    list1 = ['a', 'b', 'c', 'd', 'e', 'f']
    list2 = ['d', 'e', 'f', 'g', 'h']
    assert fun(list1, list2) == (['a', 'b', 'c'], ["g", "h"])

    print('Testing completed!')