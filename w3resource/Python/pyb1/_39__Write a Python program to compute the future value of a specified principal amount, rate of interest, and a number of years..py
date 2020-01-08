#39. Write a Python program to compute the future value of a specified principal amount, rate of interest, and a number of years.

def fun(**kwargs):
    try:
        item1 = kwargs["item1"]
        item2 = kwargs["item2"]
        item3 = kwargs["item3"]
    except:
        return "Item 1 or 2 are empty."

    future_value = item1 * ((1 + (0.01 * item2)) ** item3)
    future_value = round(future_value, 2)
    return future_value

if __name__ == "__main__":
    # These "asserts" are used for self-checking and not for testing
    itemOne = {"item1":  10000}
    itemTwo = {"item2": 3.5}
    itemThree = {"item3": 7}
    assert fun(**itemOne, **itemTwo, **itemThree) == 12722.79

    print('Testing completed!')