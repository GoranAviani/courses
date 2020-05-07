#38. Write a Python program to solve (x + y) * (x + y)
def calculation(**kwargs):
    try:
        item1 = kwargs["item1"]
        item2 = kwargs["item2"]
    except KeyError as e:
        print("Can not find value {}" .format(e))
    else:
        return ((item1 + item2) * (item1 + item2))

def main():
    # These "asserts" are used for self-checking and not for testing
    all_items = {"item1": 2, "item2": 3}
    assert calculation(**all_items) == 25
    print('Testing completed!')

if __name__ == "__main__":
    main()