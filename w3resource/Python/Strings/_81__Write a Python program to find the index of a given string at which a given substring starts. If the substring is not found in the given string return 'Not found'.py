# _81__Write a Python program to find the index of a given string at which a given substring starts. If the substring is not found in the given string return 'Not found'

def fun(**kwargs):
    try:
        item1 = kwargs["item1"]
        item2 = kwargs["item2"]
    except:
        return "Item 1 or 2 are empty."

    text = item1.split(" ")

    counter = 0
    for y in text:
        if y.find(item2) != -1:
            return counter
        counter += 1

    return "Not Found"


if __name__ == "__main__":
    # These "asserts" are used for self-checking and not for testing
    itemOne = {"item1": "Python Exercises"}
    itemTwo = {"item2": "Ex"}
    print(fun(**itemOne, **itemTwo))
    assert fun(**itemOne, **itemTwo) == 1

    print('Testing completed!')