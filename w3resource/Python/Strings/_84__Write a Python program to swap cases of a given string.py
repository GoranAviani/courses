# 84. Write a Python program to swap cases of a given string.

def fun(**kwargs):
    try:
        item1 = kwargs["item1"]
    except:
        return "Item 1 or 2 are empty."

    result = ""
    for x in item1:
        if x.isupper():
            result += x.lower()
        else:
            result += x.upper()
    return result



if __name__ == "__main__":
    # These "asserts" are used for self-checking and not for testing
    itemOne = {"item1":  "pYTHON eXERCISES"}
    assert fun(**itemOne) == "Python Exercises"
    itemOne = {"item1": "pYTHON eXERCISes"}
    assert fun(**itemOne) == "Python ExercisES"
    itemOne = {"item1": "The car is a new BeetLE"}
    assert fun(**itemOne) == "tHE CAR IS A NEW bEETle"
    print('Testing completed!')