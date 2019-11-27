# 12. Write a Python program to print a specified list after removing the 0th, 4th and 5th elements. Go to the editor
# Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# Expected Output : ['Green', 'White', 'Black']

def fun(text):
    removeItems = [0, 4, 5]
    result = []
    for x in range(0, len(text) - 1):
        if x in removeItems:
            pass
        else:
            result.append(text[x])

    return result


if __name__ == "__main__":
    # These "asserts" are used for self-checking and not for testing
    assert fun(['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']) == ['Green', 'White', 'Black']

    print('Testing completed!')