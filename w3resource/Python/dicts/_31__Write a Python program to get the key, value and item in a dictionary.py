#31. Write a Python program to get the key, value and item in a dictionary.

def fun(item1):
    count = 0
    result = ""
    for k,v in item1.items():
        count += 1
        result += str(k)+str(v)+str(count)

    return result
if __name__ == "__main__":
    # These "asserts" are used for self-checking and not for testing
    assert fun({11: 10, 12: 20, 23: 30, 34: 40, 15: 50, 16: 60}) == "111011220223303344041550516606"

    print('Testing completed!')