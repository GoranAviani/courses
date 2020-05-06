#39. Write a Python program to compute the future value of a
# specified principal amount, rate of interest, and a number of years.

def fun(**kwargs):
    try:
        item1 = kwargs["item1"]
        item2 = kwargs["item2"]
        item3 = kwargs["item3"]
    except KeyError as e:
        print("Item {} can not be retrieved." .format(e))
    else:
        future_value = item1 * ((1 + (0.01 * item2)) ** item3)
        future_value = round(future_value, 2)
        return future_value

def main():
    # These "asserts" are used for self-checking and not for testing
    all_items = {"item1": 10000, "item2": 3.5, "item3": 7}
    assert fun(**all_items) == 12722.79
    print('Testing completed!')
if __name__ == "__main__":
    main()
